import sys

print("hello credit simulator")


cnt = len(sys.argv)-1
print("args:", cnt)

if cnt == 1:
    print("argv:", sys.argv[1])
