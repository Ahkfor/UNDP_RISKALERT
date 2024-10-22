from transformers import AutoTokenizer, AutoModelForMaskedLM
import torch


def text_summary(text):
    """
    Function to summarize humanitarian text using HumBert
    :param text: text to be summarized
    """
    # Load the tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained('nlp-thedeep/humbert')
    model = AutoModelForMaskedLM.from_pretrained("nlp-thedeep/humbert")

    # Input text
    encoded_input = tokenizer(text, return_tensors='pt')

    # Get model output
    output = model(**encoded_input)

    # Get the predicted token IDs
    predicted_token_ids = torch.argmax(output.logits, dim=-1)

    # Convert predicted token IDs to tokens and decode them into text
    predicted_text = tokenizer.decode(predicted_token_ids[0], skip_special_tokens=True)

    # Print the predicted text
    return predicted_text

