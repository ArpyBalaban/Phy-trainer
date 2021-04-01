import json

def get_user_data():
    name = input("Hello there!, What's your name/surname?")


def loadExistingUsers():
    with open('user.json') as existing_users:
        users = json.load(existing_users)
        return users


def chack_for_username(username, users):
    for user in users:
        s = users.get("Name_Surname")
        if(username == s):
            print(username)

def save_to_file(users):
    f = open("user.json","w")
    f.write(json.dumps(users,indent = 2))
    f.close


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
    while (True):
        print("Hello, I am Phy-trainer")
        insert_mode = input("Are you a new user? (yes/no)")
        if(insert_mode == "no"):
            username =input("Enter username: ")
            check_for_username(username, users)
            break
        elif(insert_mode == "yes"):
            #current_user = Add_user()
            users.append(current_user)
            break
        else:
            print ("please enter a valid input ")
    
    #recommend_exercise(current_user)
    save_to_file(users)

def Add_user():
	user = {
		"name_surname" : "",
		"age" : 0,
		"gender" : [0],
		"starting_weight" : 0,
		"height" : 0,
		"fitness_level" : [0],
		"health_restrictions" : [0],
		}
	user["name"] = input("Please insert your name and surname: ")
	user["age"] = input("Please insert your age: ")
	user["gender"] = input("Please select your gender")
	user["starting_weight"] = input("Please insert your current weight: ")
	user["height"] = input("Please insert your height: ")
	user["fitness_level"] = input("Please select your fitness level: ")
	user["health_restrictions"] = input("Please select your health conditions from the list: ")
	





main()
