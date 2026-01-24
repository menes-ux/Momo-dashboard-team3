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
-- This is Transactions Table
CREATE TABLE Transactions (
    transactionId CHAR(36) PRIMARY KEY,
    amount DECIMAL(10,2) NOT NULL,
    currency VARCHAR(5) DEFAULT 'RWF',
    transactionDate DATETIME NOT NULL,
    transactionType ENUM('INCOMING','OUTGOING') NOT NULL,
    fee DECIMAL(10,2) DEFAULT 0,
    balanceAfter DECIMAL(10,2) NOT NULL,
    categoryId CHAR(36),
    logId CHAR(36) NOT NULL,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (categoryId) REFERENCES TransactionCategories(categoryId),
    FOREIGN KEY (logId) REFERENCES SystemLogs(logId),
    CONSTRAINT amount_positive CHECK (amount >= 0),
    CONSTRAINT balance_positive CHECK (balanceAfter >= 0)
);

-- This is Transaction Users Table
CREATE TABLE TransactionUsers (
    transactionId CHAR(36),
    userId CHAR(36),
    role ENUM('SENDER','RECEIVER') NOT NULL,
    PRIMARY KEY (transactionId, userId, role),
    FOREIGN KEY (transactionId) REFERENCES Transactions(transactionId) ON DELETE CASCADE,
    FOREIGN KEY (userId) REFERENCES Users(userId)
);
