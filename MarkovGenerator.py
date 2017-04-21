from freqmap import FrequencyMap


class MarkovGenerator:

    _end = '%%MarkovEnds%%'

    def __init__(self):
        self.letters = FrequencyMap()
        self.words = FrequencyMap()

    def __str__(self):
        output = 'Letters------------------\n' + str(self.letters) + \
            '\n\nWords--------------------\n' + str(self.words)
        return output

    def add_word(self, word):
        MarkovGenerator._add(self.letters, word)

    def add_sentence(self, sentence):
        MarkovGenerator._add(self.words, sentence.split())

    def add_from_file(self, filename, separator='\n\n'):
        with open(filename, 'r') as f:
            for line in f:
                for sentence in line.split(separator):
                    self.add_sentence(sentence)

    def next_word(self, max_count=-1, separator=''):
        return MarkovGenerator._next(self.letters, max_count, separator)

    def next_sentence(self, max_count=-1, separator=' '):
        return MarkovGenerator._next(self.words, max_count, separator)

    def _add(target, sequence):
        target.add(MarkovGenerator._end, sequence[0])
        target.feed(sequence)
        target.add(sequence[len(sequence) - 1], MarkovGenerator._end)

    def _next(source, max_count=-1, separator=''):
        output = []
        last = source.random_from(MarkovGenerator._end)
        while max_count != 0 and (output == '' or last != MarkovGenerator._end):
            output.append(last)
            last = source.random_from(last)
            max_count -= 1
        return separator.join(output)
