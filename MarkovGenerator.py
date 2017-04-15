from NGramMap import NGramMap


class MarkovGenerator:

    def __init__(self):
        self.letters = NGramMap()

    def new_input(self, new_input):
        last = '\\start'
        for char in new_input:
            self.letters.add(last, char)
            last = char
        self.letters.add(last, '\end')

    def next_word(self, max_count=-1):
        output = ''
        last = self.letters.random_from('\start')
        while max_count != 0 and last != '\end':
            output += last
            last = self.letters.random_from(last)
        return output
