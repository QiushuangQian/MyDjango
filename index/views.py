from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello World.")


def mydate(request, year, month, day):
    return HttpResponse(str(year) + '/' + str(month) + '/' + str(day))


# 视图函数myyear将模板myyear.html作为响应内容并生成相应的网站返回给用户
def myyear(request, year):
    return render(request, 'myyear.html')


# 参数为字典的视图
def myyear_dict(request, year, month):
    return render(request, 'myyear_dict.html', {'month': month})
