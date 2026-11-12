from pathlib import Path

ROOT = Path(r"D:\research\Indic Tokenizer Study\data\raw")

def load(lang, split="devtest"):
    path = ROOT / split / f"{lang}.{split}"
    return path.read_text(encoding="utf-8").splitlines()

en = load("eng_Latn")
hi = load("hin_Deva")
print(len(en), len(hi))        
print(en[0])
print(hi[0])
