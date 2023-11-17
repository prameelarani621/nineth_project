from django.shortcuts import render

# Create your views here.
def data_render(request):
    data='hello it if fack data'
    d={'fack':data}
    return render(request,'data_render.html',context=d)

def login(request):
    data='good for u'
    d={'nice':data}
    return render(request,'login.html',context=d)