"""
Note: the code and pseudocode written in the .py file are assuming that there is a dictionary which contains all of the unique words in the database, and the positions were in the database they appear


The blast algorithm is made from a sequence of steps, denoted below:
-take the input query (DNA, for now) and create a list of words from it
-take all those words, and create a nested list that contains all of the positions of all of the words in the query, that are in the database
-take those positions of the words in the database, and experiment with shifting them back and forth, in order to get the best sequence to put in the Smith-Waterman algorithm
-run the Smith-Waterman algorithm and receive seeds
-input the seeds in a DP minimum edit distance algorithm, that compares it with the original input sequence
-return the top five minimum edit distance seeds, or the seeds in increasing order of edit distance, or something else TBD


"""

#from colinscode import databasedict

def createListofWords(input_seq):
    """
    takes the input sequence, and returns all of the possible words from it
    as of now, we're only looking at DNA, so words are 11 bases long

    input_seq : sequence that the user inputs, given as a string

    returns input_words, list of words in input sequence
    """

    #checking that input string is correct
    if len(input_seq)<11:
        assert len(input_seq)=>11, "input string too small"

    #if there's only one word
    if len(input_seq) == 11:
        return input_seq
    #else
    input_words = []
    for i in len(input_seq-10):
        input_words.append(input_seq[i:i+11])
    return input_words

def createPositionsList(input_words, databasedict):
    """
    takes in a list of words in input sequence and the dictionary of the data
    returns a nested list of all the positions of the words in the database

    input_words: list of words in input_seq
    databasedict: dictionary that contains all unique words in the database and the positions where they occur

    returns position_list, nested list
    """
    position_list = [] #output list
    #find the corresponding positions for each word
    for word in input_words:
        if word in databasedict: #make sure the word is there
            position_list.append(databasedict[word])
    return position_list



# Test Functions

### Test Functions for createListofWords

### Test Functions for createPositionsList