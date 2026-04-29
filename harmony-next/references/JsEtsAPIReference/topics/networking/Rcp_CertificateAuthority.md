# Rcp_CertificateAuthority

**概述**

用于验证远程服务器标识的证书颁发机构（CA）。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| char * content | 用于验证对等的证书颁发机构证书捆绑包。应采用PEM格式。 |
| char * filePath | 用于验证对等方的证书颁发机构证书文件的路径。文件应为PEM格式。 |
| char * folderPath | 包含用于验证对等项的多个CA证书的目录的路径。 此目录中的文件应为PEM格式。 文件必须以主题名称的哈希和扩展名“.0”命名。 |

**结构体成员变量说明**

**content**

```ets
char* Rcp_CertificateAuthority::content
```

描述

用于验证对等的证书颁发机构证书捆绑包。它应采用PEM格式。

**filePath**

```ets
char* Rcp_CertificateAuthority::filePath
```

描述

用于验证对等方的证书颁发机构证书文件的路径。文件应为PEM格式。

**folderPath**

```ets
char* Rcp_CertificateAuthority::folderPath
```

描述

包含用于验证对等项的多个CA证书的目录的路径。 此目录中的文件应为PEM格式。

文件必须以主题名称的哈希和扩展名“.0”命名。