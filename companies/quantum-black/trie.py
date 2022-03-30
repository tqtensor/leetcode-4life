class Trie:
    def __init__(self):
        self.trie = {}
        self.terminals = set()

    def insert(self, word: str) -> None:
        ptr = self.trie
        for c in word:
            if c not in ptr:
                ptr[c] = {}
            ptr = ptr[c]
        self.terminals.add(id(ptr))

    def search(self, word: str) -> bool:
        ptr = self.searchPrefix(word)
        if ptr is None:
            return False
        if id(ptr) not in self.terminals:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None

    def searchPrefix(self, prefix: str):
        ptr = self.trie
        for c in prefix:
            if c not in ptr:
                return None
            ptr = ptr[c]
        return ptr


if __name__ == "__main__":
    trie = Trie()
    trie.insert("tang")
    trie.insert("thai")
    print(trie.startsWith("tha"))
