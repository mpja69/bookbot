def main():
    book_path = "books/frankenstein.txt"
    text = read_file(book_path)
    count = count_words(text)
    print(count)
    freq = calculate_frequency(text)
    print(freq)

    print_report(book_path, count, freq)

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


def get_num(item):
    return item["num"]

def print_report(name, num, freq):
    print(f"--- Begin report of {name} ---")
    print(f"{num} words found in the document")
    print()
    chars = []
    for k,v in freq.items():
        if k.isalpha():
            chars.append({"name": k, "num": v})
    chars.sort(key=get_num, reverse=True)

    for ch in chars:
        print(f"The '{ch["name"]}' character was found {ch["num"]} times")

    print("--- End report ---")
    
main()

