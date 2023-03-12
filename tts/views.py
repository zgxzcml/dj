from django.shortcuts import render
from gtts import gTTS
import googletrans
# tts = gTTS('hello', lang="")
# tts.save('hello.mp3')

def randstr():
    from random import randint as ri
    st = ""
    for i in range(10):
        st += chr(ri(65,90))
    return st

# Create your views here.
def index(request):
    context = {
        "ndict" : googletrans.LANGUAGES
    }
    bf = request.GET.get("bf", "")
    if bf:
        to = request.GET.get("to", "")
        tts = gTTS(bf, lang=to)
        fname = randstr()
        tts.save(f"media/tts/{fname}.mp3")
        context.update({
            "to" : to,
            "bf" : bf,
            "fn" : fname
        })
    
    return render(request, "tts/index.html", context)