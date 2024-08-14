from django.urls import path
from  spamornot import views

urlpatterns = [
    path("",views.ok),
    path("pred",views.predict,name="pred")
]