#########################
#
# This script gets a wikipedia article and styles it - that is all.
# Uses the wikipedia module from https://wikipedia.readthedocs.org/
#
# (c) Benedikt Bramboeck
#
# Genral problem:
#  * formatedstring won't go into textBox, normal text works though _ why?
#    ValueError: depythonifying 'float', got 'unicode'
#  * selection could be made better 
#
#########################


#fix to get the external module to work within Drawbot
import sys
sys.path.append("/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/")

import wikipedia

wikipedia.set_lang('de')
minlength = 3000

##Db Defaults
size('A4Landscape')
hFont = 'Charter-Bold'
tFont = 'Charter-Roman'
iFont = 'Charter-Italic'
x = 30
y = 30
w = (width()-100)/2
h = height()-140

def getPage():
    rpage = wikipedia.page(wikipedia.random(1))
    while len(rpage.content) <= minlength:
        try:
            #TODO: Exception for lists
            rpage = wikipedia.page(wikipedia.random(1))
        except wikipedia.exceptions.DisambiguationError as e:
            print 'ERROR'
            rpage = wikipedia.page(e.options[0])
        else:
            print 'MISS'
            rpage = wikipedia.page(wikipedia.random(1))
    return rpage
    
def drawText(s):
    fontSize(10)
    overflow = textBox(s,(x, y, w, h))
    textBox(overflow,(x + width()/2, y, w-30, h))

rpage = getPage() 
print rpage.title

#drawText(rpage)
txt = FormattedString()
links = rpage.links
rpagewords = rpage.content.split(' ')

#print rpagewords
#print links
#rpagewords = ' '.join(rpagewords)
#print rpagewords
#txt.append(rpagewords)

for w in rpagewords:
    if w in links:
        txt.append(w + ' ', iFont)
    else:
        txt.append(w + ' ', tFont)
#print rpage.links
#It does work with a normal text field, however, the textBox produces an error
text(txt, (x,y))
#textBox(txt, (x,y, w, h))
#drawText(txt)
