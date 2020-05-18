# https://pythonbasics.org/transcribe-audio/

import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.utils import make_chunks
from os import path
import glob


def wav_to_text(prefix, filename, counter):

    output_filename = prefix + '_txt/' + prefix + '_' + str(counter) + '.txt'

    if path.exists(output_filename):
        # Skip already completed files
        return

    print('Beginning ' + output_filename)
    output_txt = open(output_filename, "w+")

    audio = AudioSegment.from_wav(filename)
    # recognize_sphinx works best on smaller chunks
    chunks = make_chunks(audio, 30000)

    for chunk in chunks:
        chunk_filename = 'temp_chunked_audio_wav/chunk.wav'
        chunk.export(chunk_filename, format='wav')

        r = sr.Recognizer()
        with sr.AudioFile(chunk_filename) as source:
            audio = r.record(source)  # read the chunk
            rec = r.recognize_sphinx(audio)  # recognize the chunk as text
            output_txt.write(rec)
        os.remove(chunk_filename)

    output_txt.close()


if __name__ == '__main__':

    SHAPIRO_PATH = 'ben_shapiro_wav'
    PSA_PATH = 'psa_wav'

    # This repetition could be refactored to obey DRY, being lazy...
    for i, file in enumerate(glob.glob(SHAPIRO_PATH + '/*.wav')):
        wav_to_text('ben_shapiro', file, i + 1)

    for i, file in enumerate(glob.glob(PSA_PATH + '/*.wav')):
        wav_to_text('psa', file, i + 1)


