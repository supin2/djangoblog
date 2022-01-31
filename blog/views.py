from django.shortcuts import render

# Create your views here.
def index(Req):
    context = {

    }
    return render(Req, "index.html", context=context)