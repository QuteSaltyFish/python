def countwords(filename):
    try:
        with open(filename) as f_obj:
            content = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " doesn't exist."
        print(msg)
    else:
        # Count the approximate number of words in the file.
        words = content.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words
                                                           ) + " words.")


filename = 'Alice.txt'
countwords(filename)
