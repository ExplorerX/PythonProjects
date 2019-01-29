# 在使用while的时候如果while被break打断就不走else，如果不打断就走else
count = 0
while count < 5:
    count += 1
    if count == 3:
        break
    print('Loop', count)
else:
    print('循环正常执行完了')
print('Out of while loop!')
