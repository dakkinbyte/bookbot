def print_file(file_path):
        print(file_path)

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def stringConversion(input_string):
    words = input_string.split(' ')
    word_count = len(words)
    print("Word count: ", word_count)

def main():
    file_contents = read_file('books/frankenstein.txt')
    print_file(file_contents)
    stringConversion(file_contents)

if __name__ == "__main__":
    main()