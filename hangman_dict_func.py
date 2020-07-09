import random 
name = "Hangman"
if name=="Hangman":
    def game():
        print("Good Luck ! ", name) 
        words = {1:['rainbow', 'computer', 'science', 'programming', 
		    'python', 'mathematics', 'player', 'condition', 
		    'reverse', 'water', 'board', 'marvel'],2:['run','swim','fight','blue','red']}
        nums=[1,2]
        n=random.choice(nums)
        word = random.choice(words[n]) 
        print("Guess the characters") 
        guesses = '' 
        turns = 12
        while turns > 0: 
            failed = 0
            for eachchar in word:
                if eachchar in guesses:
                    print(eachchar) 
                else: 
                    print("_") 
                    failed += 1
            if failed == 0: 
                print("You Win") 
                print("The word is: ", word) 
                break
            guess = input("guess a character:") 
            guesses += guess 
            if guess not in word: 
                turns -= 1
                print("Wrong") 
                print("You have", + turns, 'more guesses') 
                if turns == 0: 
                    print("You Loose") 
name = input("What is your name? ")
choice=input('start game: y or n >>>')
if choice=='y':
    game()