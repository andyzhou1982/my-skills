# Iterative Builder (中文版)

循序渐进构建生产级项目的 Claude Code 插件。

## 功能

- 从需求文本描述自动分析并规划分阶段实施方案
- 支持 RAG 系统、Web 应用、API 服务、数据管道等常见场景
- 会话中断后可恢复上下文继续构建
- 支持 bug 修复并自动分析影响范围

## 安装

将此插件目录复制到 Claude Code 插件目录，或使用：

```bash
cc --plugin-dir /path/to/iterative-builder-zh
```

## 命令

### `/build` - 启动新项目

从需求描述开始构建项目，支持技术栈选择。

```bash
/build <需求描述>
```

示例：
```bash
/build 创建一个 RAG 文档问答系统，支持 PDF 上传、智能分块和流式回答
```

### `/continue` - 恢复项目

读取项目规划文件，恢复上下文后继续构建。

```bash
/continue [项目目录]
```

示例：
```bash
/continue                    # 当前目录
/continue ./my-rag-project   # 指定目录
```

### `/fix` - 修复 Bug

报告 bug 并触发修复，自动分析影响范围。

```bash
/fix <bug描述>
```

示例：
```bash
/fix Day 2 的 API 返回格式和前端期望不一致
/fix 文档上传后分块数量总是 0
/fix 搜索响应时间超过 10 秒
```

## 工作流程

1. **需求分析** - 从描述中提取核心功能
2. **技术栈选择** - 展示选项供用户选择或自定义
3. **阶段规划** - 创建 task_plan.md、findings.md、progress.md
4. **增量实现** - Day 1 MVP 开始，逐步增强到生产级
5. **中断恢复** - 随时使用 `/continue` 恢复上下文
6. **Bug 修复** - 使用 `/fix` 修复问题并评估影响

## 组件

| 组件 | 名称 | 说明 |
|------|------|------|
| Command | `/build` | 启动项目构建流程 |
| Command | `/continue` | 恢复中断的项目会话 |
| Command | `/fix` | 触发 bug 修复流程 |
| Agent | `bug-fixer` | 修正 bug 并分析影响范围 |
| Skill | `iterative-project-builder-zh` | 提供方法论和模板 |

## 规划文件

每个项目包含三个核心文件：

| 文件 | 用途 |
|------|------|
| `task_plan.md` | 阶段规划、技术决策、进度 |
| `findings.md` | 研究发现、技术笔记 |
| `progress.md` | 会话日志、测试结果、修复记录 |

## 许可证

MIT
