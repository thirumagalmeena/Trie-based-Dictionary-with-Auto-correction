class FrequencyMap:
    def __init__(self):
        self.freq = {}

    def insert(self, word: str):
        word = word.lower()
        if word in self.freq:
            self.freq[word] += 1
        else:
            self.freq[word] = 1

    def get_frequency(self, word: str) -> int:
        return self.freq.get(word.lower(), 0)

    def get_sorted_words(self, words: list) -> list:
        # Sort given words by frequency (high to low)
        return sorted(words, key=lambda w: -self.get_frequency(w))
