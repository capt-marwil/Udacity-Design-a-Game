# -*- coding: utf-8 -*-
from random import randint

class HangMan(object):
    _static_words = ['Brander', 'mauston', 'matronized', 'supercilious', 'unexterminated', 'wile', 'conductible', 'expertism', 'excitingly', 'obliteration', 'inefficient', 'preclosing', 'leatherhead', 'siltation', 'Latvian', 'analogised', 'kif', 'sharpness', 'sild', 'omniscience', 'resegregation', 'felspathose', 'monumentalizing', 'superstamp', 'hypermetropia', 'palatelike', 'aborigine', 'bolyai', 'Treason', 'overhanging', 'sage', 'nonpsychologic', 'reproclaim', 'applicatorily', 'clactonian', 'charlton', 'unconcluded', 'prediphtheritic', 'semiboiled', 'cotswold', 'photolithoprint', 'melampus', 'Ejective', 'neuroembryology', 'negroize', 'redate', 'smokelessness', 'ingemination', 'claimant', 'viborg', 'healthy', 'gasogene', 'godsend', 'handybilly', 'relegated', 'lucrative', 'Subsidization', 'complect', 'refroze', 'exclusionism', 'manipur', 'thinkingly', 'answerlessly', 'uninterpolated', 'undernourish', 'indianapolis', 'untotalled', 'anthropophagic', 'szymanowski', 'amphipneustic']

    def __init__(self):
        self.secret = self.new_word()
        self.right_guesses = ''
        self.wrong_guesses = ''
        self.guessed_so_for = ''
        self.game_over = False
        self.status = 0
        self.placeholder = "_ " * len(self.secret)
        self.start_game()

    def new_word(self):
        return self._static_words[randint(0, len(self._static_words)-1)]

    def start_game(self):
        while True:
            self.print_board()
            user_guess = self.get_user_input(self.wrong_guesses + self.right_guesses)

            if user_guess in self.secret:
                self.right_guesses = self.right_guesses + user_guess

                foundAllLetters = True
                for i in range(len(self.secret)):
                    if self.secret[i] not in self.right_guesses:
                        foundAllLetters = False
                        break
                if foundAllLetters:
                    print "Gut gemacht, das gesuchte Wort lautet " + self.secret + ". Herzlichen Glückwunsch!"
                    self.game_over = True
            else:
                self.increase_status()
                self.wrong_guesses = self.wrong_guesses + user_guess

                if len(self.wrong_guesses) == 7:
                    self.print_board()
                    print "Leider hast Du keine Versuche mehr\n"
                    self.game_over = True
            if self.game_over:
                if self.new_game():
                    self.wrong_guesses = ''
                    self.right_guesses = ''
                    self.game_over = False
                    self.status = 0
                    self.secret = self.new_word()
                else:
                    break


    def get_user_input(self, already_guessed):
        while True:
            print('Gib einen Buchstaben ein.')
            user_guess = raw_input("Deine Eingabe?:")
            user_guess = user_guess.lower()
            if len(user_guess) != 1:
                print "Bitte gib nur einen Buchstaben ein."
            elif user_guess in already_guessed:
                print "Den Buchstaben hast Du schon geraten."
            elif user_guess not in "abcdefghijklmnopqrstuvwxyzäüöß":
                print "Es dürfen nur BUCHSTABEN eingegeben werden."
            else:
               return user_guess

    def increase_status(self):
        # Helper function to increase the game status
        # if status >= 7 the game aboards
        self.status += 1

    def print_board(self):
        print "Dein aktueller Status ist: " + str(self.status)

        # Print out letters that are not in the secret word
        for l in self.wrong_guesses:
            print l,

        for i in range(len(self.secret)):
            if self.secret[i] in self.right_guesses:
                self.placeholder = self.placeholder[:i] + self.secret[i] + self.placeholder[i+1:]

        for l in self.placeholder:
            print l,
        print "\n"

    def new_game(self):
        print "Möchtest Du noch einmal spielen? (Ja/Nein)"
        return raw_input().lower().startswith('j')

my_word = HangMan()

