#Count number of occurrences for a specific string
phrase = "Hello world"
print(phrase.count("l"))

#Print a specific portion of the string indicated by array
phrase = "Hello world"
print(phrase[0:5])

#Indicate sections of string to split using comma
phrase = "a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p"
print(phrase.split('-'))

#Replace part of string with another
phrase = "Hello CyberRoFlo"
print(phrase.replace("Hello", "Goodbye"))

#Self explanatory string manipulations
quote = "The quick brown fox jumped over the lazy dog."

x = quote.upper()
print(x)

x = quote.lower()
print(x)

x = quote.title()
print(x)

x = quote.capitalize()
print(x)

x = quote.swapcase()
print(x)

flag_found = ''
is_flag_found = bool(flag_found)

print(is_flag_found)