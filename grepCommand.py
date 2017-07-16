import re, os

loc = '/cygdrive/c/Swapnil/Work/Study/'
loc = '/cygdrive/c/Swapnil/Work/Study/Interview/PROGRAMS'

# for (dirpath, dirnames, filenames) in os.walk(loc):
#     print "{} {} {}".format(dirpath, dirnames, filenames)

def grepCommand(parent, pattern):
    for child in os.listdir(parent):
        childPath = os.path.join(parent, child)
        if os.path.isdir(childPath):
            grepCommand(childPath, pattern)
        else:
            fp = open (childPath, 'r')
            for line in fp.readlines():
                searchObj = re.search(pattern, line)
                if searchObj:
                    print line

grepCommand(loc, 'printf')
