##########################################################
#
#     CLASSES - Coach Steph examples
#
##########################################################

class Engineer:
    def __init__(self, name, age, grade, group_mates):
        self.name = name
        self.age = age
        self.grade = grade
        self.group_mates = group_mates
        #Could be Present or Absent - True or False
        self.attendance = []
        self.is_active = True
        self.device = {"computer": "", "serial_number": "", "asset_tag": ""}

    def __repr__(self):
        return f"Name: {self.name}, Age:{self.age}, Grade:{self.grade}"

    def take_attendance(self, is_present):
        if is_present.lower() == "present":
            self.attendance.append(True)
        else: 
            self.attendance.append(False)

    def get_present_days(self):
        present_days = 0
        for present in self.attendance:
            if present == True:
                present_days += 1
        return present_days

    def add_device(self, computer, serial_number, asset_tag):  
        self.device["computer"] = computer
        self.device["serial_number"] = serial_number
        self.device["asset_tag"] = asset_tag
        print(f"{self.name} device updated: {self.device}")

#
# Engineer OBJECTS:     
engineer_1 = Engineer("Natanael", 13, "9th", ["JC", "Benny", "Mujtaba"])
engineer_2 = Engineer("Kale", 16, "10th", ["Steven", "Ransom", "Nour"])
engineer_3 = Engineer("Chantel", 17, "11th", ["Maya", "Niki", "Indira", "Tiffany"])

# print(engineer_1)
# print(engineer_2)
# print(engineer_3)

# print(engineer_2.name)
# print(engineer_2.attendance)

engineer_2.take_attendance("Present")
engineer_2.take_attendance("Present")
engineer_2.take_attendance("Present")
engineer_2.take_attendance("Present")

# print(engineer_2.attendance)

# print(engineer_2.get_present_days())

engineers = [engineer_1, engineer_2, engineer_3]

# print("Class Present Days: ")
# for engineer in engineers:
#     print(f"{engineer.name} was present {engineer.get_present_days()} days")

for engineer in engineers: 
    print(f"Time to add {engineer.name}'s device: ")
    user_asset_tag = input("Please enter the asset tag #: ")
    user_serial_number = input("Please enter the serial #: ")
    user_computer_type = input("Please enter the computer type: ")
    engineer.add_device(user_computer_type, user_serial_number, user_asset_tag)
    print("-----------------------------------------")



#########################################################

#DICTIONARIES

#########################################################

engineer_1 = {
    "name": "Natanael",
    "age": 13,
    "grade": "9th",
    "group_mates": ["JC", "Benny", "Mujtaba"]
}

engineer_2 = {
    "name": "Kale",
    "age": 16,
    "grade": "10th",
    "group_mates": ["Steven", "Ransom", "Nour"]
}

engineers = [engineer_1, engineer_2]

print(engineer_1["name"])
print(engineer_1["group_mates"])

for current_engineer in engineers:
    print(f'Team Edge engineer {current_engineer["name"]} is in {current_engineer["grade"]} grade')
    print("These are their group mates: ")
    for person in current_engineer["group_mates"]:
        print(person)

print(engineer_1.get("grade"))
















# -------------------------------------------------------------------------------

#MY WORK

#--------------------------------------------------------------------------------
class Superhero:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.damage = damage
        self.defense = defense
        self.health = 100

    def __repr__(self):
        return f"Supername: {self.name}"

    def attack(self, opponent):
        attack_style = input(f"Which attack will you use?: {self.attack}")
        opponent.health_points = opponent.health_points - self.health

    def alive(self):
        if hero1(self.health) > 0 and 

hero1 = Superhero("Flash", {"Thunderbolt": 20})
villian1 = Superhero("Zoom", {"Grip"}, )

print(hero1)
