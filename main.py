def content():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def count_words():
    file_contents = content()
    return len(file_contents.split())

def count_characters():
    file_contents = content()
    lowered_text = file_contents.lower()
    characters = dict()
    for c in lowered_text:
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters

def report():
    print("--- Begin report ---")
    print(f"{count_words()} words found in the document\n")

    sorted_characters = dict(sorted(count_characters().items(), key=lambda item: item[1], reverse=True)) 
    for c in sorted_characters:
        if c.isalpha():
            print(f"The '{c}' character was found {sorted_characters[c]} times")
    print("--- End report ---")

def main():
    report()

if __name__ == "__main__":
    main()