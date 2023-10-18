from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from . import models
from .form import ApiKkeyForm
#from . import djopenai
# Create your views here.
@csrf_exempt 
def ai_test(request):
    result = ''
    if request.method == 'GET':
        result = {"request":"GET"}
    else:
        #print(request.body)
        #print(request.META)
        result = json.loads(request.body.decode('utf-8'))
        role = result['role']
        userdata = result['userdata']
        #result = djopenai.ChatBase(role,userdata)
    return JsonResponse(result)

def index(request):
    return render(request, 'index.html', locals())

def apikey(request):
    key = models.OpenapiKey.objects.first()
    form = ApiKkeyForm(request.POST)
    return render(request, 'apikey.html', locals())

def changeapikey(request):
    if request.method == "POST":
        form = ApiKkeyForm(request.POST)
        message = "请检查填写的内容！"
        if form.is_valid():
            newkey = form.cleaned_data['key']
            key = models.OpenapiKey.objects.first()
            key.key = newkey
            key.save()
            return render(request, 'apikey.html', locals())
    form = ApiKkeyForm(request.POST)
    return render(request, 'apikey.html', locals())

def chat(request):
    return render(request, 'index.html', locals())
