#Converter audio em texto.
#https://www.youtube.com/watch?v=UAdX0cGuC28
import whisper

model = whisper.load_model("base")
result = model.transribe("music.mp3")
with open("transci.txt", "w") as f:
    f.write(result["text"])