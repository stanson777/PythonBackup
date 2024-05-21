import sqlite3
import random


random_word=["apple", "banana", "carrot", "dog", "elephant", "flower", "guitar", "happiness", "ice cream", "jazz", "kangaroo", "lemon", "mountain", "notebook", "orange", "penguin", "quasar", "rainbow", "sunshine", "tiger"]

conn = sqlite3.connect('hangman_game.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        wins INTEGER DEFAULT 0,
        losses INTEGER DEFAULT 0
    )
''')
conn.commit()

class Game:
    def __init__(self, player_username, word):
        self.player_username = player_username
        self.word = word
        self.lives = len(self.word)
        self.bricks = ["_" for _ in range(len(self.word))]
        self.guesses = 0

    def calculating_score1(self):
        return f'You have guessed the word in {self.guesses} try'

    def calculating_score2(self):
        return f'You lost but you find {self.guesses} letters'

    def finding_and_showing(self, letter):
        for brick in range(len(self.word)):
            if letter == self.word[brick]:
                self.bricks[brick] = letter
        return self.bricks

    def checking_word(self):
        return "".join(self.bricks) == self.word

    def check_if_word_is_correct(self, word):
        return word == self.word

    def save_result_to_database(self, outcome):

        cursor.execute("SELECT * FROM players WHERE username = ?", (self.player_username,))
        player = cursor.fetchone()

        if player:

            if outcome == "win":
                cursor.execute("UPDATE players SET wins = wins + 1 WHERE username = ?", (self.player_username,))
            elif outcome == "lose":
                cursor.execute("UPDATE players SET losses = losses + 1 WHERE username = ?", (self.player_username,))
        else:

            cursor.execute("INSERT INTO players (username, wins, losses) VALUES (?, ?, ?)",
                           (self.player_username, 1 if outcome == "win" else 0, 1 if outcome == "lose" else 0))

        conn.commit()

    def game(self):
        used_letters = []
        while self.lives > 0:
            if len(used_letters) > 0:
                print("Used letters:")
                print(used_letters)
            print(self.bricks)
            question1 = input("Do you want to guess the whole word? (y/n)")
            if question1.lower() == 'y':
                question2 = input("What word do you think it is?")
                if self.check_if_word_is_correct(question2):
                    self.guesses += 1
                    print("Correct!")
                    self.save_result_to_database("win")
                    return self.calculating_score1()
                else:
                    self.guesses += 1
                    print("Incorrect")
                    self.lives -= 1
            else:
                question = input("Try to guess the letter:")
                if question in self.word:
                    self.guesses += 1
                    print("Correct")
                    self.finding_and_showing(question)
                    if self.checking_word():
                        print("You won!")
                        self.save_result_to_database("win")
                        return self.calculating_score1()
                else:
                    self.guesses += 1
                    self.lives -= 1
                    used_letters.append(question)
                    print("Sorry, wrong")
                    print(f"Remaining lives: {self.lives}")
        self.save_result_to_database("lose")
        return self.calculating_score2()

question=int(input("How many games you want to play?: "))

player_username = input("Enter your username: ")
for i in range(question):
    def gamee(user_name,word=random.choice(random_word)):

        app = Game(user_name, word)
        print(app.game())
    gamee(player_username)



def show_stats_table():
    conn=sqlite3.connect("hangman_game.db")
    cursor=conn.cursor()

    cursor.execute("SELECT * FROM players")
    players=cursor.fetchall()

    print("Statystki graczy:")
    print("Username | Wins | Losses")
    print("-"*25)

    for player in players:
        print(f"{player[1]} | {player[2]} | {player[3]}")

    conn.close()


show_stats_table()