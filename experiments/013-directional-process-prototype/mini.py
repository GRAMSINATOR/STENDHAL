"""STENDHAL P0-mini: portable, self-contained directional process test.
Standard library only. Candidate prose and semantic contribution tags are
hand-authored test inputs, not independently produced by an LLM or measured readers.
"""
from __future__ import annotations
from collections import Counter
from dataclasses import dataclass
import json
import re
import sys
import unittest

def observe(text, beats, premises=()):
    """Identify spans and repeated contribution labels; no semantic mindreading."""
    low = text.lower()
    last = {}
    movement, loops, errors = [], [], []
    for beat in beats:
        span, concept, changed = beat[:3]
        if span.lower() not in low:
            errors.append("MISSING WITNESS: " + span)
            continue
        for premise in beat[3:]:
            if premise not in premises:
                errors.append("UNWARRANTED PREMISE: " + premise)
        signature = (concept, changed)
        if concept in last and last[concept] == changed:
            loops.append(span)
        else:
            movement.append({"span": span, "concept": concept, "changed": changed})
        last[concept] = changed
    tokens = re.findall(r"\b\w+\b", low)
    repeated = {w: n for w, n in Counter(tokens).items()
                if n >= 3 and len(w) >= 4 and w not in ("they", "were", "that", "from")}
    suggestions = ["LEAVE_ALONE"]
    if loops:
        suggestions += ["COLLAPSE", "CHANGE_REPETITION", "PROTECT_INCANTATION"]
    if errors:
        suggestions += ["REMOVE_FALSE_PREMISE", "SEEK_WARRANT"]
    return {"tokens": len(tokens), "movement": movement, "flat_loops": loops,
            "warrant_errors": errors, "repeated": repeated, "opportunities": suggestions}

def patch_once(text, old, new):
    if text.count(old) != 1:
        raise ValueError("Expected a unique witnessed source span")
    return text.replace(old, new, 1)

@dataclass(frozen=True)
class Part:
    subject: str
    core: str
    tail: str = ""
    auxiliary: str = ""
    def say(self, core=None):
        return " ".join(filter(None, (self.subject, self.auxiliary, core or self.core, self.tail)))

def invert_cores(a, b):
    return a.say() + ". " + b.say() + ".", a.say(b.core) + ". " + b.say(a.core) + "."

PIANIST = {
 "surplus": (
  "The room was cold. The piano was cold. The keys were cold. "
  "Her hands were cold. Her heart was beating quickly. She played quickly.",
  [("room was cold","temperature","same"),("piano was cold","temperature","same"),
   ("keys were cold","temperature","same"),("hands were cold","temperature","same"),
   ("heart was beating quickly","acceleration","somatic"),
   ("played quickly","acceleration","musical")]
 ),
 "incantation": (
  "The room was cold. The piano was cold. The keys were cold. "
  "Her hands were warmer than she wanted. Warm enough to tremble. Warm enough to fail.",
  [("room was cold","temperature","environment"),("piano was cold","temperature","contact"),
   ("keys were cold","temperature","touch"),("hands were warmer","temperature","inversion"),
   ("Warm enough to tremble","warm","fear"),("Warm enough to fail","warm","stakes")]
 ),
}
BUS = {
 "thin": (
  "Bus ridership increased. More people rode the buses. Bus use climbed. "
  "The number of riders was higher. It was a rise in how many people took the bus.",
  [("Bus ridership increased","ridership","rise"),("More people rode","ridership","rise"),
   ("Bus use climbed","ridership","rise"),("riders was higher","ridership","rise"),
   ("rise in how many","ridership","rise")]
 ),
 "directional": (
  "Boardings increased from 10,000 to 12,000. On-time trips fell from 95% to 90%. "
  "These measure demand and reliability separately. The next question is whether the "
  "extra boardings happened on routes with worsening punctuality. The figures cannot answer it.",
  [("10,000 to 12,000","demand","quantity"),("95% to 90%","reliability","quantity"),
   ("demand and reliability separately","distinction","frame"),
   ("next question","route-level","new question"),("cannot answer it","evidence","limit")]
 ),
 "false_paradox": (
  "Ridership rose, while reliability fell. How could such a contradiction arise?",
  [("Ridership rose","ridership","rise"),("reliability fell","reliability","fall"),
   ("such a contradiction","paradox","claimed conflict","must_covaried")]
 ),
}

def process(case, order, aim):
    events = [{"type":"INTEND","aim":aim}]
    for i, name in enumerate(order):
        text, beats = case[name]
        events += [{"type":"ENACT","version":name,"text":text},
                   {"type":"PERCEIVE","version":name,"observation":observe(text,beats)}]
        if i:
            events.append({"type":"REACT","from":order[i-1],"to":name,
                           "action":"explore a different direction; selection externally specified"})
            events.append({"type":"REFRAME_INTENTION","from":aim,
                           "to":"Seek a new relation rather than repeat the prior statement"})
            aim = "Seek a new relation rather than repeat the prior statement"
    return events

class Tests(unittest.TestCase):
 def test_dead_repetition(self): self.assertEqual(len(observe(*BUS["thin"])["flat_loops"]), 4)
 def test_functional_repetition(self): self.assertEqual(len(observe(*PIANIST["incantation"])["flat_loops"]), 0)
 def test_false_paradox(self): self.assertEqual(len(observe(*BUS["false_paradox"])["warrant_errors"]), 1)
 def test_progress(self): self.assertEqual(len(observe(*BUS["directional"])["movement"]), 5)
 def test_patch(self): self.assertEqual(patch_once("A heart beat.", "heart", "piano"), "A piano beat.")
 def test_swapped_core(self):
  a,b = invert_cores(Part("Her hands","raced","over the keys"),
                     Part("The piano","trembled","beneath them"))
  self.assertEqual(b, "Her hands trembled over the keys. The piano raced beneath them.")
 def test_cold_agreement(self):
  _,b = invert_cores(Part("The wind","blowing",auxiliary="was"),
                     Part("The leaves","rustling",auxiliary="were"))
  self.assertEqual(b, "The wind was rustling. The leaves were blowing.")
 def test_does_not_hallucinate_witness(self):
  self.assertTrue(observe("An empty room.", [("an orchestra","music","new")])["warrant_errors"])
 def test_intention_revision(self):
  self.assertTrue(any(e["type"]=="REFRAME_INTENTION" for e in process(BUS, ["thin","directional"], "Report facts")))

if __name__=="__main__":
 if "--test" in sys.argv:
  sys.argv.remove("--test")
  unittest.main(verbosity=2)
 else:
  for label,case,order in (("pianist",PIANIST,["surplus","incantation"]),
                            ("bus",BUS,["thin","directional"])):
   print(label, json.dumps(process(case,order,"Create a usable initial text"),indent=2))
  print("primitive", invert_cores(Part("Her hands","raced","over the keys"),
                                    Part("The piano","trembled","beneath them")))
