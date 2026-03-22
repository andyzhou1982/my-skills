# Stage Breakdown Patterns

Common patterns for breaking complex systems into learnable stages.

## Table of Contents
1. [RAG System Pattern](#rag-system-pattern)
2. [Web Application Pattern](#web-application-pattern)
3. [API Service Pattern](#api-service-pattern)
4. [Data Pipeline Pattern](#data-pipeline-pattern)
5. [General Principles](#general-principles)

---

## RAG System Pattern

7-stage breakdown for Retrieval-Augmented Generation systems.

| Day | Theme | Core Features |
|-----|-------|---------------|
| Day 1 | Minimal RAG | Upload → Chunk → Store → Retrieve → Generate |
| Day 2 | Preprocessing | Multi-format parsing, smart chunking, metadata |
| Day 3 | Retrieval | Hybrid search (vector + BM25), reranking |
| Day 4 | Generation | Streaming, citations, anti-hallucination |
| Day 5 | Evaluation | RAGAS metrics, request tracing |
| Day 6 | Security | JWT auth, ACL, audit logs |
| Day 7 | Production | Caching, metrics, Docker deployment |

**Key progression**:
- Core flow → Data quality → Search quality → Output quality → Measure → Secure → Deploy

---

## Web Application Pattern

6-stage breakdown for full-stack web applications.

| Day | Theme | Core Features |
|-----|-------|---------------|
| Day 1 | MVP | CRUD operations, basic UI, database |
| Day 2 | Auth | User registration, login, sessions |
| Day 3 | Features | Core business logic, forms, validation |
| Day 4 | Integration | Third-party APIs, webhooks |
| Day 5 | Polish | UI/UX improvements, error handling |
| Day 6 | Production | Caching, monitoring, deployment |

**Key progression**:
- Data model → Users → Business logic → Integrations → UX → Scale

---

## API Service Pattern

5-stage breakdown for backend API services.

| Day | Theme | Core Features |
|-----|-------|---------------|
| Day 1 | Core API | Endpoints, database, basic validation |
| Day 2 | Security | Authentication, authorization, rate limiting |
| Day 3 | Reliability | Error handling, retries, circuit breakers |
| Day 4 | Observability | Logging, metrics, tracing |
| Day 5 | Production | Docker, CI/CD, documentation |

**Key progression**:
- Functionality → Security → Reliability → Visibility → Deployment

---

## Data Pipeline Pattern

5-stage breakdown for data processing systems.

| Day | Theme | Core Features |
|-----|-------|---------------|
| Day 1 | Core Pipeline | Ingest → Transform → Store |
| Day 2 | Connectors | Multiple data sources, formats |
| Day 3 | Validation | Schema validation, data quality |
| Day 4 | Monitoring | Lineage, metrics, alerts |
| Day 5 | Production | Scheduling, scaling, deployment |

**Key progression**:
- Basic flow → Sources → Quality → Visibility → Scale

---

## General Principles

### The MVP Rule
Day 1 must demonstrate the COMPLETE core value proposition:
- User can accomplish the main task
- All layers work together (frontend + backend + data)
- Not a prototype - production-quality code

### Independence Rule
Each stage must be:
- Self-contained in its directory
- Runnable without other stages
- Fully documented

### Incremental Rule
Each day adds ONE major capability:
- Not multiple unrelated features
- Builds on previous day's foundation
- Clear theme and goal

### Documentation Rule
Each day includes:
- README (EN/CN)
- CHANGES.md explaining differences from previous day
- Updated planning files

### Naming Conventions
```
day1/     # Minimal/RAG/MVP
day2/     # Enhancement name
day3/     # Enhancement name
...
dayN/     # Production/Complete
```
