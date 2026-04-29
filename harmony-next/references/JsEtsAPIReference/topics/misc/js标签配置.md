# js标签配置

js标签中包含了实例名称、页面路由信息。

| 标签 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| name | string | default | 是 | 标识JS实例的名字。 |
| pages | Array | - | 是 | 路由信息，详见“pages”。 |


 name、pages标签配置需在配置文件中的“js”标签中完成设置。

#### pages

定义每个页面的路由信息，每个页面由页面路径和页面名组成，页面的文件名即为页面名，例如：

```ets
{
  // ...
  "pages": [
    "pages/index/index",
    "pages/detail/detail"
  ]
  // ...
}
```

-

应用首页固定为"pages/index/index"。

-

页面文件名不能使用组件名称，比如：text.hml、button.hml等。

#### 示例

```ets
{
  "app": {
    "bundleName": "com.example.player",
    "version": {
        "code": 1,
        "name": "1.0"
    },
    "vendor": "example"
  },
  "module": {
    // ...
    "js": [
      {
        "name": "default",
        "pages": [
          "pages/index/index",
          "pages/detail/detail"
        ]
      }
    ],
    "abilities": [
      {
        // ...
      }
    ]
  }
```