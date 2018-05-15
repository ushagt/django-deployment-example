from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict={"text":"hello world","numbers":100}
    return render(request,'rel_app/index.html',context_dict)
def others(request):
    my_dict={"text1":"welcome django"}
    return render(request,'rel_app/others.html',context=my_dict)
def relative(request):
    return render(request,'rel_app/relative.html')
