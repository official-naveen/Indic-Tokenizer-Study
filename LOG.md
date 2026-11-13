## 13-11-2026
**Setup Project**
- Set up the project folder and virtual environment (`.venv`)
- Created `README.md`, `LOG.md`, `.gitignore` and `requirements.txt`
- Downloaded the FLORES-200 dataset into `data/raw/` 
- Created `src/test_dataset.py` to check that the data loads
- Wrote a short README with the question to stay focused

## 14-11-2026
**Created the Processed Dataset**
- Explored the FLORES-200 dataset and understood how it is structured.
- Renamed `test_dataset.py` to `load_data.py`.
- Wrote a script in `load_data.py` to collect all the data needed for the project.
- Selected 13 languages for the project:
  - Indian languages: Hindi, Marathi, Bengali, Gujarati, Punjabi, Urdu, Tamil, Telugu, Malayalam, and Kannada.
  - Foreign languages: English, Spanish, and German.
- Saved the selected language data in a CSV file: `data/processed/flores_selected_languages.csv`.