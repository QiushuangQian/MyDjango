from django import template

# 导入模板功能template，通过template声明Library对象，将对象赋值给变量register
# 过滤器以函数的形式实现，在函数前register.filter装饰器来表示该函数是一个过滤器
# 函数参数可设置一个或两个，value为HTML模板变量，agrs为过滤器定义的函数参数
# 结果必须返回


# 声明一个模板对象，称注册过滤器
register = template.Library()


# 声明并定义过滤器
@register.filter
# 字符串替换功能
def myreplace(value, agrs):
    oldValue = agrs.split(':')[0]
    newValue = agrs.split(':')[1]
    return value.replace(oldValue, newValue)

# HTML模板中使用自定义过滤器：
# # {%load myfilter%}用于导入templatetags中的myfilter.py文件
