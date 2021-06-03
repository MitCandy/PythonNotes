# SimpleString
print("Get Good")

# Backslash for using quotation inside quotation
print("Get\"Good")

# Can be assigned on variable and execute
name = "Roy"
print(name)

# Concenateable w/without variable
name1 = "Burnett"
print("Your name is " + name1)

# String w function
word = "klen"
print(word.upper) # Capitalize those words

word1 = "KLEN"
print(word1.lower) # vice versa

word2 = "I love you"
print(len(word2)) # measure the length of characters ( counted from zero, spaces included )

# Show only individual characters
myname = "Doppel"
print(myname[0]) # Prints D
print(myname[4]) # Prints e

# Another function for counting index
some_word = "Hent Have" # ( ͡° ͜ʖ ͡°) Author weeb lmao
print(some_word.index("H")) # Prints 0 and btw case sensitive
print(some_word.index("a")) # Prints 6 
