from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import base64
from urllib.parse import urlparse, parse_qs
import uuid
from datetime import datetime


class MomoTransaction(BaseHTTPRequestHandler):
    transactions = []
    transactions_dict = {}
    
    USERS = {'MomoUser1': '$Momo123', 'MomoUser2': '$Momo456'}
    
    def _set_headers(self, status=200):
        """
        This is the method that sends the http headers to the client
        """
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
    
    def verifyUserCredentials(self):
        value = self.headers.get('Authorization')
        if not value:
            return False
        
        try:
            _, creds = value.split(' ')
            username, password = base64.b64decode(creds).decode().split(':', 1)
            if username in self.USERS and self.USERS[username] == password:
                self.current_user = username
                return True
        except:
            pass
        return False
    
    def jsonResponse(self, data, status=200):
        self._set_headers(status)
        self.wfile.write(json.dumps(data, indent=2).encode())
    
    def errorResponse(self, status, message):
        self.jsonResponse({'error': True, 'message': message}, status)
    
    def _parse_path(self):
        parsed = urlparse(self.path)
        parts = parsed.path.strip('/').split('/')
        
        if len(parts) == 1 and parts[0] == 'transactions':
            return 'transactions', None, parse_qs(parsed.query)
        if len(parts) == 2 and parts[0] == 'transactions':
            return 'transactions', parts[1], parse_qs(parsed.query)
        return None, None, {}
    
    
    def do_GET(self):
        """
        This is a method that handles all the GET requests
        """
        if not self.verifyUserCredentials():
            return self.errorResponse(401, 'invalid credentials, Login with your username and password')
        
        endpoint, transactionId, params = self._parse_path()
        
        if endpoint != 'transactions':
            return self.errorResponse(404, 'Not found')
        
        if not transactionId:
            result = self.transactions
            if 'type' in params:
                transaction_type = params['type'][0].upper()
                result = [t for t in result if t.get('transactionType') == transaction_type]
            return self.jsonResponse({'success': True, 'count': len(result), "statusCode": 200, 'transactions': result})
        
        trans = self.transactions_dict.get(transactionId)
        if trans:
            return self.jsonResponse({'success': True, 'transaction': trans})
        return self.errorResponse(404, f'Transaction {transactionId} not found')
    

def startMomoTransactions(file='momoTransactions.json'):
    try:
        with open(file, 'r') as f:
            MomoTransaction.transactions = json.load(f)
            MomoTransaction.transactions_dict = {t['transactionId']: t for t in MomoTransaction.transactions}
        print(f"Loaded {len(MomoTransaction.transactions)} transactions")
    except:
        print("Error 404: No Momo transactions file found")


def run(port=8500):
    server = HTTPServer(('', port), MomoTransaction)
    print(f"\nMomo Transaction server running at http://localhost:{port}")
    server.serve_forever()

if __name__ == '__main__':
    startMomoTransactions()
    run()