import sys


def searh_word(word,string):
    return string.count(word)

if __name__ == "__main__":
    filename = sys.argv[1]
    word = sys.argv[2]
    with open(filename) as f:
        string = f.read()
        n = searh_word(word,string)
        print(f"There are {n} occurences of '{word}' in the file{filename}")