def main():
    book_path = "books/frankenstein.txt"
    text = read_file(book_path)
    count = count_words(text)
    print(count)
    freq = calculate_frequency(text)
    print(freq)

def read_file(path):
    with open(path) as f:
        file_content = f.read()
    return file_content

def count_words(text):
    words = text.split()
    return len(words)


def calculate_frequency(text):
    chars = {}
    for ch in text:
        lowered = ch.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

    
main()

