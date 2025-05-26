def load_words(file_path: str):
    words = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                word = line.strip().lower()
                if word:  # skip empty lines
                    words.append(word)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    return words
