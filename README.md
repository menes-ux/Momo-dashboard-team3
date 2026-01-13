# MoMo Data Analysis Dashboard

**Enterprise Web Development - Group Assignment 1**


---

## Team Members (Group 5)

| Name | GitHub Username |
| :--- | :--- |
| Ahmad Musa Daib | @Bangnyfe |
| Natinael Boda Borana | @Natinael-1 |
| Tokiniaina Andrianarison Disaine | @tokiniainaDisaine |
| Uchechukwu Chukwuebuka Ezeibe | @EucTech |
| Menes Nagnon Adisso | @menes-ux |

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

The following diagram illustrates the High-Level Architecture of our solution, detailing the flow from Raw XML to the Frontend Interface using Miro.

**[Click here to view the System Architecture on Miro](https://miro.com/welcomeonboard/c0F6T0IySTRqWkhFYk9yTVpGYkRVQVZ1cWswQ283Tk9laE13dlhoaHN6SnAxMjEzWXZrbkdJMzRYa2JrNktvRW90YjU4RnUxV2x6Rmt2bmpMZnlDUk8xWHB3NURXdzRGcEEyV1pvdS9rMWwycGZVNnlmaEMzQi9tc3c5aXpCQ3p0R2lncW1vRmFBVnlLcVJzTmdFdlNRPT0hdjE=?share_link_id=184634457912)**

---

## Project Management

We are using Github projects to track our progress.

* **View our Scrum Board here:** [GITHUB PROJECT](https://github.com/users/tokiniainaDisaine/projects/2/views/2)]

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
---

## Getting Started

```

### 1. Prerequisites
* Python 3.8+ installed.
* Git installed.

### 2. Installation
Install the required dependencies using pip:

```bash
# Install dependencies
pip install -r requirements.txt

## Usage
To run the ETL pipeline data and clean the data
python etl/run.py
