import config
import utils.youtube
import utils.fuzzy

def execute(text):
    hotword = utils.fuzzy.includeWord(["другое", "следующие", "следующая"], text)
    # print ("hotword: " + hotword)
    if hotword:
        config.searchindex = config.searchindex + 1
        # print(config.search_results[config.searchindex])
        if config.searchindex > 20: config.searchindex = 0
        utils.youtube.openYouTube (config.search_results, config.searchindex)
        return True
    hotword = utils.fuzzy.includeWord(["выключи", "хватит","хвати"], text)
    if hotword:
        utils.youtube.stop_music()
        return True
    hotword = utils.fuzzy.includeWord(["включи", "ключи "], text)
    print (hotword)
    if hotword:
        text = text.replace(hotword, "")
        utils.youtube.search(text)
        # for s in config.search_results: print (s)				
        utils.youtube.openYouTube (config.search_results, 0)
        return True
    return False