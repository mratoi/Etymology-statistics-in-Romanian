#*************************************#
#Student:  Mirela Ratoi
#Olat name: mratoi
#Matriculation Nr: 20-752-093
#*************************************#

from typing import List
import spacy
from typing import TextIO
nlp = spacy.load('ro_core_news_sm')


def pre_process(filename:TextIO)->str:
    """
    Preprocess the corpus to get only lowercase words, no punctuation:
    :param filename: The corpus to be processed.
    :return: a string where all the elments are word forms, no punctuation.
    """
    text = filename.read()
    text = text.lower()
    text_stripped = text.replace("\n", " ").strip()
    doc = nlp(text_stripped)
    text_no_punct = [token for token in doc if not token.is_punct]
    processed_text = ' '.join(token.text for token in text_no_punct)
    return(processed_text)


def get_list_lemma(processed_text:str)->List[str]:
    """
    Get the list of lemmas of the words in the corpus using spacy model for Romanian:
    :param processed_text: the clean string
    :return: A list of lemmas
    """
    doc =nlp(processed_text)
    lemma_list = [token.lemma_ for token in doc ]
    return(lemma_list)