# MoMo Transaction API Documentation

## BaseUrl

```
http://localhost:8500
```

## Authentication

For DEMO add use this as your Basic Auth
**Credentials:**

- Username: `MomoUser1`
- Password: `$Momo123`

or

- Username: `MomoUser2`
- Password: `$Momo456`

## Endpoints

### 1. GET /transactions

**Description:** Get all transactions

**Request:**

```bash
http://localhost:8500/transactions
```

**Response (200):**

```json
{
  "success": true,
  "count": 26,
  "transactions": [
    {
      "transactionId": "8e7406cd-6e6d-417d-b89e-fc6bc9ade73f",
      "amount": 26000.0,
      "currency": "RWF",
      "transactionType": "INCOMING",
      "transactionDate": "2024-05-10T16:30:51Z",
      "fee": 0.0,
      "balanceAfter": 24500.0,
      "category": {
        "categoryId": "e7288bd7-4204-4ae1-b714-c0c9e171707a",
        "categoryName": "Money Transfer",
        "categoryGroup": "TRANSFER"
      },
      "sender": {
        "userId": "359b1c18-8da9-4f13-8391-4166d0f187ad",
        "fullName": "Jane Smith",
        "phoneNumber": "+250788123456",
        "userType": "PERSON"
      },
      "receiver": {
        "userId": "e806359d-e4dc-4022-a18a-527a7a42f163",
        "fullName": "Account Holder",
        "phoneNumber": null,
        "userType": "PERSON"
      }
    }
  ]
}
```

### 2. GET /transactions/{id}

**Description:** Get single transaction

**Request:**

```bash
http://localhost:8500/transactions/8e7406cd-6e6d-417d-b89e-fc6bc9ade73f
```

**Response (200):**

```json
{
  "success": true,
  "count": 26,
  "transactions": [
    {
      "transactionId": "8e7406cd-6e6d-417d-b89e-fc6bc9ade73f",
      "amount": 26000.0,
      "currency": "RWF",
      "transactionType": "INCOMING",
      "transactionDate": "2024-05-10T16:30:51Z",
      "fee": 0.0,
      "balanceAfter": 24500.0,
      "category": {
        "categoryId": "e7288bd7-4204-4ae1-b714-c0c9e171707a",
        "categoryName": "Money Transfer",
        "categoryGroup": "TRANSFER"
      },
      "sender": {
        "userId": "359b1c18-8da9-4f13-8391-4166d0f187ad",
        "fullName": "Jane Smith",
        "phoneNumber": "+250788123456",
        "userType": "PERSON"
      },
      "receiver": {
        "userId": "e806359d-e4dc-4022-a18a-527a7a42f163",
        "fullName": "Account Holder",
        "phoneNumber": null,
        "userType": "PERSON"
      }
    }
  ]
}
```

**Response (404):**

```json
{
  "error": true,
  "message": "Transaction 8e7406cd-6e6d-417d-b89e-fc6bc9ade73f not found"
}
```

---

### 3. POST /transactions

**Description:** Create new transaction

**Request:**

```bash
http://localhost:8500/transactions
```

Payload will be in the format

```json
{
    "amount": 10000,
    "currency": "RWF",
    "transactionType": "OUTGOING",
    "fee": 100,
    "balanceAfter": 15000,
    "category": {
      "categoryName": "Airtime Purchase",
      "categoryGroup": "AIRTIME"
    },
    "sender": {
      "fullName": "John Doe",
      "phoneNumber": "+250788111111"
    },
    "receiver": {
      "fullName": "MTN Rwanda",
      "userType": "BUSINESS"
    }
  }
```

**Response (201):**

```json
{
  "success": true,
  "statusCode": 201,
  "transaction": {
    "amount": 7500,
    "currency": "RWF",
    "transactionType": "OUTGOING",
    "transactionDate": "2024-05-10T16:30:51Z",
    "fee": 100,
    "balanceAfter": 15000,
    "category": {
      "categoryName": "Airtime Purchase",
      "categoryGroup": "AIRTIME"
    },
    "sender": {
      "fullName": "Menes Ben",
      "phoneNumber": "+250788111111",
      "userType": "PERSON"
    },
    "receiver": {
      "fullName": "MTN Rwanda",
      "phoneNumber": null,
      "userType": "BUSINESS"
    },
    "transactionId": "18118f50-d822-40ca-bd05-2cc900f2d392",
    "createdAt": "2026-01-24T09:29:13.577847",
    "createdBy": "MomoUser1"
  }
}
```

**Response (400):**

```json
{
  "error": true,
  "message": "Missing required fields"
}
```

---

### 4. PUT /transactions/{id}

**Description:** Update transaction

**Request:**

```bash
http://localhost:8500/transactions/18118f50-d822-40ca-bd05-2cc900f2d392
```

**Payload to update any field:**

```json
{
  "amount": 12000,
  "fee": 4440,
  "balanceAfter": 20000,
  "category": {
    "categoryGroup": "UTILITY"
  }
}
```

**Response (200):**

```json
{
  "success": true,
  "statusCode": 201,
  "transaction": {
    "amount": 7500,
    "currency": "RWF",
    "transactionType": "OUTGOING",
    "transactionDate": "2024-05-10T16:30:51Z",
    "fee": 100,
    "balanceAfter": 15000,
    "category": {
      "categoryName": "Airtime Purchase",
      "categoryGroup": "AIRTIME"
    },
    "sender": {
      "fullName": "Menes Ben",
      "phoneNumber": "+250788111111",
      "userType": "PERSON"
    },
    "receiver": {
      "fullName": "MTN Rwanda",
      "phoneNumber": null,
      "userType": "BUSINESS"
    },
    "transactionId": "18118f50-d822-40ca-bd05-2cc900f2d392",
    "createdAt": "2026-01-24T09:29:13.577847",
    "createdBy": "MomoUser1"
  }
}
```

**Response (404):**

```json
{
  "error": true,
  "message": "Transaction 18118f50-d822-40ca-bd05-2cc900f2d392 not found"
}
```

---

### 5. DELETE /transactions/{id}

**Description:** Delete transaction

**Request:**

```bash
http://localhost:8500/transactions/18118f50-d822-40ca-bd05-2cc900f2d392
```

**Response (200):**

```json
{
  "success": true,
  "message": "Deleted",
  "transaction": {
    "transactionId": "uuid-123",
    "amount": 5000,
    ...
  }
}
```

**Response (404):**

```json
{
  "error": true,
  "message": "Transaction 18118f50-d822-40ca-bd05-2cc900f2d392 not found"
}
```

---

## Error Responses

## 401 Unauthorized

```json
{
  "error": true,
  "message": "Authentication required"
}
```

## 404 Not Found

```json
{
  "error": true,
  "message": "Not found"
}
```

## 400 Bad Request

```json
{
  "error": true,
  "message": "Missing required fields"
}
```

## HTTP Status Codes

     Code  Meaning

1. 200 Success
2. 201 Created
3. 400 Bad Request
4. 401 Unauthorized
5. 404 Not Found
