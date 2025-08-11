class word_manager():
        def __init__(self, word):
            self.word = word
            self.guessing = []
            self.indexer = []

        def symbol_hider(self)->None:
              self.guessing = "_" * len(self.word)

        def changing_to_list(self)->None:
              self.guessing =list(self.guessing)
        def back_to_string(self)->None:
              self.guessing = ''.join(self.guessing)
        def emptying_guesses(self)->None:
              self.guessing = []

              