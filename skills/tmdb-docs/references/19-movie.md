## Movie

### Now Playing

```
GET /3/movie/now_playing
```

Get a list of movies that are currently in theatres.

### Parameters

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |
| `page` | integer |  | *(default: `1`)* |
| `region` | string |  | ISO-3166-1 code |

### Response (200)

**Example Response:**
```json
{
  "dates": {
    "maximum": "2023-05-03",
    "minimum": "2023-03-16"
  },
  "page": 1,
  "results": [
    {
      "adult": false,
      "backdrop_path": "/iJQIbOPm81fPEGKt5BPuZmfnA54.jpg",
      "genre_ids": [
        16,
        12,
        10751,
        14,
        35
      ],
      "id": 502356,
      "original_language": "en",
      "original_title": "The Super Mario Bros. Movie",
      "overview": "While working underground to fix a water main, Brooklyn plumbers\u2014and brothers\u2014Mario and Luigi are transported down a mysterious pipe and wander into a magical new world. But when the brothers are separated, Mario embarks on an epic quest to find Luigi.",
      "popularity": 6572.614,
      "poster_path": "/qNBAXBIQlnOThrVvA6mA2B5ggV6.jpg",
      "release_date": "2023-04-05",
      "title": "The Super Mario Bros. Movie",
      "video": false,
      "vote_average": 7.5,
      "vote_count": 1456
    },
    {
      "adult": false,
      "backdrop_path": "/nDxJJyA5giRhXx96q1sWbOUjMBI.jpg",
      "genre_ids": [
        28,
        35,
        14
      ],
      "id": 594767,
      "original_language": "en",
      "original_title": "Shazam! Fury of the Gods",
      "overview": "Billy Batson and his foster siblings, who transform into superheroes by saying \"Shazam!\", are forced to get back into action and fight the Daughters of Atlas, who they must stop from using a weapon that could destroy the world.",
      "popularity": 4274.232,
      "poster_path": "/2VK4d3mqqTc7LVZLnLPeRiPaJ71.jpg",
      "release_date": "2023-03-15",
      "title": "Shazam! Fury of the Gods",
      "video": false,
      "vote_average": 6.9,
      "vote_count": 1231
    },
    {
      "adult": false,
      "backdrop_path": "/7bWxAsNPv9CXHOhZbJVlj2KxgfP.jpg",
      "genre_ids": [
        27,
        53
      ],
      "id": 713704,
      "original_language": "en",
      "original_title": "Evil Dead Rise",
      "overview": "Two sisters find an ancient vinyl that gives birth to bloodthirst
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `dates` | object |  |  |  |
| `maximum` | string |  |  | `2023-05-03` |
| `minimum` | string |  |  | `2023-03-16` |
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `87` |
| `total_results` | integer |  |  | `1734` |

---

### Popular

```
GET /3/movie/popular
```

Get a list of movies ordered by popularity.

### Parameters

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |
| `page` | integer |  | *(default: `1`)* |
| `region` | string |  | ISO-3166-1 code |

### Response (200)

**Example Response:**
```json
{
  "page": 1,
  "results": [
    {
      "adult": false,
      "backdrop_path": "/gMJngTNfaqCSCqGD4y8lVMZXKDn.jpg",
      "genre_ids": [
        28,
        12,
        878
      ],
      "id": 640146,
      "original_language": "en",
      "original_title": "Ant-Man and the Wasp: Quantumania",
      "overview": "Super-Hero partners Scott Lang and Hope van Dyne, along with with Hope's parents Janet van Dyne and Hank Pym, and Scott's daughter Cassie Lang, find themselves exploring the Quantum Realm, interacting with strange new creatures and embarking on an adventure that will push them beyond the limits of what they thought possible.",
      "popularity": 8567.865,
      "poster_path": "/ngl2FKBlU4fhbdsrtdom9LVLBXw.jpg",
      "release_date": "2023-02-15",
      "title": "Ant-Man and the Wasp: Quantumania",
      "video": false,
      "vote_average": 6.5,
      "vote_count": 1886
    },
    {
      "adult": false,
      "backdrop_path": "/iJQIbOPm81fPEGKt5BPuZmfnA54.jpg",
      "genre_ids": [
        16,
        12,
        10751,
        14,
        35
      ],
      "id": 502356,
      "original_language": "en",
      "original_title": "The Super Mario Bros. Movie",
      "overview": "While working underground to fix a water main, Brooklyn plumbers\u2014and brothers\u2014Mario and Luigi are transported down a mysterious pipe and wander into a magical new world. But when the brothers are separated, Mario embarks on an epic quest to find Luigi.",
      "popularity": 6572.614,
      "poster_path": "/qNBAXBIQlnOThrVvA6mA2B5ggV6.jpg",
      "release_date": "2023-04-05",
      "title": "The Super Mario Bros. Movie",
      "video": false,
      "vote_average": 7.5,
      "vote_count": 1456
    },
    {
      "adult": false,
      "backdrop_path": "/nDxJJyA5giRhXx96q1sWbOUjMBI.jpg",
      "genre_ids": [
        28,
        35,
        14
      ],
      "id": 594767,
      "original_language": "en",
      "original_title": "Shazam! Fury of the Gods",
      "overview": "Bi
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `38029` |
| `total_results` | integer |  |  | `760569` |

---

### Top Rated

```
GET /3/movie/top_rated
```

Get a list of movies ordered by rating.

### Parameters

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |
| `page` | integer |  | *(default: `1`)* |
| `region` | string |  | ISO-3166-1 code |

### Response (200)

**Example Response:**
```json
{
  "page": 1,
  "results": [
    {
      "adult": false,
      "backdrop_path": "/tmU7GeKVybMWFButWEGl2M4GeiP.jpg",
      "genre_ids": [
        18,
        80
      ],
      "id": 238,
      "original_language": "en",
      "original_title": "The Godfather",
      "overview": "Spanning the years 1945 to 1955, a chronicle of the fictional Italian-American Corleone crime family. When organized crime family patriarch, Vito Corleone barely survives an attempt on his life, his youngest son, Michael steps in to take care of the would-be killers, launching a campaign of bloody revenge.",
      "popularity": 100.932,
      "poster_path": "/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
      "release_date": "1972-03-14",
      "title": "The Godfather",
      "video": false,
      "vote_average": 8.7,
      "vote_count": 17806
    },
    {
      "adult": false,
      "backdrop_path": "/kXfqcdQKsToO0OUXHcrrNCHDBzO.jpg",
      "genre_ids": [
        18,
        80
      ],
      "id": 278,
      "original_language": "en",
      "original_title": "The Shawshank Redemption",
      "overview": "Framed in the 1940s for the double murder of his wife and her lover, upstanding banker Andy Dufresne begins a new life at the Shawshank prison, where he puts his accounting skills to work for an amoral warden. During his long stretch in prison, Dufresne comes to be admired by the other inmates -- including an older prisoner named Red -- for his integrity and unquenchable sense of hope.",
      "popularity": 98.25,
      "poster_path": "/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg",
      "release_date": "1994-09-23",
      "title": "The Shawshank Redemption",
      "video": false,
      "vote_average": 8.7,
      "vote_count": 23656
    },
    {
      "adult": false,
      "backdrop_path": "/ejnlCzBd5pOGAYCpxC93NXSrdrz.jpg",
      "genre_ids": [
        35,
        14
      ],
      "id": 772071,
      "original_language": "es",
      "original_title": "Cuando Sea Joven",
      "overview": "70-year-old Malena ge
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `552` |
| `total_results` | integer |  |  | `11032` |

---

### Upcoming

```
GET /3/movie/upcoming
```

Get a list of movies that are being released soon.

### Parameters

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |
| `page` | integer |  | *(default: `1`)* |
| `region` | string |  | ISO-3166-1 code |

### Response (200)

**Example Response:**
```json
{
  "dates": {
    "maximum": "2023-05-23",
    "minimum": "2023-05-04"
  },
  "page": 1,
  "results": [
    {
      "adult": false,
      "backdrop_path": "/7bWxAsNPv9CXHOhZbJVlj2KxgfP.jpg",
      "genre_ids": [
        27,
        53
      ],
      "id": 713704,
      "original_language": "en",
      "original_title": "Evil Dead Rise",
      "overview": "Two sisters find an ancient vinyl that gives birth to bloodthirsty demons that run amok in a Los Angeles apartment building and thrusts them into a primal battle for survival as they face the most nightmarish version of family imaginable.",
      "popularity": 1696.367,
      "poster_path": "/mIBCtPvKZQlxubxKMeViO2UrP3q.jpg",
      "release_date": "2023-04-12",
      "title": "Evil Dead Rise",
      "video": false,
      "vote_average": 7,
      "vote_count": 207
    },
    {
      "adult": false,
      "backdrop_path": "/5Y5pz0NX7SZS9036I733F7uNcwK.jpg",
      "genre_ids": [
        27,
        53
      ],
      "id": 758323,
      "original_language": "en",
      "original_title": "The Pope's Exorcist",
      "overview": "Father Gabriele Amorth, Chief Exorcist of the Vatican, investigates a young boy's terrifying possession and ends up uncovering a centuries-old conspiracy the Vatican has desperately tried to keep hidden.",
      "popularity": 1073.229,
      "poster_path": "/9JBEPLTPSm0d1mbEcLxULjJq9Eh.jpg",
      "release_date": "2023-04-05",
      "title": "The Pope's Exorcist",
      "video": false,
      "vote_average": 6.5,
      "vote_count": 143
    },
    {
      "adult": false,
      "backdrop_path": "/wD2kUCX1Bb6oeIb2uz7kbdfLP6k.jpg",
      "genre_ids": [
        27,
        53
      ],
      "id": 980078,
      "original_language": "en",
      "original_title": "Winnie the Pooh: Blood and Honey",
      "overview": "Christopher Robin is headed off to college and he has abandoned his old friends, Pooh and Piglet, which then leads to the duo embracing their inner monsters.",
      "popularity": 690.338,
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `dates` | object |  |  |  |
| `maximum` | string |  |  | `2023-05-23` |
| `minimum` | string |  |  | `2023-05-04` |
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `19` |
| `total_results` | integer |  |  | `369` |

---

### Details

```
GET /3/movie/{movie_id}
```

Get the top level details of a movie by ID.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `movie_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `append_to_response` | string |  | comma separated list of endpoints within this namespace, 20 items max |
| `language` | string |  | *(default: `en-US`)* |

### Response (200)

**Example Response:**
```json
{
  "adult": false,
  "backdrop_path": "/2w4xG178RpB4MDAIfTkqAuSJzec.jpg",
  "belongs_to_collection": {
    "id": 10,
    "name": "Star Wars Collection",
    "poster_path": "/pWVLFh4OuejTpUaDQbB1C4zoS2p.jpg",
    "backdrop_path": "/iY2ujEY2m68OTTlPFTiHub9joHS.jpg"
  },
  "budget": 11000000,
  "genres": [
    {
      "id": 12,
      "name": "Adventure"
    },
    {
      "id": 28,
      "name": "Action"
    },
    {
      "id": 878,
      "name": "Science Fiction"
    }
  ],
  "homepage": "http://www.starwars.com/films/star-wars-episode-iv-a-new-hope",
  "id": 11,
  "imdb_id": "tt0076759",
  "origin_country": [
    "US"
  ],
  "original_language": "en",
  "original_title": "Star Wars",
  "overview": "Princess Leia is captured and held hostage by the evil Imperial forces in their effort to take over the galactic Empire. Venturesome Luke Skywalker and dashing captain Han Solo team together with the loveable robot duo R2-D2 and C-3PO to rescue the beautiful princess and restore peace and justice in the Empire.",
  "popularity": 20.6912,
  "poster_path": "/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg",
  "production_companies": [
    {
      "id": 1,
      "logo_path": "/tlVSws0RvvtPBwViUyOFAO0vcQS.png",
      "name": "Lucasfilm Ltd.",
      "origin_country": "US"
    },
    {
      "id": 25,
      "logo_path": "/qZCc1lty5FzX30aOCVRBLzaVmcp.png",
      "name": "20th Century Fox",
      "origin_country": "US"
    }
  ],
  "production_countries": [
    {
      "iso_3166_1": "US",
      "name": "United States of America"
    }
  ],
  "release_date": "1977-05-25",
  "revenue": 775398007,
  "runtime": 121,
  "spoken_languages": [
    {
      "english_name": "English",
      "iso_639_1": "en",
      "name": "English"
    }
  ],
  "status": "Released",
  "tagline": "A long time ago in a galaxy far, far away...",
  "title": "Star Wars",
  "video": false,
  "vote_average": 8.2,
  "vote_count": 22061
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `adult` | boolean |  |  | `False` |
| `backdrop_path` | string |  |  | `/2w4xG178RpB4MDAIfTkqAuSJzec.jpg` |
| `belongs_to_collection` | object |  |  |  |
| `id` | integer |  |  | `10` |
| `name` | string |  |  | `Star Wars Collection` |
| `poster_path` | string |  |  | `/pWVLFh4OuejTpUaDQbB1C4zoS2p.jpg` |
| `backdrop_path` | string |  |  | `/iY2ujEY2m68OTTlPFTiHub9joHS.jpg` |
| `budget` | integer |  |  | `11000000` |
| `genres` | array[object] |  |  |  |
| `homepage` | string |  |  | `http://www.starwars.com/films/star-wars-episode-iv-a-new-hope` |
| `id` | integer |  |  | `11` |
| `imdb_id` | string |  |  | `tt0076759` |
| `origin_country` | array[string] |  |  |  |
| `original_language` | string |  |  | `en` |
| `original_title` | string |  |  | `Star Wars` |
| `overview` | string |  |  | `Princess Leia is captured and held hostage by the evil Imperial forces in their effort to take over the galactic Empire. Venturesome Luke Skywalker and dashing captain Han Solo team together with the loveable robot duo R2-D2 and C-3PO to rescue the beautiful princess and restore peace and justice in the Empire.` |
| `popularity` | number |  |  | `20.6912` |
| `poster_path` | string |  |  | `/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg` |
| `production_companies` | array[object] |  |  |  |
| `production_countries` | array[object] |  |  |  |
| `release_date` | string |  |  | `1977-05-25` |
| `revenue` | integer |  |  | `775398007` |
| `runtime` | integer |  |  | `121` |
| `spoken_languages` | array[object] |  |  |  |
| `status` | string |  |  | `Released` |
| `tagline` | string |  |  | `A long time ago in a galaxy far, far away...` |
| `title` | string |  |  | `Star Wars` |
| `video` | boolean |  |  | `False` |
| `vote_average` | number |  |  | `8.2` |
| `vote_count` | integer |  |  | `22061` |

---

### Account States

```
GET /3/movie/{movie_id}/account_states
```

Get the rating, watchlist and favourite status of an account.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `movie_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `session_id` | string |  |  |
| `guest_session_id` | string |  |  |

### Response (200)

**Example Response:**
```json
{
  "id": 550,
  "favorite": true,
  "rated": {
    "value": 9.0
  },
  "watchlist": false
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | integer |  |  | `550` |
| `favorite` | boolean |  |  | `True` |
| `rated` | object |  |  |  |
| `value` | integer |  |  | `9` |
| `watchlist` | boolean |  |  | `False` |

---

### Alternative Titles

```
GET /3/movie/{movie_id}/alternative_titles
```

Get the alternative titles for a movie.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `movie_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `country` | string |  | specify a ISO-3166-1 value to filter the results |

### Response (200)

**Example Response:**
```json
{
  "id": 550,
  "titles": [
    {
      "iso_3166_1": "RS",
      "title": "Borila\u010dki klub",
      "type": ""
    },
    {
      "iso_3166_1": "IL",
      "title": "Mo'adon Krav",
      "type": "romanization"
    },
    {
      "iso_3166_1": "RU",
      "title": "Boytsovskiy klub",
      "type": ""
    },
    {
      "iso_3166_1": "BG",
      "title": "Boen klub",
      "type": ""
    },
    {
      "iso_3166_1": "GR",
      "title": "Kl\u00e1b m\u00e1chis",
      "type": ""
    },
    {
      "iso_3166_1": "UA",
      "title": "Biytsivs\u02b9kyy klub",
      "type": ""
    },
    {
      "iso_3166_1": "TR",
      "title": "D\u00f6v\u00fc\u015f Klub\u00fc",
      "type": ""
    },
    {
      "iso_3166_1": "MX",
      "title": "El Club de la Pelea",
      "type": "Hispanoam\u00e9rica"
    },
    {
      "iso_3166_1": "KR",
      "title": "\ud30c\uc774\ud2b8 \ud074\ub7fd",
      "type": ""
    },
    {
      "iso_3166_1": "LV",
      "title": "C\u012b\u0146as klubs",
      "type": ""
    },
    {
      "iso_3166_1": "IR",
      "title": "\u0628\u0627\u0634\u06af\u0627\u0647 \u0645\u0634\u062a \u0632\u0646\u06cc",
      "type": ""
    },
    {
      "iso_3166_1": "PL",
      "title": "Podziemny kr\u0105g",
      "type": ""
    }
  ]
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | integer |  |  | `550` |
| `titles` | array[object] |  |  |  |

---

### Changes

```
GET /3/movie/{movie_id}/changes
```

Get the recent changes for a movie.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `movie_id` | integer | ✓ |  |

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
  "changes": [
    {
      "key": "images",
      "items": [
        {
          "id": "643197b96dea3a00d4377270",
          "action": "added",
          "time": "2023-04-08 16:35:05 UTC",
          "iso_639_1": "",
          "iso_3166_1": "",
          "value": {
            "poster": {
              "file_path": "/s9ZrHprviFCx3azfWNBtt1LPSnL.jpg"
            }
          }
        },
        {
          "id": "643197bae92d8300f46c92f5",
          "action": "added",
          "time": "2023-04-08 16:35:06 UTC",
          "iso_639_1": "",
          "iso_3166_1": "",
          "value": {
            "poster": {
              "file_path": "/xQjGTWyNHXqqACOanXwOk1mOnxU.jpg"
            }
          }
        },
        {
          "id": "643197b9e92d8301130781d3",
          "action": "added",
          "time": "2023-04-08 16:35:06 UTC",
          "iso_639_1": "",
          "iso_3166_1": "",
          "value": {
            "poster": {
              "file_path": "/2wABwAmRQldXQzMeLRmFHFfdR8K.jpg"
            }
          }
        },
        {
          "id": "643197bae92d8301130781d5",
          "action": "added",
          "time": "2023-04-08 16:35:07 UTC",
          "iso_639_1": "",
          "iso_3166_1": "",
          "value": {
            "poster": {
              "file_path": "/iTzXuEz43pifWGwR6PJZyufOFBT.jpg"
            }
          }
        },
        {
          "id": "6431aa0931032501036ef401",
          "action": "added",
          "time": "2023-04-08 17:53:13 UTC",
          "iso_639_1": "",
          "iso_3166_1": "",
          "value": {
            "poster": {
              "file_path": "/wsCBoTkV0An7Z6SZ0UQLlxvqG4x.jpg"
            }
          }
        },
        {
          "id": "6431aa0a6dea3a00b54f0fc9",
          "action": "added",
          "time": "2023-04-08 17:53:14 UTC",
          "iso_639_1": "",
          "iso_3166_1": "",
          "value": {
            "poster": {
              "file_path": "/36q02yK213MtSeicy5ZmnlLba7q.jpg"
            
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `changes` | array[object] |  |  |  |

---

### Credits

```
GET /3/movie/{movie_id}/credits
```

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `movie_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |

### Response (200)

**Example Response:**
```json
{
  "id": 550,
  "cast": [
    {
      "adult": false,
      "gender": 2,
      "id": 819,
      "known_for_department": "Acting",
      "name": "Edward Norton",
      "original_name": "Edward Norton",
      "popularity": 26.99,
      "profile_path": "/8nytsqL59SFJTVYVrN72k6qkGgJ.jpg",
      "cast_id": 4,
      "character": "The Narrator",
      "credit_id": "52fe4250c3a36847f80149f3",
      "order": 0
    },
    {
      "adult": false,
      "gender": 2,
      "id": 287,
      "known_for_department": "Acting",
      "name": "Brad Pitt",
      "original_name": "Brad Pitt",
      "popularity": 45.202,
      "profile_path": "/huV2cdcolEUwJy37QvH914vup7d.jpg",
      "cast_id": 5,
      "character": "Tyler Durden",
      "credit_id": "52fe4250c3a36847f80149f7",
      "order": 1
    },
    {
      "adult": false,
      "gender": 1,
      "id": 1283,
      "known_for_department": "Acting",
      "name": "Helena Bonham Carter",
      "original_name": "Helena Bonham Carter",
      "popularity": 22.112,
      "profile_path": "/DDeITcCpnBd0CkAIRPhggy9bt5.jpg",
      "cast_id": 285,
      "character": "Marla Singer",
      "credit_id": "631f0de8bd32090082733691",
      "order": 2
    },
    {
      "adult": false,
      "gender": 2,
      "id": 7470,
      "known_for_department": "Acting",
      "name": "Meat Loaf",
      "original_name": "Meat Loaf",
      "popularity": 7.738,
      "profile_path": "/7gKLR1u46OB8WJ6m06LemNBCMx6.jpg",
      "cast_id": 7,
      "character": "Robert \"Bob\" Paulson",
      "credit_id": "52fe4250c3a36847f80149ff",
      "order": 3
    },
    {
      "adult": false,
      "gender": 2,
      "id": 7499,
      "known_for_department": "Acting",
      "name": "Jared Leto",
      "original_name": "Jared Leto",
      "popularity": 18.969,
      "profile_path": "/ca3x0OfIKbJppZh8S1Alx3GfUZO.jpg",
      "cast_id": 286,
      "character": "Angel Face",
      "credit_id": "631f0e29ce9e91007f757d86",
      "order": 4
    },
    {
      "adult": false,
      
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | integer |  |  | `550` |
| `cast` | array[object] |  |  |  |
| `crew` | array[object] |  |  |  |

---

### External IDs

```
GET /3/movie/{movie_id}/external_ids
```

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `movie_id` | integer | ✓ |  |

### Response (200)

**Example Response:**
```json
{
  "id": 550,
  "imdb_id": "tt0137523",
  "wikidata_id": null,
  "facebook_id": "FightClub",
  "instagram_id": null,
  "twitter_id": null
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | integer |  |  | `550` |
| `imdb_id` | string |  |  | `tt0137523` |
| `wikidata_id` |  |  |  |  |
| `facebook_id` | string |  |  | `FightClub` |
| `instagram_id` |  |  |  |  |
| `twitter_id` |  |  |  |  |

---

### Images

```
GET /3/movie/{movie_id}/images
```

Get the images that belong to a movie.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `movie_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `include_image_language` | string |  | specify a comma separated list of ISO-639-1 values to query, for example: `en-US,null` |
| `language` | string |  |  |

### Response (200)

**Example Response:**
```json
{
  "backdrops": [
    {
      "aspect_ratio": 1.778,
      "height": 800,
      "iso_639_1": null,
      "file_path": "/hZkgoQYus5vegHoetLkCJzb17zJ.jpg",
      "vote_average": 5.622,
      "vote_count": 20,
      "width": 1422
    },
    {
      "aspect_ratio": 1.778,
      "height": 720,
      "iso_639_1": "en",
      "file_path": "/fygeMr16EcxJiYhdiO1LEr7iHtI.jpg",
      "vote_average": 5.318,
      "vote_count": 3,
      "width": 1280
    },
    {
      "aspect_ratio": 1.778,
      "height": 1080,
      "iso_639_1": "en",
      "file_path": "/b9HyPoxwxjxkWEUL5ErZdhApQe2.jpg",
      "vote_average": 5.312,
      "vote_count": 1,
      "width": 1920
    },
    {
      "aspect_ratio": 1.778,
      "height": 1440,
      "iso_639_1": null,
      "file_path": "/c6OLXfKAk5BKeR6broC8pYiCquX.jpg",
      "vote_average": 5.292,
      "vote_count": 18,
      "width": 2560
    },
    {
      "aspect_ratio": 1.778,
      "height": 1080,
      "iso_639_1": null,
      "file_path": "/3nv2TEz2u178xPXzdKlZdUh5uOI.jpg",
      "vote_average": 5.276,
      "vote_count": 12,
      "width": 1920
    },
    {
      "aspect_ratio": 1.778,
      "height": 1080,
      "iso_639_1": null,
      "file_path": "/yguBaPk5V0nZCcSBthre4YFMAgk.jpg",
      "vote_average": 5.212,
      "vote_count": 11,
      "width": 1920
    },
    {
      "aspect_ratio": 1.778,
      "height": 1080,
      "iso_639_1": null,
      "file_path": "/xRyINp9KfMLVjRiO5nCsoRDdvvF.jpg",
      "vote_average": 5.206,
      "vote_count": 9,
      "width": 1920
    },
    {
      "aspect_ratio": 1.778,
      "height": 1080,
      "iso_639_1": null,
      "file_path": "/bsfJoKVAqFzlhvbt8AffjvYAtN4.jpg",
      "vote_average": 5.19,
      "vote_count": 5,
      "width": 1920
    },
    {
      "aspect_ratio": 1.778,
      "height": 1080,
      "iso_639_1": null,
      "file_path": "/kpRWGjh3SsYjuF26HyRhCJJkMRk.jpg",
      "vote_average": 5.19,
      "vote_count": 5,
      "width": 1920
    },
    {
      "aspect_ratio": 1.778,
  
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `backdrops` | array[object] |  |  |  |
| `id` | integer |  |  | `550` |
| `logos` | array[object] |  |  |  |
| `posters` | array[object] |  |  |  |

---

### Keywords

```
GET /3/movie/{movie_id}/keywords
```

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `movie_id` | string | ✓ |  |

### Response (200)

**Example Response:**
```json
{
  "id": 550,
  "keywords": [
    {
      "id": 818,
      "name": "based on novel or book"
    },
    {
      "id": 825,
      "name": "support group"
    },
    {
      "id": 851,
      "name": "dual identity"
    },
    {
      "id": 1541,
      "name": "nihilism"
    },
    {
      "id": 1721,
      "name": "fight"
    },
    {
      "id": 3927,
      "name": "rage and hate"
    },
    {
      "id": 4142,
      "name": "insomnia"
    },
    {
      "id": 4565,
      "name": "dystopia"
    },
    {
      "id": 9181,
      "name": "alter ego"
    },
    {
      "id": 11687,
      "name": "breaking the fourth wall"
    },
    {
      "id": 34117,
      "name": "cult film"
    },
    {
      "id": 156761,
      "name": "split personality"
    },
    {
      "id": 179173,
      "name": "quitting a job"
    },
    {
      "id": 212803,
      "name": "dissociative identity disorder"
    },
    {
      "id": 260426,
      "name": "self destructiveness"
    }
  ]
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | integer |  |  | `550` |
| `keywords` | array[object] |  |  |  |

---

### Latest

```
GET /3/movie/latest
```

Get the newest movie ID.

### Response (200)

**Example Response:**
```json
{
  "adult": false,
  "backdrop_path": null,
  "belongs_to_collection": null,
  "budget": 0,
  "genres": [],
  "homepage": "",
  "id": 1119232,
  "imdb_id": null,
  "original_language": "fr",
  "original_title": "K\u00f6nig Charles III",
  "overview": "",
  "popularity": 0.0,
  "poster_path": null,
  "production_companies": [],
  "production_countries": [],
  "release_date": "",
  "revenue": 0,
  "runtime": 0,
  "spoken_languages": [],
  "status": "Released",
  "tagline": "",
  "title": "K\u00f6nig Charles III",
  "video": false,
  "vote_average": 0.0,
  "vote_count": 0
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `adult` | boolean |  |  | `False` |
| `backdrop_path` |  |  |  |  |
| `belongs_to_collection` |  |  |  |  |
| `budget` | integer |  |  | `0` |
| `genres` | array |  |  |  |
| `homepage` | string |  |  |  |
| `id` | integer |  |  | `1119232` |
| `imdb_id` |  |  |  |  |
| `original_language` | string |  |  | `fr` |
| `original_title` | string |  |  | `König Charles III` |
| `overview` | string |  |  |  |
| `popularity` | integer |  |  | `0` |
| `poster_path` |  |  |  |  |
| `production_companies` | array |  |  |  |
| `production_countries` | array |  |  |  |
| `release_date` | string |  |  |  |
| `revenue` | integer |  |  | `0` |
| `runtime` | integer |  |  | `0` |
| `spoken_languages` | array |  |  |  |
| `status` | string |  |  | `Released` |
| `tagline` | string |  |  |  |
| `title` | string |  |  | `König Charles III` |
| `video` | boolean |  |  | `False` |
| `vote_average` | integer |  |  | `0` |
| `vote_count` | integer |  |  | `0` |

---

### Lists

```
GET /3/movie/{movie_id}/lists
```

Get the lists that a movie has been added to.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `movie_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |
| `page` | integer |  | *(default: `1`)* |

### Response (200)

**Example Response:**
```json
{
  "id": 550,
  "page": 1,
  "results": [
    {
      "description": "Movies I own",
      "favorite_count": 0,
      "id": 8248696,
      "item_count": 409,
      "iso_639_1": "en",
      "list_type": "movie",
      "name": "My Movies",
      "poster_path": null
    },
    {
      "description": "",
      "favorite_count": 0,
      "id": 8211179,
      "item_count": 842,
      "iso_639_1": "en",
      "list_type": "movie",
      "name": "myList",
      "poster_path": null
    },
    {
      "description": "I watch way too much but not everything till the end",
      "favorite_count": 0,
      "id": 142064,
      "item_count": 2245,
      "iso_639_1": "en",
      "list_type": "movie",
      "name": "Watched",
      "poster_path": null
    },
    {
      "description": "",
      "favorite_count": 0,
      "id": 8168597,
      "item_count": 14752,
      "iso_639_1": "en",
      "list_type": "movie",
      "name": "movies",
      "poster_path": null
    },
    {
      "description": "",
      "favorite_count": 0,
      "id": 7054306,
      "item_count": 1551,
      "iso_639_1": "es",
      "list_type": "movie",
      "name": "Peliculas",
      "poster_path": null
    },
    {
      "description": "",
      "favorite_count": 0,
      "id": 7075790,
      "item_count": 1358,
      "iso_639_1": "es",
      "list_type": "movie",
      "name": "Accion",
      "poster_path": null
    },
    {
      "description": "",
      "favorite_count": 0,
      "id": 7102641,
      "item_count": 452,
      "iso_639_1": "en",
      "list_type": "movie",
      "name": "Seen movies",
      "poster_path": null
    },
    {
      "description": "",
      "favorite_count": 0,
      "id": 8191899,
      "item_count": 412,
      "iso_639_1": "fr",
      "list_type": "movie",
      "name": "Vu",
      "poster_path": null
    },
    {
      "description": "",
      "favorite_count": 0,
      "id": 127215,
      "item_count": 498,
      "iso_639_1": "en",
      "list_type": "movie",
      "name":
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | integer |  |  | `550` |
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `122` |
| `total_results` | integer |  |  | `2422` |

---

### Recommendations

```
GET /3/movie/{movie_id}/recommendations
```

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `movie_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |
| `page` | integer |  | *(default: `1`)* |

### Response (200)

**Example Response:**
```json
{}
```

---

### Release Dates

```
GET /3/movie/{movie_id}/release_dates
```

Get the release dates and certifications for a movie.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `movie_id` | integer | ✓ |  |

### Response (200)

**Example Response:**
```json
{
  "id": 550,
  "results": [
    {
      "iso_3166_1": "BG",
      "release_dates": [
        {
          "certification": "c",
          "descriptors": [],
          "iso_639_1": "",
          "note": "",
          "release_date": "2012-08-28T00:00:00.000Z",
          "type": 3
        }
      ]
    },
    {
      "iso_3166_1": "CH",
      "release_dates": [
        {
          "certification": "18",
          "descriptors": [],
          "iso_639_1": "de",
          "note": "",
          "release_date": "1999-11-04T00:00:00.000Z",
          "type": 3
        },
        {
          "certification": "18",
          "descriptors": [],
          "iso_639_1": "fr",
          "note": "",
          "release_date": "1999-11-10T00:00:00.000Z",
          "type": 3
        }
      ]
    },
    {
      "iso_3166_1": "IE",
      "release_dates": [
        {
          "certification": "18",
          "descriptors": [],
          "iso_639_1": "",
          "note": "",
          "release_date": "1999-11-12T00:00:00.000Z",
          "type": 3
        }
      ]
    },
    {
      "iso_3166_1": "NL",
      "release_dates": [
        {
          "certification": "16",
          "descriptors": [],
          "iso_639_1": "",
          "note": "",
          "release_date": "1999-11-04T00:00:00.000Z",
          "type": 3
        },
        {
          "certification": "16",
          "descriptors": [],
          "iso_639_1": "",
          "note": "DVD",
          "release_date": "2004-08-04T00:00:00.000Z",
          "type": 5
        },
        {
          "certification": "16",
          "descriptors": [],
          "iso_639_1": "",
          "note": "Net 5",
          "release_date": "2002-10-26T00:00:00.000Z",
          "type": 5
        }
      ]
    },
    {
      "iso_3166_1": "US",
      "release_dates": [
        {
          "certification": "",
          "descriptors": [],
          "iso_639_1": "",
          "note": "CMJ Film Festival",
          "release_date": "1999-09-21T00
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | integer |  |  | `550` |
| `results` | array[object] |  |  |  |

---

### Reviews

```
GET /3/movie/{movie_id}/reviews
```

Get the user reviews for a movie.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `movie_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |
| `page` | integer |  | *(default: `1`)* |

### Response (200)

**Example Response:**
```json
{
  "id": 550,
  "page": 1,
  "results": [
    {
      "author": "Goddard",
      "author_details": {
        "name": "",
        "username": "Goddard",
        "avatar_path": "/https://secure.gravatar.com/avatar/f248ec34f953bc62cafcbdd81fddd6b6.jpg",
        "rating": null
      },
      "content": "Pretty awesome movie.  It shows what one crazy person can convince other crazy people to do.  Everyone needs something to believe in.  I recommend Jesus Christ, but they want Tyler Durden.",
      "created_at": "2018-06-09T17:51:53.359Z",
      "id": "5b1c13b9c3a36848f2026384",
      "updated_at": "2021-06-23T15:58:09.421Z",
      "url": "https://www.themoviedb.org/review/5b1c13b9c3a36848f2026384"
    },
    {
      "author": "Brett Pascoe",
      "author_details": {
        "name": "Brett Pascoe",
        "username": "SneekyNuts",
        "avatar_path": "/https://secure.gravatar.com/avatar/04d45e186650672a416315dac947b3d6.jpg",
        "rating": 9.0
      },
      "content": "In my top 5 of all time favourite movies. Great story line and a movie you can watch over and over again.",
      "created_at": "2018-07-05T13:22:41.754Z",
      "id": "5b3e1ba1925141144c007f17",
      "updated_at": "2021-06-23T15:58:10.199Z",
      "url": "https://www.themoviedb.org/review/5b3e1ba1925141144c007f17"
    },
    {
      "author": "MSB",
      "author_details": {
        "name": "MSB",
        "username": "msbreviews",
        "avatar_path": "/https://secure.gravatar.com/avatar/992eef352126a53d7e141bf9e8707576.jpg",
        "rating": 8.0
      },
      "content": "If you enjoy reading my Spoiler-Free reviews, please follow my blog @\r\nhttps://www.msbreviews.com\r\n\r\nDavid Fincher\u2019s new film, Mank, is coming soon on Netflix, released six years after his latest installment, Gone Girl. Therefore, this week I\u2019m reviewing five of Fincher\u2019s movies. Se7en was the first one, and now it\u2019s time for one of the most culturally impactful films of the 90s, Fight Club. This i
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | integer |  |  | `550` |
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `1` |
| `total_results` | integer |  |  | `8` |

---

### Similar

```
GET /3/movie/{movie_id}/similar
```

Get the similar movies based on genres and keywords.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `movie_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |
| `page` | integer |  | *(default: `1`)* |

### Response (200)

**Example Response:**
```json
{
  "page": 1,
  "results": [
    {
      "adult": false,
      "backdrop_path": "/3YAldML4EDyoC6RBpzceALigrAZ.jpg",
      "genre_ids": [
        18,
        14
      ],
      "id": 9300,
      "original_language": "en",
      "original_title": "Orlando",
      "overview": "England, 1600. Queen Elizabeth I promises Orlando, a young nobleman obsessed with poetry, that she will grant him land and fortune if he agrees to satisfy a very particular request.",
      "popularity": 7.768,
      "poster_path": "/xvz0qZkXXMq3dH2Revxii8drxWc.jpg",
      "release_date": "1992-12-11",
      "title": "Orlando",
      "video": false,
      "vote_average": 6.966,
      "vote_count": 262
    },
    {
      "adult": false,
      "backdrop_path": "/4TQgxCYdaizZr9bfjQYVsZPZVGE.jpg",
      "genre_ids": [
        28,
        80,
        18,
        9648,
        53
      ],
      "id": 9311,
      "original_language": "en",
      "original_title": "Smilla's Sense of Snow",
      "overview": "Smilla Jaspersen, half Danish, half Greenlander, attempts to understand the death of a small boy who falls from the roof of her apartment building. Suspecting wrongdoing, Smilla uncovers a trail of clues leading towards a secretive corporation that has made several mysterious expeditions to Greenland. Scenes from the film were shot in Copenhagen and western Greenland. The film was entered into the 47th Berlin International Film Festival, where director Bille August was nominated for the Golden Bear.",
      "popularity": 11.958,
      "poster_path": "/3eeCYGVWb4Ic8SFpARGWOjyl9Md.jpg",
      "release_date": "1997-02-28",
      "title": "Smilla's Sense of Snow",
      "video": false,
      "vote_average": 6.351,
      "vote_count": 202
    },
    {
      "adult": false,
      "backdrop_path": "/mILBIbGUP465jmCgzFCM2F0JnrZ.jpg",
      "genre_ids": [
        18,
        878,
        53
      ],
      "id": 9314,
      "original_language": "en",
      "original_title": "Nineteen Eighty-Four",
      "overv
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `364` |
| `total_results` | integer |  |  | `7269` |

---

### Translations

```
GET /3/movie/{movie_id}/translations
```

Get the translations for a movie.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `movie_id` | integer | ✓ |  |

### Response (200)

**Example Response:**
```json
{
  "id": 550,
  "translations": [
    {
      "iso_3166_1": "SA",
      "iso_639_1": "ar",
      "name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
      "english_name": "Arabic",
      "data": {
        "homepage": "",
        "overview": "\u0625\u062f\u0648\u0627\u0631\u062f \u064a\u062a\u0639\u0631\u0636 \u0644\u0636\u063a\u0648\u0637 \u062d\u062a\u0649 \u064a\u0635\u0644 \u0628\u0647 \u0627\u0644\u062d\u0627\u0644 \u0625\u0644\u0649 \u0623\u0646\u0647 \u0644\u0627 \u064a\u0633\u062a\u0637\u064a\u0639 \u0627\u0644\u0646\u0648\u0645 \u0644\u0641\u062a\u0631\u0627\u062a\u064d \u0637\u0648\u064a\u0644\u0629\u060c \u0644\u0643\u0646\u0647 \u064a\u062c\u062f \u0628\u0639\u0636 \u0627\u0644\u0633\u0644\u0627\u0645 \u0641\u064a \u062c\u0644\u0633\u0627\u062a \u0627\u0644\u0639\u0644\u0627\u062c \u0627\u0644\u0646\u0641\u0633\u064a \u0627\u0644\u062c\u0645\u0627\u0639\u064a\u060c \u064a\u062a\u0639\u0631\u0641 \u0625\u062f\u0648\u0627\u0631\u062f \u0639\u0644\u0649 \u0623\u062d\u062f \u0627\u0644\u0623\u0634\u062e\u0627\u0635 \u0648\u0647\u0648 (\u062a\u0627\u064a\u0644\u0631 \u062f\u064a\u0631\u062f\u0646) \u0627\u0644\u0630\u064a \u064a\u062d\u0631\u0631\u0647 \u0645\u0646 \u062a\u0639\u0644\u0642\u0647 \u0628\u0627\u0644\u0623\u0634\u064a\u0627\u0621 \u0627\u0644\u0630\u064a \u062a\u0633\u062a\u0639\u0628\u062f\u0647 \u060c\u062b\u0645 \u064a\u062d\u0631\u0631\u0647 \u0645\u0646 \u062e\u0648\u0641\u0647 \u0645\u0646 \u0627\u0644\u0646\u0627\u0633. \u064a\u0642\u0648\u0645\u0627\u0646 \u0645\u0639\u064b\u0627 \u0628\u0625\u0646\u0634\u0627\u0621 \u0646\u0627\u062f\u064a \u0627\u0644\u0642\u062a\u0627\u0644 \u0627\u0644\u0630\u064a \u064a\u062c\u0630\u0628 \u0627\u0644\u0643\u062b\u064a\u0631 \u0645\u0646 \u0627\u0644\u0623\u0641\u0631\u0627\u062f \u0627\u0644\u0645\u062d\u0628\u0637\u064a\u0646 \u060c\u0627\u0644\u0630\u064a\u0646 \u064a\u0642\u0648\u0645\u0648\u0646 \u0628\u0625\u062e\u0631\u0627\u062c \u0637\u0627\u0642\u0629 \u063a\u0636\u0628\u0647\u0645 \u0648
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | integer |  |  | `550` |
| `translations` | array[object] |  |  |  |

---

### Videos

```
GET /3/movie/{movie_id}/videos
```

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `movie_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |

### Response (200)

**Example Response:**
```json
{
  "id": 550,
  "results": [
    {
      "iso_639_1": "en",
      "iso_3166_1": "US",
      "name": "Fight Club (1999) Trailer - Starring Brad Pitt, Edward Norton, Helena Bonham Carter",
      "key": "O-b2VfmmbyA",
      "site": "YouTube",
      "size": 720,
      "type": "Trailer",
      "official": false,
      "published_at": "2016-03-05T02:03:14.000Z",
      "id": "639d5326be6d88007f170f44"
    },
    {
      "iso_639_1": "en",
      "iso_3166_1": "US",
      "name": "#TBT Trailer",
      "key": "BdJKm16Co6M",
      "site": "YouTube",
      "size": 1080,
      "type": "Trailer",
      "official": true,
      "published_at": "2014-10-02T19:20:22.000Z",
      "id": "5c9294240e0a267cd516835f"
    }
  ]
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | integer |  |  | `550` |
| `results` | array[object] |  |  |  |

---

### Watch Providers

```
GET /3/movie/{movie_id}/watch/providers
```

Get the list of streaming providers we have for a movie.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `movie_id` | integer | ✓ |  |

### Response (200)

**Example Response:**
```json
{
  "id": 550,
  "results": {
    "AE": {
      "link": "https://www.themoviedb.org/movie/550-fight-club/watch?locale=AE",
      "flatrate": [
        {
          "logo_path": "/emthp39XA2YScoYL1p0sdbAH2WA.jpg",
          "provider_id": 119,
          "provider_name": "Amazon Prime Video",
          "display_priority": 12
        }
      ],
      "rent": [
        {
          "logo_path": "/peURlLlr8jggOwK53fJ5wdQl05y.jpg",
          "provider_id": 2,
          "provider_name": "Apple TV",
          "display_priority": 1
        },
        {
          "logo_path": "/tbEdFQDwx5LEVr8WpSeXQSIirVq.jpg",
          "provider_id": 3,
          "provider_name": "Google Play Movies",
          "display_priority": 3
        }
      ],
      "buy": [
        {
          "logo_path": "/peURlLlr8jggOwK53fJ5wdQl05y.jpg",
          "provider_id": 2,
          "provider_name": "Apple TV",
          "display_priority": 1
        },
        {
          "logo_path": "/tbEdFQDwx5LEVr8WpSeXQSIirVq.jpg",
          "provider_id": 3,
          "provider_name": "Google Play Movies",
          "display_priority": 3
        }
      ]
    },
    "AL": {
      "link": "https://www.themoviedb.org/movie/550-fight-club/watch?locale=AL",
      "buy": [
        {
          "logo_path": "/5GEbAhFW2S5T8zVc1MNvz00pIzM.jpg",
          "provider_id": 35,
          "provider_name": "Rakuten TV",
          "display_priority": 9
        },
        {
          "logo_path": "/tbEdFQDwx5LEVr8WpSeXQSIirVq.jpg",
          "provider_id": 3,
          "provider_name": "Google Play Movies",
          "display_priority": 1000
        }
      ]
    },
    "AR": {
      "link": "https://www.themoviedb.org/movie/550-fight-club/watch?locale=AR",
      "buy": [
        {
          "logo_path": "/tbEdFQDwx5LEVr8WpSeXQSIirVq.jpg",
          "provider_id": 3,
          "provider_name": "Google Play Movies",
          "display_priority": 6
        }
      ],
      "flatrate": [
        {
          "logo_path": "/emthp39XA2YS
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | integer |  |  | `550` |
| `results` | object |  |  |  |
| `AE` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=AE` |
| `flatrate` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `AL` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=AL` |
| `buy` | array[object] |  |  |  |
| `AR` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=AR` |
| `buy` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `AT` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=AT` |
| `flatrate` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `AU` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=AU` |
| `flatrate` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `BA` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=BA` |
| `buy` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `BB` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=BB` |
| `flatrate` | array[object] |  |  |  |
| `BE` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=BE` |
| `rent` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `BG` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=BG` |
| `rent` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `BH` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=BH` |
| `buy` | array[object] |  |  |  |
| `BO` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=BO` |
| `flatrate` | array[object] |  |  |  |
| `BR` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=BR` |
| `flatrate` | array[object] |  |  |  |
| `BS` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=BS` |
| `flatrate` | array[object] |  |  |  |
| `CA` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=CA` |
| `rent` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `CH` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=CH` |
| `flatrate` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `CL` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=CL` |
| `buy` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `CO` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=CO` |
| `buy` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `CR` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=CR` |
| `flatrate` | array[object] |  |  |  |
| `CV` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=CV` |
| `buy` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `CZ` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=CZ` |
| `flatrate` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `DE` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=DE` |
| `flatrate` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `DK` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=DK` |
| `rent` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `DO` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=DO` |
| `flatrate` | array[object] |  |  |  |
| `EC` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=EC` |
| `buy` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `EE` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=EE` |
| `buy` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `EG` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=EG` |
| `rent` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `ES` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=ES` |
| `rent` | array[object] |  |  |  |
| `ads` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `FI` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=FI` |
| `flatrate` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `FJ` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=FJ` |
| `buy` | array[object] |  |  |  |
| `FR` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=FR` |
| `rent` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `GB` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=GB` |
| `flatrate` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `GF` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=GF` |
| `flatrate` | array[object] |  |  |  |
| `GI` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=GI` |
| `flatrate` | array[object] |  |  |  |
| `GR` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=GR` |
| `flatrate` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `GT` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=GT` |
| `flatrate` | array[object] |  |  |  |
| `HK` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=HK` |
| `flatrate` | array[object] |  |  |  |
| `HN` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=HN` |
| `flatrate` | array[object] |  |  |  |
| `HR` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=HR` |
| `buy` | array[object] |  |  |  |
| `ads` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `HU` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=HU` |
| `flatrate` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `ID` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=ID` |
| `flatrate` | array[object] |  |  |  |
| `IE` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=IE` |
| `rent` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `IL` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=IL` |
| `buy` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `IN` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=IN` |
| `flatrate` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `IQ` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=IQ` |
| `flatrate` | array[object] |  |  |  |
| `IS` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=IS` |
| `buy` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `IT` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=IT` |
| `buy` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `JM` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=JM` |
| `flatrate` | array[object] |  |  |  |
| `JO` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=JO` |
| `flatrate` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `JP` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=JP` |
| `flatrate` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `KR` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=KR` |
| `flatrate` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `KW` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=KW` |
| `buy` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `LB` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=LB` |
| `flatrate` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `LI` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=LI` |
| `flatrate` | array[object] |  |  |  |
| `LT` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=LT` |
| `rent` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `LV` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=LV` |
| `flatrate` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `MD` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=MD` |
| `buy` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `MK` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=MK` |
| `flatrate` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `MT` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=MT` |
| `flatrate` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `MU` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=MU` |
| `buy` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `MX` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=MX` |
| `flatrate` | array[object] |  |  |  |
| `MY` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=MY` |
| `flatrate` | array[object] |  |  |  |
| `MZ` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=MZ` |
| `rent` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `NL` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=NL` |
| `buy` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `NO` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=NO` |
| `rent` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `NZ` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=NZ` |
| `flatrate` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `OM` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=OM` |
| `buy` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `PA` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=PA` |
| `flatrate` | array[object] |  |  |  |
| `PE` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=PE` |
| `rent` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `PH` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=PH` |
| `flatrate` | array[object] |  |  |  |
| `PK` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=PK` |
| `flatrate` | array[object] |  |  |  |
| `PL` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=PL` |
| `buy` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `PS` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=PS` |
| `flatrate` | array[object] |  |  |  |
| `PT` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=PT` |
| `buy` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `PY` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=PY` |
| `flatrate` | array[object] |  |  |  |
| `QA` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=QA` |
| `flatrate` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `RO` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=RO` |
| `flatrate` | array[object] |  |  |  |
| `RS` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=RS` |
| `flatrate` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `RU` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=RU` |
| `rent` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `SA` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=SA` |
| `flatrate` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `SE` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=SE` |
| `buy` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `SG` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=SG` |
| `flatrate` | array[object] |  |  |  |
| `SI` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=SI` |
| `buy` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `SK` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=SK` |
| `buy` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `SM` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=SM` |
| `flatrate` | array[object] |  |  |  |
| `SV` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=SV` |
| `flatrate` | array[object] |  |  |  |
| `TH` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=TH` |
| `flatrate` | array[object] |  |  |  |
| `TR` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=TR` |
| `rent` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `TT` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=TT` |
| `flatrate` | array[object] |  |  |  |
| `TW` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=TW` |
| `flatrate` | array[object] |  |  |  |
| `UG` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=UG` |
| `rent` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `US` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=US` |
| `rent` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `UY` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=UY` |
| `flatrate` | array[object] |  |  |  |
| `VE` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=VE` |
| `rent` | array[object] |  |  |  |
| `flatrate` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |
| `YE` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=YE` |
| `flatrate` | array[object] |  |  |  |
| `ZA` | object |  |  |  |
| `link` | string |  |  | `https://www.themoviedb.org/movie/550-fight-club/watch?locale=ZA` |
| `flatrate` | array[object] |  |  |  |
| `rent` | array[object] |  |  |  |
| `buy` | array[object] |  |  |  |

---

### Add Rating

```
POST /3/movie/{movie_id}/rating
```

Rate a movie and save it to your rated list.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `movie_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `guest_session_id` | string |  |  |
| `session_id` | string |  |  |

### Request Body

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `RAW_BODY` | string | ✓ |  |  |

### Response (200)

**Example Response:**
```json
{
  "status_code": 1,
  "status_message": "Success."
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `status_code` | integer |  |  | `1` |
| `status_message` | string |  |  | `Success.` |

---

### Delete Rating

```
DELETE /3/movie/{movie_id}/rating
```

Delete a user rating.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `movie_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `guest_session_id` | string |  |  |
| `session_id` | string |  |  |

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