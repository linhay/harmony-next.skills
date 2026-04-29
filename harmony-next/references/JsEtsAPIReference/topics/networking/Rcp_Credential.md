# Rcp_Credential

**概述**

凭据。某些服务器或代理服务器需要。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| char * username | 凭据的用户名。默认值为""。 |
| char * password | 凭据的密码。默认值为""。 |

**结构体成员变量说明**

**password**

```ets
char* Rcp_Credential::password
```

描述

凭据的密码。默认值为""。

**username**

```ets
char* Rcp_Credential::username
```

描述

凭据的用户名。默认值为""。