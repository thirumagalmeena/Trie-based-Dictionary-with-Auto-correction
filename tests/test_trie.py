import unittest
from src.trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        for word in ['hello', 'help', 'helium']:
            self.trie.insert(word)

    def test_search(self):
        self.assertTrue(self.trie.search('hello'))
        self.assertFalse(self.trie.search('helix'))

    def test_startswith(self):
        self.assertTrue(self.trie.starts_with('hel'))
        self.assertFalse(self.trie.starts_with('hex'))

    def test_get_words_with_prefix(self):
        result = self.trie.get_words_with_prefix('he')
        self.assertIn('hello', result)
        self.assertIn('help', result)

if __name__ == '__main__':
    unittest.main()
