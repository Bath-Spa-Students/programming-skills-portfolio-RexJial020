
toppings = [
    "pepperoni",
    "mushrooms",
    "onions",
    "sausage",
    "bacon",
    "extra cheese",
    "black olives",
    "green peppers"]

#the list of available pizza toppings.
print ("~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("Pizza toppings available:")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~")
for topping in toppings:
    print(topping)

#an empty list to store the toppings you selected.
selected_toppings = []

#input promt
while True:
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #a simple design to make the code look nice.
    enter_topping = input("\nEnter a topping (type 'quit' when you're done adding toppings):\n")
    if enter_topping == 'quit':
        break
    if enter_topping in toppings:
        selected_toppings.append(enter_topping)
        print (f"\nYou are adding {enter_topping} to your pizza.")
    else:
        print("\nInvalid topping. Please choose from the available options.")

#print the selected toppings
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("You selected the following toppings for your pizza:")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for topping in selected_toppings:
    print(topping)
