# !/usr/bin/env python
# -*- coding: utf-8 -*-

#########################################################
#
# A simple script to create a random string of city names
# from a to z and copy that to Robofont’s Space Center. 
# The content in the file cities.txt is based on data 
# from http://www.geonames.org/
#
# 2015 Benedikt Bramböck
# @arialcrime
#
#########################################################

from mojo.UI import OpenSpaceCenter

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

# Copy list of cities to clipboard
# os.system("echo '%s' | pbcopy" % azcities)

print azcities
sp = OpenSpaceCenter(CurrentFont())
sp.setRaw(azcities)