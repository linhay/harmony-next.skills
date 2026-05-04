# NDK涉及的musl libc接口使用限制的说明

**概述**

开发者使用DevEco Studio或者NDK进行应用开发时，可能涉及到使用musl libc的接口能力，因为musl libc的个别接口可能受多种系统和环境的限制而无法使用，此时可以通过本文档进行接口问题排查。

如果确认是下列原因导致接口调用报错，请通过“华为开发者联盟官网”->“支持”，[在线提单](https://developer.huawei.com/consumer/cn/support/)方式获取支持。

**Seccomp机制影响的musl接口**

**确定进程因为Seccomp机制终止的方法**

- 查看进程faultlog日志，如果报错原因是signal:SIGSYS，且栈顶在ld-musl-{架构}.so.1库里，则进程终止可能是由Seccomp机制引起的。
```ets
cat /data/log/faultlog/faultlogger/cppcrash-xxxx
```
 错误示例：
```ets
Process name:com.example.myapplication
Reason:Signal:SIGSYS(UNKNOWN)
Fault thread Info:
Tid:13893, Name:e.myapplication
#00 pc 000a5d30 /system/lib/ld-musl-arm.so.1(sethostname+16)(584c9d0a0e9000497bb0d66799a9526a)
#01 pc 00002f68 /data/storage/el1/bundle/libs/arm/libentry.so(test()+64)
```

**常见可能受Seccomp机制影响的接口列表如下**

| 头文件 | musl接口名称 |
| --- | --- |
| fcntl.h | name_to_handle_at |
| fcntl.h | open_by_handle_at |
| grp.h | initgroups |
| grp.h | setgroups |
| sched.h | setns |
| sched.h | unshare |
| sys/fanotify.h | fanotify_init |
| sys/fanotify.h | fanotify_mark |
| sys/fsuid.h | setfsgid |
| sys/fsuid.h | setfsuid |
| sys/klog.h | klogctl |
| sys/mount.h | mount |
| sys/mount.h | umount2 |
| sys/mount.h | umount |
| sys/msg.h | msgctl |
| sys/msg.h | msgget |
| sys/msg.h | msgrcv |
| sys/msg.h | msgsnd |
| sys/reboot.h | reboot |
| sys/sem.h | semctl |
| sys/sem.h | semget |
| sys/sem.h | semop |
| sys/sem.h | semtimedop |
| sys/shm.h | shmat |
| sys/shm.h | shmctl |
| sys/shm.h | shmdt |
| sys/shm.h | shmget |
| sys/stat.h | mkfifo |
| sys/stat.h | mkfifoat |
| sys/stat.h | mknod |
| sys/stat.h | mknodat |
| sys/swap.h | swapoff |
| sys/swap.h | swapon |
| time.h | clock_settime |
| sys/time.h | settimeofday |
| sys/timex.h | adjtimex |
| sys/timex.h | clock_adjtime |
| unistd.h | acct |
| unistd.h | chroot |
| unistd.h | pause |
| unistd.h | setdomainname |
| unistd.h | setegid |
| unistd.h | setgid |
| unistd.h | sethostname |
| unistd.h | setregid |
| unistd.h | setresgid |
| unistd.h | setreuid |
| unistd.h | setuid |
| None | pivot_root |
| None | init_module |
| None | delete_module |

**内核没有对外开放影响的musl接口**

| 头文件 | musl接口名称 |
| --- | --- |
| sys/fanotify.h | fanotify_init |
| sys/fanotify.h | fanotify_mark |
| unistd.h | acct |

**SELinux机制影响的musl接口**

**确定接口因为SELinux机制报错的方法**

- 引入errno.h头文件，检查errno错误状态码，如果错误状态码是EACCES，则接口报错可能是由SELinux机制引起的。

**常见可能受SELinux机制影响的接口列表如下**

| 头文件 | musl接口名称 |
| --- | --- |
| net/if.h | if_indextoname |
| net/if.h | if_nametoindex |
| pty.h | forkpty |
| pty.h | openpty |
| semaphore.h | sem_open |
| semaphore.h | sem_unlink |
| stdlib.h | ptsname |
| stdlib.h | ptsname_r |
| stdlib.h | posix_openpt |
| stdlib.h | unlockpt |
| stdio.h | popen |
| stdio.h | pclose |
| sys/ioctl.h | ioctl |
| sys/mman.h | shm_open |
| sys/mman.h | shm_unlink |
| sys/mount.h | mount |
| sys/mount.h | umount |
| sys/mount.h | umount2 |
| sys/msg.h | msgctl |
| sys/msg.h | msgget |
| sys/msg.h | msgrcv |
| sys/msg.h | msgsnd |
| sys/sem.h | semget |
| sys/sem.h | semctl |
| sys/sem.h | semop |
| sys/sem.h | semtimedop |
| sys/shm.h | shmget |
| sys/shm.h | shmat |
| sys/shm.h | shmdt |
| sys/shm.h | shmctl |
| sys/stat.h | mkfifo |
| sys/stat.h | mkfifoat |
| sys/stat.h | mknod |
| sys/stat.h | mknodat |
| termios.h | tcgetattr |
| termios.h | tcsetattr |
| termios.h | tcsendbreak |
| termios.h | tcdrain |
| termios.h | tcflush |
| termios.h | tcflow |
| termios.h | tcgetsid |
| unistd.h | link |
| unistd.h | linkat |
| unistd.h | readlink |
| unistd.h | readlinkat |
| unistd.h | symlink |
| unistd.h | symlinkat |
| unistd.h | tcgetpgrp |
| unistd.h | tcsetpgrp |
| utmp.h | login_tty |

**沙箱机制影响的musl接口**

沙箱机制可参考 [应用沙箱目录](../../guides/应用沙箱目录.md)。

引入errno.h头文件，检查errno错误状态码，如果错误状态码是ENOENT，则接口报错可能是由沙箱机制引起的。

常见可能受沙箱机制影响的接口列表如下：

| 头文件 | musl接口名称 |
| --- | --- |
| fcntl.h | open |
| fcntl.h | openat |
| nl_types.h | catopen |
| stdio.h | fopen |
| stdio.h | freopen |
| stdio.h | rename |
| stdio.h | renameat |
| stdio.h | renameat2 |
| stdio.h | tmpfile |
| stdio.h | tmpfile64 |

**空实现或默认失败的musl接口**

| 头文件 | musl接口名称 |
| --- | --- |
| netdb.h | getnetbyaddr |
| netdb.h | getnetbyname |
| stdio_ext.h | __fsetlocking |
| unistd.h | brk |
| utmp.h | getutent |
| utmp.h | pututline |
| utmp.h | setutent |
| utmp.h | pututline |
| utmp.h | utmpname |

**需要特殊权限才能执行的musl接口**

引入errno.h头文件，检查errno错误状态码，如果错误状态码是EPERM，则接口报错可能是由系统Capabilities安全机制引起的，也有可能是内核其他安全管控引起的。

常见可能受Capabilities机制影响的接口如下：

| 头文件 | musl接口名称 | Capabilities权限 |
| --- | --- | --- |
| None | pivot_root | CAP_SYS_ADMIN |
| None | init_module | CAP_SYS_MODULE |
| None | delete_module | CAP_SYS_MODULE |
| fcntl.h | open_by_handle_at | CAP_DAC_READ_SEARCH |
| sys/klog.h | klogctl | CAP_SYS_ADMIN |
| sys/mount.h | mount | CAP_SYS_ADMIN |
| sys/mount.h | umount | CAP_SYS_ADMIN |
| sys/mount.h | umount2 | CAP_SYS_ADMIN |
| sys/reboot.h | reboot | CAP_SYS_BOOT |
| sys/swap.h | swapon | CAP_SYS_ADMIN |
| sys/swap.h | swapoff | CAP_SYS_ADMIN |
| sys/time.h | settimeofday | CAP_SYS_TIME |
| unistd.h | setdomainname | CAP_SYS_ADMIN |
| unistd.h | sethostname | CAP_SYS_ADMIN |
| unistd.h | chroot | CAP_SYS_CHROOT |