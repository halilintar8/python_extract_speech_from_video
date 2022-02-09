from deep_translator import GoogleTranslator

translated = GoogleTranslator(source='auto', target='en').translate_file('recognized_jap.txt')

with open('translated_result.txt',mode ='w') as file: 
      file.write("Translated Result:") 
      file.write("\n") 
      file.write(translated) 
      print("ready!")

