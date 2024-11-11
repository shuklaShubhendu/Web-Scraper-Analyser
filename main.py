import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import os

# Function to extract article text from URL
def extract_article_text(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract article text from <div class="td-post-content">
        article_text = ""
        article_content = soup.find('div', class_='td-post-content')
        if article_content:
            # Find all <p> and <li> tags within the article content
            paragraphs = article_content.find_all(['p', 'li'])
            # Extract text from each <p> and <li> tag and concatenate
            for paragraph in paragraphs:
                article_text += paragraph.get_text(separator='\n') + '\n\n'
            # Remove extra spaces and newlines
            article_text = re.sub(r'\n\s*\n', '\n\n', article_text.strip())
        else:
            raise ValueError("No article content found.")
        
        return article_text
    except Exception as e:
        print(f"Error occurred while extracting text from {url}: {e}")
        return None

# Load the input.xlsx file
df = pd.read_excel("Input.xlsx")

# Create a folder named "extracted_text" if it doesn't exist
output_folder = "extracted_text"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']
    # Extract article text
    article_text = extract_article_text(url)
    if article_text:
        # Save the extracted article in a text file inside the "extracted_text" folder
        file_path = os.path.join(output_folder, f"{url_id}.txt")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(article_text)
        print(f"Article text extracted from {url} and saved as {file_path}")
    else:
        print(f"Failed to extract article text from {url}")

print("Extraction completed.")
