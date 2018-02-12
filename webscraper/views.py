from django.shortcuts import render

# Create your views here.
def WSdatabase(request):
    context = {
        'title':"WSdatabase",
        }
    return render(request,'WSdatabase.html',context)
