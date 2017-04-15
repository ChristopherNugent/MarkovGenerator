# About

A Markov chain generator based on N-Gram mappings capable of 
generating both words and sentences

# Usage

Import the `MarkovGenerator` class from `MarkovGenerator.py`, and instanciate it.

Use the `new_word()` method to add content for word generation

Use the `new_sentence()` method to add content for sentence generation, and each
word in the sentence will be fed to the `new_word()` method
