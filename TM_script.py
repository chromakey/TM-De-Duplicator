"""
This is a script to find duplicate source entries with different translations in a TMX file.  
This will only work with Python 2.7 (as opposed to Python 3)

No support is implied or available for this script, you're on your own.  If it breaks your TM, sorry I can't help you.  User beware!
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

realcount = 0
match_count = 0
unique_segments = []

print "Please wait, this could take a while depending on the size of the TMX file: \n"

while count !=0:
    subcount = realcount + 1
    
    #the source line is what we want to compare the remaining lines against
    source_line = lines[realcount]
    
    #if the line is of the type that we actually want to compare
    if (source_line[0:27] == "<tuv xml:lang=\"en-US\"><seg>" and source_line[28] != "<"):     
        #examine all of the lines after the source to see if there is a match
        different_trans_count = 0
        while subcount < count:
            
            target_line = lines[subcount]
            #If the source of the source segment matches the source of the target segment, log it
            if source_line == target_line:
                source_line = source_line[:-13]
                announce_text = (source_line[27:])
                if lines[realcount + 1] != lines[subcount + 1]:
                    different_trans_count += 1
                    
                    #check to see if we already have a log entry for it
                    is_unique = 1
                    for seg in unique_segments:
                        if seg == announce_text:
                            is_unique = 0
                            break
                    
                    if is_unique == 1:
                        log.write(announce_text + "\n")
                        unique_segments.append(announce_text)
                        match_count += 1
                        
            subcount = subcount + 1
        
        count -= 1
        realcount += 1
    
    else:
        count -= 1
        realcount += 1

#Show match count
if match_count == 0:
    print "No matches found!"
else:        
    print "Total number of matches: %i" % match_count

exit()