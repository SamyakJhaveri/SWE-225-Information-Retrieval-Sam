# from lib2to3.pgen2.tokenize import tokenize
import re
import timeit
import operator
from string import punctuation

def tokenize(text_file_name):
    ''' Problem sub-statement from the Assignment 1 Description on Canvas:
        Write a method/function that reads in a text file and returns a list of 
        the tokens in that file. 
        For the purposes of this project, a token is a 
            1. sequence of alphanumeric characters along with a few special 
            characters [a-zA-Z0-9@#*&'],
            2. independent of capitalization (so Apple, apple, aPpLe 
        are the same token). 
        
        You are allowed to use regular expressions if you wish to 
        (and you can use some regexp engine, no need to write it from 
        scratch), but you are not allowed to import a tokenizer (e.g. from NLTK),
        since you are being asked to write a tokenizer. 
        Input: Text File Path
        Output: List of tokens in that text file
        TODO: Make it take input of file path from command line
        TODO: Make it more efficient by tokenizing it line-by-line instead of jamming 
        the whole text file into memeor at once. Use help from the link Pooja Sent you
        TODO: Try the other tokenization techniques from the tokenization_playground
        TODO: Explain the code as per the instructions of the Assignment
    '''
    # sample text in string form: 'Your New Password is: E.D.I.T.H@tony#glasses.'
    # Step 1 Read a text file (from Computer)
    f = open(text_file_name, 'r')
    # contents = f.read()
    # f.close()
    # return contents


    # Step 2 Tokenize the text in the text document
    #   Step 2.a Convert everything into lowercase
    # contents = contents.lower()
    # print(contents)
    #   Step 2.b Tokenize the text using Regex Python library

    # Writing to a file
 
    # Using readline()
    count = 0
    clean_text = ''
    while True:
        count += 1
 
        # Get next line from file
        line = f.readline()
        line = line.lower()
        # if line is empty
        # end of file is reached
        if not line:
            break
        clean_line = re.sub(r"[^a-zA-Z0-9@#*&'\s]+", "", line)
        clean_text += clean_line
        # print("Line{}: {}".format(count, line.strip()))
 
    f.close()
    
    # clean_text = re.sub(r"[^a-zA-Z0-9@#*&'\s]+", "", contents)
    tokens = clean_text.split()
    return tokens

def computeWordFrequencies(tokens):
    '''
    Problem sub-statement from the Assignment 1 Description on Canvas::
    Write another method/function that counts the number of occurrences of each token in the token list. 
    Remember that you should write this assignment yourself from scratch so you are not allowed to 
    import a counter when the assignment asks you to write that method.
    Input: List<Tokens>
    Output: Map<Token, Count> which is essentially a dictionary
    TODO: Explain the code as per the instructions of the Assignment
    '''
    token_dict = {}
    for token in tokens:
        if token in token_dict:
            token_dict[token] += 1
        else:
            token_dict[token] = 1
    return token_dict

def print_tokens(token_dict):
    '''
    Finally, write a method that prints out the word frequency count onto the screen. 
    The print out should be ordered by decreasing frequency (so, the highest frequency 
    words first).
    Input: token_dict (Dictionary of Tokens)
    Output: prints th tokens in descending order of their frequencies 
    '''

    sorted_token_list = []
    # sorted_token_dict = dict(sorted(token_dict.items(), key=operator.itemgetter(1),reverse=True))

    print('The tokens with their frequencies in sorted order (descending) are:')
    for k, v in (sorted(token_dict.items(), key=lambda item: item[1], reverse = True)):
        print('({}: {})'.format(k, v))
    


def main():
    s = 'part_a_test_text.txt'

    tokens = tokenize(s)
    print('The Tokens are:{}'.format(tokens))

    token_dict = computeWordFrequencies(tokens)
    print('The tokens with their frequencies are:{}'.format(token_dict))
    print_tokens(token_dict)
    


if __name__ == "__main__":
    main()





