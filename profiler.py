import re

filter_words = ["idiot", "moron", "retard", "bitch", "fuckface", "sweetie", "sweetheart", "sweety", "darling", "darlin'", "darlin", "sweetums", "dontard", "libtard", "libtards", "ass", "nigger", "\(\(\(", "asshole", "nigga", "nibba", "gae", "cuck", "kike", "porchmonkey", "bastard", "bitch", "cock", "cunt", "cretin", "cum", "whore", "dick", "dimwit", "faggot", "fag", "fatso", "fuck", "inbred", "ignoramus", "jerk", "low-life", "nitwit", "pigfucker", "pillock", "pissface", "shit-eater", "shit stain", "skullfuck", "shitter", "twerp", "twat", "turdball", "turd", "wanker", "whorefucker", "whoreson", "twit", "tranny"]

def slur_sum(statement):
    if(statement == ""):
        return 0
    result = 0
    for w in filter_words:
        searchResult = re.findall(w, statement, flags=re.IGNORECASE)
        if searchResult != None:
            result += len(searchResult) 
    return result