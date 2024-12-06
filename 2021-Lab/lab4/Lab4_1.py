class LongestWord:
    def __init__(self, sentence):
        self.sentence = sentence

    def find_longest(self):
        words = self.sentence.split()
        longest_word = max(words, key=len) # O(n)
        return longest_word
    

sentence = "Python programming is both fun and educational"
finder = LongestWord(sentence)
longest_word = finder.find_longest()

