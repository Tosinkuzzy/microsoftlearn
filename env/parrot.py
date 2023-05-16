# building a multi-line string
# the first line stores the first part of the message.
# second line operator += takes the string that was stored in prompt
# add the new string onto it
# the prompt now span two lines. 
prompt = "If you tell us who you are, we can personalise the messages you see."
prompt += "\nWhat is your name? "

name = input(prompt)
print("\nHello, " + name.title() + "!")
