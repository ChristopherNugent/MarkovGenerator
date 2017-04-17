from collections import Counter
from random import randrange


class NGramMap:
    def __init__(self):
        self.map = dict()

    def add(self, key, value):
        try:
            self.map[key].update([value])
        except KeyError:
            self.map.update({key: Counter()})
            self.map[key].update([value])

    def common_from(self, key):
        """Returns the most common answer for a given key.
        Raises KeyError if the pattern does not exist."""
        return self.map[key].most_common(1)[0][0]

    def random_from(self, key):
        """Randomly returns a value of the given key based on the probability
        that the value follows the key"""
        rand = randrange(sum(self.map[key].values()))
        for inner_key in self.map[key]:
            rand -= self.map[key][inner_key]
            if rand < 0:
                return inner_key

    def __str__(self):
        string = ''
        for key in self.map:
            string += str(key) + ' -->'
            for value in self.map[key].most_common():
                string += ' ' + str(value)
            string += '\n'
        return string
