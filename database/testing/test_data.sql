INSERT INTO Users VALUES
('u1','Alice Mukamana','0788123456','PERSON'),
('u2','Jean Habimana','0722123456','PERSON'),
('u3','Eric Niyonzima','0733123456','PERSON'),
('u4','MTN MoMo System','0790000000','SYSTEM'),
('u5','Claire Uwimana','0789988776','PERSON');

INSERT INTO CategoryGroups VALUES
('g1','TRANSFER'),
('g2','PAYMENT'),
('g3','AIRTIME'),
('g4','DATA'),
('g5','UTILITY');

INSERT INTO TransactionCategories VALUES
('c1','P2P Transfer','User to user transfer','g1'),
('c2','Merchant Payment','Pay merchant','g2'),
('c3','Airtime Purchase','Buy airtime','g3'),
('c4','Data Bundle','Buy data','g4'),
('c5','Electricity','Utility payment','g5');

INSERT INTO SystemLogs VALUES
('l1','MTN','Transfer successful',NOW(),NOW(),'PROCESSED'),
('l2','MTN','Merchant payment',NOW(),NOW(),'PROCESSED'),
('l3','MTN','Airtime purchased',NOW(),NOW(),'PROCESSED'),
('l4','MTN','Pending confirmation',NOW(),NULL,'PENDING'),
('l5','MTN','Transaction failed',NOW(),NOW(),'FAILED');

INSERT INTO Services VALUES
('s1','MTN Airtime','AIRTIME','123'),
('s2','REG Utility','UTILITY','456'),
('s3','MTN Data','DATA','789'),
('s4','Local Merchant','MERCHANT','0788000000'),
('s5','MoMo Transfer','UTILITY',NULL);

INSERT INTO Transactions VALUES
('t1','EXT1001',5000,'RWF',NOW(),'OUTGOING',50,45000,'c1','s5','l1'),
('t2','EXT1002',10000,'RWF',NOW(),'OUTGOING',100,34900,'c2','s4','l2'),
('t3','EXT1003',1500,'RWF',NOW(),'OUTGOING',0,33400,'c3','s1','l3'),
('t4','EXT1004',3000,'RWF',NOW(),'OUTGOING',30,30370,'c4','s3','l4'),
('t5','EXT1005',20000,'RWF',NOW(),'OUTGOING',200,10170,'c5','s2','l5');

INSERT INTO TransactionUsers VALUES
('t1','u1','SENDER'),
('t1','u2','RECEIVER'),
('t2','u1','SENDER'),
('t2','u4','RECEIVER'),
('t3','u1','SENDER'),
('t3','u4','RECEIVER'),
('t4','u5','SENDER'),
('t4','u1','RECEIVER'),
('t5','u3','SENDER'),
('t5','u4','RECEIVER');
