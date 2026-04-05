## Company

### Details

```
GET /3/company/{company_id}
```

Get the company details by ID.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `company_id` | integer | ✓ |  |

### Response (200)

**Example Response:**
```json
{
  "description": "",
  "headquarters": "San Francisco, California",
  "homepage": "https://www.lucasfilm.com",
  "id": 1,
  "logo_path": "/o86DbpburjxrqAzEDhXZcyE8pDb.png",
  "name": "Lucasfilm Ltd.",
  "origin_country": "US",
  "parent_company": null
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `description` | string |  |  |  |
| `headquarters` | string |  |  | `San Francisco, California` |
| `homepage` | string |  |  | `https://www.lucasfilm.com` |
| `id` | integer |  |  | `1` |
| `logo_path` | string |  |  | `/o86DbpburjxrqAzEDhXZcyE8pDb.png` |
| `name` | string |  |  | `Lucasfilm Ltd.` |
| `origin_country` | string |  |  | `US` |
| `parent_company` |  |  |  |  |

---

### Alternative Names

```
GET /3/company/{company_id}/alternative_names
```

Get the company details by ID.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `company_id` | integer | ✓ |  |

### Response (200)

**Example Response:**
```json
{
  "id": 1,
  "results": [
    {
      "name": "\ub8e8\uce74\uc2a4\ud544\ub984",
      "type": ""
    },
    {
      "name": "Lucasfilm Limited, LLC",
      "type": ""
    },
    {
      "name": "Lucasfilm Ltd. LLC",
      "type": ""
    },
    {
      "name": "Lucasfilm",
      "type": ""
    }
  ]
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |

---

### Images

```
GET /3/company/{company_id}/images
```

Get the company logos by id.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `company_id` | integer | ✓ |  |

### Response (200)

**Example Response:**
```json
{
  "id": 1,
  "logos": [
    {
      "aspect_ratio": 2.97979797979798,
      "file_path": "/o86DbpburjxrqAzEDhXZcyE8pDb.png",
      "height": 99,
      "id": "5aa080d6c3a3683fea00011e",
      "file_type": ".svg",
      "vote_average": 5.384,
      "vote_count": 2,
      "width": 295
    },
    {
      "aspect_ratio": 3.03951367781155,
      "file_path": "/tlVSws0RvvtPBwViUyOFAO0vcQS.png",
      "height": 329,
      "id": "63306b352b8a430096598b3d",
      "file_type": ".svg",
      "vote_average": 5.312,
      "vote_count": 1,
      "width": 1000
    }
  ]
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | integer |  |  | `1` |
| `logos` | array[object] |  |  |  |