## Trending

### All

```
GET /3/trending/all/{time_window}
```

Get the trending movies, TV shows and people.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `time_window` | string | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | `ISO-639-1`-`ISO-3166-1` code *(default: `en-US`)* |

### Response (200)

**Example Response:**
```json
{
  "page": 1,
  "results": [
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
      "popularity": 609.941,
      "release_date": "2023-03-08",
      "video": false,
      "vote_average": 7.374,
      "vote_count": 684
    },
    {
      "adult": false,
      "backdrop_path": "/b9UCfDzwiWw7mIFsIQR9ZJUeh7q.jpg",
      "id": 868759,
      "title": "Ghosted",
      "original_language": "en",
      "original_title": "Ghosted",
      "overview": "Salt-of-the-earth Cole falls head over heels for enigmatic Sadie \u2014 but then makes the shocking discovery that she\u2019s a secret agent. Before they can decide on a second date, Cole and Sadie are swept away on an international adventure to save the world.",
      "poster_path": "/liLN69YgoovHVgmlHJ876PKi5Yi.jpg",
      "media_type": "movie",
      "genre_ids": [
        10749,
        28,
        35
      ],
      "popularity": 619.83,
      "release_date": "2023-04-21",
      "video": false,
      "vote_average": 7.318,
      "vote_count": 359
    },
    {
      "adult": false,
      "backdrop_path": "/iJQIbOPm81fPEGKt5BPuZmfnA54.jpg",
      "id": 502356,
      "title": "The Super Mario Bros. Movie",
      "original_language": "en",
      "original_title": "The Super Mario Bros. Movie",
      "overview": "While working underground to fix a water main, Brooklyn plumbers\u2014and brothers\u2014Mario and Luigi are transported down a mysterious pipe and wander into a magical new world. But when the brothers are separated, Mario embarks on an epic quest to find Luigi.",
      "poster_path": "/qN
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `1000` |
| `total_results` | integer |  |  | `20000` |

---

### Movies

```
GET /3/trending/movie/{time_window}
```

Get the trending movies on TMDB.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `time_window` | string | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | `ISO-639-1`-`ISO-3166-1` code *(default: `en-US`)* |

### Response (200)

**Example Response:**
```json
{
  "page": 1,
  "results": [
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
      "popularity": 609.941,
      "release_date": "2023-03-08",
      "video": false,
      "vote_average": 7.374,
      "vote_count": 684
    },
    {
      "adult": false,
      "backdrop_path": "/b9UCfDzwiWw7mIFsIQR9ZJUeh7q.jpg",
      "id": 868759,
      "title": "Ghosted",
      "original_language": "en",
      "original_title": "Ghosted",
      "overview": "Salt-of-the-earth Cole falls head over heels for enigmatic Sadie \u2014 but then makes the shocking discovery that she\u2019s a secret agent. Before they can decide on a second date, Cole and Sadie are swept away on an international adventure to save the world.",
      "poster_path": "/liLN69YgoovHVgmlHJ876PKi5Yi.jpg",
      "media_type": "movie",
      "genre_ids": [
        10749,
        28,
        35
      ],
      "popularity": 619.83,
      "release_date": "2023-04-21",
      "video": false,
      "vote_average": 7.318,
      "vote_count": 359
    },
    {
      "adult": false,
      "backdrop_path": "/iJQIbOPm81fPEGKt5BPuZmfnA54.jpg",
      "id": 502356,
      "title": "The Super Mario Bros. Movie",
      "original_language": "en",
      "original_title": "The Super Mario Bros. Movie",
      "overview": "While working underground to fix a water main, Brooklyn plumbers\u2014and brothers\u2014Mario and Luigi are transported down a mysterious pipe and wander into a magical new world. But when the brothers are separated, Mario embarks on an epic quest to find Luigi.",
      "poster_path": "/qN
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `1000` |
| `total_results` | integer |  |  | `20000` |

---

### People

```
GET /3/trending/person/{time_window}
```

Get the trending people on TMDB.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `time_window` | string | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | `ISO-639-1`-`ISO-3166-1` code *(default: `en-US`)* |

### Response (200)

**Example Response:**
```json
{
  "page": 1,
  "results": [
    {
      "adult": false,
      "id": 224513,
      "name": "Ana de Armas",
      "original_name": "Ana de Armas",
      "media_type": "person",
      "popularity": 349.766,
      "gender": 1,
      "known_for_department": "Acting",
      "profile_path": "/3vxvsmYLTf4jnr163SUlBIw51ee.jpg",
      "known_for": [
        {
          "adult": false,
          "backdrop_path": "/ilRyazdMJwN05exqhwK4tMKBYZs.jpg",
          "id": 335984,
          "title": "Blade Runner 2049",
          "original_language": "en",
          "original_title": "Blade Runner 2049",
          "overview": "Thirty years after the events of the first film, a new blade runner, LAPD Officer K, unearths a long-buried secret that has the potential to plunge what's left of society into chaos. K's discovery leads him on a quest to find Rick Deckard, a former LAPD blade runner who has been missing for 30 years.",
          "poster_path": "/gajva2L0rPYkEWjzgFlBXCAVBE5.jpg",
          "media_type": "movie",
          "genre_ids": [
            878,
            18
          ],
          "popularity": 79.571,
          "release_date": "2017-10-04",
          "video": false,
          "vote_average": 7.531,
          "vote_count": 11771
        },
        {
          "adult": false,
          "backdrop_path": "/4HWAQu28e2yaWrtupFPGFkdNU7V.jpg",
          "id": 546554,
          "title": "Knives Out",
          "original_language": "en",
          "original_title": "Knives Out",
          "overview": "When renowned crime novelist Harlan Thrombey is found dead at his estate just after his 85th birthday, the inquisitive and debonair Detective Benoit Blanc is mysteriously enlisted to investigate. From Harlan's dysfunctional family to his devoted staff, Blanc sifts through a web of red herrings and self-serving lies to uncover the truth behind Harlan's untimely death.",
          "poster_path": "/pThyQovXQrw2m0s9x82twj48Jq4.jpg",
          "media_type": "movie",
          "genre_ids
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `1000` |
| `total_results` | integer |  |  | `20000` |

---

### TV

```
GET /3/trending/tv/{time_window}
```

Get the trending TV shows on TMDB.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `time_window` | string | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | `ISO-639-1`-`ISO-3166-1` code *(default: `en-US`)* |

### Response (200)

**Example Response:**
```json
{
  "page": 1,
  "results": [
    {
      "adult": false,
      "backdrop_path": "/8P15FsYcTwQZ4G5rRMd1TKD14Aq.jpg",
      "id": 103768,
      "name": "Sweet Tooth",
      "original_language": "en",
      "original_name": "Sweet Tooth",
      "overview": "On a perilous adventure across a post-apocalyptic world, a lovable boy who's half-human and half-deer searches for a new beginning with a gruff protector.",
      "poster_path": "/dBxxtfhC4vYrxB2fLsSxOTY2dQc.jpg",
      "media_type": "tv",
      "genre_ids": [
        18,
        10765
      ],
      "popularity": 137.498,
      "first_air_date": "2021-06-04",
      "vote_average": 7.928,
      "vote_count": 1094,
      "origin_country": [
        "US"
      ]
    },
    {
      "adult": false,
      "backdrop_path": "/pGtvfzfIRCsiudAWlzlGZ74co5l.jpg",
      "id": 124800,
      "name": "Love & Death",
      "original_language": "en",
      "original_name": "Love & Death",
      "overview": "The true story of Candy and Pat Montgomery and Betty and Allan Gore \u2013 two churchgoing couples enjoying their small town Texas life\u2026 until an extramarital affair leads somebody to pick up an axe.",
      "poster_path": "/8WchbT0UPQeo3PZ6G01fhccYaQB.jpg",
      "media_type": "tv",
      "genre_ids": [
        80,
        18
      ],
      "popularity": 72.051,
      "first_air_date": "2023-04-27",
      "vote_average": 7.2,
      "vote_count": 4,
      "origin_country": [
        "US"
      ]
    },
    {
      "adult": false,
      "backdrop_path": "/zE9jOFPFCz30cFY606KdhHQbPhI.jpg",
      "id": 221802,
      "name": "The Nurse",
      "original_language": "da",
      "original_name": "Sygeplejersken",
      "overview": "Pernille Kurzmann Larsen, a fresh-faced nurse at a hospital, begins to question the attention-seeking tendencies of her colleague, Christina Aistrup Hansen. As Pernille delves deeper into her suspicions, she starts to believe that Christina's behavior may be linked to a series of patient deaths.",
     
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `1000` |
| `total_results` | integer |  |  | `20000` |