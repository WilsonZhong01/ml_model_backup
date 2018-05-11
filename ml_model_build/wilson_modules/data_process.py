# -*- coding:utf-8-*-
import pandas as pd
import string, re, collections
from collections import namedtuple
import numpy as np

# check if the feature includes words in our words_library

def ads_search(obj_content):
    if obj_content:
        file_obj = open('/home/wilson/Desktop/databases/words_library.txt', 'r')
        words_library = file_obj.read()
        ads_library = re.compile(words_library, re.I)
#         print(obj_content)
        result = ads_library.findall(obj_content)
        if result:
            
            return 0 # exist ads return 0
        else:
            return 1
    else:
        return 1


# check if the feature includes phone numbers
def phone_search(feature_s):
    if feature_s:
        phone_re = re.compile('(\d{3}\D{0,1}\d{3}\D{0,1}\d{4})')
        phone_label = phone_re.findall(feature_s)
        if phone_label:
            return 0# contains 0
        else:
            #         print("This sentence doesn't contain phone num")
            return 1
    else:
        return 1


# count the length of a string
def string_len(sentence_in):
    count_en = count_dg = count_sp = count_zh = count_pu = 0
    if sentence_in:
        s_leng = len(sentence_in)
        for one in sentence_in:
            if one in string.ascii_letters:
                count_en += 1
            elif one.isdigit():
                count_dg += 1
            elif one.isspace():
                count_sp += 1
            elif one.isalpha():
                count_zh += 1
            else:
                count_pu += 1

        total_chars = count_en + count_dg + count_sp + count_zh + count_pu
        if total_chars == s_leng:
            return (count_en, count_dg, count_sp, count_zh, count_pu)
        else:
            print('String length counting is wrong')
            return None
    else:
        return (count_en, count_dg, count_sp, count_zh, count_pu)


# count the num of english words in one signature
def count_words(sentence_in):
    if sentence_in:
        word_find = re.compile('[a-zA-Z0-9]+')
        counter = collections.Counter(word_find.findall(sentence_in))
        kind_words = len(counter)
        num_words = sum(counter.values())
        return (kind_words, num_words)
    else:
        return(0,0)

def apply_and_concat(dataframe, field, func, column_names):
    return pd.concat((
        dataframe,
        dataframe[field].apply(
            lambda cell: pd.Series(func(cell), index=column_names))), axis=1)

