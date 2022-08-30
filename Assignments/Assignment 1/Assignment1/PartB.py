import re
import sys
import timeit
import operator
from string import punctuation
from assignment1_part_a import *
# can make a global object of part_a.py here to access functions from parrt_a.py here.
def common_tokens(tokens1, tokens2):
    common_token_counter = 0
    return (len(tokens1.intersection(tokens2)))


    # takes text file inputs from comman line
    # sends the paths of the text files to part_a.py
    # part_a.py returns list of tokens upon tokenizing the text in the file
    # total 2 token loists are recieved from part_a.py - one for each text file inputted here
    # every time there is a common token found among both the token lists, the counter increments
    # return the counter


def main():
    input_file_path_1 = sys.argv[1]
    input_file_path_2 = sys.argv[2]
    obj = part_a()
    tokens1 = obj.tokenize(input_file_path_1)
    tokens2 = obj.tokenize(input_file_path_2)
    tokens1 = set(tokens1)
    tokens2 = set(tokens2)
    print(common_tokens(tokens1, tokens2))



if __name__=="__main__":
    main()

# References/Bibliography: Taken some help from Stack Overflow, YouTube, GeeksforGeeks and Python Documentation

