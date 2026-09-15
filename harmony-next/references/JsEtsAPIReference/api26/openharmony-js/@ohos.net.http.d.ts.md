# @ohos.net.http.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2023 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * @file Data Request
 * @kit NetworkKit
 */
import type { AsyncCallback, Callback } from './@ohos.base';
import type connection from './@ohos.net.connection';
import type cert from './@ohos.security.cert';
/**
 * The **http** module provides APIs for implementing HTTP data request capabilities. An application can initiate a data
 * request over HTTP. Common HTTP methods include **GET**, **POST**, **OPTIONS**, **HEAD**, **PUT**, **DELETE**,
 * **PATCH**, **TRACE**, and **CONNECT**.
 *
 * @syscap SystemCapability.Communication.NetStack
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 6
 */
declare namespace http {
    /**
     * Defines the network proxy configuration.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     */
    type HttpProxy = connection.HttpProxy;
    /**
     * Socks5 Proxy Configuration Information.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @stagemodelonly
     * @since 26.0.0
     */
    type Socks5Proxy = connection.Socks5Proxy;
    /**
     * Creates an HTTP request. You can use this API to initiate or destroy an HTTP request, or enable or disable
     * listening for HTTP Response Header events. To initiate multiple HTTP requests, you must create an **HttpRequest**
     * object for each HTTP request. An **HttpRequest** object corresponds to an HTTP request.
     *
     * > **NOTE**
     * >
     * > When the request is no longer needed, call destroy() to release resources. Otherwise, memory leaks may occur.
     *
     * @returns { HttpRequest } An **HttpRequest** object, which contains the **request**, **requestInStream**,
     *     **requestSync**, **enableAutoCookie**, **destroy**, **on**, and **off** methods.
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 6
     */
    function createHttp(): HttpRequest;
    /**
     * Defines the options for initiating an HTTP request.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 6
     */
    export interface HttpRequestOptions {
        /**
         * Request method. The default value is **GET**.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        method?: RequestMethod;
        /**
         * Additional data for sending a request. This parameter is not used by default. Since API version 26, you are
         * advised to use the **body** and **queryParams** parameters preferentially.
         *
         * **Note**: Do not add this parameter if no extra data is available. If this parameter must be added, set it to
         * **undefined** or **null**. Do not pass the parameter as "".
         *
         * - If the HTTP request uses a POST, PUT, or DELETE method, this field serves as the content of the HTTP request
         * and is encoded in UTF-8 format.
         *
         * Example:
         *
         * (1) If **content-Type** is **application/x-www-form-urlencoded**, the data in the request body must be encoded in
         * the format of **key1=value1&key2=value2&key3=value3** after URL transcoding (**encodeURIComponent/encodeURI**)
         * and this field is usually in the String format.
         *
         * (2) If **content-Type** is **text/xml**, this field is usually in the String format.
         *
         * (3) If **content-Type** is **application/json**, this field is usually in the Object format.
         *
         * (4) If **content-Type** is **application/octet-stream**, this field is usually in the ArrayBuffer format.
         *
         * (5) If **content-Type** is **multipart/form-data** and the content to be uploaded is a file, this field is
         * usually in the ArrayBuffer format.
         *
         * The preceding information is for reference only and may vary according to the actual situation.
         *
         * - If the HTTP request uses the GET, OPTIONS, TRACE, or CONNECT method, this parameter serves as a supplement to
         * HTTP request parameters. Parameters of the string type need to be encoded before being passed to the HTTP
         * request. Parameters of the object type do not need to be precoded and will be directly concatenated to the URL.
         * Parameters of the ArrayBuffer type will not be concatenated to the URL.
         *
         * @type {?string | Object | ArrayBuffer} [since 6 - 10]
         * @type { ?(string | Object | ArrayBuffer) } [since 11]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        extraData?: string | Object | ArrayBuffer;
        /**
         * Type of the returned data. This parameter is not used by default. If this parameter is set, the system returns
         * the specified type of data preferentially. If the specified type is **Object**, the value can contain a maximum
         * of 65536 characters.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        expectDataType?: HttpDataType;
        /**
         * Whether to use the cache. The value **true** indicates that the cache is preferentially read when a request is
         * initiated, and the value **false** indicates that the cache is not used. The default value is **true**. The cache
         * function takes effect when the process is started. The new cached data will replace the existing cached data.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        usingCache?: boolean;
        /**
         * Priority of concurrent HTTP/HTTPS requests. A larger value indicates a higher priority. The value range is
         * [1, 1000]. The default value is **1**.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        priority?: number;
        /**
         * HTTP request header. If the request method is POST, PUT, DELETE, or null, the default value is {'content-Type': '
         * application/json'}. Otherwise, the default value is {'content-Type': 'application/x-www-form-urlencoded'}.
         *
         * If the header contains fields of numeric type, the maximum value must be an int64 integer.
         *
         * The header field supports the JSON format (as shown in
         * [Example](docroot://reference/apis-network-kit/js-apis-http.md#example)) and the Record<string, string> format.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        header?: Object;
        /**
         * Read timeout duration. The default value is **60000**, in ms. The input value must be an uint32_t integer.
         *
         * The value **0** indicates no timeout.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        readTimeout?: number;
        /**
         * Connection timeout interval. The default value is **60000**, in ms. The input value must be an uint32_t integer.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        connectTimeout?: number;
        /**
         * Protocol. The default value is automatically specified by the system.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        usingProtocol?: HttpProtocol;
        /**
         * HTTP proxy configuration. If this item is not configured, the system proxy is used by default.
         *
         * - If **usingProxy** is set to **true**, the default network proxy is used. If **usingProxy** is set to **false**,
         * no proxy is used.
         * - If **usingProxy** is of the **HttpProxy** type, the specified network proxy is used. The HttpProxy supports the
         * **username** and **password** fields from API version 22.
         *
         * @type {?boolean | HttpProxy} [since 10 - 10]
         * @type { ?(boolean | HttpProxy) } [since 11]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        usingProxy?: boolean | HttpProxy;
        /**
         * CA certificate data. If this parameter is set and the certificate is valid, the system uses the specified CA
         * certificate and the preset CA certificate. Otherwise, the system uses only the preset CA certificate. The CA
         * certificate path is the sandbox mapping path, which can be obtained by using **UIAbilityContext** APIs.
         * Currently, only **.pem** certificates are supported.
         *
         * The preset CA certificate is available at **\/etc/ssl/certs/cacert.pem**.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        caPath?: string;
        /**
         * CA certificate data. If this parameter is set and the certificate is valid, the system uses the specified CA
         * certificate and the preset CA certificate. Otherwise, the system uses only the preset CA certificate. If both
         * **caPath** and **caData** are set, **caData** is ignored by the system. Currently, only certificates in **.pem**
         * format are supported. The maximum length is 8000 bytes. Only one certificate can be specified. A certificate
         * chain is not allowed.
         *
         * The preset CA certificate is available at **\/etc/ssl/certs/cacert.pem**. This path is the sandbox mapping path,
         * which can be obtained by using **UIAbilityContext** APIs.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        caData?: string;
        /**
         * Security communication protocol. You can use TLS (default) or TLCP. If TLCP is used, the related options (such as
         * **caPath**, **clientCert**, and **clientEncCert**) must be set to valid values.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 20
         */
        sslType?: SslType;
        /**
         * Client certificate, which is used by the server to verify the client identity.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 20
         */
        clientEncCert?: ClientCert;
        /**
         * Download start position. This field can be used only for the GET method. As stipulated in section 3.1 of RFC 723
         * 3, servers are allowed to ignore range requests.
         *
         * - If the HTTP PUT method is used, do not use this option because it may conflict with other options.
         * - The value ranges from **1** to **4294967296** (4 GB). If the value is out of this range, this field does not
         * take effect.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        resumeFrom?: number;
        /**
         * Download end position. This field can be used only for the GET method. As stipulated in section 3.1 of RFC 7233,
         * servers are allowed to ignore range requests.
         *
         * - If the HTTP PUT method is used, do not use this option because it may conflict with other options.
         * - The value ranges from **1** to **4294967296** (4 GB). If the value is out of this range, this field does not
         * take effect.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        resumeTo?: number;
        /**
         * Client certificate.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        clientCert?: ClientCert;
        /**
         * Whether to use an HTTPS server for DNS resolution.
         *
         * - The value must be URL-encoded in the following format: "https:// host:port/path".
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        dnsOverHttps?: string;
        /**
         * Array of DNS servers used for DNS resolution.
         *
         * - A maximum of three DNS servers can be set. If there are more than three DNS servers, only the first three DNS
         * servers are used.
         * - The DNS servers must be expressed as IPv4 or IPv6 addresses.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        dnsServers?: Array<string>;
        /**
         * Maximum number of bytes in a response.
         *
         * The default value is 5*1024*1024, in bytes. The maximum value is **100*1024*1024**.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        maxLimit?: number;
        /**
         * Form data list. This field is valid when **content-Type** is set to **multipart/form-data**.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        multiFormDataList?: Array<MultiFormData>;
        /**
         * Dynamic configuration of certificate pinning. One or more certificate PINs can be specified.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @since 12
         */
        certificatePinning?: CertificatePinning | CertificatePinning[];
        /**
         * Certificate authority (CA), which is used to verify the identity of a remote server. If the parameter is not set,
         * the default value is used. The options are as follows:
         *
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 18
         */
        remoteValidation?: RemoteValidation;
        /**
         * TLS configuration.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 18
         */
        tlsOptions?: TlsOptions;
        /**
         * Whether to verify the server identity during a secure connection. The identity is not verified by default.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 18
         */
        serverAuthentication?: ServerAuthentication;
        /**
         * IP address family. You can specify an address type for domain name resolution.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @since 15
         */
        addressFamily?: AddressFamily;
        /**
         * Used to allow the client to declare the target domain name to the server in the TLS handshake phase by
         * configuring the server name indication (SNI). In this way, the server can select the corresponding SSL/TLS
         * certificate based on the domain name for encrypted communication.
         *
         * - The default value is an empty string. The value of **sniHostName** can contain a maximum of 255 characters. If
         * the length limit is exceeded or the value is an empty string, the setting does not take effect.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @since 23
         */
        sniHostName?: string;
        /**
         * The maximum number of redirections can be specified for HttpRequest.
         *
         * - The default value is 30.
         * - The value range is [0, 2147483647]. If the value is set to **0**, redirection is disabled. If the number of
         * redirections on the server exceeds the maximum number of redirections, error code 2300047 is returned. If the
         * value is out of the range, the default value **30** takes effect.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @since 23
         */
        maxRedirects?: number;
        /**
         * Custom request method. For example, when the WebDAV extension protocol is implemented, **customMethod** has a
         * higher priority than **method**.
         *
         * - The default value is an empty string. The value can contain a maximum of 128 characters. If the value exceeds 1
         * 28 characters, the setting does not take effect.
         * - If **customMethod** meets the WebDAV extension protocol request requirements but the server does not support
         * the request, the server response code of the request is usually 405 or 501 (the actual result depends on the
         * server behavior).
         * - If **customMethod** does not meet the WebDAV extension protocol request requirements, the server response code
         * of the request is usually 400 or 405 (the actual result depends on the server behavior).
         *
         * @syscap SystemCapability.Communication.NetStack
         * @since 23
         */
        customMethod?: string;
        /**
         * Used to specify the network to be activated in an HTTP request.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @since 23
         */
        pathPreference?: PathPreference;
        /**
         * Whether to reuse the connection for an HTTP request. The default value is **true**, meaning to reuse the existing
         * connection. The value **false** means the opposite. This field can be used together with the **inactivityMs**
         * field to customize the connection timeout interval.
         *
         * - Connection reuse means that after an HTTP request is completed, the underlying TCP connection is not
         * immediately closed. Instead, it remains in the connection pool. If subsequent HTTP requests have the same target
         * address, the connection can be reused, reducing the overhead of TCP and TLS handshakes and improving performance.
         *
         * **Since**: 26.0.0
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 26.0.0
         */
        reuseConnections?: boolean;
        /**
         * Maximum idle time of a connection in the connection pool. If this value is exceeded, the connection is closed.
         * The unit is ms. The default value is 118s. The system calculates the connection idle time, rounds it down to
         * seconds, and then compares it with the configured value.
         *
         * - The value range is (0, 2147483647]. If a value less than or equal to 0 is passed, the system uses the default
         * value 118s. This parameter does not take effect when **reuseConnections** is set to **false**.
         *
         * **Since**: 26.0.0
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 26.0.0
         */
        inactivityMs?: number;
        /**
         * Specifies the use of a SOCKS5 proxy. Note that this configuration takes precedence over usingProxy.
         * It is recommended not to configure both simultaneously.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 26.0.0
         */
        usingSocks5Proxy?: Socks5Proxy;
        /**
         * Indicates whether to enable partial chain verification.
         * The default value is true when SslType is set to TLS, and false when SslType is set to TLCP.
         * If set to false, the certificate chain must verify up to a trusted root CA.
         * If set to true, the verification succeeds if the chain builds to a trusted intermediate CA,
         * without requiring a path to a trusted root CA.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 26.0.0
         */
        enablePartialChain?: boolean;
        /**
         * Request parameters appended to the URL.
         *
         * - The value can be a string or a **QueryParamObject**. A string is directly appended to the URL (without repeated
         * encoding). A **QueryParamObject** is automatically encoded and serialized by the system.
         * - When a string is used, the leading **?** is not required. Use **&** to separate multiple parameters.
         * - If both **queryParams** and **extraData** are configured, **queryParams** takes precedence, and the URL
         * parameter supplementation logic in **extraData** is ignored.
         *
         * **Since**: 26.0.0
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @crossplatform
         * @since 26.0.0
         */
        queryParams?: string | QueryParamObject;
        /**
         * HTTP request body. After this field is set, the framework preferentially sends this field as the request body.
         *
         * - The value can be a string, an object, or an **ArrayBuffer**. A string is sent as the original value, an object
         * is serialized before being sent, and an **ArrayBuffer** is sent in binary format.
         * - If both **body** and **extraData** are configured, **body** takes precedence and **extraData** will be ignored.
         * - This field can be used with any request method to explicitly specify the request body.
         *
         * **Since**: 26.0.0
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @crossplatform
         * @since 26.0.0
         */
        body?: string | Object | ArrayBuffer;
    }
    /**
     * Defines HTTP server identity verification information.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @atomicservice
     * @since 18
     */
    export interface ServerAuthentication {
        /**
         * Server credential. The default value is **undefined**.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 18
         */
        credential: Credential;
        /**
         * Server identity verification type. If the type is not set, negotiation with the server is required.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 18
         */
        authenticationType?: AuthenticationType;
    }
    /**
     * Defines the TLS configuration.
     *
     * @unionmember { 'system' } TLS version of the system. This field is defaulted to **system** when the value is not
     *     set.
     * @unionmember { TlsConfig } Custom TLS version and cipher suites.
     * @syscap SystemCapability.Communication.NetStack
     * @atomicservice
     * @since 18
     */
    export type TlsOptions = 'system' | TlsConfig;
    /**
     * X509 certificate.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @stagemodelonly
     * @since 26.0.0
     */
    export type X509Cert = cert.X509Cert;
    /**
     * The validation context of {@link ValidationCallback}
     *
     * @syscap SystemCapability.Communication.NetStack
     * @stagemodelonly
     * @since 26.0.0
     */
    export interface ValidationContext {
        /**
         * The raw data which in PEM format of certificate.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 26.0.0
         */
        pemCerts: string[];
        /**
         * X509 certificate chain.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 26.0.0
         */
        x509Certs: X509Cert[];
        /**
         * The host of this request.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 26.0.0
         */
        host: string;
        /**
         * The real IP which this request connect to.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 26.0.0
         */
        ip: string;
    }
    /**
     * Self defined remote validation.
     * This API uses a promise to return the result.
     *
     * @param { ValidationContext } context - Certificate context.
     * @returns { boolean | Promise<boolean> } Returns a boolean value indicating whether the validation is successful.
     *     Promise used to return the result. The value true indicates valid, and false indicates invalid.
     * @syscap SystemCapability.Communication.NetStack
     * @stagemodelonly
     * @since 26.0.0
     */
    export type ValidationCallback = (context: ValidationContext) => boolean | Promise<boolean>;
    /**
     * Enumerates the identity verification modes of the remote server.
     *
     * @unionmember { 'system' } Use of the system CA. This field is defaulted to **system** when the value is not set.
     * @unionmember { 'skip' } Skipping of CA verification. This field has a fixed value of **skip**.
     * @unionmember { ValidationCallback } use custom validation. [since 26.0.0]
     * @syscap SystemCapability.Communication.NetStack
     * @atomicservice
     * @since 18
     */
    export type RemoteValidation = 'system' | 'skip' | ValidationCallback;
    /**
     * Enumerates server authentication modes in a session.
     *
     * @unionmember { 'basic' } Basic authentication mode. This field has a fixed value of **basic**.
     * @unionmember { 'ntlm' } NTLM authentication mode. This field has a fixed value of **ntlm**.
     * @unionmember { 'digest' } Digest authentication mode. This field has a fixed value of **digest**.
     * @syscap SystemCapability.Communication.NetStack
     * @atomicservice
     * @since 18
     */
    export type AuthenticationType = 'basic' | 'ntlm' | 'digest';
    /**
     * Defines the secure communications protocol.
     *
     * @unionmember { 'TLS' } TLS protocol. The value is fixed to **TLS**.
     * @unionmember { 'TLCP' } TLCP protocol. The value is fixed to **TLCP**.
     *     <br>**NOTE**
     *     <br>(1) The certificate supports the following string specifications:
     *     <br> - UTF8String (English character set)
     *     <br> - PrintableString
     *     <br>  - IA5String
     *     <br>Supported since API Version 22:
     *     <br> - TeletexString
     *     <br>(2) The certificate supports the following extended specifications:
     *     <br> - BasicConstraints (OID 2.5.29.19)
     *     <br> - KeyUsage (OID2.5.29.15)
     *     <br> - SubjectKeyIdentifier (OID2.5.29.14)
     *     <br> - AuthorityKeyIdentifier (OID2.5.29.35)
     *     <br>Supported since API Version 22:
     *     <br> - SubjectAltName (OID 2.5.29.17)
     *     <br> - ExtendedKeyUsage (OID 2.5.29.37)
     *     <br>
     * @syscap SystemCapability.Communication.NetStack
     * @atomicservice
     * @since 20
     */
    export type SslType = 'TLS' | 'TLCP';
    /**
     * Enumerates the types of networks specified in an HTTP request.
     *
     * > **NOTE**
     * >
     * > It is recommended that this parameter be used in scenarios such as network concurrency.
     *
     * > If the specified network is not activated, the system uses the default network.
     *
     * @unionmember { 'auto' } Specifies the default network connection in an HTTP request.
     * @unionmember { 'primaryCellular' } Specifies the default cellular network connection in an HTTP request when the
     *     cellular network is activated.
     * @unionmember { 'secondaryCellular' } Specifies the cellular network connection of the secondary SIM card in an HTTP
     *     request when dual cellular networks are activated.
     * @syscap SystemCapability.Communication.NetStack
     * @since 23
     */
    export type PathPreference = 'auto' | 'primaryCellular' | 'secondaryCellular';
    /**
     * Defines the single-value type that can be used in **QueryParamObject**.
     *
     * @unionmember { string } String type.
     * @unionmember { int } Number type, which is converted into a string before being encoded.
     * @unionmember { boolean } Boolean type, which is converted into a string before being encoded.
     * @unionmember { null } Null type, which is serialized in the format of only the key without the = value.
     * @unionmember { undefined } Undefined type, which is serialized in the format of only the key without the = value.
     * @syscap SystemCapability.Communication.NetStack
     * @stagemodelonly
     * @crossplatform
     * @since 26.0.0
     */
    export type QueryParamValue = string | number | boolean | null | undefined;
    /**
     * Defines the key-value object type used to construct URL query parameters.
     *
     * > **NOTE**
     * >
     * > (1) The property name is used as the key of the **QueryParamObject** parameter. The corresponding property value
     * > can be a single **QueryParamValue** or a **QueryParamValue** array.
     *
     * > (2) The array will be expanded into multiple parameters with the same name. For example, **{ tag: ['a', 'b'] }**
     * > will be serialized into **tag=a&tag=b**.
     *
     * > (3) The key and value are automatically URL-encoded by the system. You should pass the original, unencoded
     * > content.
     *
     * > (4) To strictly control the parameter sequence or repeat the key sequence, you are advised to use the **string**
     * > of **queryParams**.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @stagemodelonly
     * @crossplatform
     * @since 26.0.0
     */
    export type QueryParamObject = Record<string, QueryParamValue | QueryParamValue[]>;
    /**
     * Enumerates the types of HTTP interceptors.
     *
     * | Name  | Value|Description                                  |
     * | ------ | --|-------------------------------------- |
     * | INITIAL_REQUEST |'INITIAL_REQUEST' |Intercepts after the initial HTTP request is assembled.|
     * | REDIRECTION | 'REDIRECTION' |Intercepts when a redirection response is received.|
     * | CACHE_CHECKED | 'READ_CACHE' |Intercepts when the HTTP cache is checked and hit.|
     * | NETWORK_CONNECT | 'CONNECT_NETWORK' |Intercepts before the network request is sent.|
     * | FINAL_RESPONSE | 'FINAL_RESPONSE' |Intercepts when the final HTTP response is obtained.|
     *
     * @syscap SystemCapability.Communication.NetStack
     * @atomicservice
     * @since 22
     */
    export enum InterceptorType {
        /**
         * Intercept after the initial HTTP request is assembled.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 22
         */
        INITIAL_REQUEST = 'INITIAL_REQUEST',
        /**
         * Intercept when we get a redirection responsed and is going to send another request.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 22
         */
        REDIRECTION = 'REDIRECTION',
        /**
         * Intercept after we checked the HTTP cache.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 22
         */
        CACHE_CHECKED = 'READ_CACHE',
        /**
         * Intercept when we perform network connection, such as TLS and TCP.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 22
         */
        NETWORK_CONNECT = 'CONNECT_NETWORK',
        /**
         * Intercept when we get the final HTTP response.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 22
         */
        FINAL_RESPONSE = 'FINAL_RESPONSE'
    }
    /**
     * Defines HTTP request context data. The object instance is passed as a parameter in the
     * [interceptorHandle]{@link http.HttpInterceptor.interceptorHandle} method of the interceptor. You can use this
     * object to obtain and modify the information about the HTTP request.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @atomicservice
     * @since 22
     */
    export interface HttpRequestContext {
        /**
         * The URL of an HTTP request interceptor. It can be modified in an interceptor.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 22
         */
        url: string;
        /**
         * The header of an HTTP request interceptor. It can be modified in an interceptor.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 22
         */
        header: Object;
        /**
         * The header of an HTTP request interceptor. It can be modified in an interceptor.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 22
         */
        body: Object;
    }
    /**
     * Specifies whether to continue to process the interceptor chain.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @atomicservice
     * @since 22
     */
    export type ChainContinue = boolean;
    /**
     * Defines the HTTP interceptor API, which is used to define the interception processing function.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @atomicservice
     * @since 22
     */
    export interface HttpInterceptor {
        /**
         * The type of this interceptor. It defines when this intercptor would be called.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 22
         */
        interceptorType: InterceptorType;
        /**
         * Intercepts the HTTP processing and modifies it as required.
         *
         * @param { HttpRequestContext } reqContext - the context of the target HTTP request.
         * @param { HttpResponse } rspContext - the context of the target HTTP response.
         * @returns { Promise<ChainContinue> } Continues the HTTP processing or stops and returns an HTTP response.
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 22
         */
        interceptorHandle(reqContext: HttpRequestContext, rspContext: HttpResponse): Promise<ChainContinue>;
    }
    /**
     * Defines HTTP interceptor chain.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @atomicservice
     * @since 22
     * @class HttpInterceptorChain
     */
    export class HttpInterceptorChain {
        /**
         * Obtains all interceptor instances in the current interceptor chain.
         *
         * @returns { HttpInterceptor[] } Returns all interceptor instances added by the
         *     [addChain]{@link http.HttpInterceptorChain#addChain} method.
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 22
         */
        public getChain(): HttpInterceptor[];
        /**
         * Adds an interceptor to the HTTP client.
         *
         * > **NOTE**
         * >
         * > An interceptor chain cannot contain interceptor instances of the same type. If interceptors of the same type
         * > are passed in, the error code **2300802** (Duplicated interceptor type in the chain) is reported.
         *
         * @param { HttpInterceptor[] } chain - Interception chain composed of interceptor instances. A single interceptor
         *     or multiple interceptors of different types can be passed in.
         * @returns { boolean } Whether the interceptor is added successfully. The value **true** indicates that the
         *     interceptor is successfully added, and the value **false** indicates the opposite.
         * @throws { BusinessError } 2300801 - Parameter type not supported by the interceptor.
         * @throws { BusinessError } 2300802 - Duplicated interceptor type in the chain.
         * @throws { BusinessError } 2300999 - Internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 22
         */
        public addChain(chain: HttpInterceptor[]): boolean;
        /**
         * Adds an interceptor chain to the target HTTP request. Each HTTP request instance can have only one interceptor
         * chain attached.
         *
         * > **NOTE**
         * >
         * > After an interceptor chain is attached to an [HttpRequest]{@link http.HttpRequest} instance, when the instance
         * > initiates an HTTP request, interceptors of the corresponding type in the attached interceptor chain are
         * > triggered.
         *
         * > For more information about how to trigger interceptors using HTTP requests, see
         * > [HTTP Interceptor Function Code Example](docroot://network/http-request.md#http-interceptor).
         *
         * > The HTTP interceptor feature is supported only by
         * > [HttpRequest.request]{@link http.HttpRequest.request(url: string, callback: AsyncCallback<HttpResponse>)} APIs,
         * > and is not supported by
         * > [HttpRequest.requestInStream]{@link http.HttpRequest.requestInStream(url: string, callback: AsyncCallback<number>)}
         * > APIs (streaming transmission).
         *
         * @param { HttpRequest } httpRequest - [HttpRequest]{@link http.HttpRequest} that initiates an HTTP request.
         * @returns { boolean } Whether the interceptor is attached successfully. The value **true** indicates that the
         *     interceptor is successfully added, and the value **false** indicates the opposite.
         * @throws { BusinessError } 2300801 - Parameter type not supported by the interceptor.
         * @throws { BusinessError } 2300999 - Internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 22
         */
        public apply(httpRequest: HttpRequest): boolean;
    }
    /**
     * Represents the credential used for server identity verification in a session, including the user name and password.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @atomicservice
     * @since 18
     */
    export interface Credential {
        /**
         * Username of credential. Default is ''.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 18
         */
        username: string;
        /**
         * Password of credential. Default is ''.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 18
         */
        password: string;
    }
    /**
     * Defines the TLS configuration, including the version and cipher suite.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @atomicservice
     * @since 18
     */
    export interface TlsConfig {
        /**
         * Earliest TLS version.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 18
         */
        tlsVersionMin: TlsVersion;
        /**
         * Latest TLS version.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 18
         */
        tlsVersionMax: TlsVersion;
        /**
         * Array of cipher suite types. If no cipher suite type is set, all supported cipher suite types are carried by
         * default. For details about the cipher suite types, see
         * [TlsV13SpecificCipherSuite]{@link http.TlsV13SpecificCipherSuite},
         * [TlsV12SpecificCipherSuite]{@link http.TlsV12SpecificCipherSuite} and
         * [TlsV10SpecificCipherSuite]{@link http.TlsV10SpecificCipherSuite}.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 18
         */
        cipherSuites?: CipherSuite[];
    }
    /**
     * Enumerates cipher suites supported by TLS 1.3 or later.
     *
     * @unionmember { 'TLS_AES_128_GCM_SHA256' } Supported cipher suite: TLS_AES_128_GCM_SHA256. The value is a string.
     * @unionmember { 'TLS_AES_256_GCM_SHA384' } Supported cipher suite: TLS_AES_256_GCM_SHA384. The value is a string.
     * @unionmember { 'TLS_CHACHA20_POLY1305_SHA256' } Supported cipher suite: TLS_CHACHA20_POLY1305_SHA256. The value is
     *     a string.
     * @syscap SystemCapability.Communication.NetStack
     * @atomicservice
     * @since 18
     */
    export type TlsV13SpecificCipherSuite = 'TLS_AES_128_GCM_SHA256' | 'TLS_AES_256_GCM_SHA384' | 'TLS_CHACHA20_POLY1305_SHA256';
    /**
     * Enumerates cipher suites supported by TLS 1.2 or later.
     *
     * @unionmember { 'TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256' } Supported cipher suite: TLS_ECDHE_ECDSA_WITH_AES_128
     *     _GCM_SHA256. The value is a string.
     * @unionmember { 'TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256' } Supported cipher suite: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA
     *     256. The value is a string.
     * @unionmember { 'TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384' } Supported cipher suite: TLS_ECDHE_ECDSA_WITH_AES_256
     *     _GCM_SHA384. The value is a string.
     * @unionmember { 'TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384' } Supported cipher suite: TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA
     *     384. The value is a string.
     * @unionmember { 'TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256' } Supported cipher suite:
     *     TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256. The value is a string.
     * @unionmember { 'TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256' } Supported cipher suite: TLS_ECDHE_RSA_WITH_CHACHA20
     *     _POLY1305_SHA256. The value is a string.
     * @unionmember { 'TLS_RSA_WITH_AES_128_GCM_SHA256' } Supported cipher suite: TLS_RSA_WITH_AES_128_GCM_SHA256. The
     *     value is a string.
     * @unionmember { 'TLS_RSA_WITH_AES_256_GCM_SHA384' } Supported cipher suite: TLS_RSA_WITH_AES_256_GCM_SHA384. The
     *     value is a string.
     * @syscap SystemCapability.Communication.NetStack
     * @atomicservice
     * @since 18
     */
    export type TlsV12SpecificCipherSuite = 'TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256' | 'TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256' | 'TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384' | 'TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384' | 'TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256' | 'TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256' | 'TLS_RSA_WITH_AES_128_GCM_SHA256' | 'TLS_RSA_WITH_AES_256_GCM_SHA384';
    /**
     * Enumerates cipher suites supported by TLS 1.0 or later.
     *
     * @unionmember { 'TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA' } Supported cipher suite: TLS_ECDHE_ECDSA_WITH_AES_128
     *     _CBC_SHA. The value is a string.
     * @unionmember { 'TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA' } Supported cipher suite: TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA.
     *     The value is a string.
     * @unionmember { 'TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA' } Supported cipher suite: TLS_ECDHE_ECDSA_WITH_AES_256
     *     _CBC_SHA. The value is a string.
     * @unionmember { 'TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA' } Supported cipher suite: TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA.
     *     The value is a string.
     * @unionmember { 'TLS_RSA_WITH_AES_128_CBC_SHA' } Supported cipher suite: TLS_RSA_WITH_AES_128_CBC_SHA. The value is
     *     a string.
     * @unionmember { 'TLS_RSA_WITH_AES_256_CBC_SHA' } Supported cipher suite: TLS_RSA_WITH_AES_256_CBC_SHA. The value is
     *     a string.
     * @unionmember { 'TLS_RSA_WITH_3DES_EDE_CBC_SHA' } Supported cipher suite: TLS_RSA_WITH_3DES_EDE_CBC_SHA. The value
     *     is a string.
     * @syscap SystemCapability.Communication.NetStack
     * @atomicservice
     * @since 18
     */
    export type TlsV10SpecificCipherSuite = 'TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA' | 'TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA' | 'TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA' | 'TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA' | 'TLS_RSA_WITH_AES_128_CBC_SHA' | 'TLS_RSA_WITH_AES_256_CBC_SHA' | 'TLS_RSA_WITH_3DES_EDE_CBC_SHA';
    /**
     * Declares the cipher suite.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @atomicservice
     * @since 18
     */
    export type CipherSuite = TlsV13CipherSuite;
    /**
     * Declares the cipher suite for TLS 1.3, which is also compatible with TLS 1.2.
     *
     * @unionmember { TlsV12CipherSuite } [TlsV11CipherSuite]{@link http.TlsV11CipherSuite}.
     * @unionmember { TlsV13SpecificCipherSuite } [TlsV13SpecificCipherSuite]{@link http.TlsV13SpecificCipherSuite}.
     * @syscap SystemCapability.Communication.NetStack
     * @atomicservice
     * @since 18
     */
    export type TlsV13CipherSuite = TlsV12CipherSuite | TlsV13SpecificCipherSuite;
    /**
     * Declares the cipher suite for TLS 1.2, which is also compatible with TLS 1.1.
     *
     * @unionmember { TlsV11CipherSuite } [TlsV11CipherSuite]{@link http.TlsV11CipherSuite}.
     * @unionmember { TlsV12SpecificCipherSuite } [TlsV12SpecificCipherSuite]{@link http.TlsV12SpecificCipherSuite}.
     * @syscap SystemCapability.Communication.NetStack
     * @atomicservice
     * @since 18
     */
    export type TlsV12CipherSuite = TlsV11CipherSuite | TlsV12SpecificCipherSuite;
    /**
     * Declares the cipher suite for TLS 1.1, which is the same as that for TLS1.0.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @atomicservice
     * @since 18
     */
    export type TlsV11CipherSuite = TlsV10CipherSuite;
    /**
     * Declares the cipher suite for TLS 1.0.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @atomicservice
     * @since 18
     */
    export type TlsV10CipherSuite = TlsV10SpecificCipherSuite;
    /**
     * Enumerates TLS versions.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @atomicservice
     * @since 18
     */
    export enum TlsVersion {
        /**
         * TLS version 1.0.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 18
         */
        TLS_V_1_0 = 4,
        /**
         * TLS version 1.1.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 18
         */
        TLS_V_1_1 = 5,
        /**
         * TLS version 1.2.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 18
         */
        TLS_V_1_2 = 6,
        /**
         * TLS version 1.3.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @atomicservice
         * @since 18
         */
        TLS_V_1_3 = 7
    }
    /**
     * Defines the type of multi-form data.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 12]
     * @since 11
     */
    export interface MultiFormData {
        /**
         * Data name.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        name: string;
        /**
         * Data type, for example, **text/plain**, **image/png**, **image/jpeg**, **audio/mpeg**, or **video/mp4**.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        contentType: string;
        /**
         * Name of the file uploaded to the server.
         *
         * **Note**: If this field is specified, the **filename** field is added to the request header, indicating the name
         * of the file uploaded to the server.
         *
         * (1) If the data to be uploaded is a file and the file content is specified via the **data** field, the
         * **remoteFileName** field usually needs to be set to specify the name of the file to be uploaded to the server (
         * the actual result depends on the server). If the file path is specified via the **filePath** field, the
         * **filename** field will be automatically added to the request header. Its default value is the file name in the
         * **filePath** field. If a different name is required, it can also be changed via this field.
         *
         * (2) When the data to be uploaded is in binary format, the **remoteFileName** field must be set.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        remoteFileName?: string;
        /**
         * Form data content.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        data?: string | Object | ArrayBuffer;
        /**
         * File path of the form data. If **data** is not specified, **filePath** must be set.
         *
         * **Note**: The file format supported by the file management module must be passed. You can call
         * [access]{@link @ohos.file.fs:access} to check whether the file exists and is accessible.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        filePath?: string;
    }
    /**
     * Enumerates certificate types.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 12]
     * @since 11
     */
    export enum CertType {
        /**
         * PEM certificate.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        PEM = 'PEM',
        /**
         * DER certificate.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        DER = 'DER',
        /**
         * P12 certificate.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        P12 = 'P12'
    }
    /**
     * Enumerates IP address families of the target domain name.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @since 15
     */
    export enum AddressFamily {
        /**
         * Automatically selects the IPv4 or IPv6 address of the target domain name.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @since 15
         */
        DEFAULT = 'CURL_IPRESOLVE_WHATEVER',
        /**
         * Resolves only the IPv4 address of the target domain name and ignores the IPv6 address.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @since 15
         */
        ONLY_V4 = 'CURL_IPRESOLVE_V4',
        /**
         * Resolves only the IPv6 address of the target domain name and ignores the IPv4 address.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @since 15
         */
        ONLY_V6 = 'CURL_IPRESOLVE_V6'
    }
    /**
     * Defines the client certificate type.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 12]
     * @since 11
     */
    export interface ClientCert {
        /**
         * Path of the certificate file.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        certPath: string;
        /**
         * Certificate type. The default value is **PEM**.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        certType?: CertType;
        /**
         * Path of the certificate key file.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        keyPath: string;
        /**
         * Password of the certificate key file. The default value is an empty string.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        keyPassword?: string;
    }
    /**
     * Defines the dynamic configuration of certificate pinning.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @since 12
     */
    interface CertificatePinning {
        /**
         * Certificate PIN of the string type.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @since 12
         */
        publicKeyHash: string;
        /**
         * Encryption algorithm. Currently, only SHA-256 is supported.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @since 12
         */
        hashAlgorithm: 'SHA-256';
    }
    /**
     * Defines an HTTP request task. Before invoking APIs provided by **HttpRequest**, you must call
     * [createHttp()]{@link http.createHttp} to create an **HttpRequestTask** object.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 6
     */
    export interface HttpRequest {
        /**
         * Initiates an HTTP request to a given URL. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > (1) This API can receive only data whose size is less than 5 MB. If the data size exceeds 5 MB, you need to set
         * > **maxLimit** to a larger value in [HttpRequestOptions]{@link http.HttpRequestOptions} or call
         * > [requestInStream]{@link http.HttpRequest.requestInStream(url: string, callback: AsyncCallback<number>)} to
         * > initiate a streaming request. Since API version 23, this API can receive a maximum of 50 MB data. In versions
         * > earlier than API version 23, this API can receive a maximum of 5 MB data, and any data exceeding this threshold
         * > will fail to be received.
         *
         * > (2) If you need to pass in cookies, add them to the **options** parameter.
         *
         * > (3) If the URL contains non-English characters, call **encodeURL(url)** to encode the URL before initiating an
         * > HTTP request.
         *
         * @permission ohos.permission.INTERNET
         * @param { string } url - URL for initiating an HTTP request.
         * @param { AsyncCallback<HttpResponse> } callback - Callback used to return the result.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2300001 - Unsupported protocol.
         * @throws { BusinessError } 2300003 - Invalid URL format or missing URL.
         * @throws { BusinessError } 2300005 - Failed to resolve the proxy name.
         * @throws { BusinessError } 2300006 - Failed to resolve the host name.
         * @throws { BusinessError } 2300007 - Failed to connect to the server.
         * @throws { BusinessError } 2300008 - Invalid server response.
         * @throws { BusinessError } 2300009 - Access to the remote resource denied.
         * @throws { BusinessError } 2300016 - Error in the HTTP2 framing layer.
         * @throws { BusinessError } 2300018 - Transferred a partial file.
         * @throws { BusinessError } 2300023 - Failed to write the received data to the disk or application.
         * @throws { BusinessError } 2300025 - Upload failed.
         * @throws { BusinessError } 2300026 - Failed to open or read local data from the file or application.
         * @throws { BusinessError } 2300027 - Out of memory.
         * @throws { BusinessError } 2300028 - Operation timeout.
         * @throws { BusinessError } 2300047 - The number of redirections reaches the maximum allowed.
         * @throws { BusinessError } 2300052 - The server returned nothing (no header or data).
         * @throws { BusinessError } 2300055 - Failed to send data to the peer.
         * @throws { BusinessError } 2300056 - Failed to receive data from the peer.
         * @throws { BusinessError } 2300058 - Local SSL certificate error.
         * @throws { BusinessError } 2300059 - The specified SSL cipher cannot be used.
         * @throws { BusinessError } 2300060 - Invalid SSL peer certificate or SSH remote key.
         * @throws { BusinessError } 2300061 - Invalid HTTP encoding format.
         * @throws { BusinessError } 2300063 - Maximum file size exceeded.
         * @throws { BusinessError } 2300070 - Remote disk full.
         * @throws { BusinessError } 2300073 - Remote file already exists.
         * @throws { BusinessError } 2300077 - The SSL CA certificate does not exist or is inaccessible.
         * @throws { BusinessError } 2300078 - Remote file not found.
         * @throws { BusinessError } 2300094 - Authentication error.
         * @throws { BusinessError } 2300999 - Internal error.
         * @throws { BusinessError } 2300998 - It is not allowed to access this domain. [since 12]
         * @throws { BusinessError } 2300997 - Cleartext traffic not permitted. [since 18]
         * @throws { BusinessError } 2300996 - The request was intercepted by the HTTP global
         *     interceptor. [since 26.0.0]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        request(url: string, callback: AsyncCallback<HttpResponse>): void;
        /**
         * Initiates an HTTP request containing specified options to a given URL. This API uses an asynchronous callback to
         * return the result.
         *
         * > **NOTE**
         * >
         * > (1) This API can receive only data whose size is less than 5 MB. If the data size exceeds 5 MB, you need to set
         * > **maxLimit** to a larger value in [HttpRequestOptions]{@link http.HttpRequestOptions} or call
         * > [requestInStream]{@link http.HttpRequest.requestInStream(url: string, callback: AsyncCallback<number>)} to
         * > initiate a streaming request. Since API version 23, this API can receive a maximum of 50 MB data. In versions
         * > earlier than API version 23, this API can receive a maximum of 5 MB data, and any data exceeding this threshold
         * > will fail to be received.
         *
         * > (2) If you need to pass in cookies, add them to the **options** parameter.
         *
         * > (3) If the URL contains non-English characters, call **encodeURL(url)** to encode the URL before initiating an
         * > HTTP request.
         *
         * @permission ohos.permission.INTERNET
         * @param { string } url - URL for initiating an HTTP request.
         * @param { HttpRequestOptions } options - Request options. For details, see
         *     [HttpRequestOptions]{@link http.HttpRequestOptions}.
         * @param { AsyncCallback<HttpResponse> } callback - Callback used to return the result. If the operation is
         *     successful, the callback content is an [HttpResponse]{@link http.HttpResponse} object; otherwise, the
         *     callback content is undefined.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2300001 - Unsupported protocol.
         * @throws { BusinessError } 2300003 - Invalid URL format or missing URL.
         * @throws { BusinessError } 2300005 - Failed to resolve the proxy name.
         * @throws { BusinessError } 2300006 - Failed to resolve the host name.
         * @throws { BusinessError } 2300007 - Failed to connect to the server.
         * @throws { BusinessError } 2300008 - Invalid server response.
         * @throws { BusinessError } 2300009 - Access to the remote resource denied.
         * @throws { BusinessError } 2300016 - Error in the HTTP2 framing layer.
         * @throws { BusinessError } 2300018 - Transferred a partial file.
         * @throws { BusinessError } 2300023 - Failed to write the received data to the disk or application.
         * @throws { BusinessError } 2300025 - Upload failed.
         * @throws { BusinessError } 2300026 - Failed to open or read local data from the file or application.
         * @throws { BusinessError } 2300027 - Out of memory.
         * @throws { BusinessError } 2300028 - Operation timeout.
         * @throws { BusinessError } 2300047 - The number of redirections reaches the maximum allowed.
         * @throws { BusinessError } 2300052 - The server returned nothing (no header or data).
         * @throws { BusinessError } 2300055 - Failed to send data to the peer.
         * @throws { BusinessError } 2300056 - Failed to receive data from the peer.
         * @throws { BusinessError } 2300058 - Local SSL certificate error.
         * @throws { BusinessError } 2300059 - The specified SSL cipher cannot be used.
         * @throws { BusinessError } 2300060 - Invalid SSL peer certificate or SSH remote key.
         * @throws { BusinessError } 2300061 - Invalid HTTP encoding format.
         * @throws { BusinessError } 2300063 - Maximum file size exceeded.
         * @throws { BusinessError } 2300070 - Remote disk full.
         * @throws { BusinessError } 2300073 - Remote file already exists.
         * @throws { BusinessError } 2300077 - The SSL CA certificate does not exist or is inaccessible.
         * @throws { BusinessError } 2300078 - Remote file not found.
         * @throws { BusinessError } 2300094 - Authentication error.
         * @throws { BusinessError } 2300999 - Internal error.
         * @throws { BusinessError } 2300998 - It is not allowed to access this domain. [since 12]
         * @throws { BusinessError } 2300997 - Cleartext traffic not permitted. [since 18]
         * @throws { BusinessError } 2300996 - The request was intercepted by the HTTP global
         *     interceptor. [since 26.0.0]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        request(url: string, options: HttpRequestOptions, callback: AsyncCallback<HttpResponse>): void;
        /**
         * Initiates an HTTP request containing specified options to a given URL. This API uses a promise to return the
         * result.
         *
         * > **NOTE**
         * >
         * > (1) This API can receive only data whose size is less than 5 MB. If the data size exceeds 5 MB, you need to set
         * > **maxLimit** to a larger value in [HttpRequestOptions]{@link http.HttpRequestOptions} or call
         * > [requestInStream]{@link http.HttpRequest.requestInStream(url: string, callback: AsyncCallback<number>)} to
         * > initiate a streaming request. Since API version 23, this API can receive a maximum of 50 MB data. In versions
         * > earlier than API version 23, this API can receive a maximum of 5 MB data, and any data exceeding this threshold
         * > will fail to be received.
         *
         * > (2) If you need to pass in cookies, add them to the **options** parameter.
         *
         * > (3) If the URL contains non-English characters, call **encodeURL(url)** to encode the URL before initiating an
         * > HTTP request.
         *
         * @permission ohos.permission.INTERNET
         * @param { string } url - URL for initiating an HTTP request.
         * @param { HttpRequestOptions } [options] - Request options. For details, see
         *     [HttpRequestOptions]{@link http.HttpRequestOptions}.
         * @returns { Promise<HttpResponse> } Promise used to return the result.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2300001 - Unsupported protocol.
         * @throws { BusinessError } 2300003 - Invalid URL format or missing URL.
         * @throws { BusinessError } 2300005 - Failed to resolve the proxy name.
         * @throws { BusinessError } 2300006 - Failed to resolve the host name.
         * @throws { BusinessError } 2300007 - Failed to connect to the server.
         * @throws { BusinessError } 2300008 - Invalid server response.
         * @throws { BusinessError } 2300009 - Access to the remote resource denied.
         * @throws { BusinessError } 2300016 - Error in the HTTP2 framing layer.
         * @throws { BusinessError } 2300018 - Transferred a partial file.
         * @throws { BusinessError } 2300023 - Failed to write the received data to the disk or application.
         * @throws { BusinessError } 2300025 - Upload failed.
         * @throws { BusinessError } 2300026 - Failed to open or read local data from the file or application.
         * @throws { BusinessError } 2300027 - Out of memory.
         * @throws { BusinessError } 2300028 - Operation timeout.
         * @throws { BusinessError } 2300047 - The number of redirections reaches the maximum allowed.
         * @throws { BusinessError } 2300052 - The server returned nothing (no header or data).
         * @throws { BusinessError } 2300055 - Failed to send data to the peer.
         * @throws { BusinessError } 2300056 - Failed to receive data from the peer.
         * @throws { BusinessError } 2300058 - Local SSL certificate error.
         * @throws { BusinessError } 2300059 - The specified SSL cipher cannot be used.
         * @throws { BusinessError } 2300060 - Invalid SSL peer certificate or SSH remote key.
         * @throws { BusinessError } 2300061 - Invalid HTTP encoding format.
         * @throws { BusinessError } 2300063 - Maximum file size exceeded.
         * @throws { BusinessError } 2300070 - Remote disk full.
         * @throws { BusinessError } 2300073 - Remote file already exists.
         * @throws { BusinessError } 2300077 - The SSL CA certificate does not exist or is inaccessible.
         * @throws { BusinessError } 2300078 - Remote file not found.
         * @throws { BusinessError } 2300094 - Authentication error.
         * @throws { BusinessError } 2300999 - Internal error.
         * @throws { BusinessError } 2300998 - It is not allowed to access this domain. [since 12]
         * @throws { BusinessError } 2300997 - Cleartext traffic not permitted. [since 18]
         * @throws { BusinessError } 2300996 - The request was intercepted by the HTTP global
         *     interceptor. [since 26.0.0]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        request(url: string, options?: HttpRequestOptions): Promise<HttpResponse>;
        /**
         * Initiates an HTTP network request based on the URL and related configuration options (optional). This API returns
         * the response synchronously.
         *
         * > **NOTE**
         * >
         * > (1) This API can receive data of up to 50 MB. To receive more than 50 MB of data, set the **maxLimit**
         * > parameter in [HttpRequestOptions]{@link http.HttpRequestOptions}.
         *
         * > (2) If you need to pass in cookies, add them to the **options** parameter.
         *
         * > (3) If the URL contains non-English characters, call **encodeURL(url)** to encode the URL before initiating an
         * > HTTP request.
         *
         * > (4) This API is synchronous and blocks the current thread until an HTTP response or error code is returned.
         *
         * **Required permission**: ohos.permission.INTERNET
         *
         * @permission ohos.permission.INTERNET
         * @param { string } url - URL for initiating an HTTP request.
         * @param { HttpRequestOptions } [options] - Request options. For details, see
         *     [HttpRequestOptions]{@link http.HttpRequestOptions}.
         * @returns { HttpResponse } HTTP request response result that is returned synchronously.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2300001 - Unsupported protocol.
         * @throws { BusinessError } 2300003 - Invalid URL format or missing URL.
         * @throws { BusinessError } 2300005 - Failed to resolve the proxy name.
         * @throws { BusinessError } 2300006 - Failed to resolve the host name.
         * @throws { BusinessError } 2300007 - Failed to connect to the server.
         * @throws { BusinessError } 2300008 - Invalid server response.
         * @throws { BusinessError } 2300009 - Access to the remote resource denied.
         * @throws { BusinessError } 2300016 - Error in the HTTP2 framing layer.
         * @throws { BusinessError } 2300018 - Transferred a partial file.
         * @throws { BusinessError } 2300023 - Failed to write the received data to the disk or application.
         * @throws { BusinessError } 2300025 - Upload failed.
         * @throws { BusinessError } 2300026 - Failed to open or read local data from the file or application.
         * @throws { BusinessError } 2300027 - Out of memory.
         * @throws { BusinessError } 2300028 - Operation timeout.
         * @throws { BusinessError } 2300047 - The number of redirections reaches the maximum allowed.
         * @throws { BusinessError } 2300052 - The server returned nothing (no header or data).
         * @throws { BusinessError } 2300055 - Failed to send data to the peer.
         * @throws { BusinessError } 2300056 - Failed to receive data from the peer.
         * @throws { BusinessError } 2300058 - Local SSL certificate error.
         * @throws { BusinessError } 2300059 - The specified SSL cipher cannot be used.
         * @throws { BusinessError } 2300060 - Invalid SSL peer certificate or SSH remote key.
         * @throws { BusinessError } 2300061 - Invalid HTTP encoding format.
         * @throws { BusinessError } 2300063 - Maximum file size exceeded.
         * @throws { BusinessError } 2300070 - Remote disk full.
         * @throws { BusinessError } 2300073 - Remote file already exists.
         * @throws { BusinessError } 2300077 - The SSL CA certificate does not exist or is inaccessible.
         * @throws { BusinessError } 2300078 - Remote file not found.
         * @throws { BusinessError } 2300094 - Authentication error.
         * @throws { BusinessError } 2300996 - The request was intercepted by the HTTP global interceptor.
         * @throws { BusinessError } 2300997 - Cleartext traffic not permitted.
         * @throws { BusinessError } 2300998 - It is not allowed to access this domain.
         * @throws { BusinessError } 2300999 - Internal error.
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @crossplatform
         * @since 26.0.0
         */
        requestSync(url: string, options?: HttpRequestOptions): HttpResponse;
        /**
         * Initiates an HTTP request containing specified options to a given URL. This API uses an asynchronous callback to
         * return the result, which is a streaming response.
         *
         * @permission ohos.permission.INTERNET
         * @param { string } url - URL for initiating an HTTP request.
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the request is successful,
         *     **err** is **undefined**, and the HTTP result code is returned. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2300001 - Unsupported protocol.
         * @throws { BusinessError } 2300003 - Invalid URL format or missing URL.
         * @throws { BusinessError } 2300005 - Failed to resolve the proxy name.
         * @throws { BusinessError } 2300006 - Failed to resolve the host name.
         * @throws { BusinessError } 2300007 - Failed to connect to the server.
         * @throws { BusinessError } 2300008 - Invalid server response.
         * @throws { BusinessError } 2300009 - Access to the remote resource denied.
         * @throws { BusinessError } 2300016 - Error in the HTTP2 framing layer.
         * @throws { BusinessError } 2300018 - Transferred a partial file.
         * @throws { BusinessError } 2300023 - Failed to write the received data to the disk or application.
         * @throws { BusinessError } 2300025 - Upload failed.
         * @throws { BusinessError } 2300026 - Failed to open or read local data from the file or application.
         * @throws { BusinessError } 2300027 - Out of memory.
         * @throws { BusinessError } 2300028 - Operation timeout.
         * @throws { BusinessError } 2300047 - The number of redirections reaches the maximum allowed.
         * @throws { BusinessError } 2300052 - The server returned nothing (no header or data).
         * @throws { BusinessError } 2300055 - Failed to send data to the peer.
         * @throws { BusinessError } 2300056 - Failed to receive data from the peer.
         * @throws { BusinessError } 2300058 - Local SSL certificate error.
         * @throws { BusinessError } 2300059 - The specified SSL cipher cannot be used.
         * @throws { BusinessError } 2300060 - Invalid SSL peer certificate or SSH remote key.
         * @throws { BusinessError } 2300061 - Invalid HTTP encoding format.
         * @throws { BusinessError } 2300063 - Maximum file size exceeded.
         * @throws { BusinessError } 2300070 - Remote disk full.
         * @throws { BusinessError } 2300073 - Remote file already exists.
         * @throws { BusinessError } 2300077 - The SSL CA certificate does not exist or is inaccessible.
         * @throws { BusinessError } 2300078 - Remote file not found.
         * @throws { BusinessError } 2300094 - Authentication error.
         * @throws { BusinessError } 2300999 - Internal error.
         * @throws { BusinessError } 2300998 - It is not allowed to access this domain. [since 12]
         * @throws { BusinessError } 2300997 - Cleartext traffic not permitted. [since 18]
         * @throws { BusinessError } 2300996 - The request was intercepted by the HTTP global
         *     interceptor. [since 26.0.0]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 18]
         * @atomicservice [since 15]
         * @since 10
         */
        requestInStream(url: string, callback: AsyncCallback<number>): void;
        /**
         * Initiates an HTTP request containing specified options to a given URL. This API uses an asynchronous callback to
         * return the result, which is a streaming response.
         *
         * @permission ohos.permission.INTERNET
         * @param { string } url - URL for initiating an HTTP request.
         * @param { HttpRequestOptions } options - Request options. For details, see
         *     [HttpRequestOptions]{@link http.HttpRequestOptions}.
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the request is successful,
         *     **err** is **undefined**, and the [HTTP result code]{@link http.ResponseCode} is returned. Otherwise, **err**
         *     is an error object.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2300001 - Unsupported protocol.
         * @throws { BusinessError } 2300003 - Invalid URL format or missing URL.
         * @throws { BusinessError } 2300005 - Failed to resolve the proxy name.
         * @throws { BusinessError } 2300006 - Failed to resolve the host name.
         * @throws { BusinessError } 2300007 - Failed to connect to the server.
         * @throws { BusinessError } 2300008 - Invalid server response.
         * @throws { BusinessError } 2300009 - Access to the remote resource denied.
         * @throws { BusinessError } 2300016 - Error in the HTTP2 framing layer.
         * @throws { BusinessError } 2300018 - Transferred a partial file.
         * @throws { BusinessError } 2300023 - Failed to write the received data to the disk or application.
         * @throws { BusinessError } 2300025 - Upload failed.
         * @throws { BusinessError } 2300026 - Failed to open or read local data from the file or application.
         * @throws { BusinessError } 2300027 - Out of memory.
         * @throws { BusinessError } 2300028 - Operation timeout.
         * @throws { BusinessError } 2300047 - The number of redirections reaches the maximum allowed.
         * @throws { BusinessError } 2300052 - The server returned nothing (no header or data).
         * @throws { BusinessError } 2300055 - Failed to send data to the peer.
         * @throws { BusinessError } 2300056 - Failed to receive data from the peer.
         * @throws { BusinessError } 2300058 - Local SSL certificate error.
         * @throws { BusinessError } 2300059 - The specified SSL cipher cannot be used.
         * @throws { BusinessError } 2300060 - Invalid SSL peer certificate or SSH remote key.
         * @throws { BusinessError } 2300061 - Invalid HTTP encoding format.
         * @throws { BusinessError } 2300063 - Maximum file size exceeded.
         * @throws { BusinessError } 2300070 - Remote disk full.
         * @throws { BusinessError } 2300073 - Remote file already exists.
         * @throws { BusinessError } 2300077 - The SSL CA certificate does not exist or is inaccessible.
         * @throws { BusinessError } 2300078 - Remote file not found.
         * @throws { BusinessError } 2300094 - Authentication error.
         * @throws { BusinessError } 2300999 - Internal error.
         * @throws { BusinessError } 2300998 - It is not allowed to access this domain. [since 12]
         * @throws { BusinessError } 2300997 - Cleartext traffic not permitted. [since 18]
         * @throws { BusinessError } 2300996 - The request was intercepted by the HTTP global
         *     interceptor. [since 26.0.0]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 18]
         * @atomicservice [since 15]
         * @since 10
         */
        requestInStream(url: string, options: HttpRequestOptions, callback: AsyncCallback<number>): void;
        /**
         * Initiates an HTTP request containing specified options to a given URL. This API uses a promise to return the
         * result, which is a streaming response.
         *
         * @permission ohos.permission.INTERNET
         * @param { string } url - URL for initiating an HTTP request.
         * @param { HttpRequestOptions } [options] - Request options. For details, see
         *     [HttpRequestOptions]{@link http.HttpRequestOptions}.
         * @returns { Promise<number> } Promise used to return the [result]{@link http.ResponseCode}.
         * @throws { BusinessError } 401 - Parameter error.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 2300001 - Unsupported protocol.
         * @throws { BusinessError } 2300003 - Invalid URL format or missing URL.
         * @throws { BusinessError } 2300005 - Failed to resolve the proxy name.
         * @throws { BusinessError } 2300006 - Failed to resolve the host name.
         * @throws { BusinessError } 2300007 - Failed to connect to the server.
         * @throws { BusinessError } 2300008 - Invalid server response.
         * @throws { BusinessError } 2300009 - Access to the remote resource denied.
         * @throws { BusinessError } 2300016 - Error in the HTTP2 framing layer.
         * @throws { BusinessError } 2300018 - Transferred a partial file.
         * @throws { BusinessError } 2300023 - Failed to write the received data to the disk or application.
         * @throws { BusinessError } 2300025 - Upload failed.
         * @throws { BusinessError } 2300026 - Failed to open or read local data from the file or application.
         * @throws { BusinessError } 2300027 - Out of memory.
         * @throws { BusinessError } 2300028 - Operation timeout.
         * @throws { BusinessError } 2300047 - The number of redirections reaches the maximum allowed.
         * @throws { BusinessError } 2300052 - The server returned nothing (no header or data).
         * @throws { BusinessError } 2300055 - Failed to send data to the peer.
         * @throws { BusinessError } 2300056 - Failed to receive data from the peer.
         * @throws { BusinessError } 2300058 - Local SSL certificate error.
         * @throws { BusinessError } 2300059 - The specified SSL cipher cannot be used.
         * @throws { BusinessError } 2300060 - Invalid SSL peer certificate or SSH remote key.
         * @throws { BusinessError } 2300061 - Invalid HTTP encoding format.
         * @throws { BusinessError } 2300063 - Maximum file size exceeded.
         * @throws { BusinessError } 2300070 - Remote disk full.
         * @throws { BusinessError } 2300073 - Remote file already exists.
         * @throws { BusinessError } 2300077 - The SSL CA certificate does not exist or is inaccessible.
         * @throws { BusinessError } 2300078 - Remote file not found.
         * @throws { BusinessError } 2300094 - Authentication error.
         * @throws { BusinessError } 2300999 - Internal error.
         * @throws { BusinessError } 2300998 - It is not allowed to access this domain. [since 12]
         * @throws { BusinessError } 2300997 - Cleartext traffic not permitted. [since 18]
         * @throws { BusinessError } 2300996 - The request was intercepted by the HTTP global
         *     interceptor. [since 26.0.0]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 18]
         * @atomicservice [since 15]
         * @since 10
         */
        requestInStream(url: string, options?: HttpRequestOptions): Promise<number>;
        /**
         * Stops an HTTP request task and releases system resources.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        destroy(): void;
        /**
         * Registers an observer for HTTP Response Header events.
         *
         * @param { "headerReceive" } type - Event type. The value is **headerReceive**.
         * @param { AsyncCallback<Object> } callback - Callback used to return the result. If the operation is successful,
         *     **error** is **undefined**, and **data** is the received HTTP response header. Otherwise, **error** is an
         *     error object.
         * @syscap SystemCapability.Communication.NetStack
         * @since 6
         * @deprecated since 8
         * @useinstead on_headersReceive
         */
        on(type: "headerReceive", callback: AsyncCallback<Object>): void;
        /**
         * Unregisters the observer for HTTP Response Header events.
         *
         * @param { "headerReceive" } type - Event type. The value is **headerReceive**.
         * @param { AsyncCallback<Object> } [callback] - Callback used to return the result. You can pass the callback of
         *     the **on** function if you want to cancel listening for a certain type of events. If you do not pass the
         *     callback, you will cancel listening for all events.
         * @syscap SystemCapability.Communication.NetStack
         * @since 6
         * @deprecated since 8
         * @useinstead off_headersReceive
         */
        off(type: "headerReceive", callback?: AsyncCallback<Object>): void;
        /**
         * Registers an observer for HTTP Response Header events.
         *
         * @param { "headersReceive" } type - Event type. The value is **headersReceive**.
         * @param { Callback<Object> } callback - Callback used to return the HTTP response header.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        on(type: "headersReceive", callback: Callback<Object>): void;
        /**
         * Unregisters the observer for HTTP Response Header events.
         *
         * @param { "headersReceive" } type - Event type. The value is **headersReceive**.
         * @param { Callback<Object> } callback - Callback used to return the result. You can pass the callback of the
         *     **on** function if you want to cancel listening for a certain type of events. If you do not pass the
         *     callback, you will cancel listening for all events. [since 8 - 10]
         * @param { Callback<Object> } [callback] - Callback used to return the result. You can pass the callback of the
         *     **on** function if you want to cancel listening for a certain type of events. If you do not pass the
         *     callback, you will cancel listening for all events. [since 11]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        off(type: "headersReceive", callback?: Callback<Object>): void;
        /**
         * Registers a one-time observer for HTTP Response Header events. Once triggered, the observer will be removed. This
         * API uses an asynchronous callback to return the result.
         *
         * @param { "headersReceive" } type - Event type. The value is **headersReceive**.
         * @param { Callback<Object> } callback - Callback used to return the HTTP response header.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 15]
         * @since 8
         */
        once(type: "headersReceive", callback: Callback<Object>): void;
        /**
         * Registers an observer for events indicating receiving of HTTP streaming responses.
         *
         * @param { "dataReceive" } type - Event type. The value is **dataReceive**.
         * @param { Callback<ArrayBuffer> } callback - Callback used to return the result. If the operation is successful,
         *     **error** is **undefined**, and **data** is the received HTTP streaming data of the ArrayBuffer type.
         *     Otherwise, **error** is an error object.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 18]
         * @atomicservice [since 15]
         * @since 10
         */
        on(type: "dataReceive", callback: Callback<ArrayBuffer>): void;
        /**
         * Unregisters the observer for events indicating receiving of HTTP streaming responses.
         *
         * @param { "dataReceive" } type - Event type. The value is **dataReceive**.
         * @param { Callback<ArrayBuffer> } [callback] - Callback used to return the result. You can pass the callback of
         *     the **on** function if you want to cancel listening for a certain type of events. If you do not pass the
         *     callback, you will cancel listening for all events.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 18]
         * @atomicservice [since 15]
         * @since 10
         */
        off(type: "dataReceive", callback?: Callback<ArrayBuffer>): void;
        /**
         * Registers an observer for events indicating completion of receiving HTTP streaming responses.
         *
         * @param { "dataEnd" } type - Event type. The value is **dataEnd**.
         * @param { Callback<void> } callback - Callback used to return the result. If the operation is successful, **err**
         *     is **undefined**; otherwise, **err** is an **Error** object.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 18]
         * @atomicservice [since 15]
         * @since 10
         */
        on(type: "dataEnd", callback: Callback<void>): void;
        /**
         * Unregisters the observer for events indicating completion of receiving HTTP streaming responses.
         *
         * @param { "dataEnd" } type - Event type. The value is **dataEnd**.
         * @param { Callback<void> } [callback] - Callback used to return the result. You can pass the callback of the
         *     **on** function if you want to cancel listening for a certain type of events. If you do not pass the
         *     callback, you will cancel listening for all events.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 18]
         * @atomicservice [since 15]
         * @since 10
         */
        off(type: "dataEnd", callback?: Callback<void>): void;
        /**
         * Registers an observer for events indicating progress of receiving HTTP streaming responses.
         *
         * @param { 'dataReceiveProgress' } type - Event type. The value is **dataReceiveProgress**.
         * @param { Callback<{ receiveSize: number, totalSize: number}> } callback - Callback used to return the result. If the
         *     operation is successful, the callback content is a
         *     [DataReceiveProgressInfo]{@link http.DataReceiveProgressInfo} object; otherwise, the callback content is
         *     **undefined**. [since 10 - 10]
         * @param { Callback<DataReceiveProgressInfo> } callback - Callback used to return the result. If the operation is
         *     successful, the callback content is a [DataReceiveProgressInfo]{@link http.DataReceiveProgressInfo} object;
         *     otherwise, the callback content is **undefined**. [since 11]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @atomicservice [since 15]
         * @since 10
         */
        on(type: 'dataReceiveProgress', callback: Callback<DataReceiveProgressInfo>): void;
        /**
         * Unregisters the observer for events indicating progress of receiving HTTP streaming responses.
         *
         * @param { 'dataReceiveProgress' } type - Event type. The value is **dataReceiveProgress**.
         * @param { Callback<{ receiveSize: number, totalSize: number}> } [callback] - Callback used to return the result. You
         *     can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If
         *     you do not pass the callback, you will cancel listening for all events. [since 10 - 10]
         * @param { Callback<DataReceiveProgressInfo> } callback - Callback used to return the result. You can pass the
         *     callback of the **on** function if you want to cancel listening for a certain type of events. If you do not
         *     pass the callback, you will cancel listening for all events. [since 11]
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @atomicservice [since 15]
         * @since 10
         */
        off(type: 'dataReceiveProgress', callback?: Callback<DataReceiveProgressInfo>): void;
        /**
         * Registers an observer for events indicating progress of sending HTTP requests.
         *
         * @param { 'dataSendProgress' } type - Event type. The value is **dataSendProgress**.
         * @param { Callback<DataSendProgressInfo> } callback - Callback used to return the result. If the operation is
         *     successful, the callback content is a [DataSendProgressInfo]{@link http.DataSendProgressInfo} object;
         *     otherwise, the callback content is **undefined**.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @atomicservice [since 15]
         * @since 11
         */
        on(type: 'dataSendProgress', callback: Callback<DataSendProgressInfo>): void;
        /**
         * Unregisters the observer for events indicating progress of sending HTTP requests.
         *
         * @param { 'dataSendProgress' } type - Event type. The value is **dataSendProgress**.
         * @param { Callback<DataSendProgressInfo> } [callback] - Callback used to return the result. You can pass the
         *     callback of the **on** function if you want to cancel listening for a certain type of events. If you do not
         *     pass the callback, you will cancel listening for all events.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @atomicservice [since 15]
         * @since 11
         */
        off(type: 'dataSendProgress', callback?: Callback<DataSendProgressInfo>): void;
        /**
         * Sets whether to automatically carry and share cookies. That is, whether to automatically reuse the cookies
         * delivered by the server among multiple requests of the same **HttpRequest** instance.
         *
         * > **NOTE**
         * >
         * > (1) The default value is **false**, indicating that cookies are not automatically carried.
         *
         * > (2) If the value is changed from **false** to **true**, the setting takes effect when the **request** API is
         * > called to initiate a request, and cookies are automatically shared.
         *
         * > (3) If the value is changed from **true** to **false**, the cookie sharing status stored in the current
         * > instance is cleared.
         *
         * @param { boolean } enable - Whether to automatically carry cookies. **true**: yes; **false**: no.
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 26.0.0
         */
        enableAutoCookie(enable: boolean): void;
    }
    /**
     * Defines an HTTP request method.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 6
     */
    export enum RequestMethod {
        /**
         * Describes the communication options of the target resource.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        OPTIONS = "OPTIONS",
        /**
         * Requests the representation of the specified resource. The GET request should only retrieve data and should not
         * contain the request content.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        GET = "GET",
        /**
         * Requests the same response (but does not have a response body) as the GET request.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        HEAD = "HEAD",
        /**
         * Submits an entity to a specified resource, which usually causes a status change on the server.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        POST = "POST",
        /**
         * Replaces all current representations of the target resource with the requested content.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        PUT = "PUT",
        /**
         * Deletes the specified resource.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        DELETE = "DELETE",
        /**
         * Performs a message loopback test along the path to the target resource.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        TRACE = "TRACE",
        /**
         * Establishes a tunnel to the server identified by the target resource.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        CONNECT = "CONNECT",
        /**
         * Modifies a resource partially.
         *
         * **Since**: 26.0.0
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @crossplatform
         * @since 26.0.0
         */
        PATCH = "PATCH"
    }
    /**
     * Enumerates the response codes for an HTTP request.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 6
     */
    export enum ResponseCode {
        /**
         * The request is successful. This return code is generally used for GET and POST requests.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        OK = 200,
        /**
         * "Created." The request has been successfully sent and a new resource is created.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        CREATED = 201,
        /**
         * "Accepted." The request has been accepted for processing, but the processing has not been completed.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        ACCEPTED = 202,
        /**
         * "Non-Authoritative Information." The request is successful.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        NOT_AUTHORITATIVE = 203,
        /**
         * "No Content." The server has successfully fulfilled the request but there is no additional content to send in the
         * response payload body.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        NO_CONTENT = 204,
        /**
         * "Reset Content." The server has successfully fulfilled the request and desires that the user agent reset the
         * content.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        RESET = 205,
        /**
         * "Partial Content." The server has successfully fulfilled the partial GET request for a given resource.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        PARTIAL = 206,
        /**
         * "Multiple Choices." The requested resource corresponds to any one of a set of representations.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        MULT_CHOICE = 300,
        /**
         * "Moved Permanently." The requested resource has been assigned a new permanent URI and any future references to
         * this resource will be redirected to this URI.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        MOVED_PERM = 301,
        /**
         * "Moved Temporarily." The requested resource is moved temporarily to a different URI.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        MOVED_TEMP = 302,
        /**
         * "See Other." The response to the request can be found under a different URI.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        SEE_OTHER = 303,
        /**
         * "Not Modified." The client has performed a conditional GET request and access is allowed, but the content has not
         * been modified.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        NOT_MODIFIED = 304,
        /**
         * "Use Proxy." The requested resource can only be accessed through the proxy.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        USE_PROXY = 305,
        /**
         * "Bad Request." The request could not be understood by the server due to incorrect syntax.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        BAD_REQUEST = 400,
        /**
         * "Unauthorized." The request requires user authentication.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        UNAUTHORIZED = 401,
        /**
         * "Payment Required." This code is reserved for future use.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        PAYMENT_REQUIRED = 402,
        /**
         * "Forbidden." The server understands the request but refuses to process it.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        FORBIDDEN = 403,
        /**
         * "Not Found." The server does not find anything matching the Request-URI.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        NOT_FOUND = 404,
        /**
         * "Method Not Allowed." The method specified in the request is not allowed for the resource identified by the
         * Request-URI.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        BAD_METHOD = 405,
        /**
         * "Not Acceptable." The server cannot fulfill the request according to the content characteristics of the request.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        NOT_ACCEPTABLE = 406,
        /**
         * "Proxy Authentication Required." The request requires user authentication with the proxy.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        PROXY_AUTH = 407,
        /**
         * "Request Timeout." The client fails to generate a request within the timeout period.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        CLIENT_TIMEOUT = 408,
        /**
         * "Conflict." The request cannot be fulfilled due to a conflict with the current state of the resource. Conflicts
         * are most likely to occur in response to a PUT request.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        CONFLICT = 409,
        /**
         * "Gone." The requested resource has been deleted permanently and is no longer available.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        GONE = 410,
        /**
         * "Length Required." The server refuses to process the request without a defined Content-Length.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        LENGTH_REQUIRED = 411,
        /**
         * "Precondition Failed." The precondition in the request is incorrect.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        PRECON_FAILED = 412,
        /**
         * "Request Entity Too Large." The server refuses to process a request because the request entity is larger than the
         * server is able to process.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        ENTITY_TOO_LARGE = 413,
        /**
         * "Request-URI Too Long." The Request-URI is too long for the server to process.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        REQ_TOO_LONG = 414,
        /**
         * "Unsupported Media Type." The server is unable to process the media format in the request.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        UNSUPPORTED_TYPE = 415,
        /**
         * "Range Not Satisfiable." The server cannot serve the requested ranges.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        RANGE_NOT_SATISFIABLE = 416,
        /**
         * "Internal Server Error." The server encounters an unexpected error that prevents it from fulfilling the request.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        INTERNAL_ERROR = 500,
        /**
         * "Not Implemented." The server does not support the function required to fulfill the request.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        NOT_IMPLEMENTED = 501,
        /**
         * "Bad Gateway." The server acting as a gateway or proxy receives an invalid response from the upstream server.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        BAD_GATEWAY = 502,
        /**
         * "Service Unavailable." The server is currently unable to process the request due to a temporary overload or
         * system maintenance.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        UNAVAILABLE = 503,
        /**
         * "Gateway Timeout." The server acting as a gateway or proxy does not receive requests from the remote server
         * within the timeout period.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        GATEWAY_TIMEOUT = 504,
        /**
         * The server does not support the HTTP protocol version used in the client request.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        VERSION = 505
    }
    /**
     * Enumerates HTTP protocol versions.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    export enum HttpProtocol {
        /**
         * HTTP1.1.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        HTTP1_1 = 0,
        /**
         * HTTP2.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        HTTP2 = 1,
        /**
         * HTTP3. If the system or server does not support HTTP3, the HTTP protocol of an earlier version is used.
         *
         * **Note**: This parameter takes effect only for HTTPS URLs. If this parameter is set to HTTP, the request will
         * fail.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        HTTP3 = 2
    }
    /**
     * Enumerates HTTP data types.
     *
     * | Name| Value| Description    |
     * | ------------------  | -- | ----------- |
     * | STRING              | 0 | String type.|
     * | OBJECT              | 1 | Object type.   |
     * | ARRAY_BUFFER        | 2 | Binary array type.|
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    export enum HttpDataType {
        /**
         * The returned type is string.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        STRING = 0,
        /**
         * The returned type is Object.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        OBJECT = 1,
        /**
         * The returned type is ArrayBuffer.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        ARRAY_BUFFER = 2
    }
    /**
     * Defines the response to an HTTP request.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 6
     */
    export interface HttpResponse {
        /**
         * Response content returned based on **Content-type** in the response header. If **HttpRequestOptions** does not
         * contain the **expectDataType** field, the response content is returned according to the following rules:
         *
         * - application/json: string in JSON format
         * - application/octet-stream: ArrayBuffer
         * - image: ArrayBuffer
         * - Others: string
         *
         * If **HttpRequestOptions** contains the **expectDataType** field, the response content must be of the same type as
         * the data returned by the server.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        result: string | Object | ArrayBuffer;
        /**
         * Type of the return value.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        resultType: HttpDataType;
        /**
         * Result code for an HTTP request. If the callback function is successfully executed, a result code defined in
         * [ResponseCode]{@link http.ResponseCode} will be returned. Otherwise, an error code will be returned in the
         * **err** field in **AsyncCallback**.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        responseCode: ResponseCode | number;
        /**
         * Response header. The return value is a string in JSON format. If you want to use specific content in the
         * response, you need to implement parsing of that content. Common fields and parsing methods are as follows:
         *
         * - content-type: header['content-type']
         * - status-line: header['status-line']
         * - date: header.date/header['date']
         * - server: header.server/header['server']
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        header: Object;
        /**
         * Original cookies returned by the server. How to process the cookies is up to your decision.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 8
         */
        cookies: string;
        /**
         * Time consumed in each phase of an HTTP request.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        performanceTiming: PerformanceTiming;
        /**
         * Detailed information about the HTTP request interaction.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @since 24
         */
        connectionExtraInfo?: ConnectionExtraInfo;
    }
    /**
     * Defines the detailed information about the HTTP request interaction.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @stagemodelonly
     * @since 24
     */
    export interface ConnectionExtraInfo {
        /**
         * HTTP version used in the
         * [request]{@link http.HttpRequest.request(url: string, callback: AsyncCallback<HttpResponse>)}, for example, 'HTTP
         * /1.0', 'HTTP/1.1', 'HTTP/2', 'HTTP/2 over TLS', 'HTTP/3', or 'Unknown/Non-HTTP'.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 24
         */
        networkProtocolName: string;
        /**
         * TLS version used in the request. It is returned only when the TLS protocol is used.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 24
         */
        tlsVersion?: TlsVersion;
        /**
         * Cipher suite used in the request. It is returned only when the TLS protocol is used.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 24
         */
        cipherSuite?: CipherSuite;
        /**
         * IP address of the client in the request process.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 24
         */
        localAddress: string;
        /**
         * IP address of the server in the request process.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 24
         */
        remoteAddress: string;
        /**
         * Port number of the client in the request process. The value ranges from 1 to 65535.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 24
         */
        localPort: number;
        /**
         * Port number of the server in the request process. The value ranges from 1 to 65535.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 24
         */
        remotePort: number;
        /**
         * Whether to reuse the connection in the request process. **true**: yes; **false**: no.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 24
         */
        isReusedConnection: boolean;
        /**
         * Whether to use a proxy in the request process. **true**: yes; **false**: no.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 24
         */
        isProxyConnection: boolean;
        /**
         * Whether the local cache is hit in the request process. **true**: yes; **false**: no.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 24
         */
        isCacheHit: boolean;
        /**
         * Number of redirections in the request process.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @stagemodelonly
         * @since 24
         */
        redirectCount: number;
    }
    /**
     * Configures the timing for performance tracing, in ms.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 12]
     * @since 11
     */
    export interface PerformanceTiming {
        /**
         * Duration from the time when the
         * [request]{@link http.HttpRequest.request(url: string, callback: AsyncCallback<HttpResponse>)} is sent to the time
         * when the DNS resolution is complete.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        dnsTiming: number;
        /**
         * Duration from the time when the
         * [request]{@link http.HttpRequest.request(url: string, callback: AsyncCallback<HttpResponse>)} is sent to the time
         * when the TCP connection is complete.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        tcpTiming: number;
        /**
         * Duration from the time when the
         * [request]{@link http.HttpRequest.request(url: string, callback: AsyncCallback<HttpResponse>)} is sent to the time
         * when the TLS connection is complete.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        tlsTiming: number;
        /**
         * Duration from the time when the
         * [request]{@link http.HttpRequest.request(url: string, callback: AsyncCallback<HttpResponse>)} is sent to the time
         * when the first byte is sent.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        firstSendTiming: number;
        /**
         * Duration from the time when the
         * [request]{@link http.HttpRequest.request(url: string, callback: AsyncCallback<HttpResponse>)} is sent to the time
         * when the first byte is received.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        firstReceiveTiming: number;
        /**
         * Duration from the time when the
         * [request]{@link http.HttpRequest.request(url: string, callback: AsyncCallback<HttpResponse>)} is sent to the time
         * when the request is complete.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        totalFinishTiming: number;
        /**
         * Duration from the time when the
         * [request]{@link http.HttpRequest.request(url: string, callback: AsyncCallback<HttpResponse>)} is sent to the time
         * when all redirection steps are complete.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        redirectTiming: number;
        /**
         * Duration from the time when the
         * [request]{@link http.HttpRequest.request(url: string, callback: AsyncCallback<HttpResponse>)} is sent to the time
         * when the header resolution is complete.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        responseHeaderTiming: number;
        /**
         * Duration from the time when the
         * [request]{@link http.HttpRequest.request(url: string, callback: AsyncCallback<HttpResponse>)} is sent to the time
         * when the body resolution is complete.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        responseBodyTiming: number;
        /**
         * Duration from the time when the
         * [request]{@link http.HttpRequest.request(url: string, callback: AsyncCallback<HttpResponse>)} is sent to the time
         * when a callback is returned to the application.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @since 11
         */
        totalTiming: number;
    }
    /**
     * Defines the data receiving progress information.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 12]
     * @atomicservice [since 15]
     * @since 11
     */
    export interface DataReceiveProgressInfo {
        /**
         * Amount of data that has been received, in bytes.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @atomicservice [since 15]
         * @since 11
         */
        receiveSize: number;
        /**
         * Amount of data to be received, in bytes.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @atomicservice [since 15]
         * @since 11
         */
        totalSize: number;
    }
    /**
     * Defines the data sending progress information.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 12]
     * @atomicservice [since 15]
     * @since 11
     */
    export interface DataSendProgressInfo {
        /**
         * Amount of data to be sent each time, in bytes.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @atomicservice [since 15]
         * @since 11
         */
        sendSize: number;
        /**
         * Amount of data to be sent, in bytes.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 12]
         * @atomicservice [since 15]
         * @since 11
         */
        totalSize: number;
    }
    /**
     * Creates an **HttpResponseCache** object that stores the response data of HTTP requests. You can call
     * [flush]{@link http.HttpResponseCache.flush(callback: AsyncCallback<void>)} and
     * [delete]{@link http.HttpResponseCache.delete(callback: AsyncCallback<void>)} in the object.
     *
     * @param { number } cacheSize - Cache size. The maximum value is 10*1024*1024 (10 MB). The maximum value is used by
     *     default.
     * @returns { HttpResponseCache } Object that stores the response to the HTTP request.
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function createHttpResponseCache(cacheSize?: number): HttpResponseCache;
    /**
     * Defines an object that stores the response to an HTTP request. Before invoking APIs provided by
     * **HttpResponseCache**, you must call [createHttpResponseCache()]{@link http.createHttpResponseCache} to create an
     * **HttpRequestTask** object.
     *
     * **Usage of Keywords in the Response Header**
     * - **`Cache-Control`**: specifies the cache policy, for example, `no-cache`, `no-store`, `max-age`, `public`, or
     * `private`.
     * - **`Expires`**: specifies the expiration time of a resource. The value is in the GMT format.
     * - **`ETag`**: identifies the resource version. The client can use the `If-None-Match` request header to check
     * whether the resource has been modified.
     * - **`Last-Modified`**: specifies the last modification time of a resource. The client can use the
     * `If-Modified-Since` request header to check whether a resource has been modified.
     * - **`Vary`**: specifies the parts of the request header that affect the cached response. This field is used to
     * distinguish different cache versions.
     *
     * When using these keywords, ensure that the response header is correctly configured on the server. The client
     * determines whether to use the cached resource and how to verify whether the resource is the latest based on the
     * response header. Correct cache policies help to improve application performance and user experience.
     *
     * **How to Set the Cache-Control Header**
     * `Cache-Control` is a common header, but it is usually used on the server. It allows you to define when, how, and
     * how long a response should be cached. The following are some common `Cache-Control` directives:
     *
     * - **`no-cache`**: indicates that the response can be stored in the cache, but it must be verified with the origin
     * server before each reuse. If the resource remains unchanged, the response status code is 304 (Not Modified). In
     * this case, the resource content is not sent, and the resource in the cache is used. If the resource has expired,
     * the response status code is 200 and the resource content is sent.
     * - `no-store`: indicates that resources cannot be cached. Resources must be obtained from the server for each
     * request.
     * - `max-age`: specifies the maximum cache duration, in seconds. For example, `Cache-Control: max-age=3600` indicates
     * that the valid cache duration is 3,600 seconds (that is, 1 hour).
     * - `public`: indicates that the response can be cached by any object, for example, the client that sends the request
     * or the proxy server.
     * - `private`: indicates that the response can be cached only by a single user and cannot be used as a shared cache (
     * that is, the response cannot be cached by the proxy server).
     * - `must-revalidate`: indicates that a resource must be revalidated with the origin server once it has become
     * stable.
     * - **`no-transform`**: indicates that the proxy server is not allowed to modify the response content.
     * - **`proxy-revalidate`**: works in a way similar to `must-revalidate`, but applies only to shared caches.
     * - **`s-maxage`**: works in a way similar to `max-age`, but applies only to shared caches.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    export interface HttpResponseCache {
        /**
         * Flushes data in the cache to the file system so that the cached data can be accessed in the next HTTP request.
         * This API uses an asynchronous callback to return the result. Cached data includes the response header (header),
         * response body (result), cookies, request time (requestTime), and response time (responseTime).
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result.  If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        flush(callback: AsyncCallback<void>): void;
        /**
         * Flushes data in the cache to the file system so that the cached data can be accessed in the next HTTP request.
         * This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        flush(): Promise<void>;
        /**
         * Disables the cache and deletes the data in it. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        delete(callback: AsyncCallback<void>): void;
        /**
         * Disables the cache and deletes the data in it. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Communication.NetStack
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        delete(): Promise<void>;
    }
}
export default http;

```
