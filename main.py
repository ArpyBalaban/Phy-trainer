import json

def loadExistingUsers():
    with open('user.json') as existing_users:
        users = json.load(existing_users)
        return users


def check_for_username(username, users):
    for user in users:
        s = user["name_surname"]
        if(username == s):
            print(username)
            return 0

def save_to_file(users):
    f = open("user.json","w")
    f.write(json.dumps(users,indent = 2))
    f.close

def add_user():
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
                "health_restrictions" : [0],
                }
        user["name_surname"] = input("Please insert your name and surname: ")
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

        user["starting_weight"] = input("Please insert your current weight: ")
        user["height"] = input("Please insert your height in centimeters: ")
        user["fitness_level"] = input("Please select your fitness level (1 being the lowest, 3 the highest): ")
        user["health_restrictions"] = input("Please enter any health restrictions you may have ")
        return user
	

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

    print("Hello, I am Phy-trainer")
    insert_mode = input("Are you a new user? (yes/no)")
    n = 1
    while(n != 0):
        if(insert_mode == "no"):
            username =input("Enter username: ")
            n = check_for_username(username, users)

            if(n == 0):
                print("Welcome back "+ username)
                break
            else:
                print("Sorry you are not a current user")
                answer =input("Would you like to register? (yes,no): ")
                while(True):
                    if(answer == "no"):
                        print("Goodbye")
                        n = 0
                        break
                    elif(answer == "yes"):
                        insert_mode = "yes"
                        break
                    else:
                        print("please enter yes or no")


        elif(insert_mode == "yes"):
            current_user = add_user()
            users.append(current_user)
            save_to_file(users)
            break

        else:
            print ("please enter a valid input ")
    
    #recommend_exercise(current_user)
    save_to_file(users)


main()
