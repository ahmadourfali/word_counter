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
        return words
    except FileNotFoundError:
        print("The file 'test.txt' was not found.")

def print_result(all_the_words, the_top_5):
    print("="*30)
    print(f"There are {all_the_words} different words")
    print("The top five word:")
    print("="*30)
    for word, frequency in the_top_5:
        print(f"- {word:<5} {frequency:<2} times")
    print("="*30)

if __name__ == "__main__":
    sorted_words = sorted(get_words().items(), key=lambda item: item[1], reverse=True)
    all_words = len(sorted_words)
    top_5 = sorted_words[:5]
    print_result(all_words, top_5)
