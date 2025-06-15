#(1)变量的赋值
x="hello"
y=123
z=y
print(x)
print(y)
print(z)

# hello
# 123
# 123



# (2)数据类型
# 数据类型1-整数型（int）
# 例如1，2，3，1415926
num1=666
# 数据类型2-浮点数型（float）
# 例如3.1415926
num2=3.14
# 数据类型3-布尔型（bool）
# 例如True,False
num3=True
num4=False
# 数据类型4-字符串型（str）
# 例如"China","hello"
num5="hello,world"



# (3)进制转换
# bin()是十进制转二进制，0b表二进制
# oct()是十进制转八进制，0o表八进制
# hex()是十进制转十六进制，0x表十六进制
print(bin(142857))
print(oct(142857))
print(hex(142857))

# 0b100010111000001001
# 0o427011
# 0x22e09



# (4) 数据类型转换
# 显式转换：使用内置函数如int(),float(),str(),bool()等进行类型转换。
# 例如：int("123")将字符串转换为整数。
# 隐式转换：Python在某些情况下自动进行类型转换，例如在算术运算中。



# (5)查看数据类型
# type()可以查看数据类型
print(type(123))
print(type("hello"))

# <class 'int'>
# <class 'str'>