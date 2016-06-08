"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided
codeskulptor.set_timeout(30)

WORDFILE = "assets_scrabble_words3.txt"
#print codeskulptor.file2url("assets_scrabble_words3.txt")


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    result = []
    pointer = None
    for item in list1:
        if item != pointer:
            result.append(item)
            pointer = item
    return result

#print remove_duplicates([])
#print remove_duplicates([1,1])
#print remove_duplicates([1,3,3,4,4,5])

def binary_search(item, sorted_list):
    """
    help function
    """
    if sorted_list == []:
        return False
    if len(sorted_list) == 1:
        return item == sorted_list[0]
    elif item < sorted_list[len(sorted_list)/2]:
        return binary_search(item, sorted_list[:len(sorted_list)/2])
    elif item > sorted_list[len(sorted_list)/2]:
        return binary_search(item, sorted_list[len(sorted_list)/2 + 1:])
    else:
        return True
        
#print binary_search(1, [0,1,2,3])

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    result = []
    if len(list1) < len(list2):
        iterate = list1
        sorted_list = list2
    else:
        iterate = list2
        sorted_list = list1
        
    for item in iterate:
        if binary_search(item, sorted_list):
            result.append(item)
    return result

#print intersect([], [])
#print intersect([1,2], [2,3])
#print intersect([1,2,3,4], [5,6])
#print intersect([1,2,3,4], [1,2,3,4,5])

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """   
    result = []
    list1_num = len(list1)
    list2_num = len(list2)
    pointer1 = 0
    pointer2 = 0
    while (pointer1 < list1_num and pointer2 < list2_num):
        if list1[pointer1] <= list2[pointer2]:
            result.append(list1[pointer1])
            pointer1 += 1
        else:
            result.append(list2[pointer2])
            pointer2 += 1
    result +=  list1[pointer1:] + list2[pointer2:]
    return result

#print merge([], [])
#print merge([1,2], [2,3])
#print merge([1,2,3,4], [5,6])
#print merge([1,2,3,4], [1,2,3,4,5])
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    len_list1 = len(list1)
    if len_list1 <= 1:
        return list1
    else:
        left = merge_sort(list1[:len_list1 / 2])
        right = merge_sort(list1[len_list1 / 2:])
        return merge(left, right)
    
    
#print merge_sort([])
#print merge_sort([1])
#print merge_sort([5,3,4,2,1])
    

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    word_len = len(word)
    if word_len == 0:
        return [""]
    fisrt_char = word[0]
    rest_word = word[1:]
    result = gen_all_strings(rest_word)
    for string in result[:]:
        for cut in range(len(string)+1):
            result.append(string[:cut] + fisrt_char + string[cut:])
    return result

#print gen_all_strings("ab")
#print gen_all_strings("abc")


# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    datafile = urllib2.urlopen(codeskulptor.file2url(filename))
    data = datafile.read()
    result = data.split()
    return result

#print load_words(WORDFILE)

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
run()

    
    