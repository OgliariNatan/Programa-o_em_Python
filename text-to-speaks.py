import pyttsx3
import time

# init mecanismo TTS
engine = pyttsx3.init()

# Obtenha a lista de vozes disponíveis e selecione uma
voices = engine.getProperty("voices")
for voice in voices:
    print(voice.id)

# Defina a voz para "brazil"
engine.setProperty("voice", "brazil")

# velociade da fala padrão 200
engine.setProperty("rate", 250)

# Volume, padrão 1.0
engine.setProperty("volume", 1.5)
time.sleep(2)
#text to he speaks
text = "Bem vindo a conversação em python\n Um pão de batata muito louco. \n A prática leva a perfeição."

#to speak
engine.say(text)
engine.runAndWait()

print("Concluida a conversa\n")
