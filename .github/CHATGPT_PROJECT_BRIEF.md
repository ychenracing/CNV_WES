# ChatGPT Project Brief

> 本文件只保存长期稳定、仓库级的信息。当前任务、临时分支、SHA、测试状态和执行进度应保存在当前 Pull Request 正文中。

## 1. Project

- 项目名称：CNV_WES
- GitHub 仓库：`ychenracing/CNV_WES`
- 默认分支：`master`
- 系统定位：为 WES 数据生成和运行多种 CNV 检测工具命令的 Python 脚本集合。
- 项目最终目标：更完整的业务目标与验收口径未在仓库文档中明确。

## 2. Purpose and Non-Goals

仓库按数据环境组织脚本，用于准备输入、生成 shell 命令，并调用 CNVer、CNVnator、CoNIFER 和 SeqCNV 等外部工具。

长期非目标未在仓库文档中明确。仓库没有统一工作流引擎、服务、用户界面、可移植安装包或临床诊断说明，不应自行假定这些职责。

## 3. Architecture and Module Boundaries

- `WES/16/Run_CNVTools/`：针对 16 样本/指定数据环境生成或运行多种 CNV 工具命令。
- `WES/16/Other_tools/`：BAM 准备和辅助 shell 生成。
- `WES/Baylor/`：Baylor 数据环境的工具运行脚本。
- `WES/Local/Run_CNVTools/`：本地数据环境的 CNV 工具脚本。
- `WES/Local/Other_tools/`：从外部来源提取 CNV 及其他准备工具。

各脚本是其外部工具命令和文件布局的 Owner；外部 CNV 程序、BAM/bed 数据及运行环境不属于本仓库。仓库没有统一配置 Owner，路径和工具位置直接存在于脚本中；不得在治理文档中复制为通用默认值。

## 4. Non-Negotiable Constraints

- 脚本依赖外部 CNV 工具、样本文件和目录布局；仓库本身不提供这些依赖。
- 当前脚本使用旧版 Python 语法；Python 版本和兼容性目标未在仓库文档中正式定义。
- 环境专用路径、样本标识和生成命令必须按目标环境核验，不得从旧脚本推断为通用生产配置。
- 仓库未定义医学、临床或诊断用途；不得把研究流水线描述为临床结论系统。
- 研究数据、样本标识、本地绝对路径或凭据不得复制到治理文件和 PR 模板中。

## 5. Authoritative Sources

- 项目名称：`README.md`
- 工程约定：`AGENTS.md`
- 16 样本工具入口：`WES/16/Run_CNVTools/`
- 16 样本辅助工具：`WES/16/Other_tools/`
- Baylor 工具入口：`WES/Baylor/`
- 本地工具入口：`WES/Local/Run_CNVTools/`
- 本地辅助工具：`WES/Local/Other_tools/`
- 依赖、数据 schema、Python 版本、测试、发布和运行环境权威来源：未在仓库中定义

## 6. Standard Commands

- 安装：未在仓库中定义。
- 构建：不适用；仓库未定义构建流程。
- 单元测试、集成测试、lint、类型检查和格式检查：未在仓库中定义。
- 本地运行：各脚本可作为独立入口，但具体命令、外部程序、Python 版本、数据和权限准备均未在仓库中统一定义。
- 关键验收命令：未在仓库中定义。

## 7. Important Paths

- `WES/16/Run_CNVTools/`：16 样本 CNV 工具运行脚本。
- `WES/16/Other_tools/`：16 样本数据准备和命令生成。
- `WES/Baylor/`：Baylor 环境运行脚本。
- `WES/Local/Run_CNVTools/`：本地环境运行脚本。
- `WES/Local/Other_tools/`：本地环境辅助工具。
- `README.md`：项目名称。
- `AGENTS.md`：渐进式验证约定。

## 8. CI and Acceptance Entry Points

- 仓库没有 `.github/workflows/`，未定义 GitHub Actions 门。
- 本地验证应遵循 `AGENTS.md` 的影响范围驱动原则。
- 项目没有统一 Definition of Done；脚本行为变更需要在目标环境对生成命令、输入文件和外部工具调用进行核验。
- 纯文档治理只需验证 Markdown、路径、引用和 diff 范围。

## 9. Prohibited Actions

- 不得把研究流水线描述为临床诊断或医学建议。
- 不得把脚本中的环境专用绝对路径、样本数据或隐私信息复制到治理文件。
- 不得假定外部 CNV 工具、数据或目录在任意环境可用。
- 不得擅自改写 Git 历史或 force push。
- 不得丢弃未知或未提交工作，也不得覆盖无关改动。
- 不得把计划执行写成已验证完成。
- 不得根据旧聊天猜测当前分支、SHA、PR 或 CI 状态。

## 10. Context Loading Protocol

1. 新开发任务可以直接使用自然语言提出，不要求预先填写固定 Prompt。
2. 开始任务时先读取本文件。
3. 搜索与任务相关的开放 PR、分支和 Issue。
4. 如果存在匹配工作，从现有现场原地继续。
5. 当前动态任务状态默认维护在 Pull Request 正文。
6. 不强制普通单 PR 任务创建 Issue。
7. 优先读取目标代码、直接调用者、相关测试和直接相关配置。
8. 只有证据不足、状态冲突或影响范围扩大时才扩大读取。
9. 不默认加载完整仓库、完整聊天、完整日志或全部 GitHub Actions 历史。
10. 长对话交接使用 `conversation-continuity-guard`，但 GitHub 当前现场仍是状态权威来源。

## 11. References

- `README.md`
- `AGENTS.md`
- `WES/16/Run_CNVTools/`
- `WES/16/Other_tools/`
- `WES/Baylor/`
- `WES/Local/Run_CNVTools/`
- `WES/Local/Other_tools/`
