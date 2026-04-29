# @system.fetch (数据请求)

-

从API Version 6开始，该接口不再维护，推荐使用新接口[@ohos.net.http](@ohos.net.http (数据请求).md)。

-

本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import fetch from '@system.fetch';
```

#### fetch.fetch3+

fetch(options:{

 url: string;

 data?: string | object;

 header?: Object;

 method?: string;

 responseType?: string;

 success?: (data: FetchResponse) => void;

 fail?: (data: any, code: number) => void;

 complete?: () => void;

 } ): void

通过网络获取数据。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 资源地址。 |
| data | string | Object | 否 | 请求的参数，可选类型是字符串或者json对象。详见表 data与Content-Type关系。 |
| header | Object | 否 | 设置请求的header。 |
| method | string | 否 | 请求方法默认为GET，可选值为：OPTIONS、GET、HEAD、POST、PUT、DELETE、TRACE。 |
| responseType | string | 否 | 默认会根据服务器返回header中的Content-Type确定返回类型，支持文本和json格式。详见success返回值。 |
| success | Function | 否 | 接口调用成功的回调函数，返回值为FetchResponse。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |

**表1** data与Content-Type关系

| data | Content-Type | 说明 |
| --- | --- | --- |
| string | 不设置 | Content-Type默认为 text/plain，data值作为请求的body。 |
| string | 任意 Type | data值作为请求的body。 |
| Object | 不设置 | Content-Type默认为application/x-www-form-urlencoded，data按照资源地址规则进行encode拼接作为请求的body。 |
| Object | application/x-www-form-urlencoded | data按照资源地址规则进行encode拼接作为请求的body。 |

#### FetchResponse3+

**系统能力：** SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 否 | 否 | 表示服务器的状态code。 |
| data | string | Object | 否 | 否 | 返回数据类型由responseType确定，详见表 responseType与success中data关系。 |
| headers | Object | 否 | 否 | 表示服务器response的所有header。 |

**表2** responseType与success中data关系

| responseType | data | 说明 |
| --- | --- | --- |
| 无 | string | 服务器返回的header中的type如果是text/*或application/json、application/javascript、application/xml，值为文本内容。 |
| text | string | 返回文本内容。 |
| json | Object | 返回json格式的对象。 |

**示例：**

```ets
export default {
  data: {
    responseData: 'NA',
    url: "test_url",
  },
  fetch: function () {
    var that = this;
    fetch.fetch({
      url: that.url,
      success: function(response) {
        console.info("fetch success");
        that.responseData = JSON.stringify(response);
      },
      fail: function() {
        console.info("fetch fail");
      }
    });
  }
```

 默认支持https，如果要支持http，需要在config.json里增加network标签，属性标识 "cleartextTraffic": true。即：

```ets
{
 "deviceConfig": {
   "default": {
     "network": {
       "cleartextTraffic": true
     }
     ... // 用户的其它配置信息
    }
  ... // 用户的其它配置信息
}
```