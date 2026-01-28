INSERT INTO Users (userId, fullName, phoneNumber, userType) VALUES
('u1','Ahmad Daib','+250795585810','PERSON'),
('u2','Tokiniaina Disaine','+250752355833','PERSON'),
('u3','MTN MoMo Platform',NULL,'BUSINESS');

INSERT INTO SystemLogs (logId, smsAddress, messageBody, receivedAt, status) VALUES
('l1', 'MTN-MoMo', 'You have received 5,000 RWF from Tokiniaina Disaine', '2026-01-24 10:15:00', 'PENDING'),
('l2', 'MTN-MoMo', 'You have paid 2,000 RWF to MTN MoMo Platform', '2026-01-24 11:00:00', 'PROCESSED');

INSERT INTO TransactionCategories (categoryId, categoryName, content) VALUES
('c1', 'Peer Transfer', '{"type":"transfer","direction":"p2p"}'),
('c2', 'Utility Payment', '{"type":"payment","service":"utility"}');
