# Trie-based Dictionary with Auto-Correction

A smart dictionary system using Trie for autocomplete and Levenshtein distance for spell correction. Includes word frequency ranking using a Hash Map.

---

## Project Overview

This project builds a Trie-based dictionary system with the following capabilities:

- **Autocomplete Suggestions:** Efficiently suggests words based on user-typed prefixes.
- **Auto-correction:** Uses Levenshtein Distance to suggest corrections for misspelled words.
- **Ranking:** Utilizes a Hash Map to store word frequencies and ranks suggestions by popularity.
- **Extensible Design:** Separation of Trie and frequency components allows easy enhancement.

---

## Features

- Fast prefix-based search with Trie data structure.
- Frequency tracking with a Hash Map for ranking suggestions.
- Auto-correction of misspelled words using edit distance.
- Command-line and (optional) web interface support.
- Easy to add new words dynamically and update frequencies.
- Modular and well-tested codebase.

---


## System Architecture

- **Trie:** Stores the dictionary words character by character, enabling quick prefix searches.
- **Hash Map:** Maintains a frequency count of each word to prioritize suggestions.
- **Levenshtein Distance:** Algorithm to calculate similarity between words for auto-correction.
- **Interface:** CLI for basic interaction; Streamlit-based UI (optional) for web access.

---

## Installation

### Prerequisites
- Python 3.7 or above
- (Optional) Streamlit for web interface

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Streamlit UI

```bash
pip install streamlit
```

---

## Run Locally

```bash
python src/main.py
```

## Web Interface

```bash
streamlit run app.py
```

---

# License
- This project is licensed for educational purposes only.

---

## Contributor
**Thirumagal Meena A**  
Applied Mathematics and Computational Sciences  
Psg College of Technology  
