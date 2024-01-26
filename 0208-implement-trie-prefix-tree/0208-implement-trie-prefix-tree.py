class Trie:

    def __init__(self):
        self.trie={}

    def insert(self, word: str) -> None:
        tmp=self.trie
        for w in word:
            if w not in tmp:
                tmp[w]={}
            tmp=tmp[w]
        tmp['#']=''

    def search(self, word: str) -> bool:
        tmp=self.trie
        for w in word:
            if w not in tmp:
                return False
            tmp=tmp[w]
        if '#' not in tmp:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        tmp=self.trie
        for w in prefix:
            if w not in tmp:
                return False
            tmp=tmp[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)