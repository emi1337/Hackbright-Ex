from sys import argv

script, filename = argv

text = open(filename).read()

wordlist = []
markov_dict = {}
list_to_add = []
index = 0
linelist = text.splitlines()

for line in linelist:
    # make a list of words for each iterated line
    list_to_add = line.split(' ')
    # append that list of words to your FULL list of words
    wordlist += list_to_add

for word in wordlist:
    if index < (len(wordlist)-1):
	    markov_dict[word]=(wordlist[index+1],1)
	    print markov_dict
	    markov_dict["some"] = ("string", 1)
	    print markov_dict
	    markov_dict = {"some": ("string", 1)}
	    print markov_dict
	    index += 1
