from django.shortcuts import render


def getdata(request):
    name = 'Vasy'
    return render(request, 'getdata/getdata.html', locals())
