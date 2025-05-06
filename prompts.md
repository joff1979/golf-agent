# AI Development Prompts & Templates for Golf Agent Project

## 1. ChatGPT Prompt – Dev to Prod Transition

I'm working on [project/agent name]. I've completed [brief summary of what’s working]. I'm now trying to [specific goal – e.g., deploy to Azure as a multi-container app, secure API endpoints, etc.].

**Setup Overview:**
- Language: [e.g., Python 3.11]
- Stack: [e.g., Docker + FastAPI + Cosmos DB]
- Constraints: [e.g., no LangChain, using Ollama container]

**Request:**
1. Review this config/code: [paste or describe]
2. Identify issues for production readiness
3. Suggest improvements or best practices

Optional: Provide a deployment checklist.

---

## 2. Daily Reflection — [Date]

**What I did today:**  
- [E.g., Got the golf agent running in a container locally]  
- [Connected it to Cosmos DB using production credentials]  

**What worked well:**  
- [AI tools really accelerated deployment]  
- [Prompting ChatGPT with full context saved time]  

**What was tricky or broke:**  
- [Ollama model load was too slow in container]  
- [Couldn’t get environment variables working cleanly]  

**What I’ll do tomorrow / next:**  
- [Refactor for better container health checks]  
- [Start wiring the React frontend to API]  

**Prompt for tomorrow:**  
> “I have an API running in Azure Container Apps and I want to connect my React frontend to it securely. What’s the best approach for auth and API calls?”

---

## 3. Meta-Prompt: Generate GitHub Copilot Prompts

I'm writing a [Dockerfile / docker-compose.yaml / Python script] and want to guide GitHub Copilot to generate the right code for me.

Can you write an inline comment or code stub that will guide Copilot to:
- [Goal: e.g., set up a multi-container app with FastAPI and Ollama]
- [Constraints: e.g., environment variables from Azure, production-optimized]

Please format it as a Copilot-friendly comment or starter block.

---

## 4. Container Optimization Prompt

I’m working on a Docker-based deployment for a multi-container agent app (FastAPI + Ollama). It's working, but the workflow feels inefficient — too much manual copy/paste and hard to iterate.

Can you:
1. Suggest a cleaner dev loop for testing containers locally before pushing to Azure Container Apps?
2. Recommend ways to structure my Dockerfiles or `docker-compose.yaml` for faster iteration (e.g., mounts, caching)?
3. Optionally generate a GitHub Copilot-style prompt that would help me automate part of this (like building both images together).

---

## 5. Automating Agent Setup Prompt

I want to automate the startup process for my agent app using Python — it should:
- Start both the FastAPI server and connect to the Ollama model
- Load config from environment variables
- Handle failures gracefully (like model not responding)

Can you give me:
1. A high-level Python script to use as a base
2. A GitHub Copilot-style prompt to generate helper functions (e.g., load config, check model health)

---

## 6. Container Debugging Assistance Prompt

My container setup includes FastAPI and Ollama, and I’m running it via `docker-compose`. One or more services don’t start correctly, but I’m not getting useful logs.

Can you:
1. Suggest ways to improve my docker-compose config for better visibility (e.g., health checks, logs, command overrides)?
2. Recommend good Copilot prompts to add inline for writing a `healthcheck` section or retry logic in my Python startup?