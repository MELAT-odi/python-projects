import random
print("=" * 30)
print("  Welcome To Gussing game")
print("=" * 30)

def guessing_game():
        secret_number= random.randint(1,20)
        print("Guess the number from 1 upto 20")
        print("You have 5 attept Good Luck!")
        count=0
        while count<5:
            try:
                guess =int(input("enter ur guess: "))
            except ValueError:
                print("please enter a number")
                continue
            if 1<=guess<=20:
                if guess==secret_number:
                    print("correct🎉🏆")
                    break
                elif guess>secret_number:
                    print("Too High📈")
                    count+=1
                elif guess<secret_number:
                    print("Too low📉")
                    count+=1
            else:
                print("please enter in number with in a range")
        else:
            print(f"Game Over! The Number is {secret_number}")

while True:
    guessing_game()
    play=input("Do you want to play again? (y/n): ")
    if play.lower() !="y":
        break
