from functools import reduce


class Tree:
    def __init__(self):
        self.children = {}
        self.flag = False

    def insert(self, word):
        for letter in word:
            if letter not in self.children:
                self.children[letter] = Tree()

            self = self.children[letter]
        self.flag = True

    def all_suffixes(self, prefix):
        results = set()

        if self.flag:
            results.add(prefix)

        if not self.children:
            return results

        return reduce(lambda a, b: a | b,  [node.all_suffixes(prefix + letter) for (letter, node)
                                            in self.children.items()])

    def autocomplete(self, prefix):
        node = self
        for letter in prefix:
            if letter not in node.children:
                return None
            node = node.children[letter]
        return list(node.all_suffixes(prefix))
