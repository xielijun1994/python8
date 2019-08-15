__author__ = '大炮君'
#*****解题思路---》实现（单次实现后再循环）---》优化---》丰富******
'''
1：一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。
编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
然后显示一条消息指出这个人是否可以加入球队，
询问10次后，输出满足条件的总人数。

input()函数 从控制台获取数据，且获取的数据类型都是str类型
int(变量名/值)  强制转换为整数
'''

countSatisfied=0
countDissatisfied=0
num=5 #询问次数
while  num>=1:
    input_age=input("请输入年龄")
    sex=input('请输入性别')
    age=int(input_age)
    if sex=='f' and 10<=age<=12:
        print('可以加入球队')
        countSatisfied=countSatisfied+1
    else:
        print('不满足条件')
        countDissatisfied+=1
    num=num-1
    print(num)
print('满足条件共有%d人'%countSatisfied)
print('不满足条件共有%d人'%countDissatisfied)
