#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:35:32 2018

@author: jlopes

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3 (RLE), 2012
"""

import time


# utility function
def load_from_file(filename):
    """ Read words from filename, return list of words. """
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    return file_content


# Linear Search (see other elsewhere)
def search_linear(xs, target):
    """ Find and return the index of target in sequence xs """
    for (i, v) in enumerate(xs):
        if v == target:
            return i
    return -1


# Binary Search (see other elsewhere)
def search_binary(xs, target):
    """ Find and return the index of key in sequence xs """
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub:   # If region of interest (ROI) becomes empty
            return -1

        # Next probe should be in the middle of the ROI
        mid_index = (lb + ub) // 2

        # Fetch the item at that position
        item_at_mid = xs[mid_index]

        # print("ROI[{0}:{1}](size={2}), probed='{3}', target='{4}'"
        #       .format(lb, ub, ub-lb, item_at_mid, target))

        # How does the probed item compare to the target?
        if item_at_mid == target:
            return mid_index      # Found it!
        if item_at_mid < target:
            lb = mid_index + 1    # Use upper half of ROI next time
        else:
            ub = mid_index        # Use lower half of ROI next time


# The basic strategy is to run through each of the words in the book,
# look it up in the vocabulary, and if it is not in the vocabulary,
# save it into a new resulting list which we return from the function
def find_unknown_words(vocab, wds):
    """ Return a list of words in wds that do not occur in vocab """
    result = []
    for w in wds:
        if BINARY:
            if (search_binary(vocab, w) < 0):  # binary search
                result.append(w)
        else:
            if (search_linear(vocab, w) < 0):  # linear search
                result.append(w)
    return result


# split vocabulary in words
def load_words_from_file(filename):
    """ Read words from filename, return list of words. """
    file_content = load_from_file(filename)
    wds = file_content.split()
    return wds


# now read a sensible size vocabulary
bigger_vocab = load_words_from_file("vocab.txt")
print()
print("There are {0} words in the vocabulary.\nStarting with\n{1} "
      .format(len(bigger_vocab), bigger_vocab[:6]))


# Books are full of punctuation, and have mixtures of lowercase and uppercase
# letters. We need to clean up the contents of the book. This will involve
# removing punctuation, and converting everything to the same case
# (lowercase, because our vocabulary is all in lowercase)
def text_to_words(the_text):
    """ return a list of words with all punctuation removed,
        and all in lowercase.
    """
    my_substitutions = the_text.maketrans(
      # If you find any of these
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      # Replace them by these
      "abcdefghijklmnopqrstuvwxyz                                          ")
    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds


# clean book
def get_words_in_book(filename):
    """ Read a book from filename, and return a list of its words. """
    file_content = load_from_file(filename)
    wds = text_to_words(file_content)
    return wds


# Now we're ready to read in our book
book_words = get_words_in_book("AliceInWonderland.txt")
print()
print("There are {0} words in the book.\nThe first 24 are\n{1}"
      .format(len(book_words), book_words[:24]))

BINARY = False
BINARY = True

# let us make some timing measurements
print()
print("Finding missing words...")
t0 = time.clock()
missing_words = find_unknown_words(bigger_vocab, book_words)
t1 = time.clock()
print()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds.".format(t1-t0))
#print(missing_words)
