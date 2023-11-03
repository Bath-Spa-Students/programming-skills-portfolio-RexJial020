
# types of sandwiches i selected
sandwich_orders = ["Pastrami Sandwich",
                   "Grilled Cheese",
                   "Egg Sandwich",
                   "Chicken Sandwich",
                   "Pastrami Sandwich",
                   "Nutella Sandwich",
                   "Panini Sandwich",
                   "Pastrami Sandwich",]
# message that the deli has run out of Pastrami Sandwich
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("The deli has run out of Pastrami Sandwich!")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#while loop to remove pastrami sandwich to the list
while "Pastrami Sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami Sandwich")

# empty list
finished_sandwiches = []

for sandwich in sandwich_orders:  # print to show the sandwiches in the list
    print(f"I made your {sandwich}.\n")

finished_sandwiches = sandwich_orders

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") # design to make the code more readable
print ("The sandwiches that were made are:")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

for sandwhich in finished_sandwiches:
    print (f"{sandwhich}\n")
