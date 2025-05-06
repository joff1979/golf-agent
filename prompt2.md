# Architecture Repository – AI Prompt Playbook

This guide helps you accelerate development, documentation, and architecture work using ChatGPT and GitHub Copilot.

---

## Table of Contents

1. [Frontend UI Prompts](#1-frontend-ui-prompts)  
2. [C# API Prompts](#2-c-api-prompts)  
3. [Architecture Diagrams](#3-architecture-diagrams)  
4. [Testing (Unit + Integration)](#4-testing-unit--integration)  
5. [CI/CD & Security](#5-cicd--security)  
6. [Debugging Prompts](#6-debugging-prompts)  
7. [Architecture Documentation](#7-architecture-documentation)  
8. [Business Capability Mapping](#8-business-capability-mapping)

---

## 1. Frontend UI Prompts

```markdown
I’m building a React + TypeScript SPA. Please generate a component that:

- Fetches data from `/api/platforms`
- Uses useEffect + useState
- Displays platform name, type, and domain
- Uses Tailwind CSS
- Follows this style:
```tsx
[Insert component]
```
```

**Copilot comment:**
```tsx
// Fetch and display all platforms with Tailwind UI
```

---

## 2. C# API Prompts

```markdown
I’m working on a C# API with Cosmos DB. Please help me:

- Add endpoint to get platforms by domain
- Use async/await, DI, DTOs
```csharp
[Insert code]
```
```

**Copilot comment:**
```csharp
// GET /api/domains/{id}/platforms — query Cosmos DB and return DTO list
```

---

## 3. Architecture Diagrams

**Generate diagram:**
```markdown
Create a [Mermaid / PlantUML] diagram:
- React frontend → C# API → Cosmos DB
- Azure DevOps deploys all components
Top-down flow preferred.
```

**Explain diagram:**
```markdown
Explain this diagram for business stakeholders, focusing on flow and component purpose.
```mermaid
[Diagram here]
```

---

## 4. Testing (Unit + Integration)

**Unit tests:**
```markdown
Write xUnit + Moq tests for this method:
```csharp
[Insert method]
```
- Mock Cosmos DB
- Handle edge cases
```

**Integration tests:**
```markdown
Set up integration tests using Cosmos DB emulator. Verify response from /api/platforms.
```

**Copilot comment:**
```csharp
// Unit test for GetPlatformsByDomainAsync with mocks and error case
```

---

## 5. CI/CD & Security

**Azure DevOps pipeline:**
```markdown
Generate a pipeline that:
- Builds UI + API
- Runs tests
- Deploys with Bicep
- Fails on lint/lint/test errors
```

**Security scanning:**
```markdown
Scan Docker and Bicep with GitHub Advanced Security.
Fail pipeline on critical vulnerabilities.
```

**Code security review:**
```markdown
Review this code for hardcoded secrets, missing validation, insecure logging.
```csharp
[Code here]
```

---

## 6. Debugging Prompts

```markdown
Error debugging prompt:

**Tech stack:** [e.g. React, C#]  
**What I was doing:** [e.g. fetch data from API]  
**Error:** [Paste error message]  
**Relevant code:** [Paste snippet]  
**What I’ve tried:** [List steps]

Help me understand and fix this.
```

**Copilot comment:**
```tsx
// useEffect doesn’t trigger API call – check dependency array
```

---

## 7. Architecture Documentation

**From notes:**
```markdown
I’m documenting a system for [audience]. Convert these notes into structured architecture docs with:

- Overview
- Components
- Data Flow
- Security
- Integration
```

**Diagram narration:**
```markdown
Explain each section of the following diagram for business/tech teams:
```mermaid
[Diagram]
```

---

## 8. Business Capability Mapping

**Feature to capability:**
```markdown
Map these features to Level 1/2 capabilities:
- Payment processing
- KYC onboarding
- Account services
```

**Capability → Process → System:**
```markdown
Organize this in a 3-column table:
- Capability
- Supporting Process
- System(s)
```

**Business narrative:**
```markdown
Write a business-facing explanation of how the platform enables:
- [Capabilities]
Audience: Executives. Focus on outcomes.
```

---

Let me know if you'd like a Notion-style version, embedded diagrams, or starter files for each section.