__author__ = '大炮君'

#利用for 循环和range()函数 ，完成1-100的累加计算
# sum=0
# for i in range(1,101):
#    sum=sum+i #等价于 sum+=i
# print(sum)

#读懂题目，选取一组数据，用零散代码完成你的功能
#变成函数  def 函数名():  把零散代码变成他的函数体
#想办法提高函数的复用性
# def sum(m,n):
#     sum=0
#     for i in range(m,n):
#        sum=sum+i #等价于 sum+=i
#     print(sum)
# sum (1,5)

#请把任意字符串转成一个列表，要求字符串里面的每一个元素对应list的每一个元素
#str='hello'-->['h','e','l','l','o']
# str_1='hell0'
# list_1=[]
# for i in str_1:
#     print(i,type(i))
#     list_1.append(i)
# print(list_1)


# def str_to_list(str_1):
#     list_1=[]
#     for i in str_1:
#         print(i,type(i))
#         list_1.append(i)
#     print(list_1)
# str_to_list('nihaome')

# str_1='hell0'
# list_1=list(str_1)
# print(list_1)


#请把任意字符串转成一个列表，要求字符串里面的每一个元素对应list的每一个元素
#str='hello'-->['h','e','l','l','o']
str_1='hell0'
list1=[]
for i in str_1:
    print(i)
    list1.append(i)
print(list1)