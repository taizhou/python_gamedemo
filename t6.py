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
#�±�����ָ���������ã������������� 20 ô����������13�����ǣ�
aa.w = 20 
a.w = 13
print aa.w, a.w
#��������������£����������t��q�أ�������ʵ������
a.t = 14
a.q = 15
print a.t, a.q
#��������������£����������m��n�أ������������
aa.m = 30
aa.n = 40
print aa.m, aa.n

#����������������
#�����������,��������print��䶼����ȷִ��ô��Ϊ�Σ�
b = aa()
print b.x,b.y #ok,x,y��ʵ������
#print b.t,b.q #no
print b.m,b.n #ok,m,n�������
