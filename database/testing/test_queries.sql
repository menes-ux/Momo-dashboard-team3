--ENUM constraints
INSERT INTO Users (userId, fullName, userType)
VALUES ('u4', 'Invalid User', 'ADMIN');

--Check constaint(SystemLogs table)
INSERT INTO SystemLogs (logId, smsAddress, messageBody, receivedAt, status)
VALUES ('l3', 'MTN-MoMo', 'Invalid status test', NOW(), 'DONE');

--Primary enforcement
INSERT INTO TransactionCategories (categoryId, categoryName)
VALUES ('c1', 'Duplicate Category');
