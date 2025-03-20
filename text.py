
def clean_text(text):
    # Clean up the text by removing punctuation and special characters
    allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789 "
    text = text.lower()
    cleaned_chars = []
    for char in text:
        if char in allowed_chars:
            cleaned_chars.append(char)
    return "".join(cleaned_chars)

def word_frequency_analysis(file_path):
    # Perform word frequency analysis on a text file.
    try:
        word_counts = {}

        # Process the file line by line
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                cleaned_line = clean_text(line)
                words = cleaned_line.split()
                for word in words:
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1

        # Sort words by frequency
        sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

        # Display the 10 most frequent words
        print("The 10 most frequent words are:")
        for word, count in sorted_words[:10]:
            print(f"{word}: {count} times")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Path to the text file
file_path = "texto.txt"

# Run the word frequency analysis
word_frequency_analysis(file_path)