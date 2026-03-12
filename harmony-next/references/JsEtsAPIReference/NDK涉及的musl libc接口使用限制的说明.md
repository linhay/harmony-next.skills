# NDK涉及的musl libc接口使用限制的说明

#### 概述

开发者使用DevEco Studio或者NDK进行应用开发时，可能涉及到使用musl libc的接口能力，因为musl libc的个别接口可能受多种系统和环境的限制而无法使用，此时可以通过本文档进行接口问题排查。

如果确认是下列原因导致接口调用报错，请通过“华为开发者联盟官网”->“支持”，[在线提单](https://developer.huawei.com/consumer/cn/support/)方式获取支持。

#### Seccomp机制影响的musl接口

#### 确定进程因为Seccomp机制终止的方法

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

#### 常见可能受Seccomp机制影响的接口列表如下

头文件musl接口名称fcntl.hname_to_handle_atfcntl.hopen_by_handle_atgrp.hinitgroupsgrp.hsetgroupssched.hsetnssched.hunsharesys/fanotify.hfanotify_initsys/fanotify.hfanotify_marksys/fsuid.hsetfsgidsys/fsuid.hsetfsuidsys/klog.hklogctlsys/mount.hmountsys/mount.humount2sys/mount.humountsys/msg.hmsgctlsys/msg.hmsggetsys/msg.hmsgrcvsys/msg.hmsgsndsys/reboot.hrebootsys/sem.hsemctlsys/sem.hsemgetsys/sem.hsemopsys/sem.hsemtimedopsys/shm.hshmatsys/shm.hshmctlsys/shm.hshmdtsys/shm.hshmgetsys/stat.hmkfifosys/stat.hmkfifoatsys/stat.hmknodsys/stat.hmknodatsys/swap.hswapoffsys/swap.hswapontime.hclock_settimesys/time.hsettimeofdaysys/timex.hadjtimexsys/timex.hclock_adjtimeunistd.hacctunistd.hchrootunistd.hpauseunistd.hsetdomainnameunistd.hsetegidunistd.hsetgidunistd.hsethostnameunistd.hsetregidunistd.hsetresgidunistd.hsetreuidunistd.hsetuidNonepivot_rootNoneinit_moduleNonedelete_module

#### 内核没有对外开放影响的musl接口

头文件musl接口名称sys/fanotify.hfanotify_initsys/fanotify.hfanotify_markunistd.hacct

#### SELinux机制影响的musl接口

#### 确定接口因为SELinux机制报错的方法

- 引入errno.h头文件，检查errno错误状态码，如果错误状态码是EACCES，则接口报错可能是由SELinux机制引起的。

#### 常见可能受SELinux机制影响的接口列表如下

头文件musl接口名称net/if.hif_indextonamenet/if.hif_nametoindexpty.hforkptypty.hopenptysemaphore.hsem_opensemaphore.hsem_unlinkstdlib.hptsnamestdlib.hptsname_rstdlib.hposix_openptstdlib.hunlockptstdio.hpopenstdio.hpclosesys/ioctl.hioctlsys/mman.hshm_opensys/mman.hshm_unlinksys/mount.hmountsys/mount.humountsys/mount.humount2sys/msg.hmsgctlsys/msg.hmsggetsys/msg.hmsgrcvsys/msg.hmsgsndsys/sem.hsemgetsys/sem.hsemctlsys/sem.hsemopsys/sem.hsemtimedopsys/shm.hshmgetsys/shm.hshmatsys/shm.hshmdtsys/shm.hshmctlsys/stat.hmkfifosys/stat.hmkfifoatsys/stat.hmknodsys/stat.hmknodattermios.htcgetattrtermios.htcsetattrtermios.htcsendbreaktermios.htcdraintermios.htcflushtermios.htcflowtermios.htcgetsidunistd.hlinkunistd.hlinkatunistd.hreadlinkunistd.hreadlinkatunistd.hsymlinkunistd.hsymlinkatunistd.htcgetpgrpunistd.htcsetpgrputmp.hlogin_tty

#### 沙箱机制影响的musl接口

沙箱机制可参考 [应用沙箱目录](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-sandbox-directory)。

引入errno.h头文件，检查errno错误状态码，如果错误状态码是ENOENT，则接口报错可能是由沙箱机制引起的。

常见可能受沙箱机制影响的接口列表如下：

头文件musl接口名称fcntl.hopenfcntl.hopenatnl_types.hcatopenstdio.hfopenstdio.hfreopenstdio.hrenamestdio.hrenameatstdio.hrenameat2stdio.htmpfilestdio.htmpfile64

#### 空实现或默认失败的musl接口

头文件musl接口名称netdb.hgetnetbyaddrnetdb.hgetnetbynamestdio_ext.h__fsetlockingunistd.hbrkutmp.hgetutentutmp.hpututlineutmp.hsetutentutmp.hpututlineutmp.hutmpname

#### 需要特殊权限才能执行的musl接口

引入errno.h头文件，检查errno错误状态码，如果错误状态码是EPERM，则接口报错可能是由系统Capabilities安全机制引起的，也有可能是内核其他安全管控引起的。

常见可能受Capabilities机制影响的接口如下：

头文件musl接口名称Capabilities权限Nonepivot_rootCAP_SYS_ADMINNoneinit_moduleCAP_SYS_MODULENonedelete_moduleCAP_SYS_MODULEfcntl.hopen_by_handle_atCAP_DAC_READ_SEARCHsys/klog.hklogctlCAP_SYS_ADMINsys/mount.hmountCAP_SYS_ADMINsys/mount.humountCAP_SYS_ADMINsys/mount.humount2CAP_SYS_ADMINsys/reboot.hrebootCAP_SYS_BOOTsys/swap.hswaponCAP_SYS_ADMINsys/swap.hswapoffCAP_SYS_ADMINsys/time.hsettimeofdayCAP_SYS_TIMEunistd.hsetdomainnameCAP_SYS_ADMINunistd.hsethostnameCAP_SYS_ADMINunistd.hchrootCAP_SYS_CHROOT