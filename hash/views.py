from django.shortcuts import render
import hashlib
import json
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {}
    return render(request,'encode/index.html',context)


def encode(request):
    text = request.POST.get('encode')
    text_bytes = text.encode(encoding='utf-8')
    text_bytes_base64 = base64.b64encode(text_bytes)
    text_base64_str = text_bytes_base64.decode()
    context = {'base64_encode':text_base64_str}
    context_json = json.dumps(context)
    print(context_json)
    return HttpResponse(context_json)