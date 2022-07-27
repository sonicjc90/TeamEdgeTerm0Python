######################### Welcome: Start of the game ################################
ans = " "
inventory = []
active = True


def start_game(): 
    well = input("Enter your name here --> ")
    welcome = (f"\n Welcome {well} Joestar, you are an 18 year old child whom belongs to the infamous Joestar family. Recently, a new addition to your family known as Dio Brando has been acting strange around you and your family. It is now your job to find out what he is up to. Good Luck! ")
    print(welcome)

# ---------------------------------------------

#Instructions:

def instruct():
    print("\n----------- How to play this game: -----------")
    print("-------------------------------------------------\n")
    print("To go to different locations: Type in 'go to' and then type in the location.\n")
    print("To interact with items: Type in 'take' and then type in the item you would like to take. This will add the item to your inventory\n")
    print("To interact with NPC's, Type in 'interact' and then the name of the Npc .\n")
    print("To exit: Type in 'exit'. This will take you back outside to the beginning.\n")
    print("If you ever get stuck just type in 'help' and all these commands will pop back up.\n")




# ---------------------------------------------

#Items


class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
    
    def __repr__(self):
        return f"Item: {self.name}\n Desc: {self.desc}"

item1 = Item("Hamon","Sun Breathing Technique. Through the use of controlled breathing, the user can fill their body and attacks with sunlight energy, making it very effective against almost anything.")
item2 = Item("Sword","A very sharp sword. This weapon has the words 'Luck' inscribed on the side of it.")
item3 = Item("Furnace","Just a regular furnace... However keep your dog 'Danny' away from it at ALL COSTS....... Please.")
item4 = Item("Boxing Gloves","Your average boxing gloves.")
item5 = Item("White Pill","Your father has been being given these pills by Dio on a relatively daily basis. ")
item6 = Item("Photo of unknown Crusaders","")
item7 = Item("Special Food","Food given to you by Lady Irina. Smells very good.")
item8 = Item("Book","This appears to be Dio's Diary.")
item9 = Item("Stone Mask","Strange artifact that was found by your Father. You sense an ominous aura eminating from it.")
item10 = Item("Strange Arrow","?????????. This artifact is unkown. Where exactly did it come from. On the tip of the arrow there is an ancient language that reads 'STAND'. What could this mean?")





# ---------------------------------------------

#Dictionaries for Characters:

class Npc:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
    
    def __repr__(self):
        return f"Name: {self.name}\n Desc: {self.desc}"

npc1 = Npc("Jonathan Joestar","Son of George Joestar and your brother.\n")

npc2 = Npc("William Zepelli","Current Master of sun breathing technique known as Hamon\n")

npc3 = Npc("George Joestar", "Father of Jonathan, Dio, and you. Seems to have gotten ill after a while.\n")

npc4 = Npc("Lady Irina", "Love intrest of your brother Jonathan\n")

npc5 = Npc("Royal Guards","They stand here in order to protect and serve the Joestar family. In other words your family is rich 😝\n")

npc6 = Npc("Speedwagon", "Friend of Zepelli and Jonathan. Greatest Guy you'll ever meet. Also Funny Meme man go brrrrr.\n")

npc7 = Npc("Dio Brando","Your other brother and somewhat friend. He's been really nice to everyone over the past few years. However, this behavior has always seemed strange to you considering how much of a bully he used to be.\n ")






# ---------------------------------------------

#Locations:

class Location:
    def __init__(self, name, desc, item, npc, next):
        self.name = name
        self.desc = desc
        self.item = item 
        self.npc = npc
        self.next = next

    def __repr__(self):
        return f"{self.name}\n Description:\n {self.desc}\n \nItems: \n - {self.item}\n \nNpc/Npc's: \n- {self.npc} \n \nAvailable locations: \n \n-{self.next}  "

