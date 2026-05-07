from stats import num_of_chars, num_of_words


def get_book_text(path):
    with open(path) as file:
        file_content = file.read()
        return file_content


def main():
    file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    # print(book_text)
    print("Found " + str(num_of_words(book_text)) + " total words")
    print(num_of_chars(book_text))


main()
