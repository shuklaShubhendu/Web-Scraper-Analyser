# Web Scraper Analyzer

**Web Scraper Analyzer** is a Python-based project that scrapes textual content from web pages, performs sentiment analysis, and provides readability metrics. It is designed to extract meaningful data from websites and analyze it based on positive and negative sentiment scores.

## Features

1. **Web Scraping**: Utilizes `requests` and `BeautifulSoup` to scrape articles from specified URLs, storing each article's content as a text file.
2. **Sentiment Analysis**: Uses predefined lists of positive and negative words to analyze the sentiment of the extracted text. Calculates positive and negative scores, polarity, and subjectivity.
3. **Text Metrics**: Includes calculations of average sentence length, percentage of complex words, FOG index, word count, personal pronouns, and syllable count per word.
4. **Data Export**: Compiles analysis results into a structured Excel file for easy review and further analysis.

## Structure

- **main.py**: Extracts content from URLs and saves it to text files for analysis.
- **analysis.py**: Analyzes the text files, calculating sentiment scores and readability metrics.

## Key Calculations

- **Sentiment Scores**: Counts occurrences of positive and negative words to calculate polarity and subjectivity.
- **Readability Metrics**: Uses FOG Index and average sentence length to determine readability.
- **Additional Text Analysis**: Calculates complex words, personal pronouns, and word lengths.

---

This project can serve as a foundation for applications requiring web scraping, sentiment analysis, or readability assessments, making it versatile for a variety of data-driven tasks.
