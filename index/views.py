from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv

# Create your views here.
from index.models import Product


def index(request):
    # return HttpResponse("Hello World.")
    # render(request, template_name, context=None, content_type=None, status=None, using=None)
    # request：请求对象
    # template_name：HTML模板文件名
    # context：对HTML模板的变量赋值（字典形式）
    # content_type：响应数据的数据格式
    # status：HTTP状态码，默认为200
    # using：模板—>网页的模板引擎

    # type_list用于查询数据表字段type的数据并将数据去重
    type_list = Product.objects.values('type').distinct()
    # name_list用于查询数据表字段type和name的全部数据
    name_list = Product.objects.values('name', 'type')
    context = {'title': '首页', 'type_list': type_list, 'name_list': name_list}
    return render(request, 'index.html', context=context, status=200)


def mydate(request, year, month, day):
    return HttpResponse(str(year) + '/' + str(month) + '/' + str(day))


# 视图函数myyear将模板myyear.html作为响应内容并生成相应的网站返回给用户
def myyear(request, year):
    return render(request, 'myyear.html')


# 参数为字典的视图
def myyear_dict(request, year, month):
    return render(request, 'myyear_dict.html', {'month': month})


# 文件下载
def download(request):
    # 当接收到用户请求后，视图函数download首先定义HttpResponse的响应类型为文件（text/csv）类型，生成response对象
    response = HttpResponse(content_type='text/csv')

    # 然后在response对象上定义Content-Disposition，设置浏览器下载文件的名称。
    # attachment设置文件下载的方式，filename为文件名
    response['Content-Disposition'] = 'attachment;filename ="somefilename.csv"'

    # 使用CSV模块加载response对象，把数据写入response对象所设置的CSV文件并将response对象返回到浏览器上
    writer = csv.writer(response)
    writer.writerow(['First row', 'A', 'B', 'C'])
    return response


def login(request):
    # 相对路径
    # return redirect('/')
    # 绝对路径
    return redirect('http://127.0.0.1:8000/')
