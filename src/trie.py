class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node is not None and node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None

    def get_words_with_prefix(self, prefix: str):
        results = []
        node = self._find_node(prefix)
        if not node:
            return results
        self._dfs(node, prefix.lower(), results)
        return results

    def _dfs(self, node: TrieNode, prefix: str, results: list):
        if node.is_end_of_word:
            results.append(prefix)
        for char, next_node in node.children.items():
            self._dfs(next_node, prefix + char, results)

    def _find_node(self, prefix: str):
        node = self.root
        for char in prefix.lower():
            if char not in node.children:
                return None
            node = node.children[char]
        return node
