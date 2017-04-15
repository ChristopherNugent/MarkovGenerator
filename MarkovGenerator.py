from NGramMap import NGramMap


class MarkovGenerator:

    def __init__(self):
        self.letters = NGramMap()
        self.words = NGramMap()

    def __str__(self):
        output = 'Letters------------------\n' + str(self.letters) + \
            '\n\nWords--------------------\n' + str(self.words)
        return output

    def new_word(self, word):
        last = '\start'
        for char in word:
            self.letters.add(last, char)
            last = char
        self.letters.add(last, '\end')

    def new_sentence(self, sentence):
        last = '\start'
        words = sentence.split()
        for word in words:
            self.words.add(last, word)
            last = word
            self.new_word(word)
        self.words.add(last, '\end')

    def next_word(self, max_count=-1):
        output = ''
        last = self.letters.random_from('\start')
        while max_count != 0 and last != '\end':
            output += last
            last = self.letters.random_from(last)
            max_count -= 1
        return output

    def next_sentence(self, max_count=-1):
        output = ''
        last = self.words.random_from('\start')
        while max_count != 0 and last != '\end':
            output += last + ' '
            last = self.words.random_from(last)
            max_count -= 1
        return output[:len(output) - 1]