out = Location( "Outside of the Mansion", "You are outside of the Joestar Mansion. You stand there in awe as you feel happy and proud to be apart of such a nice and weathy family.", [item2.name, item3.name, item4.name], [],"Forest,Inside of Mansion/Living Room")
forest = Location("Forest", "Surrounding the Joestar Mansion is the forest. You enter the forest and find two people standing there and they seem to be punching a rock.", [], [npc1.name, npc2.name], "Outside of the Mansion")
bed = Location("Bedroom", "The bedroom of your father George Joestar.", [item5.name], [npc3],"Inside of Mansion/Living Room")
read = Location("Library", "The kingdom of knowledge. You are surrounded by thousands of bookshelves with tens of thousands of books.", [item6.name, item7.name, item8.name], [npc4.name],"Inside of Mansion/Living Room")
living = Location("Inside of Mansion/Living Room", "This wonderful mansion covered in a rich red and dark brown holds many items and people within it.", [item9.name, item10.name], [npc5.name, npc6.name, npc7.name], f"{out.name}, {bed.name}, {read.name}")




# ---------------------------------------------

#Player misc:

class Player:
    def __init__(self, forward, back, health):
        self.forward = True
        self.back = True
        self.health = 100
        





# ---------------------------------------------

# Controls:



# ---------------------------------------------

start_game()
instruct()
#Starting Point: 
def prompt_user():
    ans=input("Where would you like to go?\n")
    return ans

print(f"-{out.name}")
print("________________________")
print(f"-{forest.name}")
print("________________________")
print(f"-{living.name}")

# ---------------------------------------------

#Command Center |3l4ZE
def take(ans):
    global inventory
    if ans == "take Sword":
        inventory.append(item2.name)
        print(item2)
    elif ans == "take Furnace":
        print("You cannot take this item.")
    elif ans == "take Boxing Glove":
        inventory.append(item4.name)
        print(item4)
    elif ans == "take White Pill":
        inventory.append(item5.name)
        print(item5)
    elif ans == "take Photo of Crusaders":
        inventory.append(item6.name)
        print(item6)
    elif ans == "take Book":
        inventory.append(item8.name)
        print(item8)
    elif ans == "take Strange Arrow":
        inventory.append(item10.name)
        print(item10)

def talk(ans):
    global inventory
    if ans == "interact Jonathan Joestar":
        print(npc1)
        inventory.append(item1)
    elif ans == "interact William Zepelli":
        print(npc2)
    elif ans == "interact George Joestar":
        print(npc3)
    elif ans == "interact Lady Irina":
        print(npc4)
        inventory.append(item7)
    elif ans == "interact Royal Guard":
        print(npc5)
    elif ans == "interact Speedwagon":
        print(npc6)
    elif ans == "interact Dio Brando":
        print(npc7)

def go(ans):
    if ans == "go to Outside of the Mansion":
        print(f"\n{out}")
    elif ans == "go to Forest":
        print(f"\n{forest}")
    elif ans == "go to Inside of Mansion" or ans == "go to Living Room" or ans == "go to Inside of Mansion/Living Room":
        print(f"\n{living}")
    elif ans == "go to Bedroom":
        print(f"\n{bed}")
    elif ans == "go to Library":
        print(f"\n{read}")
    
def ask(ans):
    global inventory
    if ans == "inventory":
        print(f"Current Items: {inventory}")

def leave(ans):
    if ans == "exit" or "Exit":
        print(f"-{out.name}")
        print("________________________")
        print(f"-{forest.name}")
        print("________________________")
        print(f"-{living.name}")


    if ans == "Help" or "help":
        instruct()


class Base:
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack
        self.damage = damage
        self.defense = defense
        self.health = 100
    def __repr__(self)


def fight():
    global inventory




    if "Hamon"and"Sword"and"Boxing Glove"and"Special Food" in inventory:
        fight()
        
    


# def transfer():
#this function can take in a string and store it in an array

 

# ---------------------------------------------

#Game Loop


while active:
    
    ans = prompt_user()
    take(ans)
    talk(ans)
    go(ans)
    ask(ans)
    

    



# ---------------------------------------------




