from django.db import models


# Create your models here.
# 在这搭建与数据库的映射

# 在网页中展示数据：
# 定义数据模型，以类的方式定义数据表的字段。在数据库创建数据表时，数据表由模型定义的类生成
# 在视图导入模型所定义的类，该类称为数据表对象，Django为数据表对象提供独有的数据操作方法，可以实现数据库操作，获取数据
# 视图函数获取数据后，将数据以字典、列表、对象的方式传递给HTML模板，由模板引擎接收和解析，生成相应网页

# Product类与Product表构成映射关系，代码只搭建关系
# python manage.py xxx 指令创建数据表
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
