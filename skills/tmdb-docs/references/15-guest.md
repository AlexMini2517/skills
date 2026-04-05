## Guest

### Rated Movies

```
GET /3/guest_session/{guest_session_id}/rated/movies
```

Get the rated movies for a guest session.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `guest_session_id` | string | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |
| `page` | integer |  | *(default: `1`)* |
| `sort_by` | string |  | *(default: `created_at.asc`)* |

### Response (200)

**Example Response:**
```json
{
  "page": 1,
  "results": [
    {
      "adult": false,
      "backdrop_path": "/ikR2qy9xJCHX7M8i5rcvuNfdYXs.jpg",
      "genre_ids": [
        18,
        80
      ],
      "id": 16,
      "original_language": "en",
      "original_title": "Dancer in the Dark",
      "overview": "Selma, a Czech immigrant on the verge of blindness, struggles to make ends meet for herself and her son, who has inherited the same genetic disorder and will suffer the same fate without an expensive operation. When life gets too difficult, Selma learns to cope through her love of musicals, escaping life's troubles - even if just for a moment - by dreaming up little numbers to the rhythmic beats of her surroundings.",
      "popularity": 14.684,
      "poster_path": "/8Wdd3fQfbbQeoSfWpHrDfaFNhBU.jpg",
      "release_date": "2000-06-30",
      "title": "Dancer in the Dark",
      "video": false,
      "vote_average": 7.885,
      "vote_count": 1549,
      "rating": 8.5
    }
  ],
  "total_pages": 1,
  "total_results": 1
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `1` |
| `total_results` | integer |  |  | `1` |

---

### Rated TV

```
GET /3/guest_session/{guest_session_id}/rated/tv
```

Get the rated TV shows for a guest session.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `guest_session_id` | string | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |
| `page` | integer |  | *(default: `1`)* |
| `sort_by` | string |  | *(default: `created_at.asc`)* |

### Response (200)

**Example Response:**
```json
{
  "page": 1,
  "results": [
    {
      "adult": false,
      "backdrop_path": "/2OMB0ynKlyIenMJWI2Dy9IWT4c.jpg",
      "genre_ids": [
        10765,
        18,
        10759
      ],
      "id": 1399,
      "origin_country": [
        "US"
      ],
      "original_language": "en",
      "original_name": "Game of Thrones",
      "overview": "Seven noble families fight for control of the mythical land of Westeros. Friction between the houses leads to full-scale war. All while a very ancient evil awakens in the farthest north. Amidst the war, a neglected military order of misfits, the Night's Watch, is all that stands between the realms of men and icy horrors beyond.",
      "popularity": 404.299,
      "poster_path": "/7WUHnWGx5OO145IRxPDUkQSh4C7.jpg",
      "first_air_date": "2011-04-17",
      "name": "Game of Thrones",
      "vote_average": 8.436,
      "vote_count": 21025,
      "rating": 8.5
    }
  ],
  "total_pages": 1,
  "total_results": 1
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `1` |
| `total_results` | integer |  |  | `1` |

---

### Rated TV Episodes

```
GET /3/guest_session/{guest_session_id}/rated/tv/episodes
```

Get the rated TV episodes for a guest session.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `guest_session_id` | string | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |
| `page` | integer |  | *(default: `1`)* |
| `sort_by` | string |  | *(default: `created_at.asc`)* |

### Response (200)

**Example Response:**
```json
{
  "page": 1,
  "results": [
    {
      "air_date": "2011-04-17",
      "episode_number": 1,
      "id": 63056,
      "name": "Winter Is Coming",
      "overview": "Jon Arryn, the Hand of the King, is dead. King Robert Baratheon plans to ask his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys Targaryen plans to wed his sister to a nomadic warlord in exchange for an army.",
      "production_code": "101",
      "runtime": 62,
      "season_number": 1,
      "show_id": 1399,
      "still_path": "/9hGF3WUkBf7cSjMg0cdMDHJkByd.jpg",
      "vote_average": 7.843,
      "vote_count": 286,
      "rating": 8.5
    }
  ],
  "total_pages": 1,
  "total_results": 1
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `1` |
| `total_results` | integer |  |  | `1` |