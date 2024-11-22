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


def text_summary_BART(text, max_len=150):
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


def text_summary_BERT(text, max_len=150):
    """
    Function to summarize text using BERT model
    :param text: text to be summarized
    :param max_len: maximum length of the summary (in tokens)
    :return: summarized text
    """
    # Load the tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
    model = AutoModelForMaskedLM.from_pretrained('bert-base-uncased')
    
    # Clean and tokenize the text
    cleaned_text = clean_text(text)
    inputs = tokenizer(cleaned_text, return_tensors='pt', truncation=True, 
                      padding=True, max_length=512)
    
    # Get model outputs
    with torch.no_grad():
        outputs = model(**inputs)
        
    # Get the predicted token probabilities
    predictions = outputs.logits[0].softmax(dim=-1)
    
    # Get the most important sentences based on BERT predictions
    sentences = cleaned_text.split('.')
    sentence_scores = []
    
    for sentence in sentences:
        if len(sentence.strip()) > 0:
            inputs = tokenizer(sentence, return_tensors='pt')
            with torch.no_grad():
                outputs = model(**inputs)
            # Use the average prediction probability as the sentence importance score
            score = outputs.logits[0].softmax(dim=-1).mean().item()
            sentence_scores.append((sentence, score))
    
    # Sort sentences by importance score
    sentence_scores.sort(key=lambda x: x[1], reverse=True)
    
    # Select top sentences until we reach max_len
    summary_sentences = []
    current_len = 0
    
    for sentence, _ in sentence_scores:
        tokens = tokenizer.tokenize(sentence)
        if current_len + len(tokens) <= max_len:
            summary_sentences.append(sentence)
            current_len += len(tokens)
    
    # Join the selected sentences into a summary
    summary = ' '.join(summary_sentences)
    return summary


# Example
with open('Sample.txt', 'r', encoding='utf-8') as file:
    # Read the file's content
    content = file.read()

summary = text_summary_BART(content)
with open('summary.txt', 'w', encoding='utf-8') as file:
    file.write(summary)