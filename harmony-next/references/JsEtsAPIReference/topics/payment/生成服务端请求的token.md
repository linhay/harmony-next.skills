# 生成服务端请求的token

服务端API请求的Authorization标头中必须包含JWT格式的token用于鉴权。JSON Web Token（JWT）是一个开放标准（RFC 7519），定义了一种安全传输信息的方法，具体请参见[jwt.io](https://jwt.io/)。可以使用从[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)下载的私钥签名生成JWT。密钥的生成和下载请参见[配置密钥](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-set-necessary-parameters#配置密钥)。创建JWT格式的token需要以下几步：

1.

创建JWT Header

1.

创建JWT Payload

1.

创建JWT格式的token

**创建JWT Header**

Header参数如下：

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| alg | 是 | String | 算法类型，固定为ES256。 |
| typ | 是 | String | Token类型，固定为JWT。 |
| kid | 是 | String | 密钥ID，获取方式请参见配置密钥。如果有多个密钥，请使用对JWT进行签名的同一私钥的密钥ID。 |

**创建JWT Payload**

JWT负载包含访问服务端API的一些关键信息，例如密钥颁发者ID、JWT签发时间和JWT到期时间等。JWT负载参数如下：

| 参数 | 是否必选 | 参数类型 | 描述 |
| --- | --- | --- | --- |
| iss | 是 | String | 标识密钥颁发者ID（Issuer ID），获取方式请参见配置密钥的说明。 |
| aud | 是 | String | JWT的预期接收者，固定为iap-v1。 |
| iat | 是 | Long | JWT签发时间，UTC时间戳，以秒为单位。 |
| exp | 是 | Long | JWT到期时间，UTC时间戳，以秒为单位。 （exp-iat）即为JWT的有效期，有效期不能超过1小时。 |
| aid | 是 | String | APP ID，获取方式参见配置应用身份信息。 |
| digest | 是 | String | Request Body（json字符串）的hash值，用于验证Request Body的完整性，算法为sha256。 说明： 如果Request Body为空，则传空字符串""的hash值。 |

**创建JWT格式的token**

使用Header中指定的算法（ES256）以及密钥ID关联的私钥进行签名生成JWT，可以使用各种开源库来创建JWT格式的token，具体请参见[jwt.io](https://jwt.io/)。

**代码示例**

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

以下示例代码仅以Java语言为例，Python、PHP、JS、Golang语言示例代码可通过在[IAP Kit-Sample-ServerDemo](https://gitcode.com/HarmonyOS_Samples/iapkit-sample-serverdemo)中切换代码分支查看。

```ets
import com.auth0.jwt.JWT;
import com.auth0.jwt.algorithms.Algorithm;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.security.KeyFactory;
import java.security.interfaces.ECPrivateKey;
import java.security.spec.PKCS8EncodedKeySpec;
import java.time.Duration;
import java.util.Base64;
import java.util.HashMap;
import java.util.Map;
import org.apache.commons.codec.digest.DigestUtils;

public class JWTGenerator {
    /**
     * Private key file path.
     * For key generation and download, please refer to Configuring Keys.
     */
    private static final String JWT_PRI_KEY_PATH = "/path/to/key/priKey.p8"; // TODO: Need to replace it with the actual value.

    /**
     * JWT validity period, which is a UTC timestamp in seconds. The validity period cannot exceed 1 hour.
     */
    private static final long ACTIVE_TIME_SECOND = 3600;  // TODO: Need to replace it with the actual value.

    private static final Map<String, Object> JWT_HEADER = new HashMap<>();

    private static final Map<String, Object> JWT_PAYLOAD = new HashMap<>();

    static {
        // Algorithm type. The value is always ES256.
        JWT_HEADER.put("alg", "ES256");
        // Token type. The value is always JWT.
        JWT_HEADER.put("typ", "JWT");
        // Key ID.
        JWT_HEADER.put("kid", "Key ID");  // TODO: Need to replace it with the actual value.

        // Key issuer ID.
        JWT_PAYLOAD.put("iss", "Issuer ID");  // TODO: Need to replace it with the actual value.
        // Expected receiver of the JWT. The value is fixed at iap-v1.
        JWT_PAYLOAD.put("aud", "iap-v1");
        // Time when the JWT is issued. The value is a UTC timestamp, in seconds.
        // Re-put the value in the genJwt method.
        JWT_PAYLOAD.put("iat", 0);
        // Time when the JWT expires. The value is a UTC timestamp, in seconds. exp-iat indicates the validity period of the JWT, which cannot exceed one hour.
        // Re-put the value in the genJwt method.
        JWT_PAYLOAD.put("exp", 0);
        // App ID.
        JWT_PAYLOAD.put("aid", "App ID");  // TODO: Need to replace it with the actual value.
        // Hash value of the request body (JSON character string), which is used to verify the integrity of the body. The algorithm is SHA-256.
        JWT_PAYLOAD.put("digest", "");
    }

    public static String genJwt(String bodyStr) throws Exception {
        try {
            // Fetch the Private Key Content in PEM format.
            Path filePath = Paths.get(JWT_PRI_KEY_PATH);
            String fileString = new String(Files.readAllBytes(filePath), StandardCharsets.UTF_8);
            String privateKey = fileString.replace("-----BEGIN PRIVATE KEY-----", "")
                .replaceAll("\\R+", "")
                .replace("-----END PRIVATE KEY-----", "");
            KeyFactory keyFactory = KeyFactory.getInstance("EC");
            byte[] privateKeyBytes = Base64.getDecoder().decode(privateKey);
            PKCS8EncodedKeySpec keySpec = new PKCS8EncodedKeySpec(privateKeyBytes);
            ECPrivateKey ecPrivateKey = (ECPrivateKey) keyFactory.generatePrivate(keySpec);
            Map<String, Object> jwtPayload = new HashMap<>(JWT_PAYLOAD);
            long signTime = System.currentTimeMillis() / Duration.ofSeconds(1).toMillis();
            String digest = DigestUtils.sha256Hex(bodyStr);
            jwtPayload.put("iat", signTime);
            jwtPayload.put("exp", signTime + ACTIVE_TIME_SECOND);
            jwtPayload.put("digest", digest);
            return JWT.create().withHeader(JWT_HEADER).withPayload(jwtPayload).sign(Algorithm.ECDSA256(ecPrivateKey));
        } catch (Exception e) {
            // TODO: Need to replace it with the actual business logic.
            throw new Exception(e);
        }
```

pom文件

```ets
<dependency>
    <groupId>com.auth0</groupId>
    <artifactId>java-jwt</artifactId>
    <version>4.4.0</version>
</dependency>
```

**Authorization说明**

调用服务端API请求时，请求Header使用 Authorization: Bearer <JWT格式的token>传递鉴权信息，样例如下：

```ets
Authorization: Bearer eyJhbGciOi---xxx.eyJpc3MiOm---xxx.WFquGEx5gf---xxx
```