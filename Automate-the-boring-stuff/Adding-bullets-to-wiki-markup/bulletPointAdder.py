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


