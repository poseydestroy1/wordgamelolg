# import modules needed
from tkinter import messagebox
from replit import audio
from colorama import Fore, Back, Style
from words import med_words, sentences, es_words, hard_words
from dictionary import dictionary, letters
import random # pick a random prompt to write depending on your mode
import time # uses a timer to show that you have only a specific amount of time
import csv # uses a csv file to store data

import tkinter as tk
from tkinter import scrolledtext

def button_press(event):
    button.invoke()

letter = random.choice(letters)

def wordisin():
  global entered_word, used_words, score, letter
  entered_word = lettertype.get()
  print("test")
  lettertype.delete(0, tk.END)
  if letter in entered_word:
      if entered_word in used_words:
            print("Invalid word! Word already used.")
      elif entered_word in dictionary:
            used_words.append(entered_word)
            score += len(entered_word) * int(difficulty)
            print("Correct!")
      else:
            print("Incorrect!")
  else:
        print("Incorrect!")




# define the function to update the leaderboard
def update_leaderboard(name, score, mode):
    with open('leaderboard.csv', mode='r') as leaderboard_file:
        leaderboard_reader = csv.DictReader(leaderboard_file)
        leaderboard_data = list(leaderboard_reader)

    with open('leaderboard.csv', mode='w', newline='') as leaderboard_file:
        fieldnames = ['name', 'score', 'mode']
        leaderboard_writer = csv.DictWriter(leaderboard_file, fieldnames=fieldnames)
        leaderboard_writer.writeheader()

        # check if player is already on the leaderboard
        for row in leaderboard_data:
            if row['name'] == name and row['mode'].split(" ")[-1] == mode:
                if int(row['score']) < score:
                    row['score'] = str(score)
                break
        else:
          leaderboard_data.append({'name': name, 'score': str(score), 'mode': f"| They used {mode} mode on difficulty {difficulty}"})
          leaderboard_writer.writerows(leaderboard_data)


# create a function to display the leaderboard in the scrolled text widget
def display_leaderboard():
    leaderboard_text.configure(state="normal")  # enable the widget
    leaderboard_text.delete('1.0', tk.END)
    with open('leaderboard.csv', mode='r') as leaderboard_file:
        leaderboard_reader = csv.DictReader(leaderboard_file)
        sorted_leaderboard = sorted(leaderboard_reader,
                                    key=lambda row: int(row.get('score', 0)),
                                    reverse=True)
        leaderboard_text.insert(tk.END, "----- LEADERBOARD -----\n")
        for i, row in enumerate(sorted_leaderboard[:20]):
            leaderboard_text.insert(tk.END, f"{i+1}. {row['name']} - {row['score']} - {row['mode']}\n")
        leaderboard_text.insert(tk.END, "-----------------------\n")
    leaderboard_text.configure(state="disabled")  # disable the widget again



root = tk.Tk()
root.title("Leaderboard")
root.geometry("400x400")



start_button = tk.PhotoImage(file="images/Startbuttoni.gif", master=root) # create a tkinter-compatible image object from a GIF file and provide root as master
smaller_image = start_button.subsample (5, 5) # create a new image that is half as large as the original one
quit = tk.Button (root, command=root.destroy, borderwidth=0, activebackground="white")
quit.image = smaller_image # keep a reference to the image object
quit.config (image=quit.image) # set the image option of the button 
quit.pack ()

leaderboard_button = tk.Button(root, text="Display Leaderboard", command=display_leaderboard, pady = 10)
leaderboard_button.pack()
# create a scrolled text widget to display the leaderboard
leaderboard_text = scrolledtext.ScrolledText(root, width=65, height=20, state="disabled", wrap=tk.WORD)
leaderboard_text.pack(pady=10)



root.mainloop()



# print start of the game

start = tk.Tk()

# Set up the main window
start.title('The Word Game')
start.geometry('400x300')

# Create a label to ask if the user knows how to play
question_label = tk.Label(start, text='Do you know how to play the game?', font=('Comic Sans MS', 14))
question_label.pack()

