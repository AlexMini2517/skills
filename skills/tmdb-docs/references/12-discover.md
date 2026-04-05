## Discover

### Movie

```
GET /3/discover/movie
```

Find movies using over 30 filters and sort options.

### Parameters

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `certification` | string |  | use in conjunction with `region` |
| `certification.gte` | string |  | use in conjunction with `region` |
| `certification.lte` | string |  | use in conjunction with `region` |
| `certification_country` | string |  | use in conjunction with the `certification`, `certification.gte` and `certification.lte` filters |
| `include_adult` | boolean |  | *(default: `False`)* |
| `include_video` | boolean |  | *(default: `False`)* |
| `language` | string |  | *(default: `en-US`)* |
| `page` | integer |  | *(default: `1`)* |
| `primary_release_year` | integer |  |  |
| `primary_release_date.gte` | string |  |  |
| `primary_release_date.lte` | string |  |  |
| `region` | string |  |  |
| `release_date.gte` | string |  |  |
| `release_date.lte` | string |  |  |
| `sort_by` | string |  | *(default: `popularity.desc`)* |
| `vote_average.gte` | number |  |  |
| `vote_average.lte` | number |  |  |
| `vote_count.gte` | number |  |  |
| `vote_count.lte` | number |  |  |
| `watch_region` | string |  | use in conjunction with `with_watch_monetization_types ` or `with_watch_providers ` |
| `with_cast` | string |  | can be a comma (`AND`) or pipe (`OR`) separated query |
| `with_companies` | string |  | can be a comma (`AND`) or pipe (`OR`) separated query |
| `with_crew` | string |  | can be a comma (`AND`) or pipe (`OR`) separated query |
| `with_genres` | string |  | can be a comma (`AND`) or pipe (`OR`) separated query |
| `with_keywords` | string |  | can be a comma (`AND`) or pipe (`OR`) separated query |
| `with_origin_country` | string |  |  |
| `with_original_language` | string |  |  |
| `with_people` | string |  | can be a comma (`AND`) or pipe (`OR`) separated query |
| `with_release_type` | integer |  | possible values are: [1, 2, 3, 4, 5, 6] can be a comma (`AND`) or pipe (`OR`) separated query, can be used in conjunction with `region` |
| `with_runtime.gte` | integer |  |  |
| `with_runtime.lte` | integer |  |  |
| `with_watch_monetization_types` | string |  | possible values are: [flatrate, free, ads, rent, buy] use in conjunction with `watch_region`, can be a comma (`AND`) or pipe (`OR`) separated query |
| `with_watch_providers` | string |  | use in conjunction with `watch_region`, can be a comma (`AND`) or pipe (`OR`) separated query |
| `without_companies` | string |  |  |
| `without_genres` | string |  |  |
| `without_keywords` | string |  |  |
| `without_watch_providers` | string |  |  |
| `year` | integer |  |  |

### Response (200)

