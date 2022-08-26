import random
def headtail(ai_first, player_first):
    def batball(ai_first, player_first):
        while True:
            bell = str.lower(input("You have won!\nWould you like to bat first or field first? (f for field, b for bat): "))
            if (bell[0] == "f"):
                ai_first, player_first= True, False
                print("Ok. I am batting first then.")
                break
            elif (bell[0] == "b"):
                player_first, ai_first = True, False
                print("Ok. You are batting first then.")
                break
        return {"AI": ai_first, "PLAYER": player_first}
    def ai_batball(ai_first, player_first, ch):
        while True:
            print("Alas! I have won!")
            if (ch == "bat"):
                ai_first, player_first= True, False
                print("I choose bat. So start bowling up.")
                break
            else:
                player_first, ai_first = True, False
                print("I choose to field. So you better bat up.")
                break
        return {"AI": ai_first, "PLAYER": player_first}
    ch = random.choice(["bat", "field"])
    while True:
        heta = str.lower(input("Head or Tail?(h/t): "))
        if (heta[0] == "h" or heta[0] == "t"):
            i = random.randint(1, 10)
            if (i % 2 != 0):
                choice = batball(ai_first, player_first)
                break
            else:
                choice = ai_batball(ai_first, player_first, ch)
                break
    return choice
def playerScore(player_score, ai_score, target):
    print("\nYou are batting now!\n")
    while True:
        zp = int(input("Enter your value(1-6): "))
        if (0 < zp < 7):
            i = random.randint(1, 6)
            if(target == False):
                if (zp != i):
                    player_score = player_score + zp
                    print(f"Your choice: {zp}\nMy choice: {i}\nYour Total Score: {player_score}\n\n")
                else:
                    print(f"My choice: {i}\nYou are OUT! Your total score : {player_score}\n\n")
                    break
            else:
                if (zp != i):
                    player_score = player_score + zp
                    print(f"Your choice: {zp}\nMy choice: {i}\nYour Total Score: {player_score}\nRun Left: {ai_score - player_score}\n\n")
                    if ((ai_score - player_score) < 0):
                        print(f"You have won!\nYour Final score: {player_score}\nMy Final score: {ai_score}\n\n")
                        break
                else:
                    print(f"My choice: {i}\nYou are OUT! I WIN! \nYour total score: {player_score}\nMy total score: {ai_score}\nScore Difference: {ai_score - player_score}\n\n")
                    break
        else:
            print(f"Error! {zp} is either too high or too low. Value must be between 1 to 6!\n\n")
    return player_score
def aiScore(player_score, ai_score, target):
    print("\nYou are bowling now!\n")
    while True:
        zp = int(input("Enter your value(1-6): "))
        if (0 < zp < 7):
            i = random.randint(1, 6)
            if(target == False):
                if (zp != i):
                    ai_score = ai_score + i
                    print(f"My choice: {i}\nYour choice: {zp}\nMy Total Score: {ai_score}\n\n")
                else:
                    print(f"Your choice: {zp}\nI am OUT! My total score : {ai_score}\n\n")
                    break
            else:
                if (zp != i):
                    ai_score = ai_score + i
                    print(f"My choice: {i}\nYour choice: {zp}\nMy Total Score: {ai_score}\nRun Left: {player_score - ai_score}\n\n")
                    if ((player_score - ai_score) < 0):
                        print(f"I have won!\nYour Final score: {player_score}\nMy Final score: {ai_score}\n\n")
                        break
                else:
                    print(f"Your choice: {i}\nI am OUT! You WON!\nMy total score: {ai_score}\nYour total score: {player_score}\nScore Difference: {player_score - ai_score}\n\n")
                    break
        else:
            print(f"Error! {zp} is either too high or too low. Value must be between 1 to 6!\n\n")
    return ai_score
def main():
    ai_first, player_first, player_score, ai_score = False, False, 0, 0,
    choice = headtail(ai_first, player_first)
    if(choice['PLAYER'] == True):
        player_score = playerScore(player_score, ai_score, False)
        ai_score = aiScore(player_score, ai_score, True)
    elif(choice['AI'] == True):
        ai_score = aiScore(player_score, ai_score, False)
        player_score = playerScore(player_score, ai_score, True)
main()
handcricket.py
5 KB