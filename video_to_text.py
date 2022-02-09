import speech_recognition as sr
import moviepy.editor as mp

# clip = mp.VideoFileClip(r"video_recording.mov") 
clip = mp.VideoFileClip(r"Sample Student Speech.mp4")
clip.audio.write_audiofile(r"converted.wav")
# clip.audio.write_audiofile(r"converted.mp3")

r = sr.Recognizer()
audio = sr.AudioFile("converted.wav")
# audio = sr.AudioFile("converted.mp3")

with audio as source:
  audio_file = r.record(source)

result = r.recognize_google(audio_file)

# exporting the result 
# with open('recognized.txt',mode ='w') as file: 
with open('recognized2.txt',mode ='w') as file: 
   file.write("Recognized Speech:") 
   file.write("\n") 
   file.write(result) 
   print("ready!")


