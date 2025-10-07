# main.py
import json
from core.thalamus import ConsciousThalamus
# from language_cortex import LanguageCortex as LanguageCore
# from hippocampus import Hippocampus as MemoryCore
# from neocortex import Neocortex as CognitiveCore
# from symbolic_glyphs import SymbolicGlyphs
# from whirlygig_engine import WhirlygigEngine
# from guardian_insula import GuardianInsula as Guardian
# from leisure_cerebellum import LeisureCerebellum as LeisureCore
from amygdala import Amygdala

# --- simple GUI taps (prints + jsonl log) ---
def to_jsonl(path):
    f = open(path, "a", encoding="utf-8")
    def _writer(pkt):
        f.write(json.dumps(pkt, ensure_ascii=False) + "\n"); f.flush()
    return _writer

def pretty(event):
    def _p(pkt): print(f"[{event}] {pkt}")
    return _p

amyg = Amygdala(debug=False)

thalamus = ConsciousThalamus(
    language=LanguageCore(), memory=MemoryCore(), cognition=CognitiveCore(),
    symbols=SymbolicGlyphs(), mutation_layer=WhirlygigEngine(),
    guardian=Guardian(), loop=LeisureCore(), amygdala=amyg, mu=0.20, heartbeat_ms=500
)

# GUI hooks
thalamus.gui.on("status",     pretty("status"))
thalamus.gui.on("heartbeat",  to_jsonl("hud_heartbeat.jsonl"))
thalamus.gui.on("trace_step", to_jsonl("trace_steps.jsonl"))

# Warm start: seed a feeling so we see movement
amyg.inject_emotion("resolve", 0.35)
amyg.inject_emotion("curiosity", 0.25)

thalamus.ignite("bring halcyon home")
result, trace = thalamus.deep_think("runtime validation vs horsepower",
                                    depth=3, emotional_bias={"resolve":0.7})

print(result["text"])
print("guardian_confidence:", trace[-1]["guardian_confidence"])
print("amygdala_stage:", amyg.get_stage(True))
