[]()[]()

# 公共说明

[]()[]()

#### TLS协议及加密套件

TLS版本

加密套件**（IANA名称）**

TLS1.2

TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384

TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256

TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384

TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256

[]()[]()

#### 示例代码环境配置

REST API接口提供的示例代码，运行时需要进行如下配置：

- 配置maven依赖

```ets
<dependencies>
    <dependency>
        <groupId>com.alibaba.fastjson2</groupId>
        <artifactId>fastjson2</artifactId>
        <version>2.0.51</version> <!--此处替换为您项目需要的版本-->
    </dependency>
    <dependency>
        <groupId>org.apache.httpcomponents</groupId>
        <artifactId>httpclient</artifactId>
        <version>4.5.6</version> <!--此处替换为您项目需要的版本-->
    </dependency>
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
        <version>1.18.26</version> <!--此处替换为您项目需要的版本-->
    </dependency>
    <dependency>
        <groupId>ch.qos.logback</groupId>
        <artifactId>logback-classic</artifactId>
        <version>1.2.11</version> <!--此处替换为您项目需要的版本-->
    </dependency>
</dependencies>
```

- 引入CallUtils工具类（请将此工具类与API的示例代码放于同一路径下，如不在同一路径，请手动到API的示例代码添加import）

```ets
import com.alibaba.fastjson2.JSON;
import com.alibaba.fastjson2.JSONObject;
import lombok.extern.slf4j.Slf4j;
import org.apache.http.Header;
import org.apache.http.HttpEntity;
import org.apache.http.HttpStatus;
import org.apache.http.client.config.RequestConfig;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpUriRequest;
import org.apache.http.config.Registry;
import org.apache.http.config.RegistryBuilder;
import org.apache.http.conn.socket.ConnectionSocketFactory;
import org.apache.http.conn.socket.PlainConnectionSocketFactory;
import org.apache.http.conn.ssl.SSLConnectionSocketFactory;
import org.apache.http.entity.ContentType;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.impl.conn.PoolingHttpClientConnectionManager;
import org.apache.http.util.EntityUtils;
import javax.net.ssl.SSLContext;
import javax.net.ssl.TrustManagerFactory;
import java.io.IOException;
import java.security.KeyManagementException;
import java.security.KeyStore;
import java.security.KeyStoreException;
import java.security.NoSuchAlgorithmException;
import java.util.Map;
import java.util.Objects;
import java.util.function.BiFunction;

/**
 * HTTP调用工具类
 */
@Slf4j
public class CallUtils {
    public static String remoteCall(HttpUriRequest request) throws IOException {
        return remoteCall(request, CallUtils::nspErrorHandler);
    }

    public static String remoteCallOAuth(HttpUriRequest request) throws IOException {
        return remoteCall(request, CallUtils::oauthErrorHandler);
    }

    public static String remoteCallAccountApi(HttpUriRequest request) throws IOException {
        return remoteCall(request, CallUtils::accountApiErrorHandler);
    }

    public static <E extends Exception> String remoteCall(HttpUriRequest request,
        BiFunction<CloseableHttpResponse, String, E> errorHandler) throws IOException, E {
        try (CloseableHttpResponse response = getClient().execute(request)) {
            HttpEntity responseEntity = response.getEntity();
            String ret = responseEntity != null ? EntityUtils.toString(responseEntity) : null;
            EntityUtils.consume(responseEntity);
            if (errorHandler != null) {
                E error = errorHandler.apply(response, ret);
                if (null != error) {
                    throw error;
                }
            }
            return ret;
        }
    }

    public static JSONObject toJsonObject(String json) {
        return (JSONObject) JSON.parse(json);
    }

    public static StringEntity wrapJsonEntity(Object obj) {
        return new StringEntity(CallUtils.toJsonString(obj), ContentType.create("application/json", "UTF-8"));
    }

    public static String toJsonString(Object obj) {
        return JSON.toJSONString(obj);
    }

    public static IOException nspErrorHandler(CloseableHttpResponse response, String rawBody) {
        int statusCode = response.getStatusLine().getStatusCode();
        if (statusCode != 200) {
            return new IOException("call failed! status:" + statusCode + ", response data: " + rawBody);
        }
        Header nspStatus = response.getFirstHeader("NSP_STATUS");
        if (Objects.nonNull(nspStatus)) {
            return new IOException("call failed! nsp_status:" + nspStatus.getValue() + ", response data: " + rawBody);
        }
        return null;
    }

    public static IOException oauthErrorHandler(CloseableHttpResponse response, String rawBody) {
        int statusCode = response.getStatusLine().getStatusCode();
        // http状态码为200，请求成功
        if (statusCode == HttpStatus.SC_OK) {
            return null;
        }
        // http状态码非200，解析响应的body，业务视情况进行处理
        Map<String, Object> errorResponseBody = CallUtils.toJsonObject(rawBody);
        // 业务响应主错误码
        Object error = errorResponseBody.get("error");
        // 业务响应子错误码
        Object subError = errorResponseBody.get("sub_error");
        // 业务可根据返回的主+子错误码进行自己的业务处理；例：错误码不为空，抛出异常
        if (Objects.nonNull(error) && Objects.nonNull(subError)) {
            return new IOException("call failed! http status code: " + statusCode + ", response data: " + rawBody);
        }
        return null;
    }

    public static IOException accountApiErrorHandler(CloseableHttpResponse response, String rawBody) {
        int statusCode = response.getStatusLine().getStatusCode();
        // http状态码不是200，请求失败
        if (statusCode != 200) {
            return new IOException("call failed! http status code: " + statusCode + ", response data: " + rawBody);
        }
        // http状态码为200，解析响应的body，判断业务错误码
        JSONObject errorResponseBody = CallUtils.toJsonObject(rawBody);
        // 业务响应码
        Integer resultCode = errorResponseBody.getInteger("resultCode");
        // resultCode为0表示成功，非0表示失败
        if (Objects.nonNull(resultCode) && resultCode != 0) {
            return new IOException("call failed! http status code: " + statusCode + ", response data: " + rawBody);
        }
        return null;
    }

    private static CloseableHttpClient getClient() {
        PoolingHttpClientConnectionManager connectionManager = buildConnectionManager(
            new String[] {"TLSv1.2"}, new String[] {
                "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
                "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256"
            });
        connectionManager.setMaxTotal(400);
        connectionManager.setDefaultMaxPerRoute(400);
        RequestConfig config = RequestConfig.custom()
            .setConnectionRequestTimeout(100)
            .setRedirectsEnabled(false)
            .build();
        return HttpClients.custom()
            .useSystemProperties()
            .setConnectionManager(connectionManager)
            .setDefaultRequestConfig(config)
            .build();
    }

    private static PoolingHttpClientConnectionManager buildConnectionManager(String[] supportedProtocols,
        String[] supportedCipherSuites) {
        PoolingHttpClientConnectionManager connectionManager = null;
        try {
            SSLContext sc = SSLContext.getInstance("TLSv1.2");
            TrustManagerFactory tmf = TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());
            tmf.init((KeyStore) null);
            sc.init(null, tmf.getTrustManagers(), null);
            SSLConnectionSocketFactory sslsf = new SSLConnectionSocketFactory(sc, supportedProtocols,
                supportedCipherSuites, SSLConnectionSocketFactory.getDefaultHostnameVerifier());
            Registry<ConnectionSocketFactory> registry = RegistryBuilder.<ConnectionSocketFactory>create()
                .register("http", new PlainConnectionSocketFactory())
                .register("https", sslsf)
                .build();
            connectionManager = new PoolingHttpClientConnectionManager(registry);
        } catch (NoSuchAlgorithmException | KeyStoreException | KeyManagementException e) {
            log.error("build connect manager failed", e);
        }
        return connectionManager;
    }
}
```