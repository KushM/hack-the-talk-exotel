import librosa
import matplotlib.pyplot as plt

filename = 'temp.wav'
y ,sr = librosa.load(filename)
print(sr)
pitches, magnitudes= librosa.piptrack(y=y, sr=sr)
mfccs = librosa.feature.mfcc(y=y, sr=sr)
print('mfcc calc done')

#visualize mfccs

librosa.display.specshow(mfccs, x_axis='time')
#plt.imshow(mfccs)
plt.colorbar()
plt.title('MFCC')
plt.tight_layout()
plt.show()