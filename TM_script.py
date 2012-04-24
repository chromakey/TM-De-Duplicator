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
print "File %r to be checked:" % filename

print "Getting number of lines... \n"

#get number of lines in file
count = file_len(filename)
print "Total number of lines is: %i \n" % count

#open file name for reading, build array called "lines" with each line
txt = open(filename)
lines = txt.readlines()

#open the log file for writing
log = open('log.txt', 'w+')

realcount = 0

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
                announce_text = "Line number %i matches line number %i" % (realcount, subcount)
                print announce_text 
                log.write(announce_text + "\n")
            subcount = subcount + 1
        count -= 1
        realcount += 1
    else:
        neg_text = "Line %i No Hits" % realcount
        print neg_text
        log.write(neg_text + "\n")
        count -= 1
        realcount += 1