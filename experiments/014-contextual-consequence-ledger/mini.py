"""P0.2 compact: scenario-conditioned consequence ledger, not autonomous criticism.
Stdlib only. All interpretations are researcher-authored; output does not rank art.
Run: python mini.py --test ; python mini.py
"""
from dataclasses import dataclass, asdict
from difflib import SequenceMatcher
import json, sys, unittest

SOURCE = "Her hands raced over the keys. The piano trembled beneath them."
RAW = "Her hands trembled beneath them. The piano raced over the keys."
REPAIRED = "Her hands trembled over the keys. The piano raced beneath them."

@dataclass(frozen=True)
class Regime:
    name: str
    existing_tone: str
    aim: str
    material_constraint: str
    cue: str
    possibility: str
    risk: str

REGIMES = [
 Regime("literal account","stable ordinary physical scene","accurate description",
        "piano does not physically run across its own keys",
        "reader expects physical scene continuity",
        "anomalous attribution may be read as an error under a literal contract",
        "physical event inaccurately represented"),
 Regime("absurd comedy","furniture already acts; narrator stays dry","permit impossible agency",
        "objects can act impossibly in this fictional world",
        "deadpan impossible movement is an established device",
        "instrument becomes an autonomous comically mobile performer",
        "may still be too obvious or random"),
 Regime("psychological disturbance","pianist's sensorium is strained","displace agency",
        "nonliteral subjective perception allowed",
        "stress, bodily perception and viewpoint have been established",
        "instrument takes agency from the performer, making panic tangible",
        "could become unintended slapstick"),
 Regime("tragic rupture","precise grave narration to this point","make a violent tonal fracture",
        "physical realism is the baseline, not an unconditional creative law",
        "no necessary advance explanation; later reclassification possible",
        "absurdity may collide with gravity to produce disorientation",
        "could destroy sustained tragic pressure or reader trust")
]

def differences(before, after):
    a,b = before.split(),after.split()
    return [{"type":op,"before":" ".join(a[i:j]),"after":" ".join(b[k:l])}
            for op,i,j,k,l in SequenceMatcher(a=a,b=b).get_opcodes() if op!="equal"]

def inspect(candidate, regime):
    anchor = "piano raced over the keys"
    supported = anchor.casefold() in candidate.casefold()
    return {
      "regime":regime.name, "previous_tone":regime.existing_tone, "aim":regime.aim,
      "material_constraint":regime.material_constraint, "contextual_cue":regime.cue,
      "candidate":candidate, "material_changes":differences(SOURCE,candidate),
      "hypotheses":({"potential":regime.possibility, "risk":regime.risk,
                     "status":"researcher-authored, untested reader effect"} if supported else {}),
      "missing_witness":([] if supported else [anchor]),
      "permitted_next_choices":["PRESERVE","PREPARE_CONTEXT","INTENSIFY",
                                "MOVE_IN_SCENE","RESTORE_GEOMETRY","STOP"],
      "literary_verdict":None,
      "warning":"This is a traceable hypothesis ledger, not autonomous semantic perception."
    }

def run():
    return {"source":SOURCE,"raw_transform":RAW,"repaired_alternative":REPAIRED,
            "contexts":[inspect(RAW,r) for r in REGIMES]}

class Tests(unittest.TestCase):
 def test_four_regimes(self): self.assertEqual(len(run()["contexts"]),4)
 def test_odd_mutation_kept(self): self.assertIn("piano raced over",run()["raw_transform"])
 def test_repaired_separate(self): self.assertNotEqual(RAW,REPAIRED)
 def test_no_global_wrong(self): self.assertTrue(all(x["literary_verdict"] is None for x in run()["contexts"]))
 def test_opposed_readings(self): self.assertEqual(len(set(x["hypotheses"]["potential"] for x in run()["contexts"])),4)
 def test_actual_anchor(self): self.assertFalse(any(x["missing_witness"] for x in run()["contexts"]))
 def test_missing_anchor_flagged(self): self.assertTrue(inspect(SOURCE,REGIMES[0])["missing_witness"])
 def test_context_retained(self): self.assertTrue(all(x["contextual_cue"] for x in run()["contexts"]))
 def test_diff_not_empty(self): self.assertTrue(all(x["material_changes"] for x in run()["contexts"]))
 def test_keep_is_option(self): self.assertIn("PRESERVE",run()["contexts"][0]["permitted_next_choices"])

if __name__ == "__main__":
 if "--test" in sys.argv:
  sys.argv.remove("--test")
  unittest.main(verbosity=2)
 else:
  print(json.dumps(run(),indent=2,ensure_ascii=False))
