import re

import re


def clean_text_remove_stopwords(text):
    """
    This function removes special characters, unnecessary whitespace, and stop words from the input text.

    :param text: The input string to be cleaned
    :return: The cleaned string without stop words
    """
    # List of common stop words to remove
    stop_words = set([
        "the", "and", "is", "in", "at", "of", "a", "an", "for", "on", "with",
        "to", "from", "by", "that", "this", "but", "or", "as", "if", "then",
        "so", "than", "because", "while", "after", "before", "until", "since"
    ])

    # Remove special characters (anything that is not a letter, number, or whitespace)
    text = re.sub(r'[^A-Za-z0-9\s]+', '', text)

    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text).strip()

    # Split the text into words and filter out stop words
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Join the filtered words back into a single string
    cleaned_text = ' '.join(filtered_words)

    return cleaned_text


# Example usage
raw_text = "Hello! This is an example text, with special characters & unnecessary whitespace!! The purpose is to clean it up."
cleaned_text = clean_text_remove_stopwords(raw_text)
print(cleaned_text)

# Example usage
raw_text = "Hello! This    is an example text, with   special characters & unnecessary    whitespace!!"
cleaned_text = clean_text(raw_text)
print(cleaned_text)

