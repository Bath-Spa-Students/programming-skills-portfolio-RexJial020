
rivers = { 
    'Amazon':'Brazil',
    'Ganges':'India',
    'Mississippi':'United States',
    'Yukon':'Canada',
    'Nile':'Egypt', }
    
#Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
for river, country in rivers.items():
    print (f"The {river} runs through {country}.")

#Use a loop to print the name of each river included in the dictionary.
print ("\nRivers:\n")
for river in rivers:
    print (river)

#Use a loop to print the name of each country included in the dictionary.
print ("\nCountry:\n")
for country in rivers.values():
    print (country)
