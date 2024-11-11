import os
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def main():
    # Load positive and negative words from text files
    with open('positive_words.txt', 'r', encoding='latin-1') as file:
        positive_words = set(file.read().splitlines())
    with open('negative_words.txt', 'r', encoding='latin-1') as file:
        negative_words = set(file.read().splitlines())

    folder_path = 'extracted_text'
    results = analyze_text_files(folder_path, positive_words, negative_words)

    # Create DataFrame from results and save to Excel
    results_df = pd.DataFrame(results)
    results_df.to_excel('text_analysis_results.xlsx', index=False)

def analyze_text_files(folder_path, positive_words, negative_words):
    results = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            url_id = filename.split('.')[0]
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                text = file.read()
            positive_score, negative_score, polarity_score = calculate_scores(text, positive_words, negative_words)
            subjectivity_score = calculate_subjectivity_score(positive_score, negative_score, text)
            avg_sentence_length = calculate_avg_sentence_length(text)
            percentage_complex_words, fog_index = calculate_readability(text)
            avg_num_words_per_sentence = calculate_avg_num_words_per_sentence(text)
            complex_word_count = calculate_complex_word_count(text)
            word_count = calculate_word_count(text)
            syllable_per_word = calculate_syllable_per_word(text)
            personal_pronouns = calculate_personal_pronouns(text)
            avg_word_length = calculate_avg_word_length(text)
            results.append({'URL_ID': url_id, 'URL': '', 'POSITIVE SCORE': positive_score,
                            'NEGATIVE SCORE': negative_score, 'POLARITY SCORE': polarity_score,
                            'SUBJECTIVITY SCORE': subjectivity_score, 'AVG SENTENCE LENGTH': avg_sentence_length,
                            'PERCENTAGE OF COMPLEX WORDS': percentage_complex_words, 'FOG INDEX': fog_index,
                            'AVG NUMBER OF WORDS PER SENTENCE': avg_num_words_per_sentence,
                            'COMPLEX WORD COUNT': complex_word_count, 'WORD COUNT': word_count,
                            'SYLLABLE PER WORD': syllable_per_word, 'PERSONAL PRONOUNS': personal_pronouns,
                            'AVG WORD LENGTH': avg_word_length})
    return results

def calculate_scores(text, positive_words, negative_words):
    cleaned_tokens = preprocess_text(text)
    positive_score = sum(1 for word in cleaned_tokens if word in positive_words)
    negative_score = sum(1 for word in cleaned_tokens if word in negative_words)
    polarity_score = (positive_score - negative_score) / (positive_score + negative_score + 0.000001)
    return positive_score, negative_score, polarity_score

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    cleaned_tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
    return cleaned_tokens

def calculate_subjectivity_score(positive_score, negative_score, text):
    total_words = len(preprocess_text(text))
    return (positive_score + negative_score) / (total_words + 0.000001)

def calculate_avg_sentence_length(text):
    sentences = nltk.sent_tokenize(text)
    total_sentences = len(sentences)
    total_words = len(preprocess_text(text))
    return total_words / (total_sentences + 0.000001)

def calculate_readability(text):
    total_words = len(preprocess_text(text))
    complex_word_count = sum(1 for word in preprocess_text(text) if syllable_count(word) > 2)
    percentage_complex_words = (complex_word_count / total_words) * 100
    avg_sentence_length = calculate_avg_sentence_length(text)
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
    return percentage_complex_words, fog_index

def calculate_avg_num_words_per_sentence(text):
    total_words = len(preprocess_text(text))
    sentences = nltk.sent_tokenize(text)
    total_sentences = len(sentences)
    return total_words / (total_sentences + 0.000001)

def calculate_complex_word_count(text):
    return sum(1 for word in preprocess_text(text) if syllable_count(word) > 2)

def calculate_word_count(text):
    return len(preprocess_text(text))

def syllable_count(word):
    vowels = 'aeiouy'
    count = 0
    prev_char_was_vowel = False
    for char in word:
        char = char.lower()
        if char in vowels:
            if not prev_char_was_vowel:
                count += 1
                prev_char_was_vowel = True
        else:
            prev_char_was_vowel = False
    if word.endswith('e'):
        count -= 1
    if count == 0:
        count += 1
    return count

def calculate_syllable_per_word(text):
    words = preprocess_text(text)
    total_syllables = sum(syllable_count(word) for word in words)
    total_words = len(words)
    return total_syllables / (total_words + 0.000001)

def calculate_personal_pronouns(text):
    personal_pronouns = ['i', 'we', 'my', 'ours', 'us']
    tokens = word_tokenize(text.lower())
    return sum(1 for token in tokens if token in personal_pronouns)

def calculate_avg_word_length(text):
    words = preprocess_text(text)
    total_characters = sum(len(word) for word in words)
    total_words = len(words)
    return total_characters / (total_words + 0.000001)

if __name__ == "__main__":
    main()
