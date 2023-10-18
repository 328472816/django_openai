from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from . import djopenai
# Create your views here.
@csrf_exempt 
def ai_test(request):
    
    if request.method == 'GET':
        result = {"request":"GET"}
    else:
        #print(request.body)
        #print(request.META)
        result = json.loads(request.body.decode('utf-8'))
        role = result['role']
        userdata = result['userdata']
        result = djopenai.ChatBase(role,userdata)
    return JsonResponse(result)
