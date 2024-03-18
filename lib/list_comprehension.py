#!/usr/bin/env python3

def return_evens(num_list):
    new_list = [x for x in num_list if x % 2 == 0]
    return new_list

def make_exclamation(sentence_list):
    new_list = [x + '!' for x in sentence_list]
    return new_list