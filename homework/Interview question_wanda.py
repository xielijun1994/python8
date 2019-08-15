__author__ = '大炮君'

'''
例如 {"username":'admin',"password":'123456'}
1、设计1个登录的程序，不同的用户名和成对密码存在个字典里，输入正确的用户名和密码去登录
2、首先输入用户名，如果用户名不存在或者为空，则一直提示正确的用户名
3、当用户名正确时，提示输入密码，如果密码跟用户名不对应，则提示密码错误请重新输入
4、如果密码输入错误超过3次，中断程序运行
5、当输入密码错误时，提示还有几次机会
6、用户名和密码都输入正确时，提示登录成功
'''
login_dict={"username":'admin',"password":'123456'}

name_input=input("请输入你的账号")
while name_input!=login_dict["username"] or name_input=='':
    name_input=input('请输入正确的用户名')

if name_input==login_dict["username"]:
   input_password=input('请输入密码')
   if input_password==login_dict['password']:
       print('登录成功')
   num=3
   while input_password!=login_dict['password'] and num>1 : # 3 2 1
       num=num-1                                            # 2 1 0
       print('密码错，你还有',num,'次机会')
       input_password=input('请重新输入密码')
       if input_password==login_dict['password']:
           print('密码错了之后才登录成功')
           break  # 中断当前循环 密码错了之后又输对密码之后要结束当前循环





