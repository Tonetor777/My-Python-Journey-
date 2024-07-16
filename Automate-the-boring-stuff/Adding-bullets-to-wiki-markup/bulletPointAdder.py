import pyperclip

#How i did it 

text = pyperclip.paste().split("\n")
# pastes the copies lists from the clipboard and split them with the new line. 

newtext = ""
# a variable to hold the new (bullets added lists)

for line in text:
    newtext += "* " + line + "\n"
# go through each line of text and append a star and space to it with a new line at the end. 

print(newtext)
# to check the output 

pyperclip.copy(newtext)
# copy the new list to clipboard 

######################################################

# Better version / Solution in the Book 

text = pyperclip.paste()
# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)): # loop through all indexes for "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)


""" 

In My solution:
for line in text:
    newtext += "* " + line + "\n"
this is not Effecient since a string is an immutable data type each time i am appending the star to the newtext, i am not changing the value of the newtext but creating a new variable with the appended value each time. as the list number increases it becomes ineffecient. 

"""
