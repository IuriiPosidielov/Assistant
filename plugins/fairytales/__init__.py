import utils.speak
import utils.fuzzy
import utils.text
import os     

def execute(text):
    hotword = utils.fuzzy.includeWord(["скажи", "расскажи", "расскажи сказку про", "расскажи сказку о", "расскажи сказку", "расскажи рассказ"], text)
    if hotword:
        text = text.replace(hotword, "").strip()
        if not text: return True            
        path = "/home/pi/apps/Assistant/tales"
        os.system("/usr/bin/killall mpv")
        print(os.listdir(path))
        for file in os.listdir("/home/pi/apps/Assistant/tales"):
            keyword = file.replace(".txt", "").strip()
            if (keyword in text):
                pathToFile = os.path.join(path, file)
                print(pathToFile)
                with open(pathToFile, encoding = 'utf-8', mode = 'r') as f:
                    content = f.read()
                    print (content)
                    utils.speak.saveandspeak(content, pathToFile)           
                return True
    return False
