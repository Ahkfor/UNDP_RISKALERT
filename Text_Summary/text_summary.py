import nltk
import string
from rank_bm25 import BM25Okapi
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
from helper import *


def bart_summary(document_li):
    # Method 1: summarize each document using BART, then use other methods to summarize these outputs
    summary = ''

    for doc in document_li:
        summary = summary + text_summary_bart(doc, max_len=300)

    result = text_summary_bart(summary, max_len=300)
    return result





def tfidf_summary(documents, query):
    # Method 2: TF-IDF or BM25-based Retrieval + Summarization
    # Ensure NLTK resources are available
    nltk.download('punkt')
    nltk.download('punkt_tab')

    # Preprocessing function
    def preprocess(text):
        tokens = nltk.word_tokenize(text.lower())  # Tokenize and lowercase
        tokens = [word for word in tokens if word not in string.punctuation]  # Remove punctuation
        return tokens

    # Tokenize documents
    tokenized_docs = [preprocess(doc) for doc in documents]

    # Initialize BM25 model
    bm25 = BM25Okapi(tokenized_docs)

    # Retrieve top N relevant sentences
    top_n = 10
    query_tokens = preprocess(query)
    doc_scores = bm25.get_scores(query_tokens)
    top_doc_indices = sorted(range(len(doc_scores)), key=lambda i: doc_scores[i], reverse=True)[:top_n]

    # Extract relevant sentences
    retrieved_text = " ".join([documents[i] for i in top_doc_indices])

    # Summarization using TextRank
    def summarize_text(text, num_sentences=2):
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = TextRankSummarizer()
        summary = summarizer(parser.document, num_sentences)
        return " ".join(str(sentence) for sentence in summary)

    # Generate summary
    summary = summarize_text(retrieved_text, num_sentences=2)

    # Output results
    print("Query:", query)
    print("\nRetrieved Text:\n", retrieved_text)
    print("\nSummary:\n", summary)

    return summary

