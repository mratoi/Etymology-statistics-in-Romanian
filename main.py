#*************************************#
#Student:  Mirela Ratoi
#Olat name: mratoi
#Matriculation Nr: 20-752-093
#*************************************#
"""
Output statistics over the etymology of the words from a corpus.
"""
from argparse import ArgumentParser, FileType
import spacy
nlp = spacy.load('ro_core_news_sm')

from etymology import get_etymology
from pre_processing import pre_process, get_list_lemma


def main():
    parser = ArgumentParser(description="This allows you to find statistics over any corpus you would like.")
    parser.add_argument('filename', nargs= "?", type=FileType('r'), default="data/corpus.txt",
                        help="Provide any file you like to have a statistics about. ")
    args = parser.parse_args()
    processed_text = pre_process(args.filename)
    lemma_list= get_list_lemma(processed_text)
    var_lists = get_etymology(lemma_list)
    procentage_latin = round(len(var_lists[0]) * 100 / len(lemma_list),2)
    procentage_slavic = round(len(var_lists[1]) * 100 / len(lemma_list),2)
    procentage_dacian = round(len(var_lists[2]) * 100 / len(lemma_list),2)
    procentage_greek = round(len(var_lists[3]) * 100 / len(lemma_list),2)
    procentage_turkish = round(len(var_lists[4]) * 100 / len(lemma_list),2)
    procentage_divers = round(len(var_lists[5]) * 100 / len(lemma_list),2)

    print("\n", f'In the given corpus: ',"\n",
          f'The percentage of words of Latin heritage in the corpus is: {procentage_latin} %',"\n",
    f'-the percentage of words of Slavic heritage in the corpus is: {procentage_slavic} %', "\n",
    f'-the percentage of words of Dacian heritage in the corpus is: {procentage_dacian} %', "\n",
    f'-the percentage of words of Greek heritage in the corpus is: {procentage_greek} %', "\n",
    f'-the percentage of words of Turkish heritage in the corpus is: {procentage_turkish} %', "\n",
    f'-the percentage of words of other heritage in the corpus is: {procentage_divers} %')




if __name__ == '__main__':
    main()



