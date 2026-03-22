---
name: iterative-project-builder
description: Build complex production-ready projects iteratively from requirements. Use when: (1) Creating tutorial-style projects with multiple stages, (2) Breaking down complex systems into learnable phases, (3) Building MVP to production pipeline, (4) User requests "step-by-step" or "day by day" project structure, (5) Need independent runnable stages with incremental features. Transforms requirements into phased implementation with each stage building on the previous.
---

# Iterative Project Builder

Build production-ready systems through incremental, learnable stages.

## Core Methodology

```
Requirement Document
        |
        v
   [Phase Planning]
        |
   +----+----+
   |    |    |
  Day1 Day2 ... DayN
  MVP  +feat  Production
   |
   v
Each day: Independent + Runnable + Documented
```

## Phase 1: Analyze Requirements

### 1.1 Extract Core Modules
From the requirements document, identify:
- **Essential features** (must have for MVP)
- **Enhancement features** (nice to have)
- **Production features** (deployment, monitoring, security)

### 1.2 Technology Stack Decision
Before implementation, propose stack options and let user choose:
```
| Component | Option A | Option B | Rationale |
|-----------|----------|----------|-----------|
| Backend   | FastAPI  | Flask    | ...       |
| Frontend  | React    | Vue      | ...       |
| Database  | Postgres | MongoDB  | ...       |
```

### 1.3 Create Planning Files
Run `scripts/init_planning.py` to create:
- `task_plan.md` - Phases, decisions, progress
- `findings.md` - Research, technical notes
- `progress.md` - Session log, test results

## Phase 2: Plan Stages

### 2.1 Stage Breakdown Strategy
See [references/stage-patterns.md](references/stage-patterns.md) for common patterns.

**Typical breakdown**:
| Day | Theme | Goal |
|-----|-------|------|
| Day 1 | MVP | Core flow: input → process → output |
| Day 2 | Enhancement 1 | Add feature X |
| Day 3 | Enhancement 2 | Add feature Y |
| Day N | Production | Deploy, monitor, optimize |

### 2.2 Stage Independence Rules
Each stage MUST:
- Have its own directory (`day1/`, `day2/`, ...)
- Be fully runnable without other stages
- Include complete frontend AND backend
- Have its own README and documentation

### 2.3 Document in task_plan.md
```markdown
## Phases Overview

### Day 1: [Theme]
- [ ] Feature A
- [ ] Feature B
- **Status:** pending
- **Goal:** [What this stage achieves]

### Day 2: [Theme]
...
```

## Phase 3: Implement Day 1 (MVP)

### 3.1 Directory Structure
```
day1/
├── backend/
│   ├── src/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── routers/
│   │   ├── services/
│   │   └── models/
│   └── test/
├── frontend/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── components/
│   │   └── api/
│   └── package.json
├── readme.md
└── readme_cn.md
```

### 3.2 MVP Principles
- **Minimal but complete** - Core flow works end-to-end
- **No shortcuts** - Proper error handling, validation
- **Clean architecture** - Patterns that scale
- **Bilingual comments** - See [references/bilingual-comments.md](references/bilingual-comments.md)

### 3.3 Verify Day 1
```bash
# Backend compiles
cd day1/backend && python -m py_compile src/*.py

# Frontend builds
cd day1/frontend && npm run build
```

## Phase 4: Implement Subsequent Days

### 4.1 Copy Previous Day
```bash
cp -r day1 day2
```

### 4.2 Add Incremental Features
Each day adds ONE major feature area:
- Day 2: Enhanced preprocessing
- Day 3: Optimized retrieval
- Day 4: Better generation
- etc.

### 4.3 Document Changes
Create `CHANGES.md` for each day:
```markdown
# Day N Changes

## New Features
- Feature X: Description

## Modified Files
- `file.py`: Added function Y

## New Dependencies
- `library`: purpose
```

### 4.4 Update Planning Files
After each day:
1. Update `task_plan.md` - Mark day complete
2. Update `findings.md` - Document learnings
3. Update `progress.md` - Log actions

## Phase 5: Final Day (Production)

### 5.1 Production Checklist
- [ ] Caching (Redis/in-memory)
- [ ] Error handling & retry
- [ ] Rate limiting
- [ ] Performance metrics
- [ ] Docker configuration
- [ ] Health checks
- [ ] Complete documentation

### 5.2 Docker Setup
```
docker-compose.yml
├── postgres (with extensions)
├── redis (caching)
├── backend (FastAPI)
└── frontend (nginx)
```

### 5.3 Documentation
- README in English and Chinese
- API documentation (auto-generated)
- Architecture diagrams
- Deployment guide

## Resources

### scripts/
- `init_planning.py` - Initialize planning files

### references/
- `stage-patterns.md` - Common stage breakdown patterns
- `bilingual-comments.md` - Comment format guidelines

### assets/
- `task_plan.md` - Template for phase planning
- `findings.md` - Template for research notes
- `progress.md` - Template for session logging

## Quick Reference

| Task | Command |
|------|---------|
| Init planning files | `python scripts/init_planning.py` |
| Start Day N | Copy `day(N-1)` to `dayN` |
| Verify stage | Build check + manual test |
| Complete stage | Update all planning files |
