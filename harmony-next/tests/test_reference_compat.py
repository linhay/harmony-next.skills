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
        self.assertEqual(guide_rewritten, 6)
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
        self.assertNotIn("capi/headers/native_handwrite_api.h.md", index_lines)
        references_index_lines = self.paths.references_index.read_text(encoding="utf-8").splitlines()
        self.assertIn("JsEtsAPIReference/topics/misc/native_handwrite_api.h.md", references_index_lines)
        self.assertIn("JsEtsAPIReference/guides/状态管理V1-V2迁移指导.md", references_index_lines)
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
