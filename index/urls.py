from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    # 添加带有字符型，整型，slug的URL
    # <>为URL设置变量；冒号前为数据类型，后为变量名
    # path('<str:year>/<int:month>/<slug:day>',views.mydate)
    # 设置正则表达式
    re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2}).html', views.mydate),

    # 当用户访问该URL时，项目根据URL信息选择视图函数myyear处理，并命名URL为myyear
    re_path('(?P<year>[0-9]{4}).html', views.myyear, name='myyear'),

    # 参数为字典的URL
    re_path('dict/(?P<year>[0-9]{4}).htm', views.myyear_dict, {'month': '05'}, name='myyear_dict')
]