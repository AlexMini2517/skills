## Credit

### Details

```
GET /3/credit/{credit_id}
```

Get a movie or TV credit details by ID.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `credit_id` | string | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |

### Response (200)

**Example Response:**
```json
{
  "credit_type": "cast",
  "department": "Acting",
  "job": "Actor",
  "media": {
    "adult": false,
    "backdrop_path": "/uDgy6hyPd82kOHh6I95FLtLnj6p.jpg",
    "id": 100088,
    "name": "The Last of Us",
    "original_language": "en",
    "original_name": "The Last of Us",
    "overview": "Zwanzig Jahre nachdem die moderne Zivilisation zerst\u00f6rt wurde. \u2013 Joel, ein abgeh\u00e4rteter \u00dcberlebender, wird angeheuert, um Ellie, ein 14-j\u00e4hriges M\u00e4dchen, aus einer bedr\u00fcckenden Quarant\u00e4nezone zu schmuggeln. Was als kleiner Job beginnt, wird bald zu einer brutalen, herzzerrei\u00dfenden Reise, bei der die beiden die USA durchqueren m\u00fcssen und aufeinander angewiesen sind, um zu \u00fcberleben.",
    "poster_path": "/igwIPNClQpGVzb61QlGqcpT5zUy.jpg",
    "media_type": "tv",
    "genre_ids": [
      18
    ],
    "popularity": 898.378,
    "first_air_date": "2023-01-15",
    "vote_average": 8.749,
    "vote_count": 3341,
    "origin_country": [
      "US"
    ],
    "character": "Joel Miller",
    "episodes": [],
    "seasons": [
      {
        "air_date": "2023-01-15",
        "episode_count": 9,
        "id": 144593,
        "name": "Staffel 1",
        "overview": "Die 1. Staffel der Endzeit-Horrorserie The Last of Us feierte ihre Premiere am 15. Januar 2023 bei HBO. In Staffel 1 beginnt f\u00fcr den \u00dcberlebenden Joel und das M\u00e4dchen Ellie eine Reise durch das postapokalyptische Amerika, in dem Pl\u00fcnderer und mutierte Wesen ihnen nach dem Leben trachten.",
        "poster_path": "/aUQKIpZZ31KWbpdHMCmaV76u78T.jpg",
        "season_number": 1,
        "show_id": 100088
      }
    ]
  },
  "media_type": "tv",
  "id": "6024a814c0ae36003d59cc3c",
  "person": {
    "adult": false,
    "id": 1253360,
    "name": "Pedro Pascal",
    "original_name": "Pedro Pascal",
    "media_type": "person",
    "popularity": 106.095,
    "gender": 2,
    "known_for_department": "Acting",
    "profile_path": "/dBOrm29cr7NUrjiDQMTtrTyDpfy.jp
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `credit_type` | string |  |  | `cast` |
| `department` | string |  |  | `Acting` |
| `job` | string |  |  | `Actor` |
| `media` | object |  |  |  |
| `adult` | boolean |  |  | `False` |
| `backdrop_path` | string |  |  | `/uDgy6hyPd82kOHh6I95FLtLnj6p.jpg` |
| `id` | integer |  |  | `100088` |
| `name` | string |  |  | `The Last of Us` |
| `original_language` | string |  |  | `en` |
| `original_name` | string |  |  | `The Last of Us` |
| `overview` | string |  |  | `Zwanzig Jahre nachdem die moderne Zivilisation zerstört wurde. – Joel, ein abgehärteter Überlebender, wird angeheuert, um Ellie, ein 14-jähriges Mädchen, aus einer bedrückenden Quarantänezone zu schmuggeln. Was als kleiner Job beginnt, wird bald zu einer brutalen, herzzerreißenden Reise, bei der die beiden die USA durchqueren müssen und aufeinander angewiesen sind, um zu überleben.` |
| `poster_path` | string |  |  | `/igwIPNClQpGVzb61QlGqcpT5zUy.jpg` |
| `media_type` | string |  |  | `tv` |
| `genre_ids` | array[integer] |  |  |  |
| `popularity` | number |  |  | `898.378` |
| `first_air_date` | string |  |  | `2023-01-15` |
| `vote_average` | number |  |  | `8.749` |
| `vote_count` | integer |  |  | `3341` |
| `origin_country` | array[string] |  |  |  |
| `character` | string |  |  | `Joel Miller` |
| `episodes` | array |  |  |  |
| `seasons` | array[object] |  |  |  |
| `media_type` | string |  |  | `tv` |
| `id` | string |  |  | `6024a814c0ae36003d59cc3c` |
| `person` | object |  |  |  |
| `adult` | boolean |  |  | `False` |
| `id` | integer |  |  | `1253360` |
| `name` | string |  |  | `Pedro Pascal` |
| `original_name` | string |  |  | `Pedro Pascal` |
| `media_type` | string |  |  | `person` |
| `popularity` | number |  |  | `106.095` |
| `gender` | integer |  |  | `2` |
| `known_for_department` | string |  |  | `Acting` |
| `profile_path` | string |  |  | `/dBOrm29cr7NUrjiDQMTtrTyDpfy.jpg` |