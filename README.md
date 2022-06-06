# Etymology statistics in Romanian
Gitlab repository @: https://gitlab.uzh.ch/mirela-vasilica.ratoi/etymology-statistics-in-romanian 



## Description

The intention of this project is to let the user get some statistics about hoch percentage of their Romanian corpus is of Latin, Slavic, Dacian, greek,Türkish odr other different heritage. The program goes through a corpus lemmatized with the SPACY Romanian model (not the best, but there are not many resources for working with Romanian). It compares every lemma against the  words of different heritages and appends separate lists for each of them. The remaining words are appended to the list of words of Latin origin. We admit that this is not the most statiscally accurate method. The programm puts out statitics in procents retrieved through computing the lenght of the lists. 

# Idea

Is Romanian a Latin language or a Slavic language?
Many who are unfamiliar with the language assume that it must be Slavic in nature, because of its geographical position. My project  gives the user the possibility of putting in its own corpus (in a .txt format) and to get some statistics, about how many porcent of the words in their corpus are from latin, slavic, dacian, greek, turkish or others origin. 

# Research Question:

Our hypothesis is that, despite its many unique aspects, Romanian is still a Romance languageat its core and the percentage of latin vocabulary in any corus will show that. 

#Literature review:

The numbers are not always consistent, but the majority of the Romanian language history textbooks agree that the vocabulary is up to 60-70% of Latin origin. Somewhere around 15 percent of the lexical items are of Slavic origin, but there are also words of Dacian, Turkish or even German and other origins.

We are aware of the problem of borrowings: thee a lot of words which may be seen as Latin origin, but are in fact borrowings from French and Italian or other languages. We are going to ignore this aspect. The two blog articles mentioned in the References ([1] [2]) approached this question from a point of view of similarity with Latin, with other Romance languages and with other languages from the Balkan Sprachbund.

## Data and resources:
- Text data in Romanian : corpus.txt 
- Lists of most common words of different origin in Romanian:
    -Slavic words
    -Dacian words
    -Greek words
    -Turkish words
    -words of other origin
- Spacy for tokenizing and obtaining the lemma

## Installation
All the imports are specified on the files.
I provided a requirements.txt document with all the necessary intallations. 
Run main.py. It uses the default corpus as data, but one can also five their own coprus. 

## Usage
The output looks like this:

```
 In the given corpus:  
 The percentage of words of Latin heritage in the corpus is: 96.95 % 
 -the percentage of words of Slavic heritage in the corpus is: 1.0 % 
 -the percentage of words of Dacian heritage in the corpus is: 0.51 % 
 -the percentage of words of Greek heritage in the corpus is: 0.22 % 
 -the percentage of words of Turkish heritage in the corpus is: 0.17 % 
 -the percentage of words of other heritage in the corpus is: 1.15 %
 ```

## Support
If you have any questions, you cant contact me at mirela-vasilica.ratoi@uzh.ch


## License
MIT License

## Project status
The project is finalized, but one could always add more words on the lists of words of different origins, as these are still faraway from complete. 

## References
1. Miller-Broomfield, Clara: “Romanian: The forgotten Romance language”. Dialogue: The
UNRAVEL Blog. February 12,2015. https://unravellingmag.com/articles/romanian-theforgotten-
romance-language/ Issue 2. Language Profiles.

2. Languagevolcano: “Closest language to LAtin-Romanian?”. Language Volcano Blog.
https://languagevolcano.

Resources used for the lists of words of different origin:
- https://romania.fandom.com/wiki/Categorie:Liste_de_cuvinte 
- https://levantin54.wordpress.com/2013/09/12/o-sama-de-cuvinte-romanesti-de-origine-slava/


