
def open_read_lines(filename):
    file = open(filename, encoding="utf-8") # opens file, type:String
    file = file.readlines() # reads file, saves in variable
   # content = ""
    return file # returns String Object

def short_read(file):
    res = open_read_lines(file)
    shortText = [x for x in res if len(x) < 30]
    return shortText

def start_with_article(file):
    i = 0
    targets = ["Der", "Die", "Das"]
    targetsTuple = tuple(targets) # tuple [0,Der], [1,Die]. [2,Das]
    startRes = open_read_lines(file)   # read file, save in startRes
    #startText = tuple(startRes) # not needed
    endRes = [x for x in startRes if x.startswith(targetsTuple)] # X works with startswith, startRes does not as it is a list, not a string
    #endRes = [x for x in startText if startText.startswith(targetsTuple[i])]

    # After A LOT of searching... copied online. Any checks whether any (lol) value in an Iterable is true.
    # BUT this looks for the tuplet values in ANY Position not just the beginning
    #endRes2 = [x for x in startText if any(k in x for k in targetsTuple)]
    return endRes

'''Checks whether a Sentence (a single String) contains the word April'''
def contain_april(file):
    res = open_read_lines(file) # reads file
    endRes = [x for x in res if "April" in x]
    formatRes = endRes
    return endRes


#open_read_lines("wiki.txt") #works
#print(open_read_lines("wiki.txt"))
#print(short_read(file="wiki.txt")) #works
#print(start_with_article(file="wiki.txt")) #Finally works
print(contain_april("wiki.txt"))