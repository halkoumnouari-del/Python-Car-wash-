# Reads data from text file
def read_regestrations (filename):
    regestrations = []
    file = open(filename , "r")
    for line in file :
        line = line.strip()
        if line != "":
            # Splits text by | into a list
            regestrations.append(line.split("|"))
    # Closes the file
    file.close()
    return regestrations

# Appends a new record to the file
def append_regestrations(filename, data):
    #Joins list items with | and adds a new line
    line = "|".join(data) + "\n"
    # Opens file in append mode
    file = open(filename, "a")
    # Writes the line and closes the file
    file.write(line)
    file.close()
