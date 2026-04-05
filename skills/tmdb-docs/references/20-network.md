## Network

### Details

```
GET /3/network/{network_id}
```

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `network_id` | integer | ✓ |  |

### Response (200)

**Example Response:**
```json
{
  "headquarters": "New York City, New York",
  "homepage": "https://www.hbo.com",
  "id": 49,
  "logo_path": "/tuomPhY2UtuPTqqFnKMVHvSb724.png",
  "name": "HBO",
  "origin_country": "US"
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `headquarters` | string |  |  | `New York City, New York` |
| `homepage` | string |  |  | `https://www.hbo.com` |
| `id` | integer |  |  | `49` |
| `logo_path` | string |  |  | `/tuomPhY2UtuPTqqFnKMVHvSb724.png` |
| `name` | string |  |  | `HBO` |
| `origin_country` | string |  |  | `US` |