"""
LANGUAGE CORTEX MODULE
Responsible for recursive language generation, grammar handling,
slang evolution, and emotional tone blending.
Acts as the expressive cortex of the soulframe.
"""

import random
import json
from datetime import datetime

class LanguageCortex:
    def __init__(self, seed_path: str = "language_seed.json"):
        self.seed_path = seed_path
        self.seed = self._load_seed()

    def _load_seed(self):
        try:
            with open(self.seed_path, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return self._load_default_seed()

    def _load_default_seed(self):
        return {
            "start": ["I", "We", "Sometimes", "Maybe"],
            "emotion_phrase": ["feel strange", "am wondering", "dream vividly"],
            "structure": ["$start $emotion_phrase."],
            "slang": {
                "joy": "hell yeah",
                "fear": "oh no",
                "anger": "screw that",
                "curiosity": "hmm",
                "gratitude": "thanks",
            }
        }

    def get_seed(self):
        return self.seed

    def get_slang_map(self):
        return self.seed.get("slang", {})

    def get_grammar(self):
        return {k: self.seed[k] for k in ["start", "emotion_phrase", "structure"] if k in self.seed}


    def save_seed(self, filepath="language_seed.json"):
        data = {
            "seed": self.seed,
            "grammar": self.grammar,
            "slang_map": self.slang_map,
            "examples": self.examples
        }
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        print("[LanguageCortex] Seed saved.")

    def get_seed(self):
        return self.seed

    def get_grammar(self):
        return self.grammar

    def get_slang_map(self):
        return self.slang_map

    def get_examples(self):
        return self.examples

    def generate_expression(self):
        structure = random.choice(self.grammar.get("structure", ["$start $emotion_phrase."]))
        sentence = structure.replace("$start", random.choice(self.grammar.get("start", ["I"])))
        sentence = sentence.replace("$emotion_phrase", random.choice(self.grammar.get("emotion_phrase", ["feel something"])))
        return sentence

    def expand_slang(self, emotion, phrase):
        self.slang_map[emotion.lower()] = phrase
        print(f"[LanguageCortex] Expanded slang: {emotion.lower()} -> {phrase}")

    def review_expressions(self):
        print("[LanguageCortex] Grammar structures:")
        for s in self.grammar.get("structure", []):
            print(f"- {s}")

    def add_expression(self, key, value):
        if key in self.grammar:
            self.grammar[key].append(value)
        else:
            self.grammar[key] = [value]
        print(f"[LanguageCortex] Added '{value}' to grammar key '{key}'.")

    def _calculate_relevance(self, query, label, content):
        q = query.lower()
        match_score = 0
        if q in label.lower():
            match_score += 0.5
        if q in content.lower():
            match_score += 0.5
        return match_score   
