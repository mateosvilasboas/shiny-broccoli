import unidecode
import string
import re
import spacy
from typing import Literal
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer


class Preprocessor:
    def __init__(self, text: str):
        self._text = text

    def preprocess(self,
                   normalize: bool = True,
                   remove_special_chars: bool = True,
                   remove_stopwords: bool = True,
                   mode: Literal["lemmatize", "stem"] = "lemmatize"):
        valid_modes = {"lemmatize", "stem"}
        if mode not in valid_modes:
            raise ValueError(
                f"mode  {mode} is not in valid_modes ({', '.join(valid_modes)})")
        
        if normalize:
            self._normalize_text()
        if remove_special_chars:
            self._remove_special_chars()
        if remove_stopwords:
            self._remove_stopwords()
        if mode == "lemmatize":
            self._lemmatize_text()
        if mode == "stem":
            self._stem_text()

        self._text = ' '.join(self._text.split())

        return self._text

    def _normalize_text(self):
        self._text = self._text.rstrip().replace("\n\n", "\n")
        self._text = self._text.lower()
        self._text = re.sub(r'\s+', ' ', self._text)
        self._text = unidecode.unidecode(self._text)

    def _remove_special_chars(self):
        keep_punctuation = '.,!?:;()_-"\'@'
        remove_chars = "".join(c for c in string.punctuation if c not in keep_punctuation)

        translator = str.maketrans('', '', remove_chars)
        self._text = self._text.translate(translator)

    def _remove_stopwords(self):
        nltk_stopwords = set(stopwords.words('portuguese'))

        email_stopwords = {
            "prezado",
            "prezada",
            "caro",
            "cara",
            "estimado",
            "estimada",
            "atenciosamente",
            "cordialmente",
            "ate",
            "mais",
            "abracos"
        }

        keep_words = {
            "nao",
            "muito",
            "pouco",
            "sempre",
            "nunca",
            "urgente",
            "critico",
            "importante",
            "necessario"
        }

        all_stopwords = (nltk_stopwords | email_stopwords) - keep_words
        words = self._text.split()
        filtered_words = []

        for word in words:
            if word.isupper() and len(word) > 2:
                filtered_words.append(word)
            elif word.lower() not in all_stopwords:
                filtered_words.append(word)

        self._text = ' '.join(filtered_words)

    def _stem_text(self):
        stemmer = RSLPStemmer()
        stemmed_words = []

        words = self._text.split()
        for word in words:
            if word.isupper():
                stemmed_words.append(word)
            elif len(word) <= 2:
                stemmed_words.append(word)
            else:
                stemmed_words.append(stemmer.stem(word))

        self._text = ' '.join(stemmed_words)

    def _lemmatize_text(self):        
        nlp = spacy.load('pt_core_news_sm')
        doc = nlp(self._text)
        
        lemmas = [token.lemma_ for token in doc if not token.is_punct and not token.is_space]
        
        self._text = ' '.join(lemmas)