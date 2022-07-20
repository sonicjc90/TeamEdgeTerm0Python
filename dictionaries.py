#############################################################################
 #                                                                  
 #  Team Edge dictionaries: Dictionaries CHALLENGES 
 # 
 #  For this activity, you will be building a dictionary and with properties
 #  and methods. You will access the properties, set new values, and use
 #  the methods to change your dictionary state. What dictionary? Ask your coach.
 # 
 #  1. DEFINE: Make a dictionary and set its properties, printing changes in between.
 #  2. MODIFY: Add 2 new properties and assing values. Change existing values,
 #     including adding or updating values inside lists
 #  3. METHODS: Now its time to make some methods tha can make a change
 #     to your values, like a boolean, or they can print something about
 #     the dictionary. Nothing fancy, unless you fancy it.
 #  4. LITERALLY: Use string literals to put it all together in one statement.
 # 
 # #########################################################################/

print("------------------- CHALLENGE 1 : DEFINE    -------------------")

#Below is a simple example of a dictionary implementaion. 
#-->TODO: Add at least 3 comments to the dictionary below to demonstrate you understand its usage

dictionary = {
    "name": "box",
    "is_empty": True
}
#working with the dictionary:
dictionary["length"] = 12
dictionary["width"] = 8
dictionary["contents"] = ["thing 1", "thing 2", "thing 3"]
print(f"{dictionary['name']} is {dictionary['length']} {dictionary['width']}")
dictionary["contents"].append("thing 4")
print(f"{dictionary['name']} has {dictionary['contents']}")
print(dictionary)

 

#-->TODO: Declare a new dictionary and set at least 4 properties to it including: string, boolean, number, list

##################################  MY dictionary ########################### #/

games = {
    "name": "Sonic Generations",
    "release date": 2011,
    "is_favorite_game": True,
    "mc": ["Modern Sonic","Classic Sonic","Shadow", "Silver"]
}

########################################################################## #/



print("------------------- CHALLENGE 2 : MODIFY   -------------------")

#-->TODO: Print your dictionary you created above

print(f"This is the data of my favorite sonic game: {games}")

#-->TODO: Update the dictionary you just created  by adding new properties and values, including list elements, in this section.

games ["company"] = "Sega"

#-->TODO: Print your dictionary again and observe changes
print(games)

print("------------------- CHALLENGE 3 : MEHTODS   -------------------")


#-->TODO: Make a method that will update your dictionary value. It should take in a dictionary and return it modified.



#-->TODO: Call the method.



print("------------------- CHALLENGE 4 : LITERALLY   -------------------")

#-->TODO: Put it all together using a string literal to tell the story of your dictionary!

print(f"Today I would like to talk about one of my favorite games known as... {games['name']}.")
print(f"This game came out in {games['release date']} and was made by {games['company']}.")
print(f"A lot of the characters in this game include {games['mc']}")