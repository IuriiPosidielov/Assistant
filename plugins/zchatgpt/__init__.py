import utils.fuzzy
import openai
import utils.speak
import config

def execute(text):
    hotword = utils.fuzzy.includeWord(["скажи", "расскажи"], text)
    if hotword:
        utils.speak.playthinking()
        text = text.replace(hotword, "")
        openai.api_key = config.chatgpt_key
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": text},
            ]
        )

        result = ''
        for choice in response.choices:
            result += choice.message.content

        utils.speak.speakchunks(result)
        return True
    return False
