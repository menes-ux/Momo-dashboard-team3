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

## ERD Documentation

Our Momo Database has 7 Tables:

**Users Table** stores information about users in the MoMo sms, which include the system, individual and the business. Each user will has a unique id which is the primary key, along with their full name, phone number, and user type classification.

**CategoryGroups Table** categories all the transaction such as UTILITY, PAYMENT, AIRTIME, DATA, and TRANSFER. This table structures, classifys, organizes the transactions.

**TransactionCategories Table** stores transaction category details that are linked to CategoryGroups through the groupId foreign key. So each of the category will have a unique categoryId, name, and content, it helps to classify the transaction types within each group.

**SystemLogs Table** is keeps all raw SMS messages received from the MoMo system. It stores the main message body, sender address, received timestamp, processing timestamp, and status. So each log entry will have a unique id that serves as the primary key and links to processed transactions.

**Services Table** stores providers information such as utility , airtime, and merchants. So each service will have a serviceId, service name, type classification (UTILITY, AIRTIME, DATA, MERCHANT), and provider phone number.

**Transactions Table** is the core entity that stores the whole transaction data extracted from XML SMS logs. So each transaction includes financial details (amount, fee, balance after), transaction type (INCOMING/OUTGOING), and timestamps.

**TransactionUsers Table** creates a many-to-many relationship between Transactions and Users, it allow multiple participants in a single transaction. The role (SENDER/RECEIVER) is what distinguishes each user's transaction type, it helps in tracking of money flow between users.

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

* **View our Scrum Board here:** [[GITHUB PROJECT](https://github.com/users/tokiniainaDisaine/projects/2/views/2)]

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
```
---

## Database to JSON Mapping Strategy

The following table documents how our SQL columns are serialized into JSON for the API.

| Entity | SQL Column (Database) | JSON Key (API) | Data Type | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **User** | `userId` | `userId` | String (UUID) | Primary Key |
| | `fullName` | `fullName` | String | |
| | `phoneNumber` | `phoneNumber` | String | |
| | `userType` | `userType` | String | Enum value |
| **Transaction** | `transactionId` | `transactionId` | String (UUID) | Primary Key |
| | `amount` | `amount` | Number | stored as DECIMAL(10,2) |
| | `transactionDate` | `transactionDate` | String | ISO 8601 Format |
| **Complex Relations** | *N/A* | `sender` | Object | **Derived:** Join `TransactionUsers` where `role` = 'SENDER' |
| | *N/A* | `receiver` | Object | **Derived:** Join `TransactionUsers` where `role` = 'RECEIVER' |
| | `categoryId` | `category` | Object | Nested object containing category name |

---

### 1. Prerequisites
* Python 3.8+ installed.
* Git installed.

### 2. Installation
Install the required dependencies using pip:

```bash
# Install dependencies
pip install -r requirements.txt