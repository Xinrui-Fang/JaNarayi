# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import os
import shutil
import pydub
from pydub import AudioSegment
from pydub.silence import split_on_silence

import speech_recognition as sr
r = sr.Recognizer()


# %%

def crop2chunk(filename):
    # clear folder firstly

    if os.path.exists('./static/segmentFile') == False:
        os.mkdir('./static/segmentFile')
    else: 
        shutil.rmtree('./static/segmentFile')
        os.mkdir('./static/segmentFile')

    sound = AudioSegment.from_mp3(filename)
    loudness = sound.dBFS

    chunks = split_on_silence(sound,
                          #must be silent for at least half a second
                          min_silence_len=430,
                          #consider it silent if quieter than - 16 dBFS
                          silence_thresh=-45,
                          keep_silence=400
    )

    # 放弃长度小于2秒的录音片段
    for i in list(range(len(chunks)))[::-1]:
        if len(chunks[i]) <= 2000 or len(chunks[i]) >= 10000:
            chunks.pop(i)
    print('取有效分段(大于2s小于10s)：', len(chunks))
    
    '''
    for x in range(0,int(len(sound)/1000)):
        print(x,sound[x*1000:(x+1)*1000].max_dBFS)
    '''
    
    for i, chunk in enumerate(chunks):
        chunk.export("./static/segmentFile/chunk{0}.wav".format(i), format="wav")
        #print(i)



# %%



# %%
def chunk2text(filename):
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language='ja-JP')
        #print(text)
        return text



# %%



# %%


if __name__ == "__main__":

    crop2chunk("example.mp3")
    filename = "chunk4.wav"
    print(chunk2text(filename))

# %%
