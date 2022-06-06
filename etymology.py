#*************************************#
#Student:  Mirela Ratoi
#Olat name: mratoi
#Matriculation Nr: 20-752-093
#*************************************#

from typing import List, Tuple


def get_etymology(lemma_list: List)->Tuple:
    """
    Create lists of words from corpus by heritage::
    :param processed_text: the obtained lemma list
    :return: From corpus:
            -a list of latin words
            -a list of slavic words
            -a list of dacian words
            -a list of greek words
            -a list of turkish words
            -a list of  words of different origins
    """
    slavic_part = []
    dacian_part = []
    latin_part = []
    greek_part = []
    turkish_part = []
    divers_part = []
    with open('data/slavic.txt', 'r', encoding ='utf-8') as file:
        slavic_words = file.read().split("\n")
    with open('data/dacian.txt', 'r', encoding='utf-8') as file:
        dacian_words = file.read().split("\n")
    with open('data/greek.txt', 'r', encoding='utf-8') as file:
        greek_words = file.read().split("\n")
    with open('data/turkish.txt', 'r', encoding='utf-8') as file:
            turkish_words = file.read().split("\n")
    with open('data/other.txt', 'r', encoding='utf-8') as file:
        other_words = file.read().split("\n")
        for lemma in lemma_list:
            if lemma in slavic_words:
                slavic_part.append(lemma)
        for lemma in lemma_list:
            if lemma in dacian_words:
                dacian_part.append(lemma)
        for lemma in lemma_list:
            if lemma in greek_words:
                greek_part.append(lemma)
        for lemma in lemma_list:
            if lemma in turkish_words:
                turkish_part.append(lemma)
        for lemma in lemma_list:
            if lemma in other_words:
                divers_part.append(lemma)
        for lemma in lemma_list:
            if lemma not in slavic_words and lemma not in dacian_words and lemma not in greek_part \
                    and lemma not in turkish_part and lemma not in divers_part:
                latin_part.append(lemma)
    return (latin_part, slavic_part, dacian_part, greek_part,turkish_part, divers_part)
