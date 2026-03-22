#!/usr/bin/env python3
"""
Initialize planning files for iterative project
初始化迭代项目的规划文件

Usage: python init_planning.py [project_name]
"""

import os
import sys
from pathlib import Path
from datetime import datetime

# Planning file templates
TASK_PLAN_TEMPLATE = '''# Task Plan: {project_name}
<!--
  WHAT: {project_name} 的分阶段实施方案
  WHY: 将复杂系统拆解为可学习的阶段性模块
  WHEN: 在开始任何工作之前创建，每个阶段完成后更新
-->

## Goal
<!--
  目标：创建一个循序渐进的项目，从最小化实现逐步演进到完整系统
-->
[Describe the project goal - 描述项目目标]

## Current Phase
Phase 1: Planning Complete - Ready for Day 1

## Technology Stack Decisions
| Component | Choice | Rationale |
|-----------|--------|-----------|
| Backend | [TBD] | [Reason] |
| Frontend | [TBD] | [Reason] |
| Database | [TBD] | [Reason] |

## Phases Overview

### Day 1: [MVP Theme]
- [ ] [Feature A]
- [ ] [Feature B]
- **Status:** pending
- **Goal:** [What Day 1 achieves]

### Day 2: [Enhancement Theme]
- [ ] [Feature C]
- **Status:** pending
- **Goal:** [What Day 2 adds]

### Day 3: [Enhancement Theme]
- [ ] [Feature D]
- **Status:** pending
- **Goal:** [What Day 3 adds]

### Day N: Production Ready
- [ ] Performance optimization
- [ ] Docker deployment
- [ ] Complete documentation
- **Status:** pending
- **Goal:** Production deployment ready

## Key Questions
1. Technology stack selection?
2. Acceptance criteria for each phase?
3. How to ensure each phase is independently runnable?

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| (To be filled) | - |

## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
| (To be filled) | - | - |

## Notes
- Each phase must be independently runnable
- All code comments use bilingual format
- Verify end-to-end functionality after each phase
'''

FINDINGS_TEMPLATE = '''# Findings & Decisions
<!--
  WHAT: {project_name} 的研究发现和技术决策记录
  WHY: 持久化存储关键信息，防止上下文丢失
  WHEN: 每次有新发现时更新
-->

## Requirements Summary
<!--
  从需求文档提取的核心需求
-->
[Summarize core requirements from requirement document]

## Technical Stack Details
<!--
  技术栈详细说明
-->

### Backend
| Component | Library | Purpose |
|-----------|---------|---------|
| [Component] | [Library] | [Purpose] |

### Frontend
| Component | Library | Purpose |
|-----------|---------|---------|
| [Component] | [Library] | [Purpose] |

## Research Findings
<!--
  关键研究发现
-->

### Core Architecture
```
[Architecture diagram or flow]
```

## Technical Decisions
| Decision | Rationale |
|----------|-----------|
| (To be filled) | - |

## Implementation Patterns
<!--
  实现模式参考
-->

### Code Pattern Example
```python
# Example code pattern
# 示例代码模式
```

## Resources
- [Useful resources and references]

## Issues Encountered
| Issue | Resolution |
|-------|------------|
| (To be filled) | - |
'''

PROGRESS_TEMPLATE = '''# Progress Log
<!--
  WHAT: {project_name} 的进度日志
  WHY: 记录每个阶段的详细进展
  WHEN: 每个阶段完成或有重要进展时更新
-->

## Session: {date}

### Phase 1: Planning
- **Status:** complete
- **Started:** {date}
- Actions taken:
  - Created planning files
  - Analyzed requirements
  - Proposed technology stack
- Files created:
  - task_plan.md
  - findings.md
  - progress.md

### Phase 2: Day 1 Implementation
- **Status:** pending
- **Started:** [Date]
- Actions taken:
  - (To be filled)
- Files created/modified:
  - (To be filled)

## Daily Progress Plan
<!--
  每日计划与实际进度对比
-->

| Day | Plan | Status | Key Deliverables |
|-----|------|--------|------------------|
| Day 1 | [Theme] | pending | [Deliverables] |
| Day 2 | [Theme] | pending | [Deliverables] |
| Day N | Production | pending | [Deliverables] |

## Test Results
<!--
  测试结果记录
-->
| Test | Input | Expected | Actual | Status |
|------|-------|----------|--------|--------|
| (To be filled) | | | | |

## Error Log
<!--
  错误日志
-->
| Timestamp | Error | Attempt | Resolution |
|-----------|-------|---------|------------|
| (To be filled) | | | |

## 5-Question Reboot Check
<!--
  上下文检查：如果能回答这 5 个问题，说明上下文完整
-->
| Question | Answer |
|----------|--------|
| Where am I? | [Current phase] |
| Where am I going? | [Next phases] |
| What's the goal? | [Project goal] |
| What have I learned? | [Key learnings] |
| What have I done? | [Completed work] |

## Next Actions
<!--
  下一步行动项
-->
1. [Action 1]
2. [Action 2]

---
*Update after completing each phase or encountering errors*
'''

DAY_README_TEMPLATE = '''# {project_name} - Day {day}

## {theme}

{description}

---

## Features

{features}

---

## Quick Start

### Prerequisites
- [Requirement 1]
- [Requirement 2]

### 1. Setup

```bash
# Backend setup
cd backend
[setup commands]

# Frontend setup
cd frontend
[setup commands]
```

### 2. Run

```bash
# Start backend
[run command]

# Start frontend
[run command]
```

### 3. Access

| Service | URL |
|---------|-----|
| Frontend | http://localhost:3000 |
| Backend API | http://localhost:8000 |
| API Docs | http://localhost:8000/docs |

---

## Changes from Day {prev_day}

### New Features
- [Feature 1]
- [Feature 2]

### Modified Files
- `file1.ext`: [Change description]
- `file2.ext`: [Change description]

### New Dependencies
- `dependency`: [Purpose]

---

## Architecture

```
[Architecture diagram]
```

---

## License

MIT License
'''

CHANGES_TEMPLATE = '''# Day {day} Changes

## Theme
{theme}

## New Features

### 1. [Feature Name]
- Description of the feature
- How it works

## Modified Files

| File | Changes |
|------|---------|
| `file.ext` | Added function X, modified Y |

## New Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `package` | `1.0.0` | Purpose description |

## API Changes

### New Endpoints
- `POST /new-endpoint`: Description

### Modified Endpoints
- `GET /existing`: Added parameter X

## Configuration Changes

```bash
# New environment variables
NEW_VAR=value
```

## Testing

### Test Coverage
- Unit tests: [X]%
- Integration tests: [X]%

### Manual Testing
1. [Test step 1]
2. [Test step 2]

## Known Issues
- [Issue 1]

## Next Steps
- [Future enhancement 1]
'''


def create_planning_files(project_name: str, output_dir: Path):
    """Create planning files in the project directory"""
    date = datetime.now().strftime("%Y-%m-%d")

    # Create planning files
    files = {
        "task_plan.md": TASK_PLAN_TEMPLATE.format(project_name=project_name),
        "findings.md": FINDINGS_TEMPLATE.format(project_name=project_name),
        "progress.md": PROGRESS_TEMPLATE.format(
            project_name=project_name,
            date=date
        )
    }

    for filename, content in files.items():
        filepath = output_dir / filename
        if not filepath.exists():
            filepath.write_text(content, encoding='utf-8')
            print(f"Created: {filepath}")
        else:
            print(f"Exists: {filepath}")

    print(f"\nPlanning files initialized for: {project_name}")
    print("Next steps:")
    print("1. Edit task_plan.md with phase breakdown")
    print("2. Update findings.md with research notes")
    print("3. Start Day 1 implementation")


def main():
    if len(sys.argv) < 2:
        print("Usage: python init_planning.py <project_name>")
        print("Example: python init_planning.py my-rag-project")
        sys.exit(1)

    project_name = sys.argv[1]
    output_dir = Path.cwd()

    create_planning_files(project_name, output_dir)


if __name__ == "__main__":
    main()
