from django.shortcuts import render
import googletrans
# Create your views here.
def index(request):
    bf = request.GET.get("bf","")
    context = {
        "ndict" : googletrans.LANGUAGES
    }
    if bf:
        fr = request.GET.get("fr","")
        to = request.GET.get("to","")

        trans = googletrans.Translator()
        af = trans.translate(bf, src=fr, dest=to)
        context.update({
            "af" : af.text,
            "fr" : fr,
            "to" : to,
            "bf" : bf
        })
    return render(request, "trans/index.html", context)