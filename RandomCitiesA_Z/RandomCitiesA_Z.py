#########################################################
#
# A simple script to create a random string of city names
# from a to z. The content in the file cities.txt is based 
# on data from http://www.geonames.org/
#
# 2015 Benedikt Bramböck
# @arialcrime
#
#########################################################

import collections, random, string, os
cities = open('cities.txt', 'r')
letters = string.uppercase

azcities = ''

alphabetdict = collections.defaultdict(list)
for city in cities:
    city = city[:-1]
    alphabetdict[city[0].upper()].append(city)
    
#print alphabet
for l in letters: 
    
    add = random.choice(alphabetdict[l]) + ' '
    azcities += add

#comment this out if you do not want to copy the string to your clipboard
os.system("echo '%s' | pbcopy" % azcities)

print azcities
