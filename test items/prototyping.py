# PLAN FOR IMPORT/EXPORT DATA FEATURE
'''
NEW SANDBOX SCREEN MENU:    ENTER USER DATA
                            ENTER FOOD/DRINK
                            CHECK CURRENT USER LIST
                            SEE RESULTS
                            IMPORT DATA
                            EXPORT DATA

FIXES TO BE MADE: ENTERING USER DATA SHOULD BE A BUTTON, NOT A LOCK

EXPORT (on sandbox mode screen)
    # CITATION: https://www.geeksforgeeks.org/python-convert-dictionary-object-into-string/
    # convert dictionary into string 
    # using json.dumps() 
    result = json.dumps(test1)
1. convert all data into string (userinputs, fooddict)
2. concatenate and separate by ~/; (better delimiter than , because dictionary contains ,)
3. write the result string to a file

IMPORT
    # CITATION: https://www.geeksforgeeks.org/python-convert-string-dictionary-to-dictionary/
    # using json.loads() 
    # convert dictionary string to dictionary 
    res = json.loads(test_string)
1. split the text string by ~/;
2. assign each part of the split string to the variables

Name of file: userdata.txt
'''


# CITATION: https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

contentsToWrite = "This is a test!\nIt is only a test!"
writeFile("foo.txt", contentsToWrite)

contentsRead = readFile("foo.txt")
assert(contentsRead == contentsToWrite)



# CITATION: https://www.w3schools.com/python/python_file_write.asp

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())
