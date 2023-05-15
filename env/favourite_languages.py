favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
   'adam': 'pascal', 
}
# Looping through dictionary
# for name, language in favourite_languages.items():
  #  print(name.title() + "'s favourite language is " +
   #       language.title() + ".")

#for values in favourite_languages.values():
   # print(values.title())

# friends = ['phil', 'edward']
# Looping through a dict in order
# for name in sorted(favourite_languages.keys()):
for name in sorted(favourite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

if name in friends:
    print("  Hi " + name.title() + ", I see your favourite language is " +
               favourite_languages[name].title() + "!")
    
if 'erin' not in favourite_languages.keys():
    print("Erin, please take our poll")
    