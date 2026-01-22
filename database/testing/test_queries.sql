--Full transaction JOIN (core proof)
SELECT
  t.transactionId,
  u1.fullName AS sender,
  u2.fullName AS receiver,
  tc.categoryName,
  cg.groupName,
  s.serviceName,
  t.amount,
  t.currency,
  t.balanceAfter
FROM Transactions t
JOIN TransactionUsers tu1 ON t.transactionId=tu1.transactionId AND tu1.role='SENDER'
JOIN Users u1 ON tu1.userId=u1.userId
JOIN TransactionUsers tu2 ON t.transactionId=tu2.transactionId AND tu2.role='RECEIVER'
JOIN Users u2 ON tu2.userId=u2.userId
JOIN TransactionCategories tc ON t.categoryId=tc.categoryId
JOIN CategoryGroups cg ON tc.groupId=cg.groupId
JOIN Services s ON t.serviceId=s.serviceId;

--Transactions per user
SELECT u.fullName, COUNT(tu.transactionId) totalTransactions
FROM Users u
JOIN TransactionUsers tu ON u.userId=tu.userId
GROUP BY u.fullName;

--UPDATE test
UPDATE Transactions SET fee=75 WHERE transactionId='t1';

--DELETE test
DELETE FROM SystemLogs WHERE logId='l5';

--Constraint test
INSERT INTO Transactions VALUES
('tx999','EXT999',1000,'RWF',NOW(),'OUTGOING',10,900,'BAD','s1','l1');

--ENUM violation test
INSERT INTO Users VALUES
('u99','Invalid User','0700000000','ADMIN');

