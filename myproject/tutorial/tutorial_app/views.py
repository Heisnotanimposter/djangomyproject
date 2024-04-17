from django.shortcuts import render

# Create your views here.

def test(request):
    return render(request, 'tutorial_app/test.html')

def rsp(request):
    return render(request, 'tutorial_app/rsp.html')

def innerText(request):
    return render(request, 'tutorial_app/test.html')

def context_django(request):
    context = {
        'x' : 'Hello World',
        'y' : [1, 2, 3, 4, 5]
    }
    return render(request, 'tutorial_app/context_django.html', context=context)