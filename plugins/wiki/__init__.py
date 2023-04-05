import utils.fuzzy
import wikipedia
import utils.speak
import utils.text
import config

def execute(text):
    hotword = utils.fuzzy.includeWord(["что такое", "кто такой", "кто такая", "кто такие", "что это", "кто это"], text)
    if hotword:
        text = text.replace(hotword, "").strip()
        if not text: return False
        utils.speak.playthinking()       
        wikipedia.set_lang(config.language)
        suggestion = wikipedia.search(text, results=1)    
        print(suggestion)
        if (suggestion):
            print("wiki")
            result = wikipedia.summary(suggestion)
            if result:
                result = utils.text.removebracket(result)
                print("result" + result)
                utils.speak.speakwithcaching(result)
                return True
    return False