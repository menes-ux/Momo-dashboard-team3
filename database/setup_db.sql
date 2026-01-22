-- This is Users Table
CREATE TABLE Users (
    userId CHAR(36) PRIMARY KEY,
    fullName VARCHAR(100),
    phoneNumber VARCHAR(20),
    userType ENUM('PERSON','BUSINESS','SYSTEM')
);

-- This is Category Groups Table
CREATE TABLE CategoryGroups (
    groupId CHAR(36) PRIMARY KEY,
    groupName ENUM('UTILITY','PAYMENT','AIRTIME','DATA','TRANSFER')
);

-- This is Transaction Categories Table
CREATE TABLE TransactionCategories (
    categoryId CHAR(36) PRIMARY KEY,
    categoryName VARCHAR(50),
    content TEXT,
    groupId CHAR(36),
    FOREIGN KEY (groupId) REFERENCES CategoryGroups(groupId)
);

-- This is System Logs Table
CREATE TABLE SystemLogs (
    logId CHAR(36) PRIMARY KEY,
    smsAddress VARCHAR(50),
    messageBody TEXT,
    receivedAt DATETIME,
    processedAt DATETIME,
    status VARCHAR(20)
);

-- This is Services Table
CREATE TABLE Services (
    serviceId CHAR(36) PRIMARY KEY,
    serviceName VARCHAR(100),
    serviceType ENUM('UTILITY','AIRTIME','DATA','MERCHANT'),
    providerPhone VARCHAR(20)
);

-- This is Transactions Table
CREATE TABLE Transactions (
    transactionId CHAR(36) PRIMARY KEY,
    externalTransactionId VARCHAR(50) UNIQUE,
    amount DECIMAL(10,2),
    currency VARCHAR(5),
    transactionDate DATETIME,
    transactionType ENUM('INCOMING','OUTGOING'),
    fee DECIMAL(10,2),
    balanceAfter DECIMAL(10,2),
    categoryId CHAR(36),
    serviceId CHAR(36),
    logId CHAR(36),
    FOREIGN KEY (categoryId) REFERENCES TransactionCategories(categoryId),
    FOREIGN KEY (serviceId) REFERENCES Services(serviceId),
    FOREIGN KEY (logId) REFERENCES SystemLogs(logId)
);

-- This is Transaction Users Table
CREATE TABLE TransactionUsers (
    transactionId CHAR(36),
    userId CHAR(36),
    role ENUM('SENDER','RECEIVER'),
    PRIMARY KEY (transactionId, userId, role),
    FOREIGN KEY (transactionId) REFERENCES Transactions(transactionId),
    FOREIGN KEY (userId) REFERENCES Users(userId)
);