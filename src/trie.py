from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.is_end_of_word = False
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, name):
        node = self.root
        for char in name.lower():
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, query):
        node = self.root
        for char in query.lower():
            if char not in node.children:
                return []
            node = node.children[char]
        return self._get_all_words_from_node(node, query)

    def _get_all_words_from_node(self, node, prefix, count=5):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for child_char, child_node in node.children.items():
            if len(words) >= count:
                break
            words.extend(self._get_all_words_from_node(child_node, prefix + child_char, count))
        return words
