"""STENDHAL EXP-015 compact, runnable decision strategy prototype.

Run:
    python experiments/015-reconfigurable-decision-harness/mini.py --test
    python experiments/015-reconfigurable-decision-harness/mini.py

Manual decisions and world constraints are explicit fixtures, not autonomous
literary perception. Full 20-test prototype also distributed as a ZIP.
"""
from __future__ import annotations
from pathlib import Path
from difflib import SequenceMatcher
import json
import sys
import unittest
from copy import deepcopy

HERE = Path(__file__).parent
SOURCE = "Her hands raced over the keys. The piano trembled beneath them."
RAW = "Her hands trembled beneath them. The piano raced over the keys."
STRUCTURED = "Her hands trembled over the keys. The piano raced beneath them."

def config():
    return json.loads((HERE / "decision_tree.json").read_text(encoding="utf-8"))

def ordered(cfg, strategy):
    seen = set()
    result = cfg["strategies"][strategy]
    for q in result:
        if q in seen or q not in cfg["questions"]:
            raise ValueError("Unknown or duplicate question: " + q)
        if set(cfg["questions"][q].get("depends_on", [])) - seen:
            raise ValueError("Question out of dependency order: " + q)
        seen.add(q)
    return result

def ask(cfg, strategy, choices):
    trace = []
    for name in ordered(cfg, strategy):
        question = cfg["questions"][name]
        if any(choices.get(parent) not in allowed
               for parent, allowed in question.get("when", {}).items()):
            trace.append({"node": name, "state": "skipped"})
            continue
        selection = choices.get(name)
        if selection not in question["choices"]:
            raise ValueError("Missing or invalid answer: " + name)
        trace.append({"node": name, "choice": selection})
    return trace

def transform(text, method, realization=None):
    if method == "NO_EDIT": return text
    if method == "INVERT":
        if text != SOURCE: raise ValueError("Exact witness required for this small prototype")
        if realization == "raw": return RAW
        if realization == "structured": return STRUCTURED
        raise ValueError("Choose raw or structured realisation")
    if method == "TRANSFER":
        if text != SOURCE: raise ValueError("Exact witness required")
        return "Her hands raced cold across the keys. The piano beating faster beneath them."
    if method == "REPEAT": return text + " " + text.split(". ")[0] + "."
    if method == "FRACTURE": return text.replace(". The piano", ". And then. The piano", 1)
    raise ValueError("Unregistered operation")

def consequences(text, choices, layers, witnesses):
    changes = []
    for witness in witnesses:
        s = witness["span"]
        if s.lower() not in text.lower():
            changes.append({"type": "unsupported_witness", "span": s})
        elif witness["kind"] == "impossible_actor_motion":
            collision = layers.get("world.physics") == "strict" and choices["claim_status"] == "literal"
            changes.append({"type": "literal_physical_contract_collision" if collision else
                            "possible_expression_without_literal_world_change",
                            "witness": s, "conditional": True})
        else:
            changes.append({"type": "candidate_relation", "witness": s})
    if choices.get("constrain") == "yes" and layers.get("world.physics") in ("strict","permissive"):
        if choices["world_rules"] != layers["world.physics"]:
            changes.append({"type": "conflicting_world_model_and_decision"})
    if layers.get("character.Jax.voice") == "absurd_deadpan":
        changes.append({"type": "scoped_comic_voice", "global_physics_rewritten": False})
    return changes

def run(cfg, strategy, fixture):
    answers, layers = fixture["choices"], fixture["layers"]
    questions = ask(cfg, strategy, answers)
    text = transform(SOURCE, answers["operator"], answers.get("realization"))
    a, b = SOURCE.split(), text.split()
    d = [{"kind": k, "lost": " ".join(a[i:j]), "new": " ".join(b[m:n])}
         for k,i,j,m,n in SequenceMatcher(None,a,b).get_opcodes() if k != "equal"]
    decision = answers["response"]
    return {"scenario": fixture["id"], "workflow": strategy,
            "question_trace": questions, "world_model": layers,
            "source": SOURCE, "produced": text, "actual_diff": d,
            "conditional_effects": consequences(text,answers,layers,fixture["witnesses"]),
            "initial_intention": fixture["intention"],
            "revised_intention": (fixture.get("new_intention",fixture["intention"])
                                 if decision == "reframe_intention" else fixture["intention"]),
            "response": decision, "aesthetic_verdict": None,
            "epistemic_warning": "Premises and interpretations supplied by researcher, not inferred."}

