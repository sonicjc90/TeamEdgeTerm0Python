#********************************************************************
 #                                                                 
 #  Team Edge List Mini-project: THE SHOPPING LIST HELPER
 # 
 #  This project prompts users using input() to prompt users
 #  to add (or remove) items from a shopping list. It starts empty
 #  and each time the program is run it asks you to either add or 
 #  remove an item from the list. It also updates the user of its
 #  contents. The shopping list also checks to see if an item 
 #  is already present in the list and prevents you from adding it
 #  again, giving feedback along the way. 
 # 
 # ***************************************************************/

active = True

print("Welcome to Shopping List!")

welcome_message = "Hi! I'm your personal shopping assistant. Let me take your order. \n You can type 'add milk' to add milk to your shopping list. \n or you can type 'remove milk' to remove it. \n"

print(welcome_message)


#-->Todo: declare a shopping_list list

shopping_list = []


def prompt_user():

    reply = input("What do you want to add or remove?  >>  ")

    return reply
    

def check_answer(ans):
    print(ans)

    ans = ans.split()
    add_item(ans)

    # check_answer("")

    # if reply == " ":
    #     print(prompt_user())


def add_item():
#this function can take in a string and store it in an array
    

    global shopping_list

    add = shopping_list.split(" ")

    if reply == "add " + str(reply):
        shopping_list.append(reply)
       
    print(shopping_list)



def remove_item():
    

    global shopping_list

    if reply == "remove " + str(reply):
        shopping_list.remove(reply)
    elif len(shopping_list) == 0:
        print(f"You have {len(shopping_list)} items in your list.")


add_item()
#remove_item()

while active:

    check_answer(prompt_user()) #this makes the program continously prompt and check response while the boolean 'active' returns True

define 