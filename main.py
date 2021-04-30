import json
from random import randint

def loadExercises():
    with open('data.json') as existing_exe:
        exercises = json.load(existing_exe)
        return exercises


def loadExistingUsers():
    with open('user.json') as existing_users:
        users = json.load(existing_users)
        return users


def check_for_username(username, users):
    for user in users:
        s = user["name_surname"]
        if(username == s):
            return user

def save_to_file(users):
    f = open("user.json","w")
    f.write(json.dumps(users,indent = 2))
    f.close

def add_user(users):
        user = {"name_surname" : "",
                "age" : 0,
                "gender" : 0,
                "weight" : {
                    "starting_weight": 0,
                    "weight_goal": 0,
                    "current_weight": 0
                },
                "height" : 0,
                "fitness_level" : 0,
                "health_restrictions" : [0]
                }
        while(True):
            possable_username = user["name_surname"] = input("Please insert your name and surname: ")
            if not(check_for_username(possable_username, users)):
                break
            print("That username is taken, please enter a different one. ")

        user["age"] = input("Please insert your age: ")
        while(True):
            user["gender"] = input("Please select your gender F/M): ")
            if(user["gender"] == "F"):
                user["gender"] = 0
                break
            elif(user["gender"] == "M"):
                user["gender"] == 1
                break
            else:
                print("please enter a valid gender ")

        a = int(input("Please insert your current weight: "))
        user["starting_weight"] = a
        user["weight"]["current_weight"] = a
        user["height"] = int(input("Please insert your height in centimeters: "))
        user["fitness_level"] = int(input("Please select your fitness level (1 being the lowest, 3 the highest): "))
        user["health_restrictions"] = input("Please enter any health restrictions you may have ")
        return user
	

def calculate_bmi(current_user):

    meter= current_user["height"] / 100
    meter_squared = meter**2
    bmi = current_user["weight"]["current_weight"]/meter_squared
    bmi = round (bmi , 1)
    if (bmi <= 18.5):
        bmi_status = "U" #U for underweight
        print("According to your BMI, it is suggested that you gain more weight\n the exercises recommended to you will aim to bulid muscle. ")
    elif (bmi >= 25):
        bmi_status = "O" #O for overweight
        print("According to your BMI, it is suggested that you lose weight,\n the exercises recommended to you will aim to burn fat. ")
    elif (bmi < 25 and bmi > 18.5):
        bmi_status = "N" #N for normal
        print("According to your BMI, you weight is normal,\n the exercises recommended to you will aim to keep you in shape. ")

    return bmi_status

def recommend_exercise(current_user, exercises):
    selection = []
    bmi_status = calculate_bmi(current_user)
    for exercise in exercises:
        for letter in exercise["bmi_recommended"]:
            if(letter == bmi_status):
                selection.append(exercise)

    l = len(selection)
    i = randint(0, l-1)

    for types in selection[i]["type"]:
        if (types["level"] == current_user["fitness_level"]):
            chosen = types

    return chosen





def main():
    print(""" /$$$$$$$  /$$                           /$$                        /$$                              
| $$__  $$| $$                          | $$                       |__/                              
| $$  \ $$| $$$$$$$  /$$   /$$         /$$$$$$    /$$$$$$  /$$$$$$  /$$ /$$$$$$$   /$$$$$$   /$$$$$$ 
| $$$$$$$/| $$__  $$| $$  | $$ /$$$$$$|_  $$_/   /$$__  $$|____  $$| $$| $$__  $$ /$$__  $$ /$$__  $$
| $$____/ | $$  \ $$| $$  | $$|______/  | $$    | $$  \__/ /$$$$$$$| $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$      | $$  | $$| $$  | $$          | $$ /$$| $$      /$$__  $$| $$| $$  | $$| $$_____/| $$      
| $$      | $$  | $$|  $$$$$$$          |  $$$$/| $$     |  $$$$$$$| $$| $$  | $$|  $$$$$$$| $$      
|__/      |__/  |__/ \____  $$           \___/  |__/      \_______/|__/|__/  |__/ \_______/|__/      
                     /$$  | $$                                                                       
                    |  $$$$$$/                                                                       
                     \______/                                                                        """)
    users = []
    users = loadExistingUsers()
    exercises = []
    exercises = loadExercises()

    print("Hello, I am Phy-trainer")
    insert_mode = input("Are you a new user? (yes/no)")
    f = 1
    while(f != 0):
        if(insert_mode == "no"):
            username =input("Enter username: ")
            n = check_for_username(username, users)

            if(n):
                print(""" _                      _   _       
| |                    | | (_)      
| | ___   __ _  ___  __| |  _ _ __  
| |/ _ \ / _` |/ _ \/ _` | | | '_ \ 
| | (_) | (_| |  __/ (_| | | | | | |
|_|\___/ \__, |\___|\__,_| |_|_| |_|
          __/ |                     
         |___/                      """)
                print("Welcome back "+ username)
                while(True):
                    rec_exe =recommend_exercise(n, exercises)
                    print(""".......................................................................
.   o   \ o /  _ o        __|    \ /     |__         o _  \ o /   o   .
.  /|\    |     /\   __\o   \o    |    o/     o/__   /\     |    /|\  .
.  / \   / \   | \  /) |    ( \  /o\  / )    |   (\  / |   / \   / \  .
.......................................................................""")
                    print("Do "+ rec_exe["name"] + " this many times")
                    print (""" ________________________________________""")
                    print("Here are the instructions: " + rec_exe["instructions"])
                    print("____________________________________________")
                    ans = input ("When you are ready to switch exercises - press Y,\nWhen you want to quit: press Q\n")
                    if (ans == "Q"):
                        f = 0
                        break

                break
            else:
                print("Sorry you are not a current user")
                answer =input("Would you like to register? (yes,no): ")
                while(True):
                    if(answer == "no"):
                        print(""" _____                 _ _                
|  __ \               | | |               
| |  \/ ___   ___   __| | |__  _   _  ___ 
| | __ / _ \ / _ \ / _` | '_ \| | | |/ _ |
| |_\ \ (_) | (_) | (_| | |_) | |_| |  __/
 \____/\___/ \___/ \__,_|_.__/ \__, |\___|
                                __/ |     
                               |___/      """)
                        f = 0
                        break
                    elif(answer == "yes"):
                        insert_mode = "yes"
                        break
                    else:
                        print("please enter yes or no")


        elif(insert_mode == "yes"):
            current_user = add_user(users)
            users.append(current_user)
            save_to_file(users)
            rec_exe = recommend_exercise(current_user, exercises)
            break

        else:
            print ("please enter a valid input ")
    
    save_to_file(users)


main()
