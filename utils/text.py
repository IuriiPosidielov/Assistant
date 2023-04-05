import re

def nearestDelimiter(txt,  cur):
    try:
        delimiters = ".!?"          
        if(txt[cur] in delimiters) :          
            return cur
        else:
            i=cur
            while ( i>=0 ):
                if (txt[i] in delimiters) :                    
                            return i
                i=i-1
        return 0
    except Exception as e:
         return 0
    


def splitText(sentence,chunkLength):
     if (len(sentence) <= chunkLength):
        lst.append(sentence)
        return lst      
     curlng = chunkLength
     lst = []
     curlng = nearestDelimiter(sentence, curlng)
     substr = (sentence[0 : curlng]).strip()
        
     lst.append(substr)
     substr2 = (sentence[curlng : len(sentence)]).strip()
     if substr2:
        lst.append((sentence[curlng : len(sentence)]).strip())
     return lst

def splitTextMultiple(sentence,chunkLength):
     cursor = 0  
     curlng = chunkLength
     lst = []
     while (curlng < len(sentence)):
         curlng = nearestDelimiter(sentence, curlng)       
         substr = (sentence[cursor : curlng]).strip()
         cursor = curlng        
         curlng = (cursor+chunkLength*3) if (cursor+chunkLength<len(sentence)) else len(sentence)
         if not substr: break
         lst.append(substr)
     print("subfinish " + sentence[cursor : curlng])            
     laststr =  (sentence[cursor : curlng]).strip()
     if laststr:   
        lst.append(laststr)
     return lst

def clean(text):
    #re.sub(r'"', '', str)
    #removeSpecialChars = re.sub("["]", " ", z)
    return text.replace("", "")

def removebracket(txt):
    return re.sub("[\(\[].*?[\)\]]", "", txt)