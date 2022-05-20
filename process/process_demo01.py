import os

pid = os.fork()

print(pid)

if pid == 0:
    print('执行子进程， 子进程(pid)：｛0｝，父进程(pid): {1}'.format(os.getpid(), os.getppid()))
else:
    print('执行子进程， 子进程(pid)：｛0｝，父进程(pid): {1}'.format(pid, os.getppid()))