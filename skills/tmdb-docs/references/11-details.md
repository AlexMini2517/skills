## Details

### Alternative Names

```
GET /3/network/{network_id}/alternative_names
```

Get the alternative names of a network.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `network_id` | integer | ✓ |  |

### Response (200)

**Example Response:**
```json
{
  "id": 49,
  "results": [
    {
      "name": "Home Box Office",
      "type": ""
    },
    {
      "name": "HBO HD",
      "type": ""
    }
  ]
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | integer |  |  | `49` |
| `results` | array[object] |  |  |  |