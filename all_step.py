# The first kind of cipher you are going to build is called a Caesar cipher. Specifically, you will take each letter in your message, find its position in the alphabet, take the letter located after 3 positions in the alphabet, and replace the original letter with the new letter.

# To implement this, you will use the .find() method discussed in the previous step. Modify your existing .find() call passing it text[0] as the argument instead of 'z'.

# Transforming to lower case 
# lower() is responsible for that
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0])
print(index)
print(text.lower()) 



# Step 18
# Remove the last print() call. Then, instead of text[0], pass text[0].lower() as the argument to your .find() call and see the output.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0].lower())
print(index) # 7 was printed out and i dont know why maybe we will find out in the next step 

# Step 19 Declare a new variable named shifted. Use the bracket notation to access the value of alphabet at index index and assign it to your new variable.
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0].lower())
print(index)
shifted=alphabet[index] 
print(shifted) #we printed shift in the next step and 'h' wass printed

# we add + shift with index in the shifted variable  in the bacret notation 
shifted = alphabet[index +  shift ]
print(shifted) # k was printed out this time cause it added 3 to it 

#we want to repeat the process of locating the letter inside the alphabet and determine the shifted letter for each character in text  so we clear the code ofliens after the alphabet 
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

#we are trying to loop over the text variable 
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for char in text.lower():
    index = alphabet.find(char) #step 26 we added this to find the index of the character in the alphabet
    print(char, index)  # step 25 the whole chars in hello world get printed out e.g H e l l 
#the loop vairable was i before but we renamed it to something reasonable 'char'    
#step 27 we added another argument in the  print function 'index' caue the print function can accept a lot of argument by speparting it with a comma
# H -1
# e 4
# l 11
# l 11
# o 14
#   -1
# W -1
# o 14
# r 17
# l 11
# d 3
# this was logged out and we see that it is returing -1 for capitalize letter so we fix that instead of iterating  of 'text' we use 'text.lower()'

# this was what logged out after adding text.lower()
# h 7
# e 4
# l 11
# l 11
# o 14
#   -1
# w 22
# o 14
# r 17
# l 11
# d 3

#step 29 we added a new line
for char in text.lower():
    index = alphabet.find(char) 
    print(char, index)
    new_index=index + shift 
# step3 we cannot change vairable(imuttable) after creation
text = 'Hello World'
text[0] = 'Y'