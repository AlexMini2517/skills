## Account

### Details

```
GET /3/account/{account_id}
```

Get the public details of an account on TMDB.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `account_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `session_id` | string |  |  |

### Response (200)

**Example Response:**
```json
{
  "avatar": {
    "gravatar": {
      "hash": "c9e9fc152ee756a900db85757c29815d"
    },
    "tmdb": {
      "avatar_path": "/xy44UvpbTgzs9kWmp4C3fEaCl5h.png"
    }
  },
  "id": 548,
  "iso_639_1": "en",
  "iso_3166_1": "CA",
  "name": "Travis Bell",
  "include_adult": false,
  "username": "travisbell"
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `avatar` | object |  |  |  |
| `gravatar` | object |  |  |  |
| `hash` | string |  |  | `c9e9fc152ee756a900db85757c29815d` |
| `tmdb` | object |  |  |  |
| `avatar_path` | string |  |  | `/xy44UvpbTgzs9kWmp4C3fEaCl5h.png` |
| `id` | integer |  |  | `548` |
| `iso_639_1` | string |  |  | `en` |
| `iso_3166_1` | string |  |  | `CA` |
| `name` | string |  |  | `Travis Bell` |
| `include_adult` | boolean |  |  | `False` |
| `username` | string |  |  | `travisbell` |

---

### Add Favorite

```
POST /3/account/{account_id}/favorite
```

Mark a movie or TV show as a favourite.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `account_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
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

### Add To Watchlist

```
POST /3/account/{account_id}/watchlist
```

Add a movie or TV show to your watchlist.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `account_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
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

### Favorite Movies

```
GET /3/account/{account_id}/favorite/movies
```

Get a users list of favourite movies.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `account_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |
| `page` | integer |  | *(default: `1`)* |
| `session_id` | string |  |  |
| `sort_by` | string |  | *(default: `created_at.asc`)* |

### Response (200)

**Example Response:**
```json
{
  "page": 1,
  "results": [
    {
      "adult": false,
      "backdrop_path": "/se5Hxz7PArQZOG3Nx2bpfOhLhtV.jpg",
      "genre_ids": [
        28,
        12,
        16,
        10751
      ],
      "id": 9806,
      "original_language": "en",
      "original_title": "The Incredibles",
      "overview": "Bob Parr has given up his superhero days to log in time as an insurance adjuster and raise his three children with his formerly heroic wife in suburbia. But when he receives a mysterious assignment, it's time to get back into costume.",
      "popularity": 71.477,
      "poster_path": "/2LqaLgk4Z226KkgPJuiOQ58wvrm.jpg",
      "release_date": "2004-10-27",
      "title": "The Incredibles",
      "video": false,
      "vote_average": 7.702,
      "vote_count": 16162
    },
    {
      "adult": false,
      "backdrop_path": "/8eRscFbRYl681zDfkjv1jjW1KAA.jpg",
      "genre_ids": [
        878,
        28,
        12
      ],
      "id": 1452,
      "original_language": "en",
      "original_title": "Superman Returns",
      "overview": "Superman returns to discover his 5-year absence has allowed Lex Luthor to walk free, and that those he was closest to felt abandoned and have moved on. Luthor plots his ultimate revenge that could see millions killed and change the face of the planet forever, as well as ridding himself of the Man of Steel.",
      "popularity": 23.183,
      "poster_path": "/385XwTQZDpRX2d3kxtnpiLrjBXw.jpg",
      "release_date": "2006-06-28",
      "title": "Superman Returns",
      "video": false,
      "vote_average": 5.723,
      "vote_count": 3716
    },
    {
      "adult": false,
      "backdrop_path": "/xh0ZRdnL4pSqfW73HBf97xiNEFP.jpg",
      "genre_ids": [
        14,
        28
      ],
      "id": 8960,
      "original_language": "en",
      "original_title": "Hancock",
      "overview": "Hancock is a down-and-out superhero who's forced to employ a PR expert to help repair his image when the public grows weary of all the damage he's inflic
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `4` |
| `total_results` | integer |  |  | `80` |

---

### Favorite TV

```
GET /3/account/{account_id}/favorite/tv
```

Get a users list of favourite TV shows.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `account_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |
| `page` | integer |  | *(default: `1`)* |
| `session_id` | string |  |  |
| `sort_by` | string |  | *(default: `created_at.asc`)* |

### Response (200)

**Example Response:**
```json
{
  "page": 1,
  "results": [
    {
      "adult": false,
      "backdrop_path": "/bsNm9z2TJfe0WO3RedPGWQ8mG1X.jpg",
      "genre_ids": [
        18,
        80
      ],
      "id": 1396,
      "origin_country": [
        "US"
      ],
      "original_language": "en",
      "original_name": "Breaking Bad",
      "overview": "When Walter White, a New Mexico chemistry teacher, is diagnosed with Stage III cancer and given a prognosis of only two years left to live. He becomes filled with a sense of fearlessness and an unrelenting desire to secure his family's financial future at any cost as he enters the dangerous world of drugs and crime.",
      "popularity": 292.904,
      "poster_path": "/ggFHVNu6YYI5L9pCfOacjizRGt.jpg",
      "first_air_date": "2008-01-20",
      "name": "Breaking Bad",
      "vote_average": 8.878,
      "vote_count": 11548
    },
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
      "popularity": 316.756,
      "poster_path": "/7WUHnWGx5OO145IRxPDUkQSh4C7.jpg",
      "first_air_date": "2011-04-17",
      "name": "Game of Thrones",
      "vote_average": 8.436,
      "vote_count": 21000
    },
    {
      "adult": false,
      "backdrop_path": "/zP5SftyPx2VCdly369kTVVNIcT3.jpg",
      "genre_ids": [
        10759,
        35,
        18
      ],
      "id": 1404,
      "origin_country": [
        "US"
      ],
      "original_language": "en",
      "original_
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `4` |
| `total_results` | integer |  |  | `68` |

---

### Lists

```
GET /3/account/{account_id}/lists
```

Get a users list of custom lists.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `account_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `page` | integer |  | *(default: `1`)* |
| `session_id` | string |  |  |

### Response (200)

**Example Response:**
```json
{
  "page": 1,
  "results": [
    {
      "description": "",
      "favorite_count": 0,
      "id": 120174,
      "item_count": 5,
      "iso_639_1": "en",
      "list_type": "movie",
      "name": "Test Alpha Sort",
      "poster_path": null
    },
    {
      "description": "",
      "favorite_count": 0,
      "id": 8221116,
      "item_count": 4,
      "iso_639_1": "en",
      "list_type": "movie",
      "name": "Test List",
      "poster_path": null
    },
    {
      "description": "Here's a list of the films that take place in the DC Comics universe.",
      "favorite_count": 0,
      "id": 3,
      "item_count": 30,
      "iso_639_1": "en",
      "list_type": "movie",
      "name": "The DC Comics Universe",
      "poster_path": "/4H1jWsgEQOgTs4KeG5j5BorKMfX.jpg"
    },
    {
      "description": "This is a test.",
      "favorite_count": 0,
      "id": 8212330,
      "item_count": 2,
      "iso_639_1": "en",
      "list_type": "movie",
      "name": "Test List #1",
      "poster_path": null
    },
    {
      "description": "Just a UTF test list. \ud83c\udf69 \ud83d\udc1d",
      "favorite_count": 0,
      "id": 7066467,
      "item_count": 3,
      "iso_639_1": "en",
      "list_type": "movie",
      "name": "\ud83d\udea8 My Cool List!",
      "poster_path": null
    },
    {
      "description": "The idea behind this list is to collect the live action comic book movies from within the Marvel franchise.",
      "favorite_count": 0,
      "id": 1,
      "item_count": 59,
      "iso_639_1": "en",
      "list_type": "movie",
      "name": "The Marvel Universe",
      "poster_path": "/coJVIUEOToAEGViuhclM7pXC75R.jpg"
    },
    {
      "description": "Test description.",
      "favorite_count": 0,
      "id": 136203,
      "item_count": 2,
      "iso_639_1": "en",
      "list_type": "movie",
      "name": "Test From Trav's Scripts",
      "poster_path": null
    },
    {
      "description": "",
      "favorite_count": 0,
      "id": 142798,
      "item_count": 
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `2` |
| `total_results` | integer |  |  | `25` |

---

### Rated Movies

```
GET /3/account/{account_id}/rated/movies
```

Get a users list of rated movies.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `account_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |
| `page` | integer |  | *(default: `1`)* |
| `session_id` | string |  |  |
| `sort_by` | string |  | *(default: `created_at.asc`)* |

### Response (200)

**Example Response:**
```json
{
  "page": 1,
  "results": [
    {
      "adult": false,
      "backdrop_path": "/dUVbWINfRMGojGZRcO6GF1Z2nV8.jpg",
      "genre_ids": [
        12,
        14,
        28
      ],
      "id": 120,
      "original_language": "en",
      "original_title": "The Lord of the Rings: The Fellowship of the Ring",
      "overview": "Young hobbit Frodo Baggins, after inheriting a mysterious ring from his uncle Bilbo, must leave his home in order to keep it from falling into the hands of its evil creator. Along the way, a fellowship is formed to protect the ringbearer and make sure that the ring arrives at its final destination: Mt. Doom, the only place where it can be destroyed.",
      "popularity": 84.737,
      "poster_path": "/6oom5QYQ2yQTMJIbnvbkBL9cHo6.jpg",
      "release_date": "2001-12-18",
      "title": "The Lord of the Rings: The Fellowship of the Ring",
      "video": false,
      "vote_average": 8.396,
      "vote_count": 22579,
      "rating": 8.0
    },
    {
      "adult": false,
      "backdrop_path": "/YL3GPOiDcNraIJOVDCZsoOBoDy.jpg",
      "genre_ids": [
        878,
        28,
        12,
        53
      ],
      "id": 106,
      "original_language": "en",
      "original_title": "Predator",
      "overview": "A team of elite commandos on a secret mission in a Central American jungle come to find themselves hunted by an extraterrestrial warrior.",
      "popularity": 62.969,
      "poster_path": "/k3mW4qfJo6SKqe6laRyNGnbB9n5.jpg",
      "release_date": "1987-06-12",
      "title": "Predator",
      "video": false,
      "vote_average": 7.491,
      "vote_count": 6943,
      "rating": 6.0
    },
    {
      "adult": false,
      "backdrop_path": "/dqK9Hag1054tghRQSqLSfrkvQnA.jpg",
      "genre_ids": [
        18,
        28,
        80,
        53
      ],
      "id": 155,
      "original_language": "en",
      "original_title": "The Dark Knight",
      "overview": "Batman raises the stakes in his war on crime. With the help of Lt. Jim Gordon and Distr
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `47` |
| `total_results` | integer |  |  | `940` |

---

### Rated TV

```
GET /3/account/{account_id}/rated/tv
```

Get a users list of rated TV shows.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `account_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |
| `page` | integer |  | *(default: `1`)* |
| `session_id` | string |  |  |
| `sort_by` | string |  | *(default: `created_at.asc`)* |

### Response (200)

**Example Response:**
```json
{
  "page": 1,
  "results": [
    {
      "adult": false,
      "backdrop_path": "/2yZXtM2Kky1Sy0kachbDlwybl3y.jpg",
      "genre_ids": [
        10765,
        18,
        9648
      ],
      "id": 1705,
      "origin_country": [
        "US"
      ],
      "original_language": "en",
      "original_name": "Fringe",
      "overview": "FBI Special Agent Olivia Dunham, brilliant but formerly institutionalized scientist Walter Bishop and his scheming, reluctant son Peter uncover a deadly mystery involving a series of unbelievable events and realize they may be a part of a larger, more disturbing pattern that blurs the line between science fiction and technology.",
      "popularity": 151.906,
      "poster_path": "/sY9hg5dLJ93RJOyKEiu1nAtBRND.jpg",
      "first_air_date": "2008-09-09",
      "name": "Fringe",
      "vote_average": 8.109,
      "vote_count": 2050,
      "rating": 9.0
    },
    {
      "adult": false,
      "backdrop_path": "/dGzPJnh8YcUS4J10sNunohaXMVn.jpg",
      "genre_ids": [
        37,
        80,
        18
      ],
      "id": 1406,
      "origin_country": [
        "US"
      ],
      "original_language": "en",
      "original_name": "Deadwood",
      "overview": "The story of the early days of Deadwood, South Dakota; woven around actual historic events with most of the main characters based on real people. Deadwood starts as a gold mining camp and gradually turns from a lawless wild-west community into an organized wild-west civilized town. The story focuses on the real-life characters Seth Bullock and Al Swearengen.",
      "popularity": 42.61,
      "poster_path": "/4Yp35DVbVOAWkfQUIQ7pbh3u0aN.jpg",
      "first_air_date": "2004-03-21",
      "name": "Deadwood",
      "vote_average": 8.095,
      "vote_count": 670,
      "rating": 8.0
    },
    {
      "adult": false,
      "backdrop_path": "/cyieN1P9Xo5SvLasSUT7SaAAzfy.jpg",
      "genre_ids": [
        80,
        18
      ],
      "id": 1436,
      "origin_country": [
        "US"
     
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `15` |
| `total_results` | integer |  |  | `290` |

---

### Rated TV Episodes

```
GET /3/account/{account_id}/rated/tv/episodes
```

Get a users list of rated TV episodes.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `account_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |
| `page` | integer |  | *(default: `1`)* |
| `session_id` | string |  |  |
| `sort_by` | string |  | *(default: `created_at.asc`)* |

### Response (200)

**Example Response:**
```json
{
  "page": 1,
  "results": [
    {
      "air_date": "2013-10-17",
      "episode_number": 5,
      "id": 64782,
      "name": "The Workplace Proximity",
      "overview": "Amy starts working at Caltech which causes friction with Sheldon. Howard agrees with Sheldon who mentions this to Bernadette causing a big fight for the Wolowitzes.",
      "production_code": "4X5305",
      "runtime": 22,
      "season_number": 7,
      "show_id": 1418,
      "still_path": "/k8atjbd5gAsntuhbPnFpvnvo0qn.jpg",
      "vote_average": 7.242,
      "vote_count": 31,
      "rating": 8.0
    },
    {
      "air_date": "2013-12-08",
      "episode_number": 11,
      "id": 968782,
      "name": "Big Man in Tehran",
      "overview": "Brody's loyalty to the mission wavers when he meets a ghost from his past. As Lockhart's confirmation looms, Saul stares into the precipice between success and failure.",
      "production_code": "3WAH11",
      "runtime": 55,
      "season_number": 3,
      "show_id": 1407,
      "still_path": "/2JYvwe7HoEkn3BQhhHCyPzhqhh5.jpg",
      "vote_average": 8.0,
      "vote_count": 23,
      "rating": 9.0
    },
    {
      "air_date": "2014-03-23",
      "episode_number": 15,
      "id": 973273,
      "name": "Dramatics, Your Honor",
      "overview": "Alicia asks Cary to be her lawyer when Nelson Dubeck (Eric Bogosian) asks her to participate in a deposition; Will faces off with a new prosecutor while defending Jeffrey Grant (Hunter Parrish).",
      "production_code": "",
      "runtime": 43,
      "season_number": 5,
      "show_id": 1435,
      "still_path": "/eGQg94nfM6EhKrxGA8A92SXe3WT.jpg",
      "vote_average": 8.2,
      "vote_count": 11,
      "rating": 9.0
    },
    {
      "air_date": "2014-05-11",
      "episode_number": 6,
      "id": 63099,
      "name": "The Laws of Gods and Men",
      "overview": "Stannis makes a deal with the Iron Bank of Braavos. Yara and her troops storm the Dreadfort to free Theon. Meanwhile, Daenerys meets Hizdar zo Loraq 
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `10` |
| `total_results` | integer |  |  | `186` |

---

### Watchlist Movies

```
GET /3/account/{account_id}/watchlist/movies
```

Get a list of movies added to a users watchlist.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `account_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |
| `page` | integer |  | *(default: `1`)* |
| `session_id` | string |  |  |
| `sort_by` | string |  | *(default: `created_at.asc`)* |

### Response (200)

**Example Response:**
```json
{
  "page": 1,
  "results": [
    {
      "adult": false,
      "backdrop_path": "/rgNzvSagnlc32TuMEBa529QFIig.jpg",
      "genre_ids": [
        878,
        18,
        53
      ],
      "id": 76726,
      "original_language": "en",
      "original_title": "Chronicle",
      "overview": "Three high school students make an incredible discovery, leading to their developing uncanny powers beyond their understanding. As they learn to control their abilities and use them to their advantage, their lives start to spin out of control, and their darker sides begin to take over.",
      "popularity": 37.148,
      "poster_path": "/xENglsVIIWEEhhB5lgpy33tGcKI.jpg",
      "release_date": "2012-02-01",
      "title": "Chronicle",
      "video": false,
      "vote_average": 6.822,
      "vote_count": 4741
    },
    {
      "adult": false,
      "backdrop_path": "/q5zTYYhgRtUgB9MORq6TohCzxV3.jpg",
      "genre_ids": [
        28,
        18,
        53
      ],
      "id": 70435,
      "original_language": "en",
      "original_title": "Haywire",
      "overview": "A black ops soldier seeks payback after she is betrayed and left for dead.",
      "popularity": 18.699,
      "poster_path": "/iI3KOQOyTMJgxccs50zjxn3R7DF.jpg",
      "release_date": "2011-11-01",
      "title": "Haywire",
      "video": false,
      "vote_average": 5.676,
      "vote_count": 1190
    },
    {
      "adult": false,
      "backdrop_path": "/v63E5H5TD7Eay1gZPVt9ibP9riy.jpg",
      "genre_ids": [
        14,
        28,
        27
      ],
      "id": 52520,
      "original_language": "en",
      "original_title": "Underworld: Awakening",
      "overview": "Having escaped years of imprisonment, vampire warrioress Selene finds herself in a changed world where humans have discovered the existence of both Vampire and Lycan clans and are conducting an all-out war to eradicate both immortal species. Now Selene must battle the humans and a frightening new breed of super Lycans to ensure the death dealers' su
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `34` |
| `total_results` | integer |  |  | `677` |

---

### Watchlist TV

```
GET /3/account/{account_id}/watchlist/tv
```

Get a list of TV shows added to a users watchlist.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `account_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |
| `page` | integer |  | *(default: `1`)* |
| `session_id` | string |  |  |
| `sort_by` | string |  | *(default: `created_at.asc`)* |

### Response (200)

**Example Response:**
```json
{
  "page": 1,
  "results": [
    {
      "adult": false,
      "backdrop_path": "/7phlGHRupo38EnuwmkAHdNUqov3.jpg",
      "genre_ids": [
        35
      ],
      "id": 58932,
      "origin_country": [
        "US"
      ],
      "original_language": "en",
      "original_name": "The Crazy Ones",
      "overview": "The Crazy Ones is an American situation comedy series created by David E. Kelley that stars Robin Williams and Sarah Michelle Gellar. The single-camera project premiered on CBS on September 26, 2013, as part of the 2013\u201314 American television season as a Thursday night 9 pm entry. Bill D'Elia, Dean Lorey, Jason Winer, John Montgomery and Mark Teitelbaum serve as executive producers for 20th Century Fox Television.",
      "popularity": 8.939,
      "poster_path": "/s2e7hTrdmNUaJDf0yDP5b4AHvrD.jpg",
      "first_air_date": "2013-09-26",
      "name": "The Crazy Ones",
      "vote_average": 6.176,
      "vote_count": 94
    },
    {
      "adult": false,
      "backdrop_path": "/hmLTIRtVyTHShJl2Wb8LHmvUgJm.jpg",
      "genre_ids": [
        80,
        18,
        9648
      ],
      "id": 19885,
      "origin_country": [
        "GB"
      ],
      "original_language": "en",
      "original_name": "Sherlock",
      "overview": "A modern update finds the famous sleuth and his doctor partner solving crime in 21st century London.",
      "popularity": 82.572,
      "poster_path": "/7WTsnHkbA0FaG6R9twfFde0I9hl.jpg",
      "first_air_date": "2010-07-25",
      "name": "Sherlock",
      "vote_average": 8.534,
      "vote_count": 4425
    },
    {
      "adult": false,
      "backdrop_path": "/dDPwCyZG8arYwMDoQl0sm4xccCE.jpg",
      "genre_ids": [
        18,
        80,
        9648
      ],
      "id": 46952,
      "origin_country": [
        "US"
      ],
      "original_language": "en",
      "original_name": "The Blacklist",
      "overview": "Raymond \"Red\" Reddington, one of the FBI's most wanted fugitives, surrenders in person at FBI Headquarters i
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `17` |
| `total_results` | integer |  |  | `325` |