from django.urls import path, re_path
from . import views

urlpatterns = {
    # 首页
    path('', views.index),

    # 添加带有字符型，整型，slug的URL
    # <>为URL设置变量；冒号前为数据类型，后为变量名
    # path('<str:year>/<int:month>/<slug:day>',views.mydate)
    # 设置正则表达式
    re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2}).html', views.mydate),

    # 当用户访问该URL时，项目根据URL信息选择视图函数myyear处理，并命名URL为myyear
    re_path('(?P<year>[0-9]{4}).html', views.myyear, name='myyear'),

    # 设置URL额外参数：
    # 参数只能以字典的形式表示，
    # 设置的参数只能在视图函数中读取和使用，
    # 一个键值对代表一个参数，键代表参数名，值代表参数值，
    # 参数值没有数据格式限制，可以为对象、字符串、列表、元组
    # 参数为字典的URL
    re_path('dict/(?P<year>[0-9]{4}).htm', views.myyear_dict, {'month': '05'}, name='myyear_dict'),

    path('download.html', views.download),

    path('login.html', views.login),

    # 指向通用视图ListView（通用视图都要加.as_view()）
    path('index/', views.ProductList.as_view()),

    path('index/<id>.html', views.ProductList.as_view(), {'name': 'phone'})
}
