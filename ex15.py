# initiate argv module from sys library?
from sys import argv

# run the script and incorporate the filename in the python run command
script, filename = argv

# define string txt and fill it with file
txt = open(filename)

# show back name of file from python run command
# show contents of txt file with .read modifier
print "Here's your file %r:" % filename
print txt.read()

txt.close()

# ask via prompt for file name a second time
print "Type the filename again:"
file_again = raw_input("> ")

# open the filename defined in the user prompt
txt_again = open(file_again)
# show contents of txt file from prompt, again suing .read modifier
print txt_again.read()

txt_again.close()