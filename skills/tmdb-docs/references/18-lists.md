## Lists

### Lists

```
GET /3/tv/{series_id}/lists
```

Get the lists that a TV series has been added to.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `series_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |
| `page` | integer |  | *(default: `1`)* |

### Response (200)

**Example Response:**
```json
{
  "id": 1399,
  "page": 1,
  "results": [
    {
      "description": "",
      "favorite_count": 0,
      "id": 8257231,
      "item_count": 182,
      "iso_639_1": "en",
      "iso_3166_1": "US",
      "name": "Done",
      "poster_path": null
    },
    {
      "description": "",
      "favorite_count": 0,
      "id": 8258601,
      "item_count": 220,
      "iso_639_1": "en",
      "iso_3166_1": "US",
      "name": "All",
      "poster_path": null
    },
    {
      "description": "All the Great Movies I've Watched So Far",
      "favorite_count": 0,
      "id": 7092449,
      "item_count": 757,
      "iso_639_1": "en",
      "iso_3166_1": "US",
      "name": "Watched Movies",
      "poster_path": null
    },
    {
      "description": "",
      "favorite_count": 0,
      "id": 8289292,
      "item_count": 9,
      "iso_639_1": "en",
      "iso_3166_1": "US",
      "name": "watched tv series",
      "poster_path": null
    },
    {
      "description": "",
      "favorite_count": 0,
      "id": 8234063,
      "item_count": 4617,
      "iso_639_1": "en",
      "iso_3166_1": "US",
      "name": "Favorite Actors",
      "poster_path": null
    },
    {
      "description": "Eyeball Witnessed",
      "favorite_count": 0,
      "id": 47199,
      "item_count": 1864,
      "iso_639_1": "en",
      "iso_3166_1": "US",
      "name": "My Watched List",
      "poster_path": null
    },
    {
      "description": "",
      "favorite_count": 0,
      "id": 8241867,
      "item_count": 50,
      "iso_639_1": "en",
      "iso_3166_1": "US",
      "name": "My Watch List",
      "poster_path": null
    },
    {
      "description": "This is a long list of films and television shows that I have watched. Each one has been reviewed. The letters at the end of the review represent the initial of the person ranking said film. (H) is myself. Any other initial is of the person I watched that film with. (L) is the initial of my partner Libby who I enjoy showing all my favourite films.",
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | integer |  |  | `1399` |
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `96` |
| `total_results` | integer |  |  | `1906` |