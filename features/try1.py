import librosa
filename = 'temp.wav'
y ,sr = librosa.load(filename)
print(sr)
