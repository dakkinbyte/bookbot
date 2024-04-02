def main():
    file_contents = read_file('books/frankenstein.txt')
    #print_file(file_contents)
    stringConversion(file_contents)
    letterCounter(file_contents)

def print_file(file_path):
        print(file_path)

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def sortOn(data):
    return data["count"]

def listCreation(data):
    char_list = []
    for char, count in data.items():
        char_list.append({"char": char, "count": count})
    char_list.sort(key=sortOn, reverse=True)
    return char_list

def letterCounter(text):
    d = {}
    lowerCasedString = text.lower()#.split() - Didnt know you could do this. 
    for character in lowerCasedString: 
        if character.isalpha(): # check to amke sure the character is alphabetical
            if character not in d:
                d[character] = 1
            else:
                d[character] += 1 
    sorted_characters = listCreation(d)
    for item in sorted_characters:
        print(f"The '{item['char']}' character was found {item['count']} times")
    #print(f"DEBUG:", sorted_characters)

def stringConversion(text):
    words = text.split()
    word_count = len(words)
    print("Word count: ", word_count)

main()