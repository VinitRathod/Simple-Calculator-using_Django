from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def submitQuery(request):
    q = request.GET['query']
    """jsondict = {
        'q' : q
    }"""
    
    try:
        ans = eval(q)
        mydict={
            "q":q,
            "ans":ans,
            "error":False,
            "result":True
        }
        return render(request,'index.html',context=mydict)
    except:
        mydict= {
            "error" : True,
            "result":False
        }
        return render(request,'index.html',context=mydict)
    return HttpResponse(q)
    #return JsonResponse(jsondict)