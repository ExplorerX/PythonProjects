# 1.用while循环输出1 2 3 4 5 6   8 9 10
"""
count = 1
while count <= 10:
    if count == 7:
        print(' ')
    else:
        print(count, ' ')
    count += 1
"""
# 用while循环输出1 2 3 4 5 6 8 9 10
"""
count = 0
while count < 10:
    count += 1
    if count == 7:
        continue
    print(count, ' ')
"""
"""
count = 1
while count <= 10:
    print(count, ' ')
    count += 1
    if count == 7:
        count += 1
"""
# 2.求1-100的和
"""
sum1 = 0
number = 1
while number < 101:
    sum1 = sum1 + number
    number += 1
print(sum1)
"""
# 3.输出100以内的所有奇数
"""
number = 1
while number <= 100:
    if number % 2 == 1:
        print(number)
    number += 1
"""
# 4.输出100以内的所有偶数
"""
number = 1
while number <= 100:
    if number % 2 == 0:
        print(number)
    number += 1
"""
# 5.求1-2+3—……-98+99的和
"""
number = 1
sum1 = 0
while number < 100:
    if number % 2 == 0:
        number = 0 - number
    sum1 += number
    if number < 0:
        number = 0 - number
    number += 1
print(sum1)
"""
# 6.用户登录(三次机会重试)
flag = 0
while flag < 3:
    user_name = input('Please input user_name:')
    user_pwd = input('Please input user_pwd:')
    if user_name == '123' and user_pwd == '456':
        print('Success!')
        break
    else:
        print('Error,you have ', 2-flag, 'times.')
        if flag == 2:
            break
    flag += 1
