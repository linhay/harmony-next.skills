from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "reference_compat.py"
SPEC = importlib.util.spec_from_file_location("reference_compat", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ReferenceCompatTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.repo_root = Path(self.temp_dir.name)
        self.references_root = self.repo_root / "references"
        self.js_root = self.references_root / "JsEtsAPIReference"
        (self.js_root / "topics" / "misc").mkdir(parents=True)
        (self.js_root / "topics" / "components").mkdir(parents=True)
        (self.js_root / "modules" / "ohos").mkdir(parents=True)
        (self.js_root / "guides").mkdir(parents=True)
        (self.references_root / "quickStart").mkdir(parents=True)

        (self.js_root / "topics" / "misc" / "native_handwrite_api.h.md").write_text(
            "# native_handwrite_api.h\n\n起始版本： 23\n",
            encoding="utf-8",
        )
        (self.js_root / "topics" / "misc" / "HandWrite.md").write_text(
            "[native_handwrite_api.h](../../capi/headers/native_handwrite_api.h.md)\n",
            encoding="utf-8",
        )
        (self.js_root / "modules" / "ohos" / "@ohos.demo.md").write_text(
            "# @ohos.demo\n",
            encoding="utf-8",
        )
        (self.js_root / "modules" / "ohos" / "@ohos.state.md").write_text(
            (
                "[makeObserved接口：将非观察数据变为可观察数据]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-makeobserved)\n"
                "[状态管理V1和V2混用指导（API version 19及之后）]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-mixusage)\n"
            ),
            encoding="utf-8",
        )
        (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").write_text(
            (
                "[状态管理V1-V2迁移指导]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-guide)\n"
                "[状态管理V1向V2迁移场景]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-v1-v2-migration-guide)\n"
                "[组件内状态变量迁移]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-inner-component)\n"
                "[数据对象状态变量迁移]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-inner-class)\n"
                "[状态管理概述]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-overview#状态管理v2)\n"
                "[@Observed与@ObjectLink]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-observed-and-objectlink)\n"
                "[@ObservedV2与@Trace]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-observedv2-and-trace)\n"
                "[addMonitor/clearMonitor开发指南]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-addmonitor-clearmonitor#限制条件)\n"
                "[同步刷新]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-applysync-flushupdates-flushuiupdates)\n"
                "[@Env开发者指南]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-env-system-property)\n"
                "[AppStorageV2]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-appstoragev2)\n"
                "[PersistenceV2集合类型]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-persistencev2#globalconnect支持集合的类型)\n"
                "[状态管理介绍]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-introduce#触发更新)\n"
                "[@Watch开发者指南]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-watch)\n"
                "[@Monitor开发者指南]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-monitor)\n"
                "[AppStorage(应用全局的UI状态存储)]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-appstorage#storagelink)\n"
                "[LocalStorage(页面级UI状态存储)]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-localstorage#localstorageprop)\n"
                "[PersistentStorage(持久化存储UI状态)]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-persiststorage#从appstorage中访问persistentstorage初始化的属性)\n"
                "[@State装饰器指南]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state)\n"
                "[状态变量术语]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-glossary#状态变量state-variables)\n"
                "[@Provide/@Consume开发指南]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-provide-and-consume#provide支持allowoverride参数)\n"
                "[自定义组件指南]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components#component)\n"
                "[自定义组件生命周期指南]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-page-custom-components-lifecycle#自定义组件的删除)\n"
                "[使用UI上下文接口操作界面]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)\n"
                "[命名路由开发指南]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-routing#命名路由)\n"
                "[TextInput开发指南]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-text-input#密码模式)\n"
                "[支持焦点处理]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-events-focus-event#基础概念)\n"
                "[使用粘贴控件]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pastebutton)\n"
            ),
            encoding="utf-8",
        )
        (self.js_root / "modules" / "ohos" / "@ohos.more-guide.md").write_text(
            (
                "[窗口开发术语]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-terminology#自由窗口)\n"
                "[UIAbility组件基本用法]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)\n"
                "[module.json5配置文件]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#abilities标签)\n"
                "[应用启动框架AppStartup]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-startup#设置启动参数)\n"
                "[Sendable对象简介]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable#sendable支持的数据类型)\n"
                "[@Builder装饰器：自定义构建函数]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder#全局自定义构建函数)\n"
                "[$$语法：系统组件双向同步]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-two-way-sync)\n"
                "[!!语法：双向绑定]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-binding#系统组件参数双向绑定)\n"
                "[if/else：条件渲染]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-ifelse)\n"
            ),
            encoding="utf-8",
        )
        (self.js_root / "modules" / "ohos" / "@ohos.final-guide.md").write_text(
            (
                "[数据库备份与恢复]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-backup-and-restore)\n"
                "[多应用管控]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-multi-mdm#规则3配置)\n"
                "[Connectivity Kit术语]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/terminology#profile)\n"
                "[组件启动规则（Stage模型）]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-startup-rules)\n"
                "[MDM Kit开发指南]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-guide)\n"
                "[申请受限权限]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions-in-acl)\n"
                "[基于服务账号生成鉴权令牌]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-jwt-token#开发步骤)\n"
                "[通过键值型数据库实现数据持久化]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-kv-store#开发步骤)\n"
                "[声明权限]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions#在配置文件中声明权限)\n"
                "[Ability Kit术语]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-terminology#masterprocess主控进程)\n"
                "[应用上下文Context]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-context-stage#context的获取方式)\n"
                "[app.json5配置文件]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-configuration-file#multiappmode标签)\n"
                "[组件启动规则（FA模型）]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-startup-rules-fa)\n"
            ),
            encoding="utf-8",
        )
        (self.js_root / "modules" / "ohos" / "@ohos.batch2-guide.md").write_text(
            (
                "[NFC标签读写开发指南]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nfc-tag-access-guide#后台读取标签)\n"
                "[栅格布局]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-grid-layout#栅格容器断点)\n"
                "[线程间通信对象概述]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/serializable-overview)\n"
                "[受限开放权限]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/restricted-permissions#ohospermissionmanage_apn_setting)\n"
                "[资源分类与访问]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/resource-categories-and-access#资源访问)\n"
                "[ExtensionAbility组件]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/extensionability-overview)\n"
                "[UIAbility组件启动模式]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-launch-type#specified启动模式)\n"
                "[申请访问剪贴板权限]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/get-pastedata-permission-guidelines)\n"
                "[@Reusable装饰器：V1组件复用]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-reusable)\n"
                "[设置页签栏的悬浮样式]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-hds-tabs-bar-floating#迷你栏)\n"
                "[使用Picker选择媒体库资源]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-photoviewpicker#指定uri获取图片或视频资源)\n"
                "[开发准备]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-preparation)\n"
            ),
            encoding="utf-8",
        )
        (self.js_root / "modules" / "ohos" / "@ohos.batch3-guide.md").write_text(
            (
                "[代理提醒]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agent-powered-reminder#约束与限制)\n"
                "[应用沙箱目录]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-sandbox-directory#应用文件目录与应用文件路径)\n"
                "[交互基础机制说明]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-interaction-basic-principles#触摸测试)\n"
                "[通过用户首选项实现数据持久化]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-preferences#gskv存储)\n"
                "[使用RSA密钥对签名验签]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1)\n"
                "[开通Device Security服务]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice)\n"
                "[配置ArkTS卡片的配置文件]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-configuration#sceneanimationparams标签)\n"
                "[Worker简介]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/worker-introduction#文件路径注意事项)\n"
                "[UI国际化]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-internationalization#镜像状态字符对齐)\n"
                "[向用户申请授权]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request-user-authorization)\n"
                "[图片解码内存优化]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-allocator-type#系统默认的内存分配方式)\n"
            ),
            encoding="utf-8",
        )
        (self.js_root / "modules" / "ohos" / "@ohos.arkui.StateManagement (状态管理).md").write_text(
            "# @ohos.arkui.StateManagement (状态管理)\n",
            encoding="utf-8",
        )
        (self.js_root / "topics" / "components" / "List.md").write_text(
            (
                "[List与makeObserved]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/"
                "arkts-v1-v2-migration-inner-object#滚动组件)\n"
            ),
            encoding="utf-8",
        )
        (self.js_root / "topics" / "components" / "动态属性设置.md").write_text(
            (
                "[Modifier与makeObserved]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/"
                "arkts-v1-v2-migration-inner-object#modifier)\n"
            ),
            encoding="utf-8",
        )
        (self.js_root / "topics" / "components" / "WaterFlow.md").write_text(
            (
                "[WaterFlow与makeObserved]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/"
                "arkts-v1-v2-migration-inner-object#滚动组件)\n"
            ),
            encoding="utf-8",
        )
        (self.js_root / "topics" / "misc" / "rendering-guide.md").write_text(
            (
                "[ForEach开发者指南]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach)\n"
                "[LazyForEach开发者指南]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach)\n"
                "[Repeat开发者指南]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-rendering-control-repeat#参数说明)\n"
                "[BuilderNode开发指南]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-arktsnode-buildernode#节点解绑)\n"
                "[mutableBuilder开发指南]"
                "(https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-mutablebuilder)\n"
            ),
            encoding="utf-8",
        )
        (self.js_root / "guides" / "状态管理V1-V2迁移指导.md").write_text(
            "# 状态管理V1-V2迁移指导\n\n## 滚动组件\n\n## modifier\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "状态管理V1和V2混用指导（API version 19及之后）.md").write_text(
            "# 状态管理V1和V2混用指导（API version 19及之后）\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "makeObserved接口：将非观察数据变为可观察数据.md").write_text(
            "# makeObserved接口：将非观察数据变为可观察数据\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "状态管理概述.md").write_text(
            "# 状态管理概述\n\n## 状态管理V1\n\n## 状态管理V2\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "@Observed与@ObjectLink：V1数据对象观测.md").write_text(
            "# @Observed与@ObjectLink：V1数据对象观测\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "@ObservedV2与@Trace：类属性变化观测.md").write_text(
            "# @ObservedV2与@Trace：类属性变化观测\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "addMonitor与clearMonitor开发指南.md").write_text(
            "# addMonitor与clearMonitor开发指南\n\n## 限制条件\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "applySync与flushUpdates与flushUIUpdates接口：同步刷新.md").write_text(
            "# applySync与flushUpdates与flushUIUpdates接口：同步刷新\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "AppStorageV2（应用全局的UI状态存储）.md").write_text(
            "# AppStorageV2（应用全局的UI状态存储）\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "PersistenceV2（持久化存储UI状态）.md").write_text(
            "# PersistenceV2（持久化存储UI状态）\n\n## globalConnect支持集合的类型\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "窗口开发术语.md").write_text(
            "# 窗口开发术语\n\n## 自由窗口\n\n## 自由多窗模式\n\n## 沉浸式布局\n\n## 全局坐标系\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "UIAbility组件基本用法.md").write_text(
            "# UIAbility组件基本用法\n\n## 获取UIAbility的上下文信息\n\n## 获取UIAbility拉起方的信息\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "module.json5配置文件.md").write_text(
            (
                "# module.json5配置文件\n\n"
                "## pages标签\n\n"
                "## metadata标签\n\n"
                "## abilities标签\n\n"
                "## skills标签\n\n"
                "## extensionAbilities标签\n\n"
                "## shortcuts标签\n\n"
                "## wants标签\n\n"
                "## deviceTypes标签\n"
            ),
            encoding="utf-8",
        )
        (self.js_root / "guides" / "应用启动框架AppStartup.md").write_text(
            "# 应用启动框架AppStartup\n\n## 定义启动参数配置\n\n## 设置启动参数\n\n## 添加任务匹配规则\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "Sendable对象简介.md").write_text(
            "# Sendable对象简介\n\n## Sendable协议\n\n## ISendable\n\n## Sendable支持的数据类型\n\n## @Sendable装饰器\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "@Builder装饰器：自定义构建函数.md").write_text(
            "# @Builder装饰器：自定义构建函数\n\n## 全局自定义构建函数\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "$$语法：系统组件双向同步.md").write_text(
            "# $$语法：系统组件双向同步\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "!!语法：双向绑定.md").write_text(
            "# !!语法：双向绑定\n\n## 系统组件参数双向绑定\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "if-else：条件渲染.md").write_text(
            "# if/else：条件渲染\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "数据库备份与恢复.md").write_text(
            "# 数据库备份与恢复\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "多应用管控.md").write_text(
            "# 多应用管控\n\n## 规则3：配置\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "Connectivity Kit术语.md").write_text(
            "# Connectivity Kit术语\n\n## Profile\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "组件启动规则（Stage模型）.md").write_text(
            "# 组件启动规则（Stage模型）\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "MDM Kit开发指南.md").write_text(
            "# MDM Kit开发指南\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "申请受限权限.md").write_text(
            "# 申请受限权限\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "基于服务账号生成鉴权令牌.md").write_text(
            "# 基于服务账号生成鉴权令牌\n\n## 开发步骤\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "通过键值型数据库实现数据持久化.md").write_text(
            "# 通过键值型数据库实现数据持久化\n\n## 开发步骤\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "声明权限.md").write_text(
            "# 声明权限\n\n## 在配置文件中声明权限\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "Ability Kit术语.md").write_text(
            "# Ability Kit术语\n\n## MasterProcess（主控进程）\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "应用上下文Context.md").write_text(
            "# 应用上下文Context\n\n## Context的获取方式\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "app.json5配置文件.md").write_text(
            "# app.json5配置文件\n\n## multiAppMode标签\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "组件启动规则（FA模型）.md").write_text(
            "# 组件启动规则（FA模型）\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "NFC标签读写开发指南.md").write_text(
            "# NFC标签读写开发指南\n\n## 后台读取标签\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "栅格布局 (GridRow-GridCol).md").write_text(
            "# 栅格布局 (GridRow/GridCol)\n\n## 栅格容器断点\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "线程间通信对象概述.md").write_text(
            "# 线程间通信对象概述\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "受限开放权限.md").write_text(
            "# 受限开放权限\n\n## ohos.permission.MANAGE_APN_SETTING\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "资源分类与访问.md").write_text(
            "# 资源分类与访问\n\n## 资源访问\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "ExtensionAbility组件.md").write_text(
            "# ExtensionAbility组件\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "UIAbility组件启动模式.md").write_text(
            "# UIAbility组件启动模式\n\n## specified启动模式\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "申请访问剪贴板权限.md").write_text(
            "# 申请访问剪贴板权限\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "@Reusable装饰器：V1组件复用.md").write_text(
            "# @Reusable装饰器：V1组件复用\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "设置页签栏的悬浮样式.md").write_text(
            "# 设置页签栏的悬浮样式\n\n## 迷你栏\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "使用Picker选择媒体库资源.md").write_text(
            "# 使用Picker选择媒体库资源\n\n## 指定URI获取图片或视频资源\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "开发准备（媒体库）.md").write_text(
            "# 开发准备\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "代理提醒（ArkTS）.md").write_text(
            "# 代理提醒(ArkTS)\n\n## 约束与限制\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "应用沙箱目录.md").write_text(
            "# 应用沙箱目录\n\n## 应用文件目录与应用文件路径\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "交互基础机制说明.md").write_text(
            "# 交互基础机制说明\n\n## 触摸测试\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "通过用户首选项实现数据持久化.md").write_text(
            "# 通过用户首选项实现数据持久化\n\n## GSKV存储\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "使用RSA密钥对（PKCS1模式）签名验签.md").write_text(
            "# 使用RSA密钥对（PKCS1模式）签名验签\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "开通Device Security服务.md").write_text(
            "# 开通Device Security服务\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "配置ArkTS卡片的配置文件.md").write_text(
            "# 配置ArkTS卡片的配置文件\n\n## sceneAnimationParams标签\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "Worker简介.md").write_text(
            "# Worker简介\n\n## 文件路径注意事项\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "UI国际化.md").write_text(
            "# UI国际化\n\n## 镜像状态字符对齐\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "向用户申请授权.md").write_text(
            "# 向用户申请授权\n",
            encoding="utf-8",
        )
        (self.js_root / "guides" / "图片解码内存优化.md").write_text(
            "# 图片解码内存优化\n\n## 系统默认的内存分配方式\n",
            encoding="utf-8",
        )
        (self.js_root / "topics" / "components" / "应用级变量的状态管理.md").write_text(
            "# 应用级变量的状态管理\n",
            encoding="utf-8",
        )
        (self.js_root / "topics" / "components" / "自定义组件.md").write_text(
            "# 自定义组件\n",
            encoding="utf-8",
        )
        (self.js_root / "topics" / "components" / "自定义组件的生命周期.md").write_text(
            "# 自定义组件的生命周期\n",
            encoding="utf-8",
        )
        (self.js_root / "topics" / "components" / "TextInput.md").write_text(
            "# TextInput\n",
            encoding="utf-8",
        )
        (self.js_root / "topics" / "components" / "焦点事件.md").write_text(
            "# 焦点事件\n",
            encoding="utf-8",
        )
        (self.js_root / "topics" / "components" / "PasteButton.md").write_text(
            "# PasteButton\n",
            encoding="utf-8",
        )
        (self.js_root / "topics" / "components" / "状态变量变化监听.md").write_text(
            "# 状态变量变化监听\n",
            encoding="utf-8",
        )
        (self.js_root / "topics" / "components" / "ForEach.md").write_text(
            "# ForEach\n",
            encoding="utf-8",
        )
        (self.js_root / "topics" / "components" / "LazyForEach.md").write_text(
            "# LazyForEach\n",
            encoding="utf-8",
        )
        (self.js_root / "topics" / "components" / "Repeat.md").write_text(
            "# Repeat\n",
            encoding="utf-8",
        )
        (self.js_root / "topics" / "components" / "mutableBuilder.md").write_text(
            "# mutableBuilder\n",
            encoding="utf-8",
        )
        (self.js_root / "topics" / "misc" / "BuilderNode.md").write_text(
            "# BuilderNode\n",
            encoding="utf-8",
        )
        (self.references_root / "quickStart" / "intro.md").write_text(
            "# intro\n",
            encoding="utf-8",
        )
        self.paths = MODULE.build_paths(self.repo_root)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_generate_creates_compat_pages_and_indexes_them(self) -> None:
        rewritten = MODULE.rewrite_header_links(self.paths)
        guide_rewritten = MODULE.rewrite_targeted_guide_links(self.paths)
        MODULE.generate_references_index(self.paths)
        MODULE.generate_index(self.paths)

        self.assertEqual(rewritten, 1)
        self.assertEqual(guide_rewritten, 10)
        self.assertIn(
            "../../topics/misc/native_handwrite_api.h.md",
            (self.js_root / "topics" / "misc" / "HandWrite.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/状态管理V1-V2迁移指导.md#滚动组件",
            (self.js_root / "topics" / "components" / "List.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/makeObserved接口：将非观察数据变为可观察数据.md",
            (self.js_root / "modules" / "ohos" / "@ohos.state.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/状态管理V1和V2混用指导（API version 19及之后）.md",
            (self.js_root / "modules" / "ohos" / "@ohos.state.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/状态管理V1-V2迁移指导.md",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/状态管理V1-V2迁移指导.md#状态管理V1向V2迁移场景",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/状态管理V1-V2迁移指导.md#组件内状态变量迁移",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/状态管理V1-V2迁移指导.md#数据对象状态变量迁移",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/状态管理概述.md#状态管理v2",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/@Observed与@ObjectLink：V1数据对象观测.md",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/@ObservedV2与@Trace：类属性变化观测.md",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/addMonitor与clearMonitor开发指南.md#限制条件",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/applySync与flushUpdates与flushUIUpdates接口：同步刷新.md",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../topics/components/@Env：环境变量.md",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/AppStorageV2（应用全局的UI状态存储）.md",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/PersistenceV2（持久化存储UI状态）.md#globalconnect支持集合的类型",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/状态管理概述.md",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../topics/components/状态变量变化监听.md",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../topics/components/应用级变量的状态管理.md)",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "(@ohos.arkui.StateManagement (状态管理).md)",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../topics/components/自定义组件.md)",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../topics/components/自定义组件的生命周期.md)",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../types/classes/Class (UIContext).md",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../types/classes/Class (Router).md",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../topics/components/TextInput.md",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../topics/components/焦点事件.md",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../topics/components/PasteButton.md",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/窗口开发术语.md#自由窗口",
            (self.js_root / "modules" / "ohos" / "@ohos.more-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/UIAbility组件基本用法.md#获取uiability的上下文信息",
            (self.js_root / "modules" / "ohos" / "@ohos.more-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/module.json5配置文件.md#abilities标签",
            (self.js_root / "modules" / "ohos" / "@ohos.more-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/应用启动框架AppStartup.md#设置启动参数",
            (self.js_root / "modules" / "ohos" / "@ohos.more-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/Sendable对象简介.md#sendable支持的数据类型",
            (self.js_root / "modules" / "ohos" / "@ohos.more-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/@Builder装饰器：自定义构建函数.md#全局自定义构建函数",
            (self.js_root / "modules" / "ohos" / "@ohos.more-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/$$语法：系统组件双向同步.md",
            (self.js_root / "modules" / "ohos" / "@ohos.more-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/!!语法：双向绑定.md#系统组件参数双向绑定",
            (self.js_root / "modules" / "ohos" / "@ohos.more-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/if-else：条件渲染.md",
            (self.js_root / "modules" / "ohos" / "@ohos.more-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/数据库备份与恢复.md",
            (self.js_root / "modules" / "ohos" / "@ohos.final-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/多应用管控.md#规则3配置",
            (self.js_root / "modules" / "ohos" / "@ohos.final-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/Connectivity Kit术语.md#profile",
            (self.js_root / "modules" / "ohos" / "@ohos.final-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/组件启动规则（Stage模型）.md",
            (self.js_root / "modules" / "ohos" / "@ohos.final-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/MDM Kit开发指南.md",
            (self.js_root / "modules" / "ohos" / "@ohos.final-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/申请受限权限.md",
            (self.js_root / "modules" / "ohos" / "@ohos.final-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/基于服务账号生成鉴权令牌.md#开发步骤",
            (self.js_root / "modules" / "ohos" / "@ohos.final-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/通过键值型数据库实现数据持久化.md#开发步骤",
            (self.js_root / "modules" / "ohos" / "@ohos.final-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/声明权限.md#在配置文件中声明权限",
            (self.js_root / "modules" / "ohos" / "@ohos.final-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/Ability Kit术语.md#masterprocess主控进程",
            (self.js_root / "modules" / "ohos" / "@ohos.final-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/应用上下文Context.md#context的获取方式",
            (self.js_root / "modules" / "ohos" / "@ohos.final-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/app.json5配置文件.md#multiappmode标签",
            (self.js_root / "modules" / "ohos" / "@ohos.final-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/组件启动规则（FA模型）.md",
            (self.js_root / "modules" / "ohos" / "@ohos.final-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/NFC标签读写开发指南.md#后台读取标签",
            (self.js_root / "modules" / "ohos" / "@ohos.batch2-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/栅格布局 (GridRow-GridCol).md#栅格容器断点",
            (self.js_root / "modules" / "ohos" / "@ohos.batch2-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/线程间通信对象概述.md",
            (self.js_root / "modules" / "ohos" / "@ohos.batch2-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/受限开放权限.md#ohospermissionmanage_apn_setting",
            (self.js_root / "modules" / "ohos" / "@ohos.batch2-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/资源分类与访问.md#资源访问",
            (self.js_root / "modules" / "ohos" / "@ohos.batch2-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/ExtensionAbility组件.md",
            (self.js_root / "modules" / "ohos" / "@ohos.batch2-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/UIAbility组件启动模式.md#specified启动模式",
            (self.js_root / "modules" / "ohos" / "@ohos.batch2-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/申请访问剪贴板权限.md",
            (self.js_root / "modules" / "ohos" / "@ohos.batch2-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/@Reusable装饰器：V1组件复用.md",
            (self.js_root / "modules" / "ohos" / "@ohos.batch2-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/设置页签栏的悬浮样式.md#迷你栏",
            (self.js_root / "modules" / "ohos" / "@ohos.batch2-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/使用Picker选择媒体库资源.md#指定uri获取图片或视频资源",
            (self.js_root / "modules" / "ohos" / "@ohos.batch2-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/开发准备（媒体库）.md",
            (self.js_root / "modules" / "ohos" / "@ohos.batch2-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/代理提醒（ArkTS）.md#约束与限制",
            (self.js_root / "modules" / "ohos" / "@ohos.batch3-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/应用沙箱目录.md#应用文件目录与应用文件路径",
            (self.js_root / "modules" / "ohos" / "@ohos.batch3-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/交互基础机制说明.md#触摸测试",
            (self.js_root / "modules" / "ohos" / "@ohos.batch3-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/通过用户首选项实现数据持久化.md#gskv存储",
            (self.js_root / "modules" / "ohos" / "@ohos.batch3-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/使用RSA密钥对（PKCS1模式）签名验签.md",
            (self.js_root / "modules" / "ohos" / "@ohos.batch3-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/开通Device Security服务.md",
            (self.js_root / "modules" / "ohos" / "@ohos.batch3-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/配置ArkTS卡片的配置文件.md#sceneanimationparams标签",
            (self.js_root / "modules" / "ohos" / "@ohos.batch3-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/Worker简介.md#文件路径注意事项",
            (self.js_root / "modules" / "ohos" / "@ohos.batch3-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/UI国际化.md#镜像状态字符对齐",
            (self.js_root / "modules" / "ohos" / "@ohos.batch3-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/向用户申请授权.md",
            (self.js_root / "modules" / "ohos" / "@ohos.batch3-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../../guides/图片解码内存优化.md#系统默认的内存分配方式",
            (self.js_root / "modules" / "ohos" / "@ohos.batch3-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../components/ForEach.md",
            (self.js_root / "topics" / "misc" / "rendering-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../components/LazyForEach.md",
            (self.js_root / "topics" / "misc" / "rendering-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../components/Repeat.md",
            (self.js_root / "topics" / "misc" / "rendering-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "BuilderNode.md",
            (self.js_root / "topics" / "misc" / "rendering-guide.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "../components/mutableBuilder.md",
            (self.js_root / "topics" / "misc" / "rendering-guide.md").read_text(encoding="utf-8"),
        )
        self.assertNotIn(
            "#参数说明",
            (self.js_root / "topics" / "misc" / "rendering-guide.md").read_text(encoding="utf-8"),
        )
        self.assertNotIn(
            "#节点解绑",
            (self.js_root / "topics" / "misc" / "rendering-guide.md").read_text(encoding="utf-8"),
        )
        self.assertNotIn(
            "#storagelink",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertNotIn(
            "#触发更新",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertNotIn(
            "#状态变量state-variables",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertNotIn(
            "#ui上下文不明确",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertNotIn(
            "#命名路由",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertNotIn(
            "#密码模式",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )
        self.assertNotIn(
            "#基础概念",
            (self.js_root / "modules" / "ohos" / "@ohos.state-guide.md").read_text(encoding="utf-8"),
        )

        index_lines = self.paths.js_index.read_text(encoding="utf-8").splitlines()
        self.assertIn("topics/misc/native_handwrite_api.h.md", index_lines)
        self.assertIn("topics/misc/HandWrite.md", index_lines)
        self.assertIn("guides/状态管理V1-V2迁移指导.md", index_lines)
        self.assertIn("guides/窗口开发术语.md", index_lines)
        self.assertIn("guides/数据库备份与恢复.md", index_lines)
        self.assertIn("guides/NFC标签读写开发指南.md", index_lines)
        self.assertIn("guides/代理提醒（ArkTS）.md", index_lines)
        self.assertNotIn("capi/headers/native_handwrite_api.h.md", index_lines)
        references_index_lines = self.paths.references_index.read_text(encoding="utf-8").splitlines()
        self.assertIn("JsEtsAPIReference/topics/misc/native_handwrite_api.h.md", references_index_lines)
        self.assertIn("JsEtsAPIReference/guides/状态管理V1-V2迁移指导.md", references_index_lines)
        self.assertIn("JsEtsAPIReference/guides/窗口开发术语.md", references_index_lines)
        self.assertIn("JsEtsAPIReference/guides/数据库备份与恢复.md", references_index_lines)
        self.assertIn("JsEtsAPIReference/guides/NFC标签读写开发指南.md", references_index_lines)
        self.assertIn("JsEtsAPIReference/guides/代理提醒（ArkTS）.md", references_index_lines)
        self.assertIn("quickStart/intro.md", references_index_lines)

    def test_check_detects_index_drift(self) -> None:
        MODULE.rewrite_header_links(self.paths)
        MODULE.rewrite_targeted_guide_links(self.paths)
        self.paths.js_index.write_text("topics/misc/native_handwrite_api.h.md\n", encoding="utf-8")
        self.paths.references_index.write_text("quickStart/intro.md\n", encoding="utf-8")

        self.assertEqual(MODULE.check(self.paths), 1)

    def test_check_passes_after_generate(self) -> None:
        MODULE.rewrite_header_links(self.paths)
        MODULE.rewrite_targeted_guide_links(self.paths)
        MODULE.generate_references_index(self.paths)
        MODULE.generate_index(self.paths)

        self.assertEqual(MODULE.check(self.paths), 0)

    def test_check_detects_residual_targeted_guide_links(self) -> None:
        MODULE.rewrite_header_links(self.paths)
        MODULE.generate_references_index(self.paths)
        MODULE.generate_index(self.paths)

        self.assertEqual(MODULE.check(self.paths), 1)

    def test_classify_residual_detects_actionable_table_entry(self) -> None:
        text = "| params | LoginWithHuaweiIDButtonParams | 是 |\n"
        classification = MODULE.classify_residual(
            text,
            "LoginWithHuaweiIDButtonParams",
            "loginComponentManager (华为账号登录组件管理).md#section4717249182518",
        )
        self.assertEqual(classification, "actionable_internal_link")

    def test_classify_residual_ignores_code_only_occurrence(self) -> None:
        text = "```ets\nlet value: retrieval.RetrievalConfig = {}\n```\n"
        classification = MODULE.classify_residual(
            text,
            "retrieval.RetrievalConfig",
            "retrieval（检索器）.md#section95236010016",
        )
        self.assertEqual(classification, "code_or_signature_false_positive")

    def test_classify_residual_marks_external_and_guides_targets(self) -> None:
        self.assertEqual(
            MODULE.classify_residual("AppGallery Connect", "AppGallery Connect", "https://example.com/foo.md"),
            "external_link",
        )
        self.assertEqual(
            MODULE.classify_residual("collections类型", "collections类型", "../../guides/模块描述.md"),
            "historical_missing_guides_link",
        )


if __name__ == "__main__":
    unittest.main()
