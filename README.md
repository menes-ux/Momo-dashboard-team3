# 📊 MoMo Data Analysis Dashboard

**Enterprise Web Development - Group Assignment 1**

![Project Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Team Members (Group 5)

| Role | Name | GitHub Username |
| :--- | :--- | :--- |
| **Team Lead / DevOps** | [Student 1 Name] | @username |
| **Backend Architect** | [Student 2 Name] | @username |
| **ETL Engineer** | [Student 3 Name] | @username |
| **Logic Specialist** | [Student 4 Name] | @username |
| **Frontend Lead** | [Student 5 Name] | @username |

---

## Project Overview

This enterprise-grade application processes Mobile Money (MoMo) transaction logs. It is designed to demonstrate an end-to-end data pipeline (ETL) and a fullstack web visualization.

**Key Features:**
1.  **Ingest:** Parses raw XML SMS logs.
2.  **Clean:** Normalizes dates, phone numbers, and transaction amounts.
3.  **Store:** Saves structured data into a SQLite relational database.
4.  **Visualize:** Presents financial insights via a web dashboard.

---

## System Architecture

The following diagram illustrates the High-Level Architecture of our solution, detailing the flow from Raw XML to the Frontend Interface.

![Architecture Diagram](./architecture_diagram.png)
*(Ensure the file 'architecture_diagram.png' is in the root folder)*

---

## Project Management

We are using Agile methodology to track tasks and progress.

* **View our Scrum Board here:** [LINK TO TRELLO / GITHUB PROJECT]

---

## 📂 Repository Structure

```text
├── README.md                 # Project documentation
├── .env.example              # Configuration template
├── requirements.txt          # Python dependencies
├── index.html                # Frontend Entry Point
├── data/
│   ├── raw/                  # Input XML files
│   └── db.sqlite3            # Database file
├── etl/                      # Python Extraction & Transformation scripts
└── web/                      # CSS and JavaScript assets

## Getting Started

### 1. Prerequisites
* Python 3.8+ installed.
* Git installed.

### 2. Installation
Install the required dependencies using pip:

```bash
# Install dependencies
pip install -r requirements.txt

### 2. Installation
To run the ETL 