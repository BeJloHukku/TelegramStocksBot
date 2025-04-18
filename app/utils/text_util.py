import json
from pathlib import Path

class TextManager:
    def __init__(self):
        self.phrases = self._load_phrases()
    
    def _load_phrases(self):
        try:
            path = Path(__file__).parent.parent / 'locales' / 'phrases.json'
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading phrases: {e}")
            return {}

    def get(self, category: str, key: str) -> str:
        return self.phrases.get(category, {}).get(key, f"[{category}.{key} not found]")


text = TextManager()