-- Users Table
CREATE TABLE Users (
    userId CHAR(36) PRIMARY KEY,
    fullName VARCHAR(100) NOT NULL,
    phoneNumber VARCHAR(20),
    userType ENUM('PERSON','BUSINESS') DEFAULT 'PERSON',
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- This is Transaction Categories Table
CREATE TABLE TransactionCategories (
    categoryId CHAR(36) PRIMARY KEY,
    categoryName VARCHAR(50) NOT NULL,
    categoryGroup ENUM('UTILITY','PAYMENT','AIRTIME','DATA','CREDIT','DEBIT','TRANSFER') NOT NULL,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- This is System Logs Table
CREATE TABLE SystemLogs (
    logId CHAR(36) PRIMARY KEY,
    smsAddress VARCHAR(50),
    messageBody TEXT NOT NULL,
    receivedAt DATETIME NOT NULL,
    status ENUM('PENDING','PROCESSED','ERROR') DEFAULT 'PROCESSED'
);