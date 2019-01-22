def readSettings(filepath):
    dictionary = {}
    file = open(filepath, "r")
    for line in file:
        (key, value) = line.split(":")
        dictionary[key] = value
    file.close()
    return dictionary