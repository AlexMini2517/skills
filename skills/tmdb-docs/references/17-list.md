## List

### Add Movie

```
POST /3/list/{list_id}/add_item
```

Add a movie to a list.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `list_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `session_id` | string | ✓ |  |

### Request Body

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `RAW_BODY` | string |  |  |  |

### Response (200)

**Example Response:**
```json
{
  "status_code": 12,
  "status_message": "The item/record was updated successfully."
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `status_code` | integer |  |  | `12` |
| `status_message` | string |  |  | `The item/record was updated successfully.` |

---

### Check Item Status

```
GET /3/list/{list_id}/item_status
```

Use this method to check if an item has already been added to the list.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `list_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |
| `movie_id` | integer |  |  |

### Response (200)

**Example Response:**
```json
{
  "id": 1,
  "item_present": true
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | integer |  |  | `1` |
| `item_present` | boolean |  |  | `True` |

---

### Clear

```
POST /3/list/{list_id}/clear
```

Clear all items from a list.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `list_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `session_id` | string | ✓ |  |
| `confirm` | boolean | ✓ | *(default: `False`)* |

### Response (200)

**Example Response:**
```json
{
  "status_code": 12,
  "status_message": "The item/record was updated successfully."
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `status_code` | integer |  |  | `12` |
| `status_message` | string |  |  | `The item/record was updated successfully.` |

---

### Create

```
POST /3/list
```

### Parameters

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `session_id` | string | ✓ |  |

### Request Body

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `RAW_BODY` | string | ✓ |  |  |

### Response (200)

**Example Response:**
```json
{
  "status_message": "The item/record was created successfully.",
  "success": true,
  "status_code": 1,
  "list_id": 5861
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `status_message` | string |  |  | `The item/record was created successfully.` |
| `success` | boolean |  |  | `True` |
| `status_code` | integer |  |  | `1` |
| `list_id` | integer |  |  | `5861` |

---

### Delete

```
DELETE /3/list/{list_id}
```

Delete a list.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `list_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `session_id` | string | ✓ |  |

### Response (200)

**Example Response:**
```json
{
  "status_code": 12,
  "status_message": "The item/record was updated successfully."
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `status_code` | integer |  |  | `12` |
| `status_message` | string |  |  | `The item/record was updated successfully.` |

---

### Details

```
GET /3/list/{list_id}
```

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `list_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |
| `page` | integer |  | *(default: `1`)* |

### Response (200)

**Example Response:**
```json
{
  "created_by": "travisbell",
  "description": "The idea behind this list is to collect the live action comic book movies from within the Marvel franchise.",
  "favorite_count": 0,
  "id": "1",
  "items": [
    {
      "adult": false,
      "backdrop_path": "/14QbnygCuTO0vl7CAFmPf1fgZfV.jpg",
      "genre_ids": [
        28,
        12,
        878
      ],
      "id": 634649,
      "media_type": "movie",
      "original_language": "en",
      "original_title": "Spider-Man: No Way Home",
      "overview": "Peter Parker ist demaskiert und kann sein normales Leben nicht mehr von den hohen Eins\u00e4tzen als Superheld trennen. Als er Doctor Strange um Hilfe bittet, wird die Lage noch gef\u00e4hrlicher und er muss entdecken, was es wirklich bedeutet, Spider-Man zu sein.",
      "popularity": 398.217,
      "poster_path": "/iNKf4D0AzOj9GLq8ZyG3WZaqibL.jpg",
      "release_date": "2021-12-15",
      "title": "Spider-Man: No Way Home",
      "video": false,
      "vote_average": 8,
      "vote_count": 17267
    },
    {
      "adult": false,
      "backdrop_path": "/c6H7Z4u73ir3cIoCteuhJh7UCAR.jpg",
      "genre_ids": [
        878,
        28,
        12
      ],
      "id": 524434,
      "media_type": "movie",
      "original_language": "en",
      "original_title": "Eternals",
      "overview": "Die Eternals sind ein Team aus uralten Au\u00dferirdischen, die seit Tausenden von Jahren im Verborgenen auf der Erde gelebt haben. Als eine unerwartete Trag\u00f6die sie dazu zwingt, aus dem Schatten zu treten, sind sie gezwungen, sich gegen den \u00e4ltesten Feind der Menschheit, die Deviants, zu vereinen.",
      "popularity": 152.187,
      "poster_path": "/lFByFSLV5WDJEv3KabbdAF959F2.jpg",
      "release_date": "2021-11-03",
      "title": "Eternals",
      "video": false,
      "vote_average": 7,
      "vote_count": 7085
    },
    {
      "adult": false,
      "backdrop_path": "/zxWAv1A34kdYslBi4ekMDtgIGUt.jpg",
      "genre_ids": [
        28,
        12,
        14
  
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `created_by` | string |  |  | `travisbell` |
| `description` | string |  |  | `The idea behind this list is to collect the live action comic book movies from within the Marvel franchise.` |
| `favorite_count` | integer |  |  | `0` |
| `id` | string |  |  | `1` |
| `items` | array[object] |  |  |  |
| `item_count` | integer |  |  | `59` |
| `iso_639_1` | string |  |  | `en` |
| `name` | string |  |  | `The Marvel Universe` |
| `poster_path` | string |  |  | `/coJVIUEOToAEGViuhclM7pXC75R.jpg` |

---

### Remove Movie

```
POST /3/list/{list_id}/remove_item
```

Remove a movie from a list.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `list_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `session_id` | string | ✓ |  |

### Request Body

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `RAW_BODY` | string | ✓ |  |  |

### Response (200)

**Example Response:**
```json
{
  "status_code": 13,
  "status_message": "The item/record was deleted successfully."
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `status_code` | integer |  |  | `13` |
| `status_message` | string |  |  | `The item/record was deleted successfully.` |