import pyttsx3

# init mecanismo TTS
engine = pyttsx3.init()

#text to he speaks
text = "Bem vindo a conversação em python\n Um pão de batata muito louco. \n A prática leva a perfeição"

#to speak

engine.say(text)

#sleep

engine.runAndWait()

print("Concluida a conversa\n")