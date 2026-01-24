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
    
    def do_POST(self):
        """
        This is a method that handles all the POST requests
        """
        if not self.verifyUserCredentials():
            return self.errorResponse(401, 'invalid credentials, Login with your username and password')

        endpoint, _, _ = self._parse_path()
        if endpoint != 'transactions':
            return self.errorResponse(404, 'Not found')

        length = int(self.headers.get('Content-Length', 0))
        raw_body = self.rfile.read(length).decode('utf-8')

        try:
            body = json.loads(raw_body)
        except json.JSONDecodeError as e:
            print(f"JSON Error: {e}")
            return self.errorResponse(400, f'Invalid JSON: {str(e)}')

        if 'amount' not in body or 'transactionType' not in body:
            return self.errorResponse(400, 'Missing required fields')

        body['transactionId'] = body.get('transactionId', str(uuid.uuid4()))
        body['createdAt'] = datetime.now().isoformat()
        body['createdBy'] = self.current_user

        self.transactions.append(body)
        self.transactions_dict[body['transactionId']] = body

        return self.jsonResponse({'success': True, "statusCode": 201, 'transaction': body}, 201)

    def do_PUT(self):
        """
        This is a method that handles all the PUT requests
        """
        if not self.verifyUserCredentials():
            return self.errorResponse(401, 'invalid credentials, Login with your username and password')

        endpoint, transactionId, _ = self._parse_path()
        if endpoint != 'transactions' or not transactionId:
            return self.errorResponse(404, 'Not found')

        if transactionId not in self.transactions_dict:
            return self.errorResponse(404, f'Transaction {transactionId} not found')

        length = int(self.headers.get('Content-Length', 0))
        update = json.loads(self.rfile.read(length))

        currentTransaction = self.transactions_dict[transactionId]
        update['transactionId'] = transactionId
        update['updatedAt'] = datetime.now().isoformat()
        update['updatedBy'] = self.current_user

        updated = {**currentTransaction, **update}
        self.transactions_dict[transactionId] = updated

        for i, t in enumerate(self.transactions):
            if t['transactionId'] == transactionId:
                self.transactions[i] = updated
                break

        return self.jsonResponse({'success': True, "statusCode": 200, 'transaction': updated})

    def do_DELETE(self):
        """
        This is a method that handles all the DELETE requests
        """
        if not self.verifyUserCredentials():
            return self.errorResponse(401, 'invalid credentials, Login with your username and password')

        endpoint, transactionId, _ = self._parse_path()
        if endpoint != 'transactions' or not transactionId:
            return self.errorResponse(404, 'Not found')

        if transactionId not in self.transactions_dict:
            return self.errorResponse(404, f'Transaction {transactionId} not found')

        deleted = self.transactions_dict.pop(transactionId)
        self.transactions = [t for t in self.transactions if t['transactionId'] != transactionId]

        return self.jsonResponse({'success': True, "statusCode": 200, 'message': 'Deleted', 'transaction': deleted})

    def log_message(self, format, *args):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {format % args}")


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