**Example Response:**
```json
{
  "page": 1,
  "results": [
    {
      "adult": false,
      "backdrop_path": "/8YFL5QQVPy3AgrEQxNYVSgiPEbe.jpg",
      "genre_ids": [
        28,
        12,
        878
      ],
      "id": 640146,
      "original_language": "en",
      "original_title": "Ant-Man and the Wasp: Quantumania",
      "overview": "Super-Hero partners Scott Lang and Hope van Dyne, along with with Hope's parents Janet van Dyne and Hank Pym, and Scott's daughter Cassie Lang, find themselves exploring the Quantum Realm, interacting with strange new creatures and embarking on an adventure that will push them beyond the limits of what they thought possible.",
      "popularity": 9272.643,
      "poster_path": "/ngl2FKBlU4fhbdsrtdom9LVLBXw.jpg",
      "release_date": "2023-02-15",
      "title": "Ant-Man and the Wasp: Quantumania",
      "video": false,
      "vote_average": 6.5,
      "vote_count": 1856
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
      "popularity": 7212.464,
      "poster_path": "/qNBAXBIQlnOThrVvA6mA2B5ggV6.jpg",
      "release_date": "2023-04-05",
      "title": "The Super Mario Bros. Movie",
      "video": false,
      "vote_average": 7.5,
      "vote_count": 1435
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
| `total_pages` | integer |  |  | `38020` |
| `total_results` | integer |  |  | `760385` |

---

### TV

```
GET /3/discover/tv
```

Find TV shows using over 30 filters and sort options.

### Parameters

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `air_date.gte` | string |  |  |
| `air_date.lte` | string |  |  |
| `first_air_date_year` | integer |  |  |
| `first_air_date.gte` | string |  |  |
| `first_air_date.lte` | string |  |  |
| `include_adult` | boolean |  | *(default: `False`)* |
| `include_null_first_air_dates` | boolean |  | *(default: `False`)* |
| `language` | string |  | *(default: `en-US`)* |
| `page` | integer |  | *(default: `1`)* |
| `screened_theatrically` | boolean |  |  |
| `sort_by` | string |  | *(default: `popularity.desc`)* |
| `timezone` | string |  |  |
| `vote_average.gte` | number |  |  |
| `vote_average.lte` | number |  |  |
| `vote_count.gte` | number |  |  |
| `vote_count.lte` | number |  |  |
| `watch_region` | string |  | use in conjunction with `with_watch_monetization_types ` or `with_watch_providers ` |
| `with_companies` | string |  | can be a comma (`AND`) or pipe (`OR`) separated query |
| `with_genres` | string |  | can be a comma (`AND`) or pipe (`OR`) separated query |
| `with_keywords` | string |  | can be a comma (`AND`) or pipe (`OR`) separated query |
| `with_networks` | integer |  |  |
| `with_origin_country` | string |  |  |
| `with_original_language` | string |  |  |
| `with_runtime.gte` | integer |  |  |
| `with_runtime.lte` | integer |  |  |
| `with_status` | string |  | possible values are: [0, 1, 2, 3, 4, 5], can be a comma (`AND`) or pipe (`OR`) separated query |
| `with_watch_monetization_types` | string |  | possible values are: [flatrate, free, ads, rent, buy] use in conjunction with `watch_region`, can be a comma (`AND`) or pipe (`OR`) separated query |
| `with_watch_providers` | string |  | use in conjunction with `watch_region`, can be a comma (`AND`) or pipe (`OR`) separated query |
| `without_companies` | string |  |  |
| `without_genres` | string |  |  |
| `without_keywords` | string |  |  |
| `without_watch_providers` | string |  |  |
| `with_type` | string |  | possible values are: [0, 1, 2, 3, 4, 5, 6], can be a comma (`AND`) or pipe (`OR`) separated query |

### Response (200)

**Example Response:**
```json
{
  "page": 1,
  "results": [
    {
      "backdrop_path": "/mAJ84W6I8I272Da87qplS2Dp9ST.jpg",
      "first_air_date": "2023-01-23",
      "genre_ids": [
        9648,
        18
      ],
      "id": 202250,
      "name": "Dirty Linen",
      "origin_country": [
        "PH"
      ],
      "original_language": "tl",
      "original_name": "Dirty Linen",
      "overview": "To exact vengeance, a young woman infiltrates the household of an influential family as a housemaid to expose their dirty secrets. However, love will get in the way of her revenge plot.",
      "popularity": 2684.061,
      "poster_path": "/ujlkQtHAVShWyWTloGU2Vh5Jbo9.jpg",
      "vote_average": 5,
      "vote_count": 13
    },
    {
      "backdrop_path": "/wJmcuxa0C4AERmA9mejxm9qRYDj.jpg",
      "first_air_date": "2022-06-06",
      "genre_ids": [
        80,
        9648
      ],
      "id": 203504,
      "name": "Aashiqana",
      "origin_country": [
        "IN"
      ],
      "original_language": "hi",
      "original_name": "\u0906\u0936\u093f\u0915\u093e\u0928\u093e",
      "overview": "A serial killer sparks the story of uptight Yashvardhan and feisty Chikki. Plagued by misunderstandings, how far do they have to go to nab the murderer?",
      "popularity": 2658.037,
      "poster_path": "/a4Z6Uohb6Ln5vcPvMUzwyn3WBjP.jpg",
      "vote_average": 6,
      "vote_count": 8
    },
    {
      "backdrop_path": "/xGKTgJlqCkq6tAK2sOTdULh7YaX.jpg",
      "first_air_date": "2022-10-10",
      "genre_ids": [
        10766,
        18,
        35
      ],
      "id": 204370,
      "name": "The Path",
      "origin_country": [
        "BR"
      ],
      "original_language": "pt",
      "original_name": "Travessia",
      "overview": "After having her life course changed by a fake image and losing her childhood sweetheart to greed and power, Brisa, a strong woman, will struggle to rebuild her journey, raise her son, rediscover true love, and discover the truth about her origin.",
      "popularity": 25
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `7414` |
| `total_results` | integer |  |  | `148265` |