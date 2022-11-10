#part one of the code
def your_name_length(fullname):
    length = len(fullname)
    return length
def last_character(fullname):
    return fullname[-1]
def letter_e(fullname):
    if 'e' in fullname:
        index = fullname.find('e')
        return index + 1
    elif 'e' not in fullname:
        return 0
def number_of_words(fullname):
    count = 0
    for i in range(0,len(fullname)):
        if fullname[i] == " ":
            count +=1
    return count + 1
def first_name(fullname):
    for i in fullname:
        index = fullname.find(" ")
        return fullname[0:index]
def number_vowels(fullname):
    count = 0
    for i in range(0, len(fullname)):
        if fullname[i] == 'a' or fullname[i] == 'e' or fullname[i] == 'i' or fullname[i] == 'o' or fullname[i] == 'u':
            count += 1  # updates the count
    return count # returns the number of vowels from the counter
def capitalize_vowels(fullname):
    str = ""
    for i in range(len(fullname)): # for loops through the who name
        if fullname[i] == 'a' or fullname[i] == 'e' or fullname[i] == 'i' or fullname[i] == 'o' or fullname[i] == 'u':
            c = fullname[i].upper() # uppercases any vowel in the array of i since its in a for loop
            str += c # this adds the singlar vowel if its true into the empty array str
        else:
            c = fullname[i].lower() # if the letter in the array is constant than lowers it
            str += c # adds it into str if true
    return str
def centered_string(fullname):
    str1 = "" # empty string to concanate later
    str2 = ""
    for i in range(0,35):
        y = ('+') # assigns y to a str +
        str1 += y # then adds 35 +'s into the empty str1
    for i in range(0,25):
        X = ('~') # assigns x to a str ~
        str2 += X # then adds 25 ~'s into the empty str2
    return str1 + str2 + fullname + str2 + str1 # call back varaible concantate the string
def end_of_string(fullname):
    str2 = "" #empty str for later
    y = len(fullname) # gets the length of name
    if y % 2 == 0: #checks if the length is even
        c = y // 2 #if even divide the length by 2 get the index point to split it
        d = fullname[0:c] # store index in var index from 0 to wherever c is
        f = fullname[c:len(fullname)] # c till the end of length of fullname
    elif y % 2 != 0: # check if not even
        c = int(y / 2)
        d = fullname[0:c]
        f = fullname[c:len(fullname)]
    for n in range(0,70):
        o = ('+')
        str2 += o
    return d + str2 + f # combining strings
fullname = input("Please enter your name: ")
print(f"Your name is {your_name_length(fullname)} characters long. ")
print(f"The last character is: {last_character(fullname)}")
print(f"The first 'e' is at posistion {letter_e(fullname)}.")
print(f"Your name has {number_of_words(fullname)} words.")
print(f"Your first name is {first_name(fullname)}.")
print(f"Your name contains {number_vowels(fullname)} vowels.")
print(f"Your name with uppercase vowels is: {capitalize_vowels(fullname)}")
print(f"{centered_string(fullname)}")
print(f"{end_of_string(fullname)}")