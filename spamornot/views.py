from django.shortcuts import render,HttpResponse
import pickle

model=pickle.load(open("spam.pkl",'rb'))
trans=pickle.load(open("vectorizer.pkl",'rb'))


# Create your views here.
def ok(request):
    return render(request,"index.html")
    
def predict(request):
    if request.method=="POST":
        message=request.POST['name']
        msg=[message]
        k=trans.transform(msg)
        result=model.predict(k)
        return render(request,"index.html",{"result":result})
        
        