# Task 38 Compulsory Task 1

# This program will serve as an example for the similarity comparison method included in the SpaCy module:

# Import statement and shortcut name variable for 'en_core_web_sm' method:
import spacy
nlp = spacy.load('en_core_web_sm')

# Variable names given to example words after applying our nlp method:
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# print statement for similarities between 2 words:
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# The output from the above code was generally expected, however I did find it interesting to see how specifically it
# calculates the similarity.  It would be very interesting to find out exactly how it draws this comparison and makes
# a decision to such a precise mathematical figure.

# Series of words assigned as a string named tokens:
tokens = nlp('cat dog apple monkey tree fish banana')

# Nested For Loops used to iterate through our string, comparing each word with each other word:
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# When introducing more tokens, it was interesting to see some of the calculations were perhaps different that I'd
# expected. Namely I had anticipated tree having a slightly higher similarity with apple, and potentially with monkey,
# given that apples grow on trees and monkeys often live in them.

# Second string using my own example words:
tokens_new = nlp('guitar microphone gig wombat butterfly metallica')

for token1 in tokens_new:
    for token2 in tokens_new:
        print(token1.text, token2.text, token1.similarity(token2))

# For this second test I decided to combine tokens with a probably strong link (guitar/microphone, wombat/butterfly)
# with tokens that may or may not link with others (metallica/guitar), as well as throwing in some words with
# multiple meanings (like gig) to see the results.  It was interesting to see that tokens like gig/metallica
# had extremely low similarity, even going into negative values, whereas seemingly unrelated tokens like metallica/
# butterfly had relatively strong similarities.

# The pdf did not make it clear whether I should run the included example file with the simpler 'en_core_web_sm' model
# or to use it on this file, but I tried both and found that, with the data on the example file, was very difficult to
# draw a comparison between the two, given the lack of labels on the results.  Regardless, it appears that
# en_core_web_sm has no word vectors loaded with it, and so the similarity between words is based on other factors.
# Ironically the simpler model, when run on this file, did actually return stronger correlations between tokens like
# gig/metallica compared with the _md model.