# Iterative Builder (中文版)

循序渐进构建生产级项目的 Claude Code 插件。

## 功能

- 从需求文本描述自动分析并规划分阶段实施方案
- 支持 RAG 系统、Web 应用、API 服务、数据管道等常见场景
- 提供技术栈选项供用户选择
- 创建完整的规划文件模板
- 增量阶段构建：Day 1 MVP → Day N 生产级

## 安装

将此插件目录复制到 Claude Code 插件目录，或使用：

```bash
cc --plugin-dir /path/to/iterative-builder-zh
```

## 使用方法

```bash
/build <需求描述>
```

示例：
```bash
/build 创建一个 RAG 文档问答系统，支持 PDF 上传、智能分块和流式回答
```

## 工作流程

1. **需求分析** - 从描述中提取核心功能
2. **技术栈选择** - 展示选项供用户选择或自定义
3. **阶段规划** - 创建 task_plan.md、findings.md、progress.md
4. **增量实现** - Day 1 MVP 开始，逐步增强到生产级

## 组件

- **Command**: `/build` - 启动项目构建流程
- **Skill**: `iterative-project-builder-zh` - 提供方法论和模板

## 许可证

MIT