hard_scifi = {
  "id":"strict_physics_expressionist_character",
  "layers":{"world.physics":"strict","emotion.expression":"highly_metaphorical",
            "character.Jax.voice":"absurd_deadpan"},
  "intention":"Protect the physical world while expressing perceptual distress",
  "new_intention":"Try a comic interpretation inside an otherwise hard-science scene",
  "choices":{"constrain":"yes","scope":"layered","world_rules":"strict",
             "stylistic_colouring":"yes","expressive_layer":"multiple",
             "claim_status":"character_perception","operator":"INVERT",
             "realization":"raw","response":"reframe_intention"},
  "witnesses":[{"span":"piano raced over the keys","kind":"impossible_actor_motion"}]
}
literal_report = deepcopy(hard_scifi)
literal_report["id"] = "reportage"
literal_report["layers"] = {"world.physics":"strict"}
literal_report["choices"]["claim_status"] = "literal"
literal_report["choices"]["response"] = "branch"
comedy = deepcopy(hard_scifi)
comedy["id"] = "absurd_literal_comedy"
comedy["layers"] = {"world.physics":"permissive","character.Jax.voice":"absurd_deadpan"}
comedy["choices"]["world_rules"] = "permissive"
comedy["choices"]["claim_status"] = "literal"

class TestMini(unittest.TestCase):
    def test_two_legal_orders(self):
        self.assertTrue(ordered(config(),"voice_first"))
        self.assertTrue(ordered(config(),"constraints_first"))
    def test_order_changes_without_changing_text(self):
        a = run(config(),"voice_first",hard_scifi)
        b = run(config(),"constraints_first",hard_scifi)
        self.assertNotEqual(a["question_trace"][0]["node"], b["question_trace"][0]["node"])
        self.assertEqual(a["produced"], b["produced"])
    def test_precedence_guard(self):
        c=deepcopy(config()); c["strategies"]["bad"]=["scope","constrain"]
        with self.assertRaises(ValueError): ordered(c,"bad")
    def test_scoped_comic_permission_without_physics_rewrite(self):
        r=run(config(),"constraints_first",hard_scifi)
        self.assertFalse(any(e["type"]=="literal_physical_contract_collision" for e in r["conditional_effects"]))
        self.assertTrue(any(e["type"]=="scoped_comic_voice" for e in r["conditional_effects"]))
    def test_literal_world_collision_is_not_aesthetic_verdict(self):
        r=run(config(),"constraints_first",literal_report)
        self.assertTrue(any(e["type"]=="literal_physical_contract_collision" for e in r["conditional_effects"]))
        self.assertIsNone(r["aesthetic_verdict"])
    def test_comedy_world_not_a_literal_collision(self):
        r=run(config(),"voice_first",comedy)
        self.assertFalse(any(e["type"]=="literal_physical_contract_collision" for e in r["conditional_effects"]))
    def test_actual_witnessed_transform(self):
        self.assertEqual(transform(SOURCE,"INVERT","raw"), RAW)
        self.assertEqual(transform(SOURCE,"INVERT","structured"),STRUCTURED)
    def test_intention_revised(self):
        r=run(config(),"voice_first",hard_scifi)
        self.assertNotEqual(r["initial_intention"],r["revised_intention"])
    def test_dynamic_question_insertion(self):
        c=deepcopy(config()); c["questions"]["extra"]={"choices":["yes","no"],"depends_on":["operator"]}
        c["strategies"]["voice_first"].insert(-1,"extra")
        f=deepcopy(hard_scifi); f["choices"]["extra"]="yes"
        self.assertTrue(any(t["node"]=="extra" for t in run(c,"voice_first",f)["question_trace"]))

if __name__ == "__main__":
    if "--test" in sys.argv:
        sys.argv.remove("--test")
        unittest.main(verbosity=2)
    else:
        print(json.dumps([run(config(),"constraints_first",hard_scifi),
                          run(config(),"voice_first",comedy),
                          run(config(),"constraints_first",literal_report)],
                         indent=2,ensure_ascii=False))
