import utils.fuzzy
import openai
import utils.speak
import config

def execute(text):
	hotword = utils.fuzzy.includeWord(["расскажи", "скажи"], text)
	if hotword:
		utils.speak.playthinking()
		text = text.replace(hotword, "")
		openai.api_key = config.chatgpt_key
		msgs=[{"role":"system","content":"You are a helpful assistant."}]

		i = 0
		for q in config.question:
			msgs.append({"role": "user", "content": q})
			msgs.append({"role": "assistant", "content": config.answer[i]})
			i = i+1

		msgs.append({"role": "user", "content": text})
		for m in msgs:
			print(m)

		response = openai.ChatCompletion.create(
        	model="gpt-3.5-turbo",
        	messages=msgs)

		result = ''
		for choice in response.choices:
			result += choice.message.content

		config.question.append(text)
		config.answer.append(result)
		utils.speak.speakwithcaching(result)
		return True
	return False
