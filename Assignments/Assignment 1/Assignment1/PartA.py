# from lib2to3.pgen2.tokenize import tokenize
import re
import sys
import timeit
import operator
from string import punctuation
class part_a(object):
    def tokenize(self, text_file_name):
        '''
        Problem sub-statement from the Assignment 1 Description on Canvas:
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
        Explanation: This function takes the path of the file as input parameter from the driver 
        function. 
        Using this link, the text file is read into the tokenizer.
        A naive approach to tokenizing the text would be to enter the entire text file's contents into
        memory and implement the operations on the entire text at once. 
        But since this is not very memory efficient, a better approach would be to do it line-by-line.
        That is the purpose of the WHILE Loop in this function. 
        The computational complexity of this function would be O(n*m) where n is the number of smaller
        sub-parts of this file and m is the number of characters the regex engine validates in the
        text file. This is so because all the operations happening inside the WHILE Loop have time 
        complexity O(1) (Constant Time) with the help of python's in-built regex library. 
        '''
        # sample text in string form: 'Your New Password is: E.D.I.T.H@tony#glasses.'
        # Step 1 Read a text file (from Computer)
        beeg_file_obj = open(text_file_name, 'r')
        smol_chunk_size = 1024*1024 # hardcoded for the expected scale of this assignment's test inputs

        # Step 2 Tokenize the text in the text document
        #   Step 2.b Tokenize the text using Regex Python library
    
        clean_beeg_text = ''
        while True:

            smol_chunk = beeg_file_obj.read(smol_chunk_size)

            if smol_chunk == "":
                break
            clean_smol_chunk = re.sub(r"[^a-zA-Z0-9@#*&'\s]+", "", smol_chunk.lower())
            clean_beeg_text += clean_smol_chunk
            # print("Line{}: {}".format(count, line.strip()))
    
        tokens = clean_beeg_text.split()
        beeg_file_obj.close()
        return tokens
 

    def computeWordFrequencies(self, tokens):
        '''
        Problem sub-statement from the Assignment 1 Description on Canvas::
        Write another method/function that counts the number of occurrences of each token in the token list. 
        Remember that you should write this assignment yourself from scratch so you are not allowed to 
        import a counter when the assignment asks you to write that method.
        Input: List<Tokens>
        Output: Map<Token, Count> which is essentially a dictionary
        Explanation:
        This function takes a list of tokens as input parameter from the driver function. 
        It establishes a token_dict dictionary and runs over every element present in the token list.
        This token list may contain repeating elements. As the for loop executes, it checks whether
        the current element already exists in the token dictionary or not. If it doesn't then it adds it to 
        the dictionary. If it does, then it increases its corresponding value (where the element itself is
        the key) by one. 
        The time complexity of this would be O(n).
        '''
        token_dict = {}
        for token in tokens:
            if len(token) >= 2:
                if token in token_dict:
                    token_dict[token] += 1
                else:
                    token_dict[token] = 1
        return token_dict

    def print_tokens(self, token_dict):
        '''
        Finally, write a method that prints out the word frequency count onto the screen. 
        The print out should be ordered by decreasing frequency (so, the highest frequency 
        words first).
        Input: token_dict (Dictionary of Tokens)
        Output: prints th tokens in descending order of their frequencies 
        Explanation: Takes the token_dict dictionary as input from the driver function.
        This dictionary already has the frequencies of the unique tokens calculated stored in it
        as a result of the opeations onthe tokens list in the computeWordFrequencies() function.
        
        '''

        sorted_token_list = []
        # sorted_token_dict = dict(sorted(token_dict.items(), key=operator.itemgetter(1),reverse=True))

        print('The tokens with their frequencies in sorted order (descending) are:')
        for k, v in (sorted(token_dict.items(), key=lambda item: item[1], reverse = True)):
            print('{} = {}'.format(k, v))
    


def main():
    obj = part_a()
    input_file_path = sys.argv[1]
    # input_file_path = input('Enter File Path:')
    # s = 'part_a_test_text.txt'
    
    tokens = obj.tokenize(input_file_path)
    print('The Tokens are:{}'.format(tokens))

    token_dict = obj.computeWordFrequencies(tokens)
    print('The tokens with their frequencies are:{}'.format(token_dict))
    obj.print_tokens(token_dict)
    

if __name__ == "__main__":
    main()

# References/Bibliography: Taken some help from Stack Overflow, YouTube, GeeksforGeeks and Python Documentation

