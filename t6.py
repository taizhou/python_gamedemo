#! /usr/bin/python
#coding=utf-8

class aa:
      w = 10
      def __init__(self):
           self.x = 11
           self.y = 12
      def add(self):
           return self.x + self.y
					 
a = aa()
print a.add()
#下边两条指令各起何作用？结果是输出两个 20 么？还是两个13？还是？
aa.w = 20 
a.w = 13
print aa.w, a.w
#程序继续增加如下，怎样理解这t和q呢？他们是实例变量
a.t = 14
a.q = 15
print a.t, a.q
#程序继续增加如下，怎样理解这m和n呢？他们是类变量
aa.m = 30
aa.n = 40
print aa.m, aa.n

#好了再来个提升吧
#程序继续增加,下列三个print语句都能正确执行么？为何？
b = aa()
print b.x,b.y #ok,x,y是实例变量
#print b.t,b.q #no
print b.m,b.n #ok,m,n是类变量