def handle_answer(answer):
    if answer == 'yes':
        # Remove the question and show the title of the game in color
        question_label.pack_forget()
        title_label = tk.Label(start, text='The Word Game', font=('Comic Sans MS', 20), fg='blue')
        title_label.pack()
        yes_button.pack_forget()
        no_button.pack_forget()
        start.destroy()
        
    elif answer == 'no':
        # Print the instructions and then ask if the user now knows how to play
        instructions = "Welcome to the exciting world of the World Game! The contents of the instructions to the game can be seen here; ------1 Introduction -2 Sentence Mode ------3 Letter Mode -------4 Word Mode -------5 Mixed Mode ------6 Leaderboard Introduction - This game is one of the best typing games in the world. There are three different modes in this game. This includes Word Mode, Sentence Mode, Letter Mode, and Mixed Mode. Each mode has its own difficulties and challenges. Sentence Mode - In Sentence Mode, you’ll need to type in the full sentences that will be displayed upon your screen. As the difficulty level rises, the sentences become more trickier and case-sensitive. Letter Mode - In Letter Mode, you’ll be given a combination of 2-3 letters and your job is to type any word in the English dictionary that contains those letters. However you cannot use the same words again, and the score depends on the length of the word typed in. Word Mode -  In Word Mode, you’ll be given a word to spell from the English dictionary. The points awarded are equal to the length of the word. Mixed Mode - In Mixed Mode, sentences and words are mixed together. Leaderboard - But that's not all! You can climb your way up the leaderboard by earning points in each mode. Think you have what it takes to be the Word Game champion? Then let's get started"

        instructions_label = scrolledtext.ScrolledText(start, width=50, height=10, wrap=tk.WORD)
        instructions_label.insert(tk.END, instructions)
        instructions_label.pack()

        yes_button.pack_forget()
        no_button.pack_forget()
        
        question_label.configure(text='Do you now know how to play?', font=('Comic Sans MS', 14), fg='black')
        # Create a new function to handle the user's second answer
        def handle_second_answer(answer):
            if answer == 'yes':
                audio.play_file("sounds/click.mp3")
                instructions_label.pack_forget()
                title_label = tk.Label(start, text='The Word Game', font=('Comic Sans MS', 20), fg='blue')
                title_label.pack()
                yes_button2.pack_forget()  
                no_button2.pack_forget()  
                question_label.pack_forget()
                start.destroy()
                
            elif answer == 'no':
              audio.play_file("sounds/click.mp3")
              messagebox.showinfo("Read Instructions", "Please Read Instructions Again")
              
                
        # Create a button to get the user's second answer
        yes_button2 = tk.Button(start, text='Yes', font=('Comic Sans MS', 12), command=lambda: handle_second_answer('yes'))
      
        no_button2 = tk.Button(start, text='No', font=('Comic Sans MS', 12), command=lambda: 
                               handle_second_answer('no'))
        yes_button2.pack()
        no_button2.pack()
      

# Create a button to get the user's first answer
yes_button = tk.Button(start, text='Yes', font=('Comic Sans MS', 12), command=lambda: handle_answer('yes'))
no_button = tk.Button(start, text='No', font=('Comic Sans MS', 12), command=lambda: handle_answer('no'))
yes_button.pack()
no_button.pack()



start.mainloop()


mixemode = [1, 2, 3]

