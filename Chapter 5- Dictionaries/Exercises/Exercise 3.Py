
glossary = {'Variables':'A variable is a reserved memory location to store values.',
            'Values':'It is either a letter or number that works with the program.',
            'Comments':'It enhances the readability of the code and help the programmers to understand the code very carefully.',
            'Print':'Is a function that prints specified message to the screen, or other standard output device.',
            'Lists':'Is a collection of things, enclosed in [ ] and separated by commas.'}
    

#list of python terms that will be added to the existing dicitonary (glossary).
glossary['Function'] = 'A block of organized, reusable code that performs a specific task.'
glossary['Module'] = 'A file containing Python code that can be imported and used in other Python programs. Modules are a way to organize code into reusable units.'
glossary['Loop'] = 'A control structure that allows a program to repeatedly execute a block of code while a certain condition is true.'
glossary['Conditional Statements'] = 'A control structure that allows a program to make decisions and execute different code blocks based on whether a specified condition is true or false.'
glossary['Dictionary'] = 'A data structure in Python that stores key-value pairs.'


for keys, values in glossary.items():
    print(f"{keys}:\n{values}\n")

