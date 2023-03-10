# import modules needed
from PyDictionary import PyDictionary
import random, time, csv, nltk, tkinter as tk
from colorama import Fore, Back, Style
from words import med_words, sentences, es_words, hard_words
from dictionary import dictionary, letters




# define the function to update the leaderboard
def update_leaderboard(name, score, mode):
  with open('leaderboard.csv', mode='r') as leaderboard_file:
    leaderboard_reader = csv.reader(leaderboard_file)
    leaderboard_data = list(leaderboard_reader)

  with open('leaderboard.csv', mode='w', newline='') as leaderboard_file:
    leaderboard_writer = csv.writer(leaderboard_file)

    # check if player is already on the leaderboard
    for i, row in enumerate(leaderboard_data):
      if row[0] == name and row[2].split(" ")[-1] == mode:
        if int(row[1]) < score:
          leaderboard_data[i][1] = str(score)
        break
    else:
      leaderboard_data.append([
        name,
        str(score), f"| They used {mode} mode on difficulty {difficulty}"
      ])

    # write updated leaderboard to file
    leaderboard_writer.writerows(leaderboard_data)

# define the function to display the leaderboard
def display_leaderboard():
  with open('leaderboard.csv', mode='r') as leaderboard_file:
    leaderboard_reader = csv.reader(leaderboard_file)
    sorted_leaderboard = sorted(leaderboard_reader,
                                key=lambda row: int(row[1]),
                                reverse=True)

    print(Fore.BLUE + Style.DIM + "----- " + Fore.WHITE + Style.BRIGHT +
          "LEADERBOARD" + Fore.BLUE + Style.DIM + " -----" + Style.NORMAL)
    for i, row in enumerate(sorted_leaderboard[:10]):
      print(Fore.GREEN + f"{i+1}. {row[0]}  - {row[1]} - {row[2]}")
    print(Fore.BLUE + Style.DIM + "-----------------------" + Style.NORMAL)


# print start of the game

instruct = str(input("Do you know how to play the game(y/n):\n"))

if instruct.lower() in ["n", "no"]:
  print(Fore.YELLOW + "Welcome to the exciting world of the Word Game! Get ready to flex your vocabulary muscles and show off your language skills. Choose from three different game modes: Word Mode, Sentence Mode, and Letter Mode.\n" + Fore.BLUE + "In Word Mode, we'll give you a word to spell and reward you with points based on the difficulty level. In Sentence Mode, you'll need to type in the full sentence that we display on the screen. But be warned, the sentences get trickier and case-sensitive as you progress to higher levels. In Letter Mode, we'll give you a combination of 2-3 letters and challenge you to come up with as many words as possible that include those letters. However, you cant' use the same word again The score depends on how long the word is.\n" + Fore.GREEN + "But that's not all! You can climb your way up the leaderboard by earning points in each mode. Think you have what it takes to be the Word Game champion? Then let's get started!\n")

  print(Fore.WHITE + Style.BRIGHT + "THIS " + Fore.RED + "IS " + Fore.CYAN + "THE " + Fore.GREEN + "WORD " + Fore.MAGENTA + "GAME")

if instruct.lower() in ["y", "yes"]:
  print(Fore.WHITE + Style.BRIGHT + "THIS " + Fore.RED + "IS " + Fore.CYAN + "THE " + Fore.GREEN + "WORD " + Fore.MAGENTA + "GAME")




# display the leaderboard using the function from earlier
display_leaderboard()
used_words = []
repeat = "o"
while repeat == "y" or "o":

  def typing_game(mode, difficulty):
    word_mode = True if mode == "word" else False
    

    score = 0
    start_time = time.time()

    if difficulty == 1 and mode != "word":
      time_limit = 60
      print(Fore.GREEN + "Time limit: 60 seconds")
    elif difficulty == 2 and mode != "word":
      time_limit = 30
      print(Fore.YELLOW + "Time limit: 30 seconds")
    elif difficulty == 3 and mode != "word":
      time_limit = 15
      print(Fore.RED + "Time limit: 15 seconds")
    if difficulty == 1 and mode == "word":
      time_limit = 120
      print(Fore.GREEN + "Time limit: 120 seconds")
    elif difficulty == 2 and mode == "word":
      time_limit = 60
      print(Fore.YELLOW + "Time limit: 60 seconds")
    elif difficulty == 3 and mode == "word":
      time_limit = 30
      print(Fore.RED + "Time limit: 30 seconds")

    while time.time() - start_time < time_limit:
      if mode == "letter":
        letter = random.choice(letters)
        entered_word = input(Fore.BLUE + f"Type word that has these letters: {letter} \n" +
                             Fore.GREEN)
        if letter in entered_word:
          if entered_word in used_words:
            print(Fore.RED + 'Invalid word! Word already used. /n')
          if entered_word in dictionary and entered_word not in used_words:
            used_words.append(entered_word)
            score += len(entered_word) * difficulty
            print(Fore.GREEN + "Correct!\n")
            
          if entered_word not in dictionary:
            print(Fore.RED + "Incorrect!\n")
        else:
          print(Fore.RED + "Incorrect!\n")
      if word_mode:
        if difficulty == 1:
          word = random.choice(es_words)
        if difficulty == 2:
          word = random.choice(med_words)
        if difficulty == 3:
          word = random.choice(hard_words)

        entered_word = input(Fore.BLUE + f"Type the word: {word}\n" +
                             Fore.GREEN)

        if entered_word == word:
          if difficulty == 1:
            score += len(word)
          if difficulty == 2:
            score += len(word) * 1.5
          if difficulty == 3:
            score += len(word) * 3
          print(Fore.GREEN + "Correct!\n")
          score = round(score)
        else:
          score -= len(word)
          print(Fore.RED + "Incorrect!\n")
      if mode == "sentence":
        sentence = random.choice(sentences)
        entered_sentence = input(Fore.BLUE +
                                 f"Type the sentence: {sentence}\n" +
                                 Fore.GREEN)

        if difficulty == 3 and entered_sentence == sentence:
          score += len(sentence) * 2
          print(Fore.GREEN + "Correct!\n")
        elif entered_sentence.lower() == sentence.lower():
          if difficulty != 3:
            score += len(sentence) * 0.75

            print(Fore.GREEN + "Correct!\n")
        else:
          print(Fore.RED + "Incorrect!\n")

      print(Fore.WHITE + f"Score: {score}\n")
      print(Fore.LIGHTYELLOW_EX +
            f"Time elapsed: {int(time.time() - start_time)} seconds\n")
    score = round(score)
    print(f"{name}, Your final score is: {score}")

    update_leaderboard(name, score, mode)
    display_leaderboard()
    repeat = input("Do you want to play again?(y/n) ")
    if repeat == "n":
      quit()

  if __name__ == "__main__":
    print(Fore.WHITE + "Enter mode" + Fore.WHITE + "(" + Fore.GREEN + "word " +
          Fore.WHITE + "or " + Fore.RED + "sentence" + Fore.WHITE + " or " + Fore.BLUE + "letter" + Fore.WHITE + ")")
    mode = input("Enter here: ")
    difficulty = int(input("Enter the difficulty level (1, 2, 3) "))

    if repeat != "y":
      name = str(input("What is your name? "))

    if mode == "sentence" or mode == "word" or mode == "letter" and difficulty in [1, 2, 3]:
      typing_game(mode, difficulty)

    else:
      quit(Fore.RED + "Invalid input")
