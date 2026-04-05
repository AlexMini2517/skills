## Find

### Find By ID

```
GET /3/find/{external_id}
```

Find data by external ID's.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `external_id` | string | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `external_source` | string | ✓ |  |
| `language` | string |  | *(default: `en-US`)* |

### Response (200)

**Example Response:**
```json
{
  "movie_results": [
    {
      "adult": false,
      "backdrop_path": "/44immBwzhDVyjn87b3x3l9mlhAD.jpg",
      "id": 934433,
      "title": "Scream VI",
      "original_language": "en",
      "original_title": "Scream VI",
      "overview": "Following the latest Ghostface killings, the four survivors leave Woodsboro behind and start a fresh chapter.",
      "poster_path": "/wDWwtvkRRlgTiUr6TyLSMX8FCuZ.jpg",
      "media_type": "movie",
      "genre_ids": [
        27,
        9648,
        53
      ],
      "popularity": 853.917,
      "release_date": "2023-03-08",
      "video": false,
      "vote_average": 7.388,
      "vote_count": 708
    }
  ],
  "person_results": [],
  "tv_results": [],
  "tv_episode_results": [],
  "tv_season_results": []
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `movie_results` | array[object] |  |  |  |
| `person_results` | array |  |  |  |
| `tv_results` | array |  |  |  |
| `tv_episode_results` | array |  |  |  |
| `tv_season_results` | array |  |  |  |