#Magic8Ball.py
#Name:
#Date:
#Assignment:

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
  answers = [ 
    "As I see it, yes.", "Cannot predict now.", "Concentrate and ask again.", "Most likely.", "Ask again later.", "Don't rely on it.", "Interesting!."
    "Ask again later.",  "Don’t count on it.", "My reply is no.", "Reply hazy, try again.", "My sources say no.", "Yes,understood your consern.",
    "Better not tell you now.", "It is certain.", "It is decidedly so.", "Outlook not so good.", "It is certain.", "Amazing, let try it!", 
    "Signs point to yes.", "Very doubtful.", "Without a doubt.", "You may rely on it. ", "Yes – definitely."
  ]

  #Answer question randomly with one of the options from your earlier list.
  length = len(answers)
  r = random.random() * length
  r = int (r)
  print (r)
  response = answers [r]
  print (response)

if __name__ == '__main__':
  main()
