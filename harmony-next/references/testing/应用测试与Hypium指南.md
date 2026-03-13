# 应用测试与 Hypium 指南

本文为基于 HarmonyOS 官方文档整理的主题导读，聚合单元测试、UI 测试与自动化执行相关要点。

HarmonyOS 的应用测试体系以 **Hypium (HarmonyOS Python UI Test Framework)** 为核心，支持自动化单元测试和 UI 测试。

## 1. 单元测试 (Unit Test)
主要用于验证单个函数、类或逻辑模块的正确性。
*   **基础框架**：基于 `@ohos.testRunner` 模块提供运行时支持。
*   **断言库**：利用 `Hypium` 提供的断言能力（如 `expect().assertEqual()`）验证预期结果。
*   **Mock 机制**：支持模拟复杂的系统接口依赖，确保单元测试的独立性。
*   **最佳实践**：遵循 AAA (Arrange-Act-Assert) 模式编写测试用例。

## 2. UI 测试 (UI Test)
用于验证应用界面展示和用户交互逻辑。
*   **组件定位 (Find)**：
    *   通过属性定位：`By.text('Login')`、`By.id('btn_submit')`、`By.type('Button')`。
*   **模拟交互 (Action)**：
    *   支持模拟点击 (`click`)、滑动 (`scroll`)、双击、长按等事件。
*   **多模输入**：支持模拟键盘输入及多指触控事件。
*   **跨页面验证**：利用 `UiDriver` 驱动界面跳转，验证多页面流转是否正常。

## 3. 自动化测试执行 (CI/CD 集成)
*   **运行环境**：支持在真机 (Device) 或本地/远程模拟器 (Emulator/Simulator) 上运行。
*   **命令行触发**：
    可以通过 `hdc` 工具配合特定参数触发测试任务执行，便于集成到 Jenkins、GitLab CI 等自动化流水线中。
    *   例如：`hdc shell aa test -b [bundle_name] -m [module_name] -s unittest OpenHarmonyTestRunner`
*   **测试报告**：执行完成后，可在工程目录下生成详细的 HTML 格式测试报告。
