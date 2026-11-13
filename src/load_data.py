from pathlib import Path
import pandas as pd

# Raw Data Path
DATASET_DIR = Path(r"D:\research\Indic Tokenizer Study\data\raw")

# Output file
OUTPUT_CSV = Path(
    r"D:\research\Indic Tokenizer Study\data\processed\flores_selected_languages.csv"
)

LANGUAGES = {
    "English": "eng_Latn",
    "Hindi": "hin_Deva",
    "Marathi": "mar_Deva",
    "Bengali": "ben_Beng",
    "Gujarati": "guj_Gujr",
    "Punjabi": "pan_Guru",
    "Urdu": "urd_Arab",
    "Tamil": "tam_Taml",
    "Telugu": "tel_Telu",
    "Kannada": "kan_Knda",
    "Malayalam": "mal_Mlym",
    "Spanish": "spa_Latn",
    "German": "deu_Latn",
}

# SPLITS = ["dev", "devtest"]   --> Using 'dev' split

def load(lang, split="dev"):
    path = DATASET_DIR / split / f"{lang}.{split}"

    if not path.exists():
        raise FileNotFoundError(f"Dataset file not found: {path}")

    with open(path, "r", encoding="utf-8") as file:
        return file.readlines()


def process_data():
    data = {}
    for key, value in LANGUAGES.items():
        lang = load(value)
        data[key] = lang
    return data

# creating processed dataframe
data = process_data()
df = pd.DataFrame(data)

# saving the created dataframe as csv file
df.to_csv(OUTPUT_CSV, index=False)