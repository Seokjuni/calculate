from django.shortcuts import render

def 계산기(request):
    return render(request, "계산기.html")

def 결과(request):
    first = request.GET['first']
    second = request.GET['second']
    first = int(first)
    second = int(second)
    cal = request.GET['calculate']
    
    if cal == 'plus':
        result = first + second
    elif cal == 'minus':
        result = first - second
    elif cal == 'multiple':
        result = first * second
    elif cal == 'divide':
        if second != 0:
            result = first / second
        else:
            result = 'division by zero'

    return render(request, "결과.html", {'result' : result})
