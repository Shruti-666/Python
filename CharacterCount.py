#Write a program for counting the number of every character of a given text file.

import collections
import pprint

path = "E:\Python\Sample_File..txt"

with open(path,'r') as data:
    count_data = collections.Counter(data.read().upper())
    count_value = pprint.pformat(count_data)
print(count_value)