
pets = [
    #The list of dictionaries, each representing a different pet.
    {'kind': 'Cat', 'owner': 'Feb','info':'They are independent and curious animals, known for their playful and aloof nature.'},
    {'kind': 'Dog', 'owner': 'Rex','info':'They are loyal and affectionate animals, often considered as "mans best friend."'},
    {'kind': 'Guinea Pigs', 'owner': 'Jon','info':'They are small, sociable rodents known for their gentle and friendly disposition.'},
    {'kind': 'Fish', 'owner': 'Bon','info':'They are often kept in aquariums for their beauty and calming presence.'},
    {'kind': 'Hamster', 'owner': 'Lem','info':'They are small, furry rodents that make great pets for small living spaces.'}
]

#Loop through the list and print information about each pet.
for pet in pets:
    print (f"\nKind of Animal: {pet['kind']}")
    print (f"Owner's Name: {pet['owner']}")
    print (f"\nPet Info: {pet['info']}")
