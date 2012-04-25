"""
This is a script to find duplicate source entries in a TMX file.  This will only work with Python 2.7 (as opposed to Python 3)
Bill Blanchard
Licensed Under GNU/GPL 2012.
No support is implied or available for this script, you're on your own.
"""

from sys import argv

#function to gather total number of lines in file
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
        return i + 1

#get arguments passed at runtime    
script, filename = argv

#repeat file name being checked
print "File %r to be checked" % filename

print "Getting number of lines... \n"

#get number of lines in file
count = file_len(filename)
print "Total number of lines is: %i \n" % count

#open file name for reading, build array called "lines" with each line
txt = open(filename)
lines = txt.readlines()

#open the log file for writing
log = open('log.txt', 'w+')
log.write("The following source segments have matches: \n")

#Prompt user for the source segment language code
print "Please input the language code of the source you are searching against: \n"
prompt = '>'
lang_code = raw_input(prompt)

#Prompt user for the text of the source segment they would like to find duplicates for
print "Please input the text of the source segment you are searching for: \n"
prompt = '>'
source_segment = raw_input(prompt)

realcount = 0
print "The following source segments have multiple entries: \n"

while count !=0:
    subcount = realcount + 1
    
    #the source line is what we want to compare the remaining lines against
    source_line = lines[realcount]
    
    #if the line is of the type that we actually want to compare
    if source_line[0:3] == "hit":
        
        #examine all of the lines after the source to see if there is a match
        while subcount < count:
            target_line = lines[subcount]
            if source_line == target_line:
                announce_text = (source_line)
                print announce_text 
                log.write(announce_text + "\n")
            subcount = subcount + 1
        count -= 1
        realcount += 1
    else:
        #neg_text = "Line %i No Hits" % realcount
        #print neg_text
        #log.write(neg_text + "\n")
        count -= 1
        realcount += 1