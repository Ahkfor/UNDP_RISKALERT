# Multidocument Summarization
from email.utils import unquote
from helper import text_summary_bart
from urllib.parse import unquote
import os

def multi_document_summary(document_li):
    # Define the output file path
    output_file = "./ukraine_filtered_reports_bert_intermediary.txt"
    
    # Open the output file in write mode (this will create the file if it doesn't exist)
    with open(output_file, 'w', encoding='utf-8') as combined_file:
        # Loop through all files in the folder
        for filename in os.listdir(folder_path):
            # Construct the full file path
            file_path = os.path.join(folder_path, filename)
            
            # Check if it's a file (not a directory)
            if os.path.isfile(file_path):
                # Decode the filename (if it contains URL-encoded characters)
                decoded_filename = unquote(filename)
                
                # Open and read the file
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # Process the content with your BART function
                summary = text_summary_bart(content, max_len=300)
                
                # Write the decoded filename and summary to the combined file
                combined_file.write(f"File: {decoded_filename}\n")
                combined_file.write(f"Summary:\n{summary}\n")
                combined_file.write("-" * 50 + "\n")  # Separator for readability
                
                print(f"Processed: {decoded_filename}")

    print(f"All summaries have been written to {output_file}")


def text_summary_combined(file_find="/Users/ningpingwang/Desktop/UNDP_RISKALERT/ukraine_filtered_reports_bert_intermediary.txt"):
    with open(file_find, 'r', encoding='utf-8') as file:
        # Read the file's content
        content = file.read()

    summary = text_summary_bart(content) # return the summary decoded from BART

    with open(f'{file_find}_BART.txt', 'w', encoding='utf-8') as file:
        file.write(summary)

    print(f"All summaries have been written to final file")

multi_document_summary()
text_summary_combined()