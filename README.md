# MCP-Hackathon--Red-Hat-Ticket-Concierge
# 🛠️ Red Hat Ticket Concierge Agent (MCP + LlamaStack)

This project implements a secure, context-aware MCP agent that helps Red Hat employees open the correct internal ServiceNow ticket for common requests like badge access, locker assignment, and payroll support.

## 🚀 Use Case

Employees often struggle to find and fill the correct internal ticket forms across Red Hat's ServiceNow system. This agent streamlines the process by:
- Understanding a natural language request (e.g. "I lost my badge")
- Matching it to a known ticket type
- Prefilling the ticket form fields
- Opening the correct ServiceNow URL in the user's browser (with cookies)
- Leaving the final submission step to the user for security compliance

---

## 🧠 Agent Capabilities

- Classifies requests using a keyword-based matcher
- Integrates with a ticket catalog (`tickets.json`) of known ticket types
- Uses browser cookies to authenticate the user securely
- Displays ticket data in the terminal and launches the ticket form in the browser

---

## ✅ Features & Architecture

| Component              | Description                                                              |
|------------------------|--------------------------------------------------------------------------|
| **MCP Server**         | FastAPI-based MCP-compatible server that handles agent requests          |
| **LlamaStack Agent**   | Implements a registered agent with modular `Tool`s                       |
| **Ticket Matching Tool**| Classifies user intent and returns correct URL + prefill fields          |
| **CLI UI**             | Prompts user for intent, then opens ticket in browser                    |
| **Cookie Auth**        | Uses exported cookies to open prefilled ServiceNow forms securely        |

---

## 🧩 Ticket Types Supported

| Type              | Trigger Keywords                            | ServiceNow URL                                                                 |
|-------------------|---------------------------------------------|--------------------------------------------------------------------------------|
| **Badge Request** | "badge", "id", "access card"                | `https://redhat.service-now.com/help?id=sc_cat_item&sys_id=ac8bb875a82282004c7185ae62325874` |
| **Locker Request**| "locker", "cabinet", "drawer"               | `https://redhat.service-now.com/help?id=sc_cat_item&sys_id=a4d32a92978299907d14f0f3a253af04` |
| **Payroll Support**| "payroll", "salary", "missing paycheck"     | `https://redhat.service-now.com/help?id=sc_cat_item&sys_id=52f7f93f97d309187d14f0f3a253aff5` |

---

## 🔐 Security Model

- This system **does not submit** the form automatically.
- Only the **user** can submit the form after it is opened.
- Authentication is handled via browser cookies (stored in `cookies.json`).

---
