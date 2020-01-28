# MyDjango
Django学习

urls作为网址路径
path('/xxx', views.XXX) //xxx为空是指向首页 不为空时则指向 http://127.0.0.1:8000/xxx
                     //views.XXX为视图views中所定义的方法

变量：{{veriable}}
每句代码都要带{%  %}
标签：{%for%}：for循环
      {%if%}：条件判断
      {%csrf_token%}：防护跨站请求伪造攻击
      {%url%}：生成相应url地址
      {%with%}：重命名变量
      {%load%}：加载导入Django标签库
      {%static%}：读取静态资源文件夹内容
      {%extends xxx%}：模板继承
      {%block xxx%}：重写父模板代码
      
for标签模板变量：
forloop.counter：从1开始获取当前循环索引
forloop.counter0：从0开始获取当前循环索引
forloop.revcounter：索引从最大数递减，直到1
forloop.revcounter0：索引从最大数递减，直到0
forloop.first：遍历第一项元素时为True
forloop.last：遍历最后一项元素时为True
forloop.parentloop：获取上层循环的forloop

模板继承：
父模板：
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
    <meta charset="utf-8">
</head>
<body>
  {%block body%}{%endblock%}
</body>
</html>

子模版继承：
{%extends "父模板"%}
{%block body%}
... ...
{%endblock%}
