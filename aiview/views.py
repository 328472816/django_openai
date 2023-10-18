from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Create your views here.
@csrf_exempt 
def ai_test(request):
    
    if request.method == 'GET':
        result = {"request":"GET"}
    else:
        #print(request.body)
        #print(request.META)
        result = json.loads(request.body.decode('utf-8'))
        msg = result['msg']
        username = result['username']
        result = {"request":"POST","username":username,"msg":msg}
    return JsonResponse(result)
