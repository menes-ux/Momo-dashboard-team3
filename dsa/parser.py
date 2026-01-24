import xml.etree.ElementTree as ET
import json
import re
from datetime import datetime
import uuid


class MomoSmsParser:
    def __init__(self, xml_file):
        self.xml_file = xml_file
        self.transactions = []
    
    def parseAmount(self, value):
        match = re.search(r'(\d{1,3}(?:,\d{3})*|\d+)\s*RWF', value)
        return float(match.group(1).replace(',', '')) if match else 0.0
    
    def parseBalance(self, value):
        match = re.search(r'balance[:\s]+(\d{1,3}(?:,\d{3})*|\d+)\s*RWF', value, re.I)
        return float(match.group(1).replace(',', '')) if match else 0.0
    
    def parseFee(self, value):
        match = re.search(r'Fee\s+was[:\s]+(\d{1,3}(?:,\d{3})*|\d+)\s*RWF', value, re.I)
        return float(match.group(1).replace(',', '')) if match else 0.0
    
    def parsePhone(self, value):
        match = re.search(r'\(?(250\d{9})\)?', value)
        return f"+{match.group(1)}" if match else None
    
    def getTransactionType(self, value):
        return 'INCOMING' if 'received' in value.lower() or 'added to' in value.lower() else 'OUTGOING'
    
    def getTransactionCategory(self, value):
        # This is a function that categorizes transactions
        value = value.lower()
        if 'airtime' in value:
            return {'categoryName': 'Airtime Purchase', 'categoryGroup': 'AIRTIME'}
        elif 'bank deposit' in value or 'cash deposit' in value:
            return {'categoryName': 'Bank Deposit', 'categoryGroup': 'TRANSFER'}
        elif 'transferred' in value or 'received' in value:
            return {'categoryName': 'Money Transfer', 'categoryGroup': 'TRANSFER'}
        return {'categoryName': 'Other Transaction', 'categoryGroup': 'PAYMENT'}
    
    def getSenderReceiver(self, value, transactionType):
        # This function will extract the sender and receiver names form the sms body
        if transactionType == 'INCOMING':
            match = re.search(r'from\s+([A-Za-z\s]+)\s*\(', value)
            senderName = match.group(1).strip() if match else "Unknown"
            receiverName = "Account Holder"
        else:
            match = re.search(r'to\s+([A-Za-z\s]+)\s+\d+', value)
            receiverName = match.group(1).strip() if match else "Unknown"
            senderName = "Account Holder"
        
        phone = self.parsePhone(value)
        
        # Create sender
        sender = {
            'userId': str(uuid.uuid4()),
            'fullName': senderName,
            'phoneNumber': phone if transactionType == 'INCOMING' else None,
            'userType': 'PERSON'
        }
        
        # Create receiver
        receiver = {
            'userId': str(uuid.uuid4()),
            'fullName': receiverName,
            'phoneNumber': phone if transactionType == 'OUTGOING' else None,
            'userType': 'PERSON'
        }
        
        return sender, receiver
    





if __name__ == '__main__':
    import sys
    parser = MomoSmsParser(sys.argv[1])
    transactions = parser.parseSmsXml()
    parser.save_json('momoTransactions.json')