# SwaadhSutra – AI-Powered Recipe Improver

AI system that transforms basic cooking ideas into structured, improved recipes using collaborative reasoning between specialized AI agents. The system analyzes a user’s input dish, researches improvements, optimizes preparation methods, and evaluates nutritional quality to generate a refined recipe.

---

# Overview

SwaadhSutra is a multi-agent AI application that enhances recipes through structured reasoning pipelines. Instead of a single LLM response, the system distributes tasks across specialized agents that collaborate to improve flavor balance, cooking techniques, and nutrition.

The architecture combines modern LLM orchestration with a full-stack web application and containerized microservices.

Core idea:
**Input → Multi-Agent Reasoning → Refined Recipe Output**

Users provide a dish idea or rough recipe. The system then produces a structured and optimized version including ingredients, cooking steps, and nutritional insights.

This project demonstrates real-world agentic AI infrastructure using CrewAI and production-ready backend services. 

---

# Key Features

## Multi-Agent AI Pipeline

Three specialized AI agents collaborate:

**Researcher**

* Searches cooking knowledge
* Identifies ingredient improvements
* Suggests cooking techniques

**Chef**

* Constructs the final improved recipe
* Refines flavor combinations
* Structures cooking instructions

**Nutritionist**

* Evaluates nutritional value
* Suggests healthier ingredient alternatives
* Ensures balanced meal composition

Each agent has a defined role and communicates sequentially to refine the final output.

---

## Real-Time Recipe Generation

Users submit:

* dish name
* base ingredients
* rough instructions

The system generates:

* improved ingredients list
* structured cooking steps
* preparation improvements
* nutritional insights

---

## Microservices Architecture

The system separates responsibilities across services:

Frontend
Handles user interaction and recipe input.

Backend API
Manages requests and communication with the AI service.

AI Processing Service
Runs the multi-agent reasoning pipeline.

Database
Stores generated recipes and user data.

This modular design allows scaling AI workloads independently.

---

# Technology Stack

## Frontend

* React
* TailwindCSS

Purpose:

* user interface
* recipe input
* displaying generated results

---

## Backend

* Node.js
* Express

Responsibilities:

* request routing
* API endpoints
* communication with AI microservice

---

## AI Service

* FastAPI
* CrewAI
* Groq API
* Mistral LLM

Responsibilities:

* agent orchestration
* reasoning pipelines
* recipe generation

---

## Database

* MongoDB

Used for:

* storing generated recipes
* persistent application data

---

## Infrastructure

* Docker

Purpose:

* containerized services
* reproducible deployments
* microservice isolation

---

# System Architecture

```
User
 │
 ▼
React Frontend
 │
 ▼
Node.js / Express Backend
 │
 ▼
FastAPI AI Microservice
 │
 ▼
CrewAI Multi-Agent Pipeline
 ├─ Researcher
 ├─ Chef
 └─ Nutritionist
 │
 ▼
Generated Recipe
 │
 ▼
MongoDB Storage
```

---

# How the AI Pipeline Works

### Step 1 — User Input

User provides:

* recipe idea
* ingredients
* cooking style

Example input:

```
Dish: Paneer Curry
Ingredients: Paneer, tomatoes, onions, spices
```

---

### Step 2 — Research Agent

Tasks:

* identify better ingredient pairings
* analyze cooking techniques
* propose improvements

Output example:

* use kasuri methi for aroma
* suggest roasting spices first

---

### Step 3 — Chef Agent

Transforms research into:

* structured recipe
* cooking steps
* flavor optimization

---

### Step 4 — Nutritionist Agent

Evaluates:

* calorie balance
* macro nutrients
* healthier substitutions

Example:

* replace cream with yogurt
* reduce oil quantity

---

### Step 5 — Final Recipe Generation

The system outputs a refined recipe containing:

* improved ingredients
* cooking instructions
* nutritional notes

---

# Project Structure

```
SwaadhSutra
│
├── frontend
│   ├── src
│   ├── components
│   └── pages
│
├── backend
│   ├── routes
│   ├── controllers
│   └── server.js
│
├── ai-service
│   ├── agents
│   ├── tasks
│   ├── crew
│   └── main.py
│
├── database
│
├── docker
│
└── README.md
```

---

# Installation

### 1. Clone the Repository

```
git clone https://github.com/vishnubm5/SwaadhSutraa.git
cd SwaadhSutraa
```

---

### 2. Install Dependencies

Frontend

```
cd frontend
npm install
```

Backend

```
cd backend
npm install
```

AI Service

```
cd ai-service
pip install -r requirements.txt
```

---

### 3. Environment Variables

Create `.env` files.

Example:

```
GROQ_API_KEY=your_api_key
MONGO_URI=your_mongodb_uri
```

---

### 4. Run the System

Start AI service

```
uvicorn main:app --reload
```

Start backend

```
npm run start
```

Start frontend

```
npm run dev
```

---

# Example Usage

Input

```
Dish: Veg Fried Rice
Ingredients: rice, vegetables, soy sauce
```

Output

```
Improved Ingredients
- jasmine rice
- garlic
- sesame oil
- spring onions

Cooking Steps
1. Stir fry garlic in sesame oil
2. Add vegetables and sauté
3. Add cooked rice
4. Season with soy sauce

Nutrition Notes
- balanced carbohydrates and fiber
- moderate sodium levels
```

---

# Why Multi-Agent Design

Single LLM prompts often produce shallow outputs.

Agent specialization improves:

* reasoning depth
* structured outputs
* domain-specific analysis
* collaborative problem solving

Each agent focuses on a distinct dimension of the recipe.

---

# Learning Outcomes

This project demonstrates:

* multi-agent LLM orchestration
* AI microservices architecture
* CrewAI agent pipelines
* Groq LLM integration
* full-stack AI applications
* Docker-based deployment

---

# Future Improvements

* user preference memory
* dietary restriction support
* ingredient substitution engine
* meal planning system
* recipe rating and feedback loop
* RAG system for culinary knowledge

---

# Author

Vishnu Bharadwaj
AI/ML Developer
GitHub: [https://github.com/vishnubm5](https://github.com/vishnubm5)
LinkedIn: [https://linkedin.com/in/vishnu-bharadwaj-m-4745192a2](https://linkedin.com/in/vishnu-bharadwaj-m-4745192a2)
