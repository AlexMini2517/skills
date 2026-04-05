## Changes

### Movie List

```
GET /3/movie/changes
```

Get a list of all of the movie ids that have been changed in the past 24 hours.

### Parameters

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `end_date` | string |  |  |
| `page` | integer |  | *(default: `1`)* |
| `start_date` | string |  |  |

### Response (200)

**Example Response:**
```json
{
  "results": [
    {
      "id": 1120293,
      "adult": false
    },
    {
      "id": 3686,
      "adult": false
    },
    {
      "id": 1085103,
      "adult": false
    },
    {
      "id": 1120294,
      "adult": false
    },
    {
      "id": 868759,
      "adult": false
    },
    {
      "id": 380298,
      "adult": false
    },
    {
      "id": 1120295,
      "adult": false
    },
    {
      "id": 1120296,
      "adult": false
    },
    {
      "id": 748701,
      "adult": false
    },
    {
      "id": 1120297,
      "adult": false
    },
    {
      "id": 1043565,
      "adult": false
    },
    {
      "id": 1120298,
      "adult": null
    },
    {
      "id": 876969,
      "adult": false
    },
    {
      "id": 195747,
      "adult": false
    },
    {
      "id": 675720,
      "adult": false
    },
    {
      "id": 1120299,
      "adult": false
    },
    {
      "id": 836734,
      "adult": false
    },
    {
      "id": 823216,
      "adult": false
    },
    {
      "id": 1120300,
      "adult": false
    },
    {
      "id": 983282,
      "adult": false
    },
    {
      "id": 1120301,
      "adult": false
    },
    {
      "id": 261814,
      "adult": false
    },
    {
      "id": 1120302,
      "adult": false
    },
    {
      "id": 1120303,
      "adult": false
    },
    {
      "id": 1120304,
      "adult": false
    },
    {
      "id": 35725,
      "adult": false
    },
    {
      "id": 183069,
      "adult": false
    },
    {
      "id": 725582,
      "adult": false
    },
    {
      "id": 9347,
      "adult": false
    },
    {
      "id": 927479,
      "adult": false
    },
    {
      "id": 955574,
      "adult": false
    },
    {
      "id": 1120305,
      "adult": true
    },
    {
      "id": 1097394,
      "adult": null
    },
    {
      "id": 45340,
      "adult": false
    },
    {
      "id": 420808,
      "adult": false
    },
    {
      "id": 29244,
      "adult": false
    },
    {
      "id": 566250,
      "
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `results` | array[object] |  |  |  |
| `page` | integer |  |  | `3` |
| `total_pages` | integer |  |  | `57` |
| `total_results` | integer |  |  | `5700` |

---

### People List

```
GET /3/person/changes
```

### Parameters

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `end_date` | string |  |  |
| `page` | integer |  | *(default: `1`)* |
| `start_date` | string |  |  |

### Response (200)

**Example Response:**
```json
{
  "results": [
    {
      "id": 4037513,
      "adult": false
    },
    {
      "id": 2280390,
      "adult": false
    },
    {
      "id": 4037514,
      "adult": false
    },
    {
      "id": 4037515,
      "adult": false
    },
    {
      "id": 145914,
      "adult": false
    },
    {
      "id": 219174,
      "adult": false
    },
    {
      "id": 4037516,
      "adult": false
    },
    {
      "id": 2280370,
      "adult": false
    },
    {
      "id": 71787,
      "adult": false
    },
    {
      "id": 4037517,
      "adult": false
    },
    {
      "id": 3822396,
      "adult": false
    },
    {
      "id": 3824024,
      "adult": null
    },
    {
      "id": 4037518,
      "adult": false
    },
    {
      "id": 4037519,
      "adult": false
    },
    {
      "id": 4037520,
      "adult": false
    },
    {
      "id": 4037521,
      "adult": false
    },
    {
      "id": 1197804,
      "adult": false
    },
    {
      "id": 4037522,
      "adult": false
    },
    {
      "id": 4037523,
      "adult": false
    },
    {
      "id": 4037524,
      "adult": false
    },
    {
      "id": 4037525,
      "adult": false
    },
    {
      "id": 2518728,
      "adult": false
    },
    {
      "id": 2280385,
      "adult": false
    },
    {
      "id": 2002127,
      "adult": false
    },
    {
      "id": 4037526,
      "adult": false
    },
    {
      "id": 912652,
      "adult": false
    },
    {
      "id": 3167326,
      "adult": false
    },
    {
      "id": 4037527,
      "adult": false
    },
    {
      "id": 2002129,
      "adult": false
    },
    {
      "id": 1516870,
      "adult": false
    },
    {
      "id": 4037528,
      "adult": false
    },
    {
      "id": 4037529,
      "adult": false
    },
    {
      "id": 4037530,
      "adult": false
    },
    {
      "id": 1498431,
      "adult": false
    },
    {
      "id": 2836209,
      "adult": false
    },
    {
      "id": 4037531,
      "adult": false
    },
    {
   
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `results` | array[object] |  |  |  |
| `page` | integer |  |  | `1` |
| `total_pages` | integer |  |  | `53` |
| `total_results` | integer |  |  | `5292` |

---

### TV List

```
GET /3/tv/changes
```

### Parameters

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `end_date` | string |  |  |
| `page` | integer |  | *(default: `1`)* |
| `start_date` | string |  |  |

### Response (200)

**Example Response:**
```json
{
  "results": [
    {
      "id": 225591,
      "adult": false
    },
    {
      "id": 220819,
      "adult": false
    },
    {
      "id": 203857,
      "adult": false
    },
    {
      "id": 1063,
      "adult": false
    },
    {
      "id": 225601,
      "adult": false
    },
    {
      "id": 201177,
      "adult": false
    },
    {
      "id": 225602,
      "adult": false
    },
    {
      "id": 112529,
      "adult": false
    },
    {
      "id": 114922,
      "adult": false
    },
    {
      "id": 225603,
      "adult": false
    },
    {
      "id": 22569,
      "adult": false
    },
    {
      "id": 218865,
      "adult": false
    },
    {
      "id": 225332,
      "adult": false
    },
    {
      "id": 211309,
      "adult": false
    },
    {
      "id": 219847,
      "adult": false
    },
    {
      "id": 134224,
      "adult": false
    },
    {
      "id": 209265,
      "adult": false
    },
    {
      "id": 212350,
      "adult": false
    },
    {
      "id": 219241,
      "adult": false
    },
    {
      "id": 221598,
      "adult": false
    },
    {
      "id": 225217,
      "adult": false
    },
    {
      "id": 209306,
      "adult": false
    },
    {
      "id": 102051,
      "adult": false
    },
    {
      "id": 104596,
      "adult": false
    },
    {
      "id": 212989,
      "adult": false
    },
    {
      "id": 224135,
      "adult": false
    },
    {
      "id": 223043,
      "adult": false
    },
    {
      "id": 65684,
      "adult": false
    },
    {
      "id": 198988,
      "adult": false
    },
    {
      "id": 1431,
      "adult": false
    },
    {
      "id": 221854,
      "adult": false
    },
    {
      "id": 34607,
      "adult": false
    },
    {
      "id": 27485,
      "adult": false
    },
    {
      "id": 153655,
      "adult": true
    },
    {
      "id": 731,
      "adult": false
    },
    {
      "id": 111551,
      "adult": false
    },
    {
      "id": 45563,
      "adult": false
    }
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `results` | array[object] |  |  |  |
| `page` | integer |  |  | `1` |
| `total_pages` | integer |  |  | `18` |
| `total_results` | integer |  |  | `1763` |