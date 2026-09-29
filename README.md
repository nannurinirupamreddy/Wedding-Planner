# 💍 AI Wedding Planner — Multi-Agent System

An AI-powered multi-agent wedding planning system that coordinates specialized agents to research venues, investigate pricing, manage budgets, and produce a practical wedding plan based on a user's requirements.

The project uses **LangChain**, **Google Gemini**, and the **Model Context Protocol (MCP)** to give AI agents access to external tools and real-world information.

Instead of asking a single LLM to solve the entire planning problem, the system decomposes the request into specialized responsibilities and coordinates multiple agents to generate a consolidated plan.

---

## 🚀 Overview

Planning a wedding involves several interconnected decisions:

- Where should the wedding be held?
- Does the venue support the required guest count and style?
- What do venues and vendors cost?
- Can everything fit within the total budget?
- Where can traveling guests stay?
- How should guests travel between locations?
- What should the wedding-day schedule look like?

A single AI agent can attempt to answer all of these questions, but the problem naturally contains several different areas of responsibility.

This project explores a **multi-agent architecture** where specialized agents handle different parts of the planning process and contribute their findings to the final wedding plan.

A request can look like:

> Plan a wedding for 120 guests in New York City with a total budget of $40,000. I would prefer an outdoor ceremony at a modern and elegant venue, with Indian and vegetarian-friendly catering. Several guests will be traveling from out of state, so include nearby hotel recommendations, transportation options, and realistic travel times. Research current venue and catering pricing where possible, create a practical wedding-day schedule, keep the overall plan within budget, and clearly identify any prices, availability, or other details that are uncertain or estimated.

The system processes the request through specialized agents and combines their research into a structured plan.

---

## ✨ Features

- 🤖 **Multi-Agent Architecture** — Breaks a complex wedding-planning request into specialized responsibilities
- 🏛️ **Venue Research** — Searches for venues based on location, guest count, style, and indoor/outdoor preferences
- 💰 **Pricing Research** — Investigates publicly available venue and vendor pricing
- 📊 **Budget Planning** — Organizes estimated expenses around the user's total wedding budget
- 🗺️ **Google Maps Integration** — Uses external location tools through MCP
- 🏨 **Guest Logistics** — Supports research involving nearby hotels and transportation
- ⏱️ **Travel-Time Planning** — Incorporates realistic location and travel considerations
- 📅 **Wedding-Day Planning** — Helps organize the researched information into a practical schedule
- 🔎 **Uncertainty Handling** — Distinguishes researched information from estimates or details that require confirmation
- 🧠 **Shared Planning Context** — Allows specialized components to contribute toward one consolidated result

---

## 🏗️ Architecture

The application uses multiple specialized AI agents rather than relying on one general-purpose prompt.

```text
                       User Request
                            |
                            v
                    Planning Workflow
                            |
          +-----------------+-----------------+
          |                 |                 |
          v                 v                 v
     Venue Agent       Pricing Agent      Budget Agent
          |                 |                 |
          v                 v                 v
   Google Maps MCP    Pricing Research   Budget Analysis
          |                 |                 |
          +-----------------+-----------------+
                            |
                            v
                  Shared Planning Context
                            |
                            v
                 Consolidated Wedding Plan
```

Each agent focuses on a narrower responsibility while contributing information to the overall planning workflow.

---

## 🤖 Agents

### 🏛️ Venue Agent

The Venue Agent is responsible for researching potential wedding venues.

It considers requirements such as:

- Wedding location
- Guest count
- Venue style
- Indoor/outdoor preference
- Nearby locations
- Geographic suitability

The agent has access to **Google Maps tools through MCP**, allowing it to use external location information rather than relying entirely on the language model's internal knowledge.

The agent is explicitly instructed **not to invent venue details** when reliable information is unavailable.

---

### 💵 Pricing Agent

The Pricing Agent researches publicly available pricing information for venues and other relevant wedding services.

Its output is designed around information such as:

- Vendor or venue
- Price or price range
- Included services
- Source information
- Confidence in the available pricing

Wedding pricing is often incomplete or unavailable publicly, so the agent distinguishes between researched prices and information that still requires confirmation.

This helps reduce the risk of presenting uncertain estimates as verified facts.

---

### 📊 Budget Agent

The Budget Agent focuses on the financial side of the wedding plan.

It uses the user's overall budget together with information collected during the planning process to help organize spending across the wedding.

The goal is to produce a plan that is financially realistic while making uncertainty visible when exact vendor pricing is unavailable.

---

## 🔌 Model Context Protocol (MCP)

The project uses the **Model Context Protocol (MCP)** to connect AI agents with external tools.

For example, the Venue Agent connects to a **Google Maps MCP server**.

Conceptually:

```text
Venue Agent
     |
     v
LangChain Agent
     |
     v
MCP Client
     |
     v
Google Maps MCP
     |
     v
Location / Place Information
```

This architecture allows the LLM to call specialized external tools when real-world information is needed.

The MCP client is integrated using `MultiServerMCPClient`.

---

## 🧠 AI Stack

The project combines several technologies for agent orchestration and external tool access.

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| LangChain | Agent creation and orchestration |
| Google Gemini | Language model used by the agents |
| Model Context Protocol (MCP) | Standardized external tool integration |
| Google Maps MCP | Location and venue research |
| Pydantic | Structured Python data models where needed |

---

## 🔄 Workflow

A typical execution begins with the user describing the wedding they want.

```text
User Wedding Request
        |
        v
Extract Planning Requirements
        |
        v
Research Relevant Information
        |
        +----------------------+
        |                      |
        v                      v
   Venue Research        Pricing Research
        |                      |
        +----------+-----------+
                   |
                   v
             Budget Planning
                   |
                   v
          Logistics / Scheduling
                   |
                   v
          Consolidated Wedding Plan
```

The final response combines the research into a useful plan while clearly identifying information that is uncertain, estimated, or requires direct confirmation.

---

## 📝 Example Request

```text
Plan a wedding for 120 guests in New York City with a total budget
of $40,000.

I would prefer an outdoor ceremony at a modern and elegant venue,
with Indian and vegetarian-friendly catering.

Several guests will be traveling from out of state, so include
nearby hotel recommendations, transportation options, and realistic
travel times.

Research current venue and catering pricing where possible, create
a practical wedding-day schedule, keep the overall plan within
budget, and clearly identify any prices, availability, or other
details that are uncertain or estimated.
```

---

## 📋 Example Output Structure

The resulting wedding plan can organize recommendations into sections such as:

```text
Wedding Plan

1. Venue
   - Recommended venue
   - Location
   - Capacity considerations
   - Style / ceremony fit
   - Pricing confidence

2. Catering
   - Catering strategy
   - Indian / vegetarian considerations
   - Estimated or researched pricing

3. Budget
   - Venue
   - Catering
   - Transportation
   - Accommodations / logistics
   - Other wedding expenses

4. Hotels
   - Nearby accommodation options
   - Location considerations

5. Transportation
   - Routes
   - Travel times
   - Guest transportation strategy

6. Wedding-Day Schedule
   - Setup
   - Guest arrival
   - Ceremony
   - Reception
   - Transportation

7. Uncertainties
   - Pricing requiring confirmation
   - Availability requiring confirmation
   - Estimated information
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd <YOUR_REPOSITORY_NAME>
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root and add the API credentials required by the services used by the project.

Example:

```env
GOOGLE_API_KEY=your_google_ai_api_key
GOOGLE_MAPS_API_KEY=your_google_maps_api_key
```

Never commit API keys to GitHub.

Add `.env` to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

---

## ▶️ Running the Project

Run:

```bash
python3 main.py
```

Enter a wedding request when prompted.

Example:

```text
Wedding request: Plan a wedding for 120 guests in New York City
with a total budget of $40,000...
```

The agents will research the request and produce a consolidated wedding plan.

---

## 🧩 Design Decisions

### Why Multi-Agent?

Wedding planning is not one task.

It combines:

```text
Venue Discovery
      +
Pricing Research
      +
Budgeting
      +
Transportation
      +
Accommodation
      +
Scheduling
      =
Wedding Plan
```

Separating these responsibilities makes it easier to give each agent a focused role and the tools appropriate for that role.

---

### Why MCP?

AI agents become much more useful when they can interact with external systems.

Rather than writing every integration directly into the agent itself, MCP provides a standardized way for agents to access external tools.

In this project, MCP allows the venue research workflow to interact with Google Maps capabilities.

---

### Why Explicit Uncertainty?

Real-world wedding information changes frequently.

Examples include:

- Venue availability
- Catering prices
- Venue rental prices
- Hotel rates
- Vendor packages

An LLM should not silently invent these details.

The agents are therefore prompted to identify uncertain or estimated information and avoid presenting unsupported details as confirmed facts.

---

## 💡 What I Learned

Building this project gave me hands-on experience designing a multi-agent AI system for a complex, open-ended real-world problem.

Instead of relying on a single LLM prompt, I learned how to decompose a larger problem into specialized responsibilities and coordinate multiple AI agents toward a shared objective.

Through the project, I gained experience with:

- Multi-agent system architecture
- LangChain agents
- Google Gemini
- Model Context Protocol (MCP)
- Google Maps MCP integration
- External tool calling
- Shared context between AI components
- Prompt engineering
- Grounding LLM responses with external information
- Handling uncertain real-world data
- Venue and vendor research workflows
- Pricing and budget reasoning
- Coordinating specialized agents into an end-to-end application

One of the biggest lessons from the project was that building useful AI agents involves much more than calling an LLM.

Reliable agentic applications require clear responsibilities, appropriate tools, good context management, grounded information, and explicit handling of uncertainty.

---

## 🔮 Possible Future Improvements

Although the core multi-agent workflow is complete, the project could be extended with:

- Web interface for entering wedding requirements
- Persistent wedding plans and user accounts
- Vendor comparison dashboards
- More MCP integrations
- Real-time venue availability integrations
- Calendar integration
- Interactive budget editing
- Persistent long-term planning memory
- Human approval checkpoints before major planning decisions
- Automated export of the final plan to PDF
- Additional specialized agents for catering, hotels, and transportation

---

## 📚 Related Concepts

This project explores several areas of modern AI engineering:

- AI Agents
- Agentic Workflows
- Multi-Agent Systems
- Large Language Models
- Tool Calling
- Model Context Protocol
- Context Engineering
- AI Orchestration
- Grounded Generation
- Human-in-the-Loop AI

---

## 👨‍💻 Author

**Nirupam Reddy Nannuri**

Computer Science  
Stony Brook University

- LinkedIn: `linkedin.com/in/nirupamreddy/`
- GitHub: `github.com/nannurinirupamreddy`

---

## 📄 License

This project was created for educational and portfolio purposes.
