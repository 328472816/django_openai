from django.urls import path
#from django.views.static import serve
from . import views
from django.conf import settings

app_name = 'aiview'

urlpatterns = [
    path('', views.index,name='index'),
    path('apikey', views.apikey,name='apikey'),
    path('changeapikey', views.changeapikey,name='changeapikey'),
    path('chat', views.chat,name='chat'),
    path('aitest', views.ai_test,name='ai_test'),
]