counter = 0
used_words = []
repeat = "o"
while repeat == "y" or "o":

  def typing_game(mode, difficulty):
    word_mode = True if mode == "word" else False
    

    score = 0
    start_time = time.time()
    

    if difficulty == "1" and mode != "word":
      time_limit = 60
      timelabel = tk.Label(window, text = " Time limit: " + str(time_limit))
      what_mode = tk.Label(window, text = " Mode: " + mode)
      what_mode.pack()
      timelabel.pack()
    if difficulty == "2" and mode != "word":
      time_limit = 30
      timelabel = tk.Label(window, text = " Time limit: " + str(time_limit))
      what_mode = tk.Label(window, text = " Mode: " + mode)
      what_mode.pack()
      timelabel.pack()
    elif difficulty == "3" and mode != "word":
      time_limit = 15
      timelabel = tk.Label(window, text = " Time limit: " + str(time_limit))
      what_mode = tk.Label(window, text = " Mode: " + mode)
      what_mode.pack()
    if difficulty == "1" and mode == "word":
      time_limit = 120
      timelabel = tk.Label(window, text = " Time limit: " + str(time_limit))
      what_mode = tk.Label(window, text = " Mode: " + mode)
      what_mode.pack()
      timelabel.pack()
    elif difficulty == "2" and mode == "word":
      time_limit = 60
      timelabel = tk.Label(window, text = " Time limit: " + str(time_limit))
      what_mode = tk.Label(window, text = " Mode: " + mode)
      what_mode.pack()
      timelabel.pack()
    elif difficulty == "3" and mode == "word":
      time_limit = 30
      timelabel = tk.Label(window, text = " Time limit: " + str(time_limit))
      what_mode = tk.Label(window, text = " Mode: " + mode)
      what_mode.pack()
      timelabel.pack()

    while time.time() - start_time < time_limit:
      if mode == "mixed":
        wsl = random.choice(mixemode)
        if wsl == 1:
          letter = random.choice(letters)
          type_word.configure(text=f'Type a word that has these letters: "{letter}"')
          type_word.pack()
          lettertype.pack()
          button.pack()
    
        if wsl == 2:
          if difficulty == "1":
            word = random.choice(es_words)
          if difficulty == "2":
            word = random.choice(med_words)
          if difficulty == "3":
            word = random.choice(hard_words)

          entered_word = input(Fore.BLUE + f"Type the word: {word}\n" +
                             Fore.GREEN)

          if entered_word == word:
            if difficulty == "1":
              score += len(word)
            if difficulty == "2":
              score += len(word) * 1.5
            if difficulty == "3":
              score += len(word) * 3
            print(Fore.GREEN + "Correct!\n")
            score = round(score)
          else:
            score -= len(word)
            print(Fore.RED + "Incorrect!\n")
        if wsl == 3:
          sentence = random.choice(sentences)
          entered_sentence = input(Fore.BLUE +
                                 f"Type the sentence: {sentence}\n" +
                                 Fore.GREEN)

          if difficulty == "3" and entered_sentence == sentence:
            score += len(sentence) * 2
            print(Fore.GREEN + "Correct!\n")
          elif entered_sentence.lower() in sentence.lower():
            if difficulty != "3":
              score += len(entered_sentence) * 0.75

              print(Fore.GREEN + "Correct!\n")
          else:
            print(Fore.RED + "Incorrect!\n")
        
      
      if mode == "letter":
        letter = random.choice(letters)
        entered_word = input(Fore.BLUE + f"Type word that has these letters: {letter} \n" +
                             Fore.GREEN)
        if letter in entered_word:
          if entered_word in used_words:
            print(Fore.RED + 'Invalid word! Word already used. /n')
          if entered_word in dictionary and entered_word not in used_words:
            used_words.append(entered_word)
            score += len(entered_word) * int(difficulty)
            print(Fore.GREEN + "Correct!\n")
            
          if entered_word not in dictionary:
            print(Fore.RED + "Incorrect!\n")
        else:
          print(Fore.RED + "Incorrect!\n")
      if word_mode:
        if difficulty == "1":
          word = random.choice(es_words)
        if difficulty == "2":
          word = random.choice(med_words)
        if difficulty == "3":
          word = random.choice(hard_words)

        entered_word = input(Fore.BLUE + f"Type the word: {word}\n" +
                             Fore.GREEN)

        if entered_word == word:
          if difficulty == "1":
            score += len(word)
          if difficulty == "2":
            score += len(word) * 1.5
          if difficulty == "3":
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

        if difficulty == "3" and entered_sentence == sentence:
          score += len(sentence) * 2
          print(Fore.GREEN + "Correct!\n")
        elif entered_sentence.lower() in sentence.lower():
          if difficulty != "3":
            score += len(entered_sentence) * 0.75

            print(Fore.GREEN + "Correct!\n")
        else:
          print(Fore.RED + "Incorrect!\n")

      print(Fore.WHITE + f"Score: {score}\n")
      print(Fore.LIGHTYELLOW_EX +
            f"Time elapsed: {int(time.time() - start_time)} seconds\n")
    score = round(score)
    print(f"{name}, Your final score is: {score}")

    update_leaderboard(name, score, mode)
    leaderboard_button = tk.Button(window, text="Display Leaderboard",command=display_leaderboard(), pady = 10)
    leaderboard_button.pack() # create a scrolled text widget to display the leaderboard
    leaderboard_text = scrolledtext.ScrolledText(window, width=65, height=20, state="disabled", wrap=tk.WORD)
    leaderboard_text.pack(pady=10)

    repeat = input("Do you want to play again?(y/n) ")
    if repeat == "n":
      quit()

  if __name__ == "__main__":
    def enter(): 
      global name 
      global difficulty
      global mode
      audio.play_file("sounds/click.mp3")
      mode = mode_var.get()
      difficulty = difficulty_var.get()
      name = name_var.get() 
      
      if mode_var.get() in ["word", "sentence", "letter", "mixed"] and difficulty_var.get() in ["1", "2", "3"]:
        invalid_label.pack_forget()
        nameentry.pack_forget()
        name_label.pack_forget()
        entry.pack_forget()
        mode_label.pack_forget()
        wordbut.pack_forget()
        senbut.pack_forget()
        letterbut.pack_forget()
        mixbut.pack_forget()
        diff_label.pack_forget()
        easy_button.pack_forget()
        med_button.pack_forget()
        hard_button.pack_forget()
        
        
        typing_game(mode, difficulty)

      else:
        invalid_label.pack()

    
      
    



      
      

    # create a difficulty window
    window = tk.Tk()
    invalid_label = tk.Label(window, text='Invalid Input', font=('Comic Sans MS', 10), fg='red')
    window.title("Difficulty, Mode and Name")
    window.geometry("500x700")

    title_name = tk.PhotoImage(file="images/title.gif", master=window) 
    modescreen_label = tk.Label(window)
    small_titlescreen = title_name.subsample (5, 5) # create a new image that is half as large as the original one
    modescreen_label.image = small_titlescreen
    
    modescreen_label.config(image = modescreen_label.image)
    modescreen_label.pack()
    

    name_label = tk.Label(window, text="Enter Name:")
    if repeat != "y":
      name_label.pack()
      name_var = tk.StringVar()
      nameentry = tk.Entry(window, textvariable=name_var)
      nameentry.pack()
      entry = tk.Button(window, text='Submit', command=enter, width=10, height=2)
      
    lettertype = tk.Entry(window)
    type_word = tk.Label(window, text=f"Type a word that has these letters: {letters}")
    button = tk.Button(text="Enter word", command=wordisin)
    window.bind("<Enter>", button_press)


    mode_label = tk.Label(window, text="Select Mode:")
    mode_label.pack()
    mode_var = tk.StringVar()
    wordbut = tk.Radiobutton(window, text="Word", variable=mode_var, value="word")
    senbut = tk.Radiobutton(window, text="Sentence", variable=mode_var, value="sentence")
    letterbut = tk.Radiobutton(window, text="Letter", variable=mode_var, value="letter")
    mixbut = tk.Radiobutton(window, text="Mixed", variable=mode_var, value="mixed")
    
    
    wordbut.pack()
    senbut.pack()
    letterbut.pack()
    mixbut.pack()
    
    

    
    diff_label = tk.Label(window, text="Select Difficulty Level:")
    
    difficulty_var = tk.StringVar()
    
    easy_button = tk.Radiobutton(window, text="Easy", variable=difficulty_var, value="1")
    med_button = tk.Radiobutton(window, text="Medium", variable=difficulty_var, value="2")
    hard_button = tk.Radiobutton(window, text="Hard", variable=difficulty_var, value="3")

  
    diff_label.pack()
    easy_button.pack()
    med_button.pack()
    hard_button.pack()
    
    
    entry.pack(pady=20)
    window.mainloop()

    

