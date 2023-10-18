from django.urls import path
#from django.views.static import serve
from . import views
from django.conf import settings

app_name = 'aiview'

urlpatterns = [
    path('aitest', views.ai_test,name='ai_test'),
]
