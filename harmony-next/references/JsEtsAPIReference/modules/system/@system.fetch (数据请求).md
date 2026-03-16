# @system.fetch (数据请求)

-

从API Version 6开始，该接口不再维护，推荐使用新接口[@ohos.net.http](../ohos/@ohos.net.http (数据请求).md)。

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

参数名类型必填说明urlstring是资源地址。datastring | Object否请求的参数，可选类型是字符串或者json对象。详见表 data与Content-Type关系。headerObject否设置请求的header。methodstring否请求方法默认为GET，可选值为：OPTIONS、GET、HEAD、POST、PUT、DELETE、TRACE。responseTypestring否默认会根据服务器返回header中的Content-Type确定返回类型，支持文本和json格式。详见success返回值。successFunction否接口调用成功的回调函数，返回值为[FetchResponse](#ZH-CN_TOPIC_0000002529285471__fetchresponse3)。failFunction否接口调用失败的回调函数。completeFunction否接口调用结束的回调函数。

**表1** data与Content-Type关系

dataContent-Type说明string不设置Content-Type默认为 text/plain，data值作为请求的body。string任意 Typedata值作为请求的body。Object不设置Content-Type默认为application/x-www-form-urlencoded，data按照资源地址规则进行encode拼接作为请求的body。Objectapplication/x-www-form-urlencodeddata按照资源地址规则进行encode拼接作为请求的body。

#### FetchResponse3+

**系统能力：** SystemCapability.Communication.NetStack

名称类型只读可选说明codenumber否否表示服务器的状态code。datastring | Object否否返回数据类型由responseType确定，详见表 responseType与success中data关系。headersObject否否表示服务器response的所有header。

**表2** responseType与success中data关系

responseTypedata说明无string服务器返回的header中的type如果是text/*或application/json、application/javascript、application/xml，值为文本内容。textstring返回文本内容。jsonObject返回json格式的对象。

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
  }
  ... // 用户的其它配置信息
}
```