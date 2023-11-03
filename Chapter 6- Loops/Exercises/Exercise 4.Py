# types of sandwiches i selected
sandwich_orders = ["Grilled Cheese",
                   "Egg Sandwich",
                   "Chicken Sandwich",
                   "Nutella Sandwich",
                   "Panini Sandwich",]
# empty list
finished_sandwiches = []

for sandwich in sandwich_orders:  # print to show the sandwiches in the list
    print(f"I made your {sandwich}.\n")

finished_sandwiches = sandwich_orders

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") # design to make the code more readable
print ("The sandwiches that were made are:")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

for sandwhich in finished_sandwiches:
    print (sandwhich)
