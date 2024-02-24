import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from spellchecker import SpellChecker
from langdetect import detect
#from imblearn.over_sampling import SMOTE


class LanguageCleanup:
    def __init__(self):
        pass
    
    def remove_html_tags(text):
        clean_text = re.sub(r'<.*?>', '', text)
        return clean_text

    def remove_special_characters(text):
        clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        return clean_text
    
    def tokenize_text(text):
        tokens = word_tokenize(text)
        return tokens
    
    def convert_to_lowercase(text):
        lowercased_text = text.lower()
        return lowercased_text
    
    def remove_stopwords(tokens):
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [word for word in tokens if word not in stop_words]
        return filtered_tokens
    
    def stem_text(tokens):
        stemmer = PorterStemmer()
        stemmed_tokens = [stemmer.stem(word) for word in tokens]
        return stemmed_tokens

    def lemmatize_text(tokens):
        lemmatizer = WordNetLemmatizer()
        lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]
        return lemmatized_tokens
    
    def correct_spelling(text):
        spell = SpellChecker()
        tokens = word_tokenize(text)
        corrected_tokens = [spell.correction(word) for word in tokens]
        corrected_text = ' '.join(corrected_tokens)
        return corrected_text
    
    def fix_encoding(text):
        try:
            decoded_text = text.encode('utf-8').decode('utf-8')
        except UnicodeDecodeError:
            decoded_text = 'Encoding Error'
        return decoded_text
    
    def remove_whitespace(text):
        cleaned_text = ' '.join(text.split())
        return cleaned_text
    
    def extract_dates_and_times(text):
        # Implement date and time extraction logic (e.g., using regular expressions)
        pass

    '''These advanced text-cleaning techniques address more nuanced challenges that 
    you may encounter when dealing with diverse and real-world text data. 
    The selection of techniques to apply should be tailored to the specific characteristics 
    of your text data and the objectives of your project.'''
    
    def balance_text_data(X, y):
        smote = SMOTE(sampling_strategy='auto')
        X_resampled, y_resampled = smote.fit_resample(X, y)
        return X_resampled, y_resampled
    
    def detect_language(text):
        try:
            language = detect(text)
        except:
            language = 'unknown'
        return language