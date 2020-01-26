from django.shortcuts import render
from django.http import HttpResponse
import csv


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


#文件下载
def download(request):
    # 当接收到用户请求后，视图函数download首先定义HttpResponse的响应类型为文件（text/csv）类型，生成response对象
    response = HttpResponse(content_type='text/csv')

    # 然后在response对象上定义Content-Disposition，设置浏览器下载文件的名称。
    # attachment设置文件下载的方式，filename为文件名
    response['Content-Disposition'] = 'attachment;filename ="somefilename.csv"'

    #使用CSV模块加载response对象，把数据写入response对象所设置的CSV文件并将response对象返回到浏览器上
    writer = csv.writer(response)
    writer.writerow(['First row', 'A', 'B', 'C'])
    return response
