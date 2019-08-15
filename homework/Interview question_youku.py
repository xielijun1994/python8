__author__ = '大炮君'
'''
优酷面试题
#输入num 为四位数，对其按照如下的规则进行加密
1、每一位分别加5，然后分别将其替换为该数除以10取余后的结果
2、将该数的第一位和第四位互换，第二位和第三位互换
3、最后结合起来作为加密后的整数输出

ps:reverse()倒序函数  sort()排序函数

list_1=[]
num=input('请输入4位数')
for item in num:
   value= ((int(item)+5)%10)
   list_1.append(value)
print(list_1)
list_1.reverse()
print(list_1)
str_1=''
for item in  list_1:
    print(item,type(item))
    str_1=str_1+str(item)
print(str_1,type(str_1))
int_1=int(str_1)
print(int_1,type(int_1))

'''

# num=str(1234)
# new_num=''
#
# for i in num:
#     new_num_1=int(i)+5
#     new_num=new_num+str(new_num_1)
# print(new_num,type(new_num))
# res=int(new_num)%10
# print(res,type(res))


# 练习2：把列表数据a=[5,6,7,8,10,23,45]按照倒序输出，利用for 循环&range 函数
# a=[5,6,7,8,10,23,45] # 索引 6 5 4 3 2 1 0
# # for i in range(6,-1,-1):
# #    # print(i)
# #     print(a[i])
# a.reverse()
# for item in a:
#     print(item)
#

list_1=[]
num=input('请输入4位数')
for item in num:
   value= ((int(item)+5)%10)
   list_1.append(value)
print(list_1)
list_1.reverse()
print(list_1)
str_1=''
for item in  list_1:
    print(item,type(item))
    str_1=str_1+str(item)
print(str_1,type(str_1))
int_1=int(str_1)
print(int_1,type(int_1))