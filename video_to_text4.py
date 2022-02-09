# importing libraries 
import speech_recognition as sr
import moviepy.editor as mp

import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence

from deep_translator import GoogleTranslator

# clip = mp.VideoFileClip(r"Sample Student Speech.mp4")
# clip.audio.write_audiofile(r"converted2.wav")

# create a speech recognition object
r = sr.Recognizer()
# audio = sr.AudioFile("converted.wav")

# a function that splits the audio file into chunks
# and applies speech recognition
def get_large_audio_transcription(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)  
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=500,
    )
    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk 
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                # text = r.recognize_google(audio_listened)
                text = r.recognize_google(audio_listened, language="en-US")
                # text = r.recognize_google(audio_listened, language="ja")

            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text
    # return the text for all chunks detected
    return whole_text

clip = mp.VideoFileClip(r"video.mp4")
clip.audio.write_audiofile(r"converted4.wav")

# clip = mp.VideoFileClip(r"Sample Student Speech.mp4")
# clip.audio.write_audiofile(r"converted3.wav")

# clip = mp.VideoFileClip(r"indonesian - japanese.mp4")
# clip.audio.write_audiofile(r"converted_jap.wav")

if __name__ == '__main__':
    import sys
    # path = "30-4447-0004.wav"
    # path = "7601-291468-0006.wav"

    path = "converted4.wav"
    # path = "converted3.wav"
    # path = "converted_jap.wav"
    # path = sys.argv[1]

    # print("\nFull text:", get_large_audio_transcription(path))
    # with open('recognized_jap.txt',mode ='w') as file: 
    # with open('recognized3.txt',mode ='w') as file: 
    with open('recognized4.txt',mode ='w') as file: 
      file.write("Recognized Speech:") 
      file.write("\n") 
      file.write(get_large_audio_transcription(path)) 
      print("ready!")

# translated = GoogleTranslator(source='auto', target='en').translate_file('recognized_jap.txt')
# translated = GoogleTranslator(source='auto', target='en').translate_file('recognized3.txt')
translated = GoogleTranslator(source='auto', target='en').translate_file('recognized4.txt')

# with open('translated_result.txt',mode ='w') as file: 
# with open('translated_result3.txt',mode ='w') as file: 
with open('translated_result4.txt',mode ='w') as file: 
      file.write("Translated Result:") 
      file.write("\n") 
      file.write(translated) 
      print("ready!")


