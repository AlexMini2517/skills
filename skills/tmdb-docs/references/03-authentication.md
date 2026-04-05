## Authentication

### Validate Key

```
GET /3/authentication
```

Test your API Key to see if it's valid.

### Response (200)

**Example Response:**
```json
{
  "success": true,
  "status_code": 1,
  "status_message": "Success."
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `success` | boolean |  |  | `True` |
| `status_code` | integer |  |  | `1` |
| `status_message` | string |  |  | `Success.` |

---

### Create Guest Session

```
GET /3/authentication/guest_session/new
```

### Response (200)

**Example Response:**
```json
{
  "success": true,
  "guest_session_id": "1ce82ec1223641636ad4a60b07de3581",
  "expires_at": "2016-08-27 16:26:40 UTC"
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `success` | boolean |  |  | `True` |
| `guest_session_id` | string |  |  | `1ce82ec1223641636ad4a60b07de3581` |
| `expires_at` | string |  |  | `2016-08-27 16:26:40 UTC` |

---

### Create Request Token

```
GET /3/authentication/token/new
```

### Response (200)

**Example Response:**
```json
{
  "success": true,
  "expires_at": "2016-08-26 17:04:39 UTC",
  "request_token": "ff5c7eeb5a8870efe3cd7fc5c282cffd26800ecd"
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `success` | boolean |  |  | `True` |
| `expires_at` | string |  |  | `2016-08-26 17:04:39 UTC` |
| `request_token` | string |  |  | `ff5c7eeb5a8870efe3cd7fc5c282cffd26800ecd` |

---

### Create Session

```
POST /3/authentication/session/new
```

### Request Body

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `RAW_BODY` | string | ✓ |  |  |

### Response (200)

**Example Response:**
```json
{
  "success": true,
  "session_id": "79191836ddaa0da3df76a5ffef6f07ad6ab0c641"
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `success` | boolean |  |  | `True` |
| `session_id` | string |  |  | `79191836ddaa0da3df76a5ffef6f07ad6ab0c641` |

---

### Create Session (from v4 token)

```
POST /3/authentication/session/convert/4
```

### Request Body

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `RAW_BODY` | string | ✓ |  |  |

### Response (200)

**Example Response:**
```json
{
  "success": true,
  "session_id": "2629f70fb498edc263a0adb99118ac41f0053e8c"
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `success` | boolean |  |  | `True` |
| `session_id` | string |  |  | `2629f70fb498edc263a0adb99118ac41f0053e8c` |

---

### Create Session (with login)

```
POST /3/authentication/token/validate_with_login
```

This method allows an application to validate a request token by entering a username and password.

### Request Body

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `RAW_BODY` | string | ✓ |  |  |

### Response (200)

**Example Response:**
```json
{
  "success": true,
  "expires_at": "2018-07-24 04:10:26 UTC",
  "request_token": "1531f1a558c8357ce8990cf887ff196e8f5402ec"
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `success` | boolean |  |  | `True` |
| `expires_at` | string |  |  | `2018-07-24 04:10:26 UTC` |
| `request_token` | string |  |  | `1531f1a558c8357ce8990cf887ff196e8f5402ec` |

---

### Delete Session

```
DELETE /3/authentication/session
```

### Request Body

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `RAW_BODY` | string | ✓ |  |  |

### Response (200)

**Example Response:**
```json
{
  "success": true
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `success` | boolean |  |  | `True` |