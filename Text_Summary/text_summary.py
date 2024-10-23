from transformers import AutoTokenizer, AutoModelForMaskedLM
import torch
import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def clean_text(text):
    """
    This function removes unnecessary whitespace from the input text.

    :param text: The input string to be cleaned
    :return: The cleaned string
    """

    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def text_summary(text, max_len=150):
    """
    Function to summarize humanitarian text using a summarization model (BART in this case)
    :param text: text to be summarized
    :param max_len: maximum length of the summary (in tokens)
    """
    # Load the tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained('facebook/bart-large-cnn')
    model = AutoModelForSeq2SeqLM.from_pretrained('facebook/bart-large-cnn')

    # Tokenize the text
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=1024)

    # Generate summary
    summary_ids = model.generate(inputs['input_ids'], max_length=max_len, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)

    # Decode summary and return it
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary


# Example
with open('Sample.txt', 'r', encoding='utf-8') as file:
    # Read the file's content
    content = file.read()

summary = text_summary(content)
with open('summary.txt', 'w', encoding='utf-8') as file:
    file.write(summary)