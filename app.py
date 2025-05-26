import streamlit as st
from src.trie import Trie
from src.frequency_map import FrequencyMap
from src.loader import load_words
from src.levenshtein import levenshtein_distance

trie = Trie()
freq_map = FrequencyMap()
words = load_words("data/words.txt")
for word in words:
    trie.insert(word)
    freq_map.insert(word)

st.title("📚 Trie-based Dictionary")

option = st.radio("Choose action:", ["Suggest words", "Auto-correct", "Add word"])

if option == "Suggest words":
    prefix = st.text_input("Enter prefix")
    if prefix:
        suggestions = trie.get_words_with_prefix(prefix)
        ranked = freq_map.get_sorted_words(suggestions)
        st.write("Suggestions:", ranked)

elif option == "Auto-correct":
    typo = st.text_input("Enter possibly misspelled word")
    if typo:
        def get_closest_matches(word, all_words, max_distance=2):
            matches = []
            for candidate in all_words:
                dist = levenshtein_distance(word, candidate)
                if dist <= max_distance:
                    matches.append((candidate, dist))
            return sorted(matches, key=lambda x: (x[1], -freq_map.get_frequency(x[0])))

        all_words = list(freq_map.freq.keys())
        closest = get_closest_matches(typo, all_words)
        st.write("Closest Matches:")
        for word, dist in closest[:5]:
            st.write(f"{word} (distance: {dist}, freq: {freq_map.get_frequency(word)})")

elif option == "Add word":
    new_word = st.text_input("Enter new word")
    if st.button("Add") and new_word:
        trie.insert(new_word)
        freq_map.insert(new_word)
        st.success(f"Added '{new_word}' to dictionary.")
