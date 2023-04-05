def includeWord(words, text):
    for word in words:
        if (word in text):
            return word.strip()
    return ""


#print(includeWord(["другое", "следующее"], "включи алу пугачеву"))