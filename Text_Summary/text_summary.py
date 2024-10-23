from transformers import AutoTokenizer, AutoModelForMaskedLM
import torch
import re


def clean_text(text):
    """
    This function removes special characters, unnecessary whitespace, and stop words from the input text.

    :param text: The input string to be cleaned
    :return: The cleaned string without stop words
    """
    # List of common stop words to remove
    stop_words = {"the", "and", "is", "in", "at", "of", "a", "an", "for", "on", "with", "to", "from", "by", "that",
                  "this", "but", "or", "as", "if", "then", "so", "than", "because", "while", "after", "before", "until",
                  "since"}

    # Remove special characters (anything that is not a letter, number, or whitespace)
    # text = re.sub(r'[^A-Za-z0-9\s]+', '', text)

    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text).strip()

    # Split the text into words and filter out stop words
    words = text.split()
    # filtered_words = [word for word in words if word.lower() not in stop_words]

    # Join the filtered words back into a single string
    # cleaned_text = ' '.join(filtered_words)

    return text


def text_summary(text, max_len=514):
    """
    Function to summarize humanitarian text using HumBert
    :param text: text to be summarized
    """
    # Load the tokenizer and model
    text = clean_text(text)  # Assuming clean_text is your custom text preprocessing function
    tokenizer = AutoTokenizer.from_pretrained('nlp-thedeep/humbert')
    model = AutoModelForMaskedLM.from_pretrained("nlp-thedeep/humbert")

    # Tokenize the text and return input_ids and attention_mask
    tokens = tokenizer(text, return_tensors='pt', truncation=True, padding=True)

    # Split the input_ids and attention_mask
    input_ids = tokens['input_ids'][0]
    attention_mask = tokens['attention_mask'][0]

    # Split into chunks of max_len
    input_splits = [input_ids[i:i + max_len] for i in range(0, len(input_ids), max_len)]
    mask_splits = [attention_mask[i:i + max_len] for i in range(0, len(attention_mask), max_len)]

    predicted_text_li = []

    for input_ids_chunk, mask_chunk in zip(input_splits, mask_splits):
        # Create new dictionary with input_ids and attention_mask
        encoded_input = {'input_ids': input_ids_chunk.unsqueeze(0), 'attention_mask': mask_chunk.unsqueeze(0)}

        # Get model output
        output = model(**encoded_input)

        # Get the predicted token IDs
        predicted_token_ids = torch.argmax(output.logits, dim=-1)

        # Convert predicted token IDs to tokens and decode them into text
        predicted_text = tokenizer.decode(predicted_token_ids[0], skip_special_tokens=True)
        predicted_text_li.append(predicted_text)

    # Return the predicted text as a concatenated string or list
    return ' '.join(predicted_text_li)


# Example
with open('Sample.txt', 'r', encoding='utf-8') as file:
    # Read the file's content
    content = file.read()


summary = text_summary(content)
print(summary)
summary = text_summary(summary)
with open('summary.txt', 'w', encoding='utf-8') as file:
    file.write(summary)