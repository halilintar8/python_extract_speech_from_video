import speech_recognition as sr

r=sr.Recognizer()

# a=sr.AudioFile('sample_audio/speech.wav')
a=sr.AudioFile('converted.wav')
with a as source :
	audio=r.record(source)

text=r.recognize_google(audio)


file1=open(r"1.txt","a")
file1.writelines(text)
file1.close()

