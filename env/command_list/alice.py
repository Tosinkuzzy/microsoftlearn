def count_words(filename):
    """count the approximate number of words in the file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
            
    except FileNotFoundError:
        pass
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'litle_women.txt']
for filename in filenames:
    count_words(filename)
