def main():
    file_contents = read_file('books/frankenstein.txt')
    #print_file(file_contents)
    #stringConversion(file_contents)
    letterCounter(file_contents)

def print_file(file_path):
        print(file_path)

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def letterCounter(text):
    d = {}
    lowerCasedString = text.lower()
    for character in lowerCasedString: 
        # convert the character to lowercase ( lowered_string = input.lower() ) 
        # if the character is already in the directory
            # increase its count by 1
        # else add the character to the dir with a count of 1 
        if character not in d:
            d[character] = 1
        else
            d[character] += 1 

    

def stringConversion(text):
    words = input_string.split()
    word_count = len(words)
    return len(word_count)
    print("Word count: ", word_count)

main()