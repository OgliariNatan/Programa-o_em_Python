import pyttsx3

# init mecanismo TTS
engine = pyttsx3.init()
# velociade da fala padrão 200
engine.setProperty("rate", 400)

# Volume, padrão 1.0
engine.setProperty("volume", 0.5)

#text to he speaks
text = "Bem vindo a conversação em python\n Um pão de batata muito louco. \n A prática leva a perfeição"

#to speak
engine.say(text)
engine.runAndWait()

print("Concluida a conversa\n")