import random

user_action = input("Vali nendest üks (kivi, paber, käärid): " )
possible_actions = ["kivi", "paber", "käärid"]
computer_action = random.choice(possible_actions)
print(f"\nSa valid {user_action}, arvuti valib {computer_action}. \n")

if user_action == computer_action
    print(f"Mõlemad mängijad valisid) {user_action}. See on viik!")
elif user_action == "kivi"
    if computer_action == "käärid":
        print("Kivi hävitab käärid! Sa võitsid!")
    else: 
        print("Paber hävitab kivi! Sa kaotasid.")
elif user_action == "paber"
    if computer_action == "kivi":
        print("Paber hävitab kivi! Sa võitsid!")
    else:
        print("Käärid hävitavad paberi! Sa kaotasid.")
elif user_action == "käärid"
    if computer_action == "paber":
        print("Käärid lõikavad paberit! Sa võitsid!")
    else: 
        print("Kivi hävitab käärid! Sa kaotasid.")
