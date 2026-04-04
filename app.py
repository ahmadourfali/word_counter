def get_words():
    words = {}
    try:
        with open("test.txt", "r") as f:
            for line in f:
                clean_line = line.strip().lower().replace(".", "").replace("'", "").replace("!", "").split()              
                for word in clean_line:
                    if word:  
                        if word in words:
                            words[word] += 1
                        else:
                            words[word] = 1
        print(words)
    except FileNotFoundError:
        print("The file 'test.txt' was not found.")

get_words()