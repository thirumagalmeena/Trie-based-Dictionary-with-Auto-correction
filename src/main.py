from trie import Trie
from frequency_map import FrequencyMap
from loader import load_words
from levenshtein import levenshtein_distance

def get_closest_matches(word, all_words, max_distance=2):
    matches = []
    for candidate in all_words:
        dist = levenshtein_distance(word, candidate)
        if dist <= max_distance:
            matches.append((candidate, dist))
    return sorted(matches, key=lambda x: (x[1], -freq_map.get_frequency(x[0])))

def menu():
    print("\n=== Trie-based Dictionary System ===")
    print("1. Get suggestions for a prefix")
    print("2. Auto-correct a misspelled word")
    print("3. Add a new word")
    print("4. Exit")

if __name__ == "__main__":
    trie = Trie()
    freq_map = FrequencyMap()
    words = load_words("data/words.txt")

    for word in words:
        trie.insert(word)
        freq_map.insert(word)

    while True:
        menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            prefix = input("Enter prefix: ").strip().lower()
            suggestions = trie.get_words_with_prefix(prefix)
            ranked = freq_map.get_sorted_words(suggestions)
            if ranked:
                print("\nSuggestions:")
                for word in ranked:
                    print(f"{word} (freq: {freq_map.get_frequency(word)})")
            else:
                print("No suggestions found.")

        elif choice == '2':
            typo = input("Enter possibly misspelled word: ").strip().lower()
            all_words = list(freq_map.freq.keys())
            closest = get_closest_matches(typo, all_words)
            if closest:
                print("\nClosest matches:")
                for word, dist in closest[:5]:
                    print(f"{word} (distance: {dist}, freq: {freq_map.get_frequency(word)})")
            else:
                print("No close matches found.")

        elif choice == '3':
            new_word = input("Enter new word: ").strip().lower()
            if new_word:
                trie.insert(new_word)
                freq_map.insert(new_word)
                print(f"'{new_word}' added to dictionary.")
            else:
                print("Invalid word.")

        elif choice == '4':
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")
