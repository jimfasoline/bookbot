from stats import word_count, character_count, sort_chars
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    total_words = word_count(text)
    total_chars = character_count(text)
    sorted_chars = sort_chars(total_chars)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")

    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")

    print("--------- Character Count -------")
    for dict in sorted_chars:
        if(dict['char'].isalpha() == True):
            print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")
    
main()