# -------------------------------------------- 

	# You've just learned about variables, conditionals, functions, and user input. 
	# You've also created a basic calculator in a previous project.
	
	# Now imagine you are going out to eat.
	# Are you at a restaurant for a meal? Are you grabbing boba? Or are you just going to an ice cream parlor?
	# At the end of the meal, you get the bill. 

	# How do you think restaurants automate that math?

					# Let's try it!

# -------------------------------------------- 

# Scenario Parameters: 

	# When you eat out, you have the option to order one or multiple items.
	# What kind of items are available to order? There's usually a menu.
	# Allow your user to order a drink, meal, and dessert.

	# At the end of the order, the receipt comes and you have to calculate the total cost:
	# Don't forget the tax and tip!

# After this program finishes running, it should output a receipt with:
        #1. the items you ordered and their cost 
	#2. a total for your order before tax
	#3. a total for your order after tax
	#4. the amount of your tip 
	#5. the total including tax and tip

# -------------------------------------------- 


# -------------------------------------------- 

# Part 1:
# Let's start by creating the variables we'll need to keep track of the user's order
# as well as TAX and tip

# Remember: Your user should be able to order at least 3 items (a drink, meal, and dessert item). 

# --------------------------------------------

mac = 10.00
rs = 7.00
dc = 13.00
rw = 3.45
st = 3.00 
cdc = 2.00
nic = 3.00
db = 3.50
choco = 4.00
a = 0
b = 0
c = 0
d = 0
tlt = 0.00
tlt_tax = 0.00
tlt_tip = 0.00
ftlt = 0.00
final = 0.00

# -------------------------------------------- 

# Part 2:
# Next, let's display the menu. Include the food item name and it's cost. 

# Write a function that will display the menu:
# - Print each item available and it's cost. You should have at least 3 items available (a drink, meal, and dessert item). 

# --------------------------------------------

def menu():
	print('\nArsenal for Cooks Menu')
	print('-----------------------------\n')

	print('Weapon - Food:\n')

	print(f'1. Macaroni & Cheese - $10.00')
	print('choice of bacon or extra cheese \n')

	print(f'2. Rendevous Salad - $7.00')
	print('choice of onions and/or dressing \n')

	print(f'3. Dungeon Crab - $13.00')
	print('choice of any sauce \n')

	print('-----------------------------\n')

	print('Ammunition - Drink:\n')

	print(f'4. Red Wine - $3.45 \n')

	print(f'5. Shirley Temple - $3.00 \n')

	print(f'6. Cold Drink of Choice - $2.00 \n')

	print('-----------------------------\n')

	print('Kill - Dessert:\n')

	print(f'7. Neopoletan Ice Cream - $3.00  ')
	print('with syrup of choice\n')

	print(f'8. Darkness Brownie - $3.50  \n')

	print(f'9. Chocolate Cake - $4.00  ') 
	print('- Devils Cake  \n')

	print('-----------------------------\n')

menu()



# -------------------------------------------- 

# Part 3:
# Let's take the order. What did the user order? What does it cost?

# Write a function that will take the order:
# - Prompt the user to enter a drink, dessert, and meal (Bonus: give them the option to not order an item)
# - Return the cost 

# Remember! Functions are meant to be reusable, so write a function that will work when called repeatedly!

# --------------------------------------------

def weapon():
	global a
	a = int(input('Hello comrade. Please enter your weapon of choice from 1 - 3 ------> \n'))
	if a == 1:
		print('1. Macaroni & Cheese - $10.00 \n')
	elif a == 2:
		print('2. Rendevous Salad - $7.00 \n')
	elif a == 3:
		print('3. Dungeon Crab - $13.00 \n')


def ammunition():
	global b
	b = int(input('Now, enter your ammunition of choice from 4 - 6 ------> \n'))
	if b == 4:
		print(f'4. Red Wine - $3.45 \n')
	elif b == 5:
		print(f'5. Shirley Temple - $3.00 \n')
	elif b == 6:
		print(f'6. Cold Drink of Choice - $2.00 \n')


def kill(): 
	global c
	c = int(input('Finally, execute the final kill of choice from 7 - 9 ------> \n'))
	if c == 7:
		print(f'7. Neopoletan Ice Cream - $3.00  \n')
	elif c == 8:
		print(f'8. Darkness Brownie - $3.50 \n')
	elif c == 9:
		print(f'9. Chocolate Cake - $4.00  \n') 

weapon()
ammunition()
kill()












# -------------------------------------------- 

# Part 4:
# Now that you have the costs of everything ordered, let's calculate the cost of the order(including tip and tax).

# Write a function that will calculate the cost of the order, including:
# - Cost of all  ordered items
# - Tax (Look up the sales tax of your city)
# - Tip (Give the user the option to enter how much they want to tip)

# Remember! Functions are meant to be reusable, so write a function that will work when called for each person!

# -------------------------------------------- 

def calculations():
	global tlt
	global a
	global b
	global c
	if a == 1:
		tlt = tlt + mac
	elif a == 2:
		tlt = tlt + rs
	elif a == 3:
		tlt = tlt + dc

	if b == 4:
		tlt = tlt + rw
	elif b == 5:
		tlt = tlt + st
	elif b == 6:
		tlt = tlt + cdc

	if c == 7:
		tlt = tlt + nic
	elif c == 8:
		tlt = tlt + db
	elif c == 9:
		tlt = tlt + choco
	print(tlt)
calculations()






# -------------------------------------------- 

# Part 5:
# Let's print out a receipt.

# Write a function that will take the values of the order and total cost and print it out in an appealing way.

# The receipt should include:
# - Cost of each item
# - Tax for the order
# - Tip for the order
# - Total cost for the order


# -------------------------------------------- 


def receipt():
	global tlt_tax
	global tlt
	tlt_tax = tlt * 0.08875

	print('Your subtotal is: \n')
	print(format(f'{tlt} \n'))
receipt()

def tip():
	global tlt_tip
	global tlt
	d = (input('Finally would you like to enter a tip of either (10%, 15%, or 20%)? \n'))
	if d == '10%':
		tlt_tip = tlt * 0.10
	elif d == '15%':
		tlt_tip = tlt * 0.15
	elif d == '20%':
		tlt_tip = tlt * 0.20

	print(format(round(tlt_tip, 2)))
tip()

def choice():
	global a
	global b
	global c

	if a == 1:
		print('1. Macaroni & Cheese - $10.00 \n')
	elif a == 2:
		print('2. Rendevous Salad - $7.00 \n')
	elif a == 3:
		print('3. Dungeon Crab - $13.00 \n')

	if b == 4:
		print(f'4. Red Wine - $3.45 \n')
	elif b == 5:
		print(f'5. Shirley Temple - $3.00 \n')
	elif b == 6:
		print(f'6. Cold Drink of Choice - $2.00 \n')

	if c == 7:
		print(f'7. Neopoletan Ice Cream - $3.00  \n')
	elif c == 8:
		print(f'8. Darkness Brownie - $3.50 \n')
	elif c == 9:
		print(f'9. Chocolate Cake - $4.00  \n') 


print('Here is your receipt: \n')
choice()
print(format(f'Subtotal: {round(tlt, 2)}'))
print(format(f'Tax: {round(tlt_tax, 2)}'))
print(format(f'Tip: {round(tlt_tip, 2)} '))



def last():
	global final
	global tlt_tip
	global tlt_tax
	global tlt
	final = tlt + tlt_tax + tlt_tip
	print(f'Total: ${round(final, 2)}')
	
last()
# -------------------------------------------- 

# Part 6: Food Order Bot

# Call all of your functions to get your food order bot up and running!

# --------------------------------------------







# -------------------------------------------- 

# Part 7: Upchallenges!

# How many of these upchallenges can you implement?

# - Make sure the user is only entering valid values. If they enter an invalid value, prompt them to re-enter. 
# - The displayed prices should only have two decimal places.
# - Implement a rewards system (stamp cards, buy one get one, etc)

# --------------------------------------------
