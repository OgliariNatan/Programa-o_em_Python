import pyttsx3

# init mecanismo TTS
engine = pyttsx3.init()

#text to he speaks
text = "Uma pão de batata muito louco"

#to speak

engine.say(text)

#sleep

engine.runAndWait()

print("Concluida a conversa\n")