#!/usr/bin/env python

# things to fix later:
# words that end with a period should NOT have the next word be included in their markov rule list because it's a separate, potentially unrelated sentence.
    # but then do you have to keep periods on the words instead of splitting them up?
    # and do you ALSO need those because how will you make full sentences in the generator otherise --> is it just a gamble if the sentence is "ended"?

from sys import argv
import random

def make_chains(corpus):

    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    # take the 1-string text, turn it into list of words
    wordlist = []
    linelist = corpus.splitlines() # return a list, where each item is one line
    list_to_add = []

    for line in linelist:
        # make a list of words for each iterated line
        list_to_add = line.split(' ')
        # append that list of words to your FULL list of words
        wordlist += list_to_add 
    # keep index of where in the list you are
    index = 0
    # make dictionary
    markov_dict = {}
    # take every word FROM THE LIST and make a dictionary key of it if none exists
    # the dictionary value will be a list INCLUDING the following word
    # if the word exists in the dictionary
    for word in wordlist:
        # if we're NOT at the second to last word, then make the spot in the dictionary for it, otherwise the last word doesn't have a following word so you should do anything.
        if index < (len(wordlist)-2):
            word_plus_secondword = (word, wordlist[index+1])
            third_word = wordlist[index+2]
            # check to see if word PAIR is key in dictionary
            if word_plus_secondword in markov_dict:
                """
                EASIER WAY WITHOUT KEEPING COUNT FOR EACH APPEARANCE OF FOLLOWING WORD 
                """
                # if in dictionary, add THIRD word following pair to LIST found in values of that place in the dictionary
                markov_dict[word_plus_secondword].append(third_word) # values, last of strings

                """HARDER WAY NOT YET CODED OF KEEPING COUNT
                """
                # for index, (second_word, sec_word_count) in enumerate(nextword_list)
                # iterate through the markov dictionary to use the second_word list 
                # which means either increase the count or add a NEW word that follows if the word isn't in the tuple list
                
                # GET THE VALUE
                # nextword_list = markov_dict[word]
                # # print nextword_list
                # nextword = wordlist[index+1]
                # #                                 0           1              2
                # # markov_dict = {"the": (("animal", 1), ("pig", 1), ("stuff", 1)), "animal": ("does", 1), ("fell",1)}
                # if nextword in nextword_list:
                #     # use find to get index of nextword
                #     tempindex = nextword_list.index(nextword)
                #     temptuple = nextword_list[tempindex]
                #     # this index gives you a LIST of length 2 (tuple)
                #     temptuple[] += 1
                #     nextword_list[tempindex] = temptuple
                #     markov_dict[word] = nextword_list
                # else:
                #     pass


                    # add new tuple of that (nextword, 1)
                # [(wordlist[index+1]).lower(),1]

                # word.lower(), secondword_list in markov_dict.iteritems():
                # print "%s is a word here?" % word
                # LEARN TO USE ONLY VALUES OF DICTS
                
                # if it is 
                # check to see if 2nd_word is in tuples

                # iterate through value list
                # check if 2nd word is in list
                    # if is, add one to count
                    # if it isn't, append tuple to list, with count = 1
                # if it isn't
            else:
                # print "%s isn't present" % word
                markov_dict[word_plus_secondword]=[third_word]
                
                # for later when we make it more efficient
                # add third word in with count = 1 as first list of 2 in a list of words
                # markov_dict[word_plus_secondword]=[wordlist[index+2],1]

            # tell index count we're gonna be on the next word 
            index += 1
    return markov_dict

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    markoved_text = ''
    # randomly pick 2 partnered words, a random key in dictionary now being referred to as "chains" from when it was an argument during the calling of make_text
    # added those 2 words to markoved_text
    firsttuple = random.choice(chains.keys())
    randompickfollowing = firsttuple[0] + ' ' + firsttuple[1]
    
    while len(markoved_text) + len(randompickfollowing) < 141:
        markoved_text += ' ' + randompickfollowing

        lasttwolist = markoved_text.split()[-2:]

        if (lasttwolist[0], lasttwolist[1]) in chains:
            listpossiblewords = chains[(lasttwolist[0], lasttwolist[1])]
            print listpossiblewords
            markoved_text += ' ' + random.choice(listpossiblewords)
        else:
            print "couldn't find the last two words in the dictionary"


    markoved_text += '.'

    # use that function that turns the string into "sentence strings" with the first letter before the period capitalized, etc etc.
    return markoved_text

def main():
    script, filename = argv

    text = open(filename).read()

    chain_dict = make_chains(text.lower())
    random_text = make_text(chain_dict)
    print random_text


if __name__ == "__main__":
    main()

"""
dictMarkov:
{the: [(animal, 2), (pig, 4), (farm, 1), (water,9)]}
"""
