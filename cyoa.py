######################### Welcome: Start of the game ################################

def start_game(): 
    well = input("Enter your name here --> ")
    welcome = (f"\n Welcome {well} Joestar, you are an 18 year old child whom belongs to the infamous Joestar family. Recently, a new addition to your family known as Dio Brando has been acting strange around you and your family. It is now your job to find out what he is up to. Good Luck! ")
    print(welcome)

# ---------------------------------------------

#Instructions:

def instruct():
    print("\nHow to play this game:\n")
    print("To go to different locations: Type in 'go to' and then type in the location.\n")
    print("To interact with items: Type in 'take' and then type in the item you would like to take. This will add the item to your inventory\n")
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

npc1 = Npc("Jonathan Joestar","Son of George Joestar and your brother.")


npc2 = Npc("William Zepelli","Current Master of sun breathing technique known as Hamon")


npc3 = Npc("George Joestar", "Father of Jonathan, Dio, and you. Seems to have gotten ill after a while.")


npc4 = Npc("Lady Irina", "Love intrest of your brother Jonathan")


npc5 = Npc("Royal Guards","They stand here in order to protect and serve the Joestar family. In other words your family is rich 😝")


npc6 = Npc("Speedwagon", "Friend of Zepelli and Jonathan. Greatest Guy you'll ever meet. Also Funny Meme man go brrrrr.")


npc7 = Npc("Dio Brando","Your other brother and somewhat friend. He's been really nice to everyone over the past few years. However, this behavior has always seemed strange to you considering how much of a bully he used to be. ")






# ---------------------------------------------

#Locations:

class Location:
    def __init__(self, name, desc, item, npc):
        self.name = name
        self.desc = desc
        self.item = item 
        self.npc = npc
        self.next = []
    def __repr__(self):
        return f"{self.name}\n Description:\n {self.desc}\n \nItems: \n - {self.item}\n \n Npc/Npc's: {self.npc} Available locations: \n \n -{self.next}  "

out = Location( "Outside of the Mansion", "You are outside of the Joestar Mansion. You stand there in awe as you feel happy and proud to be apart of such a nice and weathy family.", [item2.name, item3.name, item4.name], [])
forest = Location("Forest", "Surrounding the Joestar Mansion is the forest. You enter the forest and find two people standing there and they seem to be punching a rock.", [item1.name], [npc1, npc2])
living = Location("Inside of Mansion/Living Room", "This wonderful mansion covered in a rich red and dark brown holds many items and people within it.", [item9.name, item10.name], [npc5, npc6, npc7])
bed = Location("Bedroom", "The bedroom of your father George Joestar.", [item5.name], [npc3])
read = Location("Library", "The kingdom of knowledge. You are surrounded by thousands of bookshelves with tens of thousands of books.", [item6.name, item7.name, item8.name], [npc4])





# ---------------------------------------------

#Player misc:

class Player:
    def __init__(self, forward, back, health):
        self.forward = True
        self.back = True
        self.health = 100





# ---------------------------------------------

# Controls:

# def movement():






# ---------------------------------------------

start_game()
instruct()
#Starting Point: 

print("Where would you like to look first?\n")

print(f"-{out.name}")
print("________________________")
print(f"-{forest.name}")
print("________________________")
print(f"-{living.name}")

where = input("----> ")

# ---------------------------------------------

#Controls

if where == "Outside of the Mansion":
    print(f"\n{out}")

# ---------------------------------------------


#Game Loop

# while

# ---------------------------------------------

