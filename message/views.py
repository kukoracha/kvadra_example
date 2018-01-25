from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Message

def index(request):
    msgs = Message.objects.all().order_by("-date")
    print(msgs)
    return render(request, 'message/index.html', context={'msgs': msgs})

def addtext(request):
    return render(request, 'message/addtext.html')

def uploadtext(request):
    if request.POST:
        msg = Message(txt=request.POST['txt'])
        msg.save()
        return HttpResponse("ok")
    return HttpResponse(status=500)

def gettext(request):
    if request.GET:
        try:
            msg = Message.objects.get(pk=request.GET["id"])
            return JsonResponse({'txt': msg.txt}, safe=True)
        except Message.DoesNotExist:
            pass
    return HttpResponse(status=500)

# Create your views here.
