


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_contents(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    print(f'\n--- Begin report of {book_path} ---')
    print(f"\n{word_count} words found in this book\n")
    for char, keys in sorted(char_count.items()):
        print(f"the '{char}' was found {keys} times ")


def get_book_contents(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(book):
    count = book.split()
    return len(count)

def get_char_count(text):
    char_dict = {}
    for i in text:
        if i.isalpha():
            char_dict[i.lower()] = char_dict.get(f'{i.lower()}', 0) + 1
    return(char_dict)
main()