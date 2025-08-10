import string
import collections

def count_word_frequency(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = [word for word in file.read().lower().translate(str.maketrans('', '', string.punctuation)).split() if word]
            return collections.Counter(words)
    except Exception as e:
        print(f"Error: {e}")
        return {}

if __name__ == "__main__":
    my_text_file = "text.txt"
    with open(my_text_file, 'w', encoding='utf-8') as f:
        f.write("Hello world.\n")
        f.write("World is beautiful. Hello again.")

    frequencies = count_word_frequency(my_text_file)

    for word, count in sorted(frequencies.items()):
        print(f"'{word}': {count}")
