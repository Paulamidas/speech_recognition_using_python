import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()
sr.Microphone.list_microphone_names()
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
print(r.recognize_google(audio))
