## Person

### Popular

```
GET /3/person/popular
```

Get a list of people ordered by popularity.

### Parameters

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
      "gender": 1,
      "id": 224513,
      "known_for": [
        {
          "adult": false,
          "backdrop_path": "/ilRyazdMJwN05exqhwK4tMKBYZs.jpg",
          "genre_ids": [
            878,
            18
          ],
          "id": 335984,
          "media_type": "movie",
          "original_language": "en",
          "original_title": "Blade Runner 2049",
          "overview": "Thirty years after the events of the first film, a new blade runner, LAPD Officer K, unearths a long-buried secret that has the potential to plunge what's left of society into chaos. K's discovery leads him on a quest to find Rick Deckard, a former LAPD blade runner who has been missing for 30 years.",
          "poster_path": "/gajva2L0rPYkEWjzgFlBXCAVBE5.jpg",
          "release_date": "2017-10-04",
          "title": "Blade Runner 2049",
          "video": false,
          "vote_average": 7.5,
          "vote_count": 11771
        },
        {
          "adult": false,
          "backdrop_path": "/4HWAQu28e2yaWrtupFPGFkdNU7V.jpg",
          "genre_ids": [
            35,
            80,
            9648
          ],
          "id": 546554,
          "media_type": "movie",
          "original_language": "en",
          "original_title": "Knives Out",
          "overview": "When renowned crime novelist Harlan Thrombey is found dead at his estate just after his 85th birthday, the inquisitive and debonair Detective Benoit Blanc is mysteriously enlisted to investigate. From Harlan's dysfunctional family to his devoted staff, Blanc sifts through a web of red herrings and self-serving lies to uncover the truth behind Harlan's untimely death.",
          "poster_path": "/pThyQovXQrw2m0s9x82twj48Jq4.jpg",
          "release_date": "2019-11-27",
          "title": "Knives Out",
          "video": false,
          "vote_average": 7.9,
          "vote_count": 10631
        },
        {
          "adult": false,
          "backdrop
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `500` |
| `total_results` | integer |  |  | `10000` |

---

### Details

```
GET /3/person/{person_id}
```

Query the top level details of a person.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `person_id` | integer | ✓ |  |

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
  "also_known_as": [
    "Thomas Jeffrey Hanks",
    "\u0422\u043e\u043c \u0425\u044d\u043d\u043a\u0441",
    "\u062a\u0648\u0645 \u0647\u0627\u0646\u0643\u0633",
    "\u30c8\u30e0\u30fb\u30cf\u30f3\u30af\u30b9",
    "\ud1b0 \ud589\ud06c\uc2a4",
    "\u0e17\u0e2d\u0e21 \u0e41\u0e2e\u0e07\u0e2a\u0e4c",
    "\u6c64\u59c6\u00b7\u6c49\u514b\u65af",
    "\u0422\u043e\u043c \u0413\u0435\u043d\u043a\u0441",
    "\u0422\u043e\u043c \u0425\u0435\u043d\u043a\u0441",
    "\u0422\u043e\u043c\u0430\u0441 \u0414\u0436\u0435\u0444\u0444\u0440\u0456 \u0413\u0435\u043d\u043a\u0441",
    "\u03a4\u03bf\u03bc \u03a7\u03b1\u03bd\u03ba\u03c2",
    "\u091f\u0949\u092e \u0939\u0948\u0902\u0915\u094d\u0938",
    "\u0d1f\u0d4b\u0d02 \u0d39\u0d3e\u0d19\u0d4d\u0d15\u0d4d\u0d38\u0d4d",
    "\u6e6f\u59c6\u2027\u6f22\u514b\u65af",
    "\u6e6f\u59c6\u00b7\u6f22\u514b"
  ],
  "biography": "Thomas Jeffrey Hanks (born July 9, 1956) is an American actor and filmmaker. Known for both his comedic and dramatic roles, Hanks is one of the most popular and recognizable film stars worldwide, and is widely regarded as an American cultural icon.\n\nHanks made his breakthrough with leading roles in the comedies Splash (1984) and Big (1988). He won two consecutive Academy Awards for Best Actor for starring as a gay lawyer suffering from AIDS in Philadelphia (1993) and a young man with below-average IQ in Forrest Gump (1994). Hanks collaborated with film director Steven Spielberg on five films: Saving Private Ryan (1998), Catch Me If You Can (2002), The Terminal (2004), Bridge of Spies (2015), and The Post (2017), as well as the 2001 miniseries Band of Brothers, which launched him as a director, producer, and screenwriter.\n\nHanks' other notable films include the romantic comedies Sleepless in Seattle (1993) and You've Got Mail (1998); the dramas Apollo 13 (1995), The Green Mile (1999), Cast Away (2000), Road to Perdition (2002), and Cloud Atlas (2012); and the biographical dramas Saving Mr. 
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `adult` | boolean |  |  | `False` |
| `also_known_as` | array[string] |  |  |  |
| `biography` | string |  |  | `Thomas Jeffrey Hanks (born July 9, 1956) is an American actor and filmmaker. Known for both his comedic and dramatic roles, Hanks is one of the most popular and recognizable film stars worldwide, and is widely regarded as an American cultural icon.

Hanks made his breakthrough with leading roles in the comedies Splash (1984) and Big (1988). He won two consecutive Academy Awards for Best Actor for starring as a gay lawyer suffering from AIDS in Philadelphia (1993) and a young man with below-average IQ in Forrest Gump (1994). Hanks collaborated with film director Steven Spielberg on five films: Saving Private Ryan (1998), Catch Me If You Can (2002), The Terminal (2004), Bridge of Spies (2015), and The Post (2017), as well as the 2001 miniseries Band of Brothers, which launched him as a director, producer, and screenwriter.

Hanks' other notable films include the romantic comedies Sleepless in Seattle (1993) and You've Got Mail (1998); the dramas Apollo 13 (1995), The Green Mile (1999), Cast Away (2000), Road to Perdition (2002), and Cloud Atlas (2012); and the biographical dramas Saving Mr. Banks (2013), Captain Phillips (2013), Sully (2016), and A Beautiful Day in the Neighborhood (2019). He has also appeared as the title character in the Robert Langdon film series, and has voiced Sheriff Woody in the Toy Story film series.

Description above from the Wikipedia article Tom Hanks, licensed under CC-BY-SA, full list of contributors on Wikipedia.` |
| `birthday` | string |  |  | `1956-07-09` |
| `deathday` |  |  |  |  |
| `gender` | integer |  |  | `2` |
| `homepage` |  |  |  |  |
| `id` | integer |  |  | `31` |
| `imdb_id` | string |  |  | `nm0000158` |
| `known_for_department` | string |  |  | `Acting` |
| `name` | string |  |  | `Tom Hanks` |
| `place_of_birth` | string |  |  | `Concord, California, USA` |
| `popularity` | number |  |  | `82.989` |
| `profile_path` | string |  |  | `/xndWFsBlClOJFRdhSt4NBwiPq2o.jpg` |

---

### Changes

```
GET /3/person/{person_id}/changes
```

Get the recent changes for a person.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `person_id` | integer | ✓ |  |

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
      "key": "biography",
      "items": [
        {
          "id": "640469b113654500ba4e859a",
          "action": "added",
          "time": "2023-03-05 10:06:41 UTC",
          "iso_639_1": "ca",
          "iso_3166_1": "ES",
          "value": "Thomas \"Tom\" Jeffrey Hanks (Concord, Calif\u00f2rnia, 9 de juliol de 1956) \u00e9s un actor de cinema i productor estatunidenc, guanyador dues vegades de l'Oscar al millor actor i considerat un dels m\u00e9s vers\u00e0tils i talentosos del cinema actual.\n\nHanks \u00e9s l'actor que m\u00e9s diners ha guanyat de tota la hist\u00f2ria del cinema amb un total de gaireb\u00e9 sis mil milions de d\u00f2lars (setembre 2006). \u00c9s tamb\u00e9 copropietari de Playtone, una companyia de producci\u00f3 de pel\u00b7l\u00edcules."
        }
      ]
    },
    {
      "key": "translations",
      "items": [
        {
          "id": "640469a7e61e6d00963c33bb",
          "action": "added",
          "time": "2023-03-05 10:06:31 UTC",
          "iso_639_1": "",
          "iso_3166_1": "",
          "value": "ca-ES"
        }
      ]
    }
  ]
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `changes` | array[object] |  |  |  |

---

### Combined Credits

```
GET /3/person/{person_id}/combined_credits
```

Get the combined movie and TV credits that belong to a person.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `person_id` | string | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |

### Response (200)

**Example Response:**
```json
{
  "cast": [
    {
      "adult": false,
      "backdrop_path": "/3h1JZGDhZ8nzxdgvkxha0qBqi05.jpg",
      "genre_ids": [
        35,
        18,
        10749
      ],
      "id": 13,
      "original_language": "en",
      "original_title": "Forrest Gump",
      "overview": "A man with a low IQ has accomplished great things in his life and been present during significant historic events\u2014in each case, far exceeding what anyone imagined he could do. But despite all he has achieved, his one true love eludes him.",
      "popularity": 62.225,
      "poster_path": "/arw2vcBveWOVZr6pxd9XTd1TdQa.jpg",
      "release_date": "1994-06-23",
      "title": "Forrest Gump",
      "video": false,
      "vote_average": 8.481,
      "vote_count": 24535,
      "character": "Forrest Gump",
      "credit_id": "52fe420ec3a36847f800074f",
      "order": 0,
      "media_type": "movie"
    },
    {
      "adult": false,
      "backdrop_path": "/vxJ08SvwomfKbpboCWynC3uqUg4.jpg",
      "genre_ids": [
        14,
        18,
        80
      ],
      "id": 497,
      "original_language": "en",
      "original_title": "The Green Mile",
      "overview": "A supernatural tale set on death row in a Southern prison, where gentle giant John Coffey possesses the mysterious power to heal people's ailments. When the cell block's head guard, Paul Edgecomb, recognizes Coffey's miraculous gift, he tries desperately to help stave off the condemned man's execution.",
      "popularity": 58.199,
      "poster_path": "/o0lO84GI7qrG6XFvtsPOSV7CTNa.jpg",
      "release_date": "1999-12-10",
      "title": "The Green Mile",
      "video": false,
      "vote_average": 8.507,
      "vote_count": 15317,
      "character": "Paul Edgecomb",
      "credit_id": "52fe424ac3a36847f8012bc7",
      "order": 0,
      "media_type": "movie"
    },
    {
      "adult": false,
      "backdrop_path": "/32zua2oKjn2EaRk7am3qK8zAlEj.jpg",
      "genre_ids": [
        36,
        18,
        12
      ],
      "id": 568,
      
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `cast` | array[object] |  |  |  |
| `crew` | array[object] |  |  |  |
| `id` | integer |  |  | `31` |

---

### External IDs

```
GET /3/person/{person_id}/external_ids
```

Get the external ID's that belong to a person.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `person_id` | integer | ✓ |  |

### Response (200)

**Example Response:**
```json
{
  "id": 31,
  "freebase_mid": "/m/0bxtg",
  "freebase_id": "/en/tom_hanks",
  "imdb_id": "nm0000158",
  "tvrage_id": 14293,
  "wikidata_id": "Q2263",
  "facebook_id": "TomHanks",
  "instagram_id": "tomhanks",
  "tiktok_id": "tomhanks",
  "twitter_id": "tomhanks",
  "youtube_id": null
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | integer |  |  | `31` |
| `freebase_mid` | string |  |  | `/m/0bxtg` |
| `freebase_id` | string |  |  | `/en/tom_hanks` |
| `imdb_id` | string |  |  | `nm0000158` |
| `tvrage_id` | integer |  |  | `14293` |
| `wikidata_id` | string |  |  | `Q2263` |
| `facebook_id` | string |  |  | `TomHanks` |
| `instagram_id` | string |  |  | `tomhanks` |
| `tiktok_id` | string |  |  | `tomhanks` |
| `twitter_id` | string |  |  | `tomhanks` |
| `youtube_id` |  |  |  |  |

---

### Images

```
GET /3/person/{person_id}/images
```

Get the profile images that belong to a person.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `person_id` | integer | ✓ |  |

### Response (200)

**Example Response:**
```json
{
  "id": 287,
  "profiles": [
    {
      "aspect_ratio": 0.666,
      "height": 980,
      "iso_639_1": null,
      "file_path": "/cckcYc2v0yh1tc9QjRelptcOBko.jpg",
      "vote_average": 5.288,
      "vote_count": 89,
      "width": 653
    },
    {
      "aspect_ratio": 0.667,
      "height": 3000,
      "iso_639_1": null,
      "file_path": "/eAOtKAc4p2C3DV8TGJQJzw8DeRv.jpg",
      "vote_average": 5.242,
      "vote_count": 40,
      "width": 2000
    },
    {
      "aspect_ratio": 0.666,
      "height": 1019,
      "iso_639_1": null,
      "file_path": "/pynwU6PGLAdDE840rC9m6jEahWg.jpg",
      "vote_average": 5.198,
      "vote_count": 7,
      "width": 679
    },
    {
      "aspect_ratio": 0.667,
      "height": 1377,
      "iso_639_1": null,
      "file_path": "/tJiSUYst4ddIaz1zge2LqCtu9tw.jpg",
      "vote_average": 5.16,
      "vote_count": 42,
      "width": 918
    },
    {
      "aspect_ratio": 0.667,
      "height": 2100,
      "iso_639_1": null,
      "file_path": "/1k9MVNS9M3Y4KejBHusNdbGJwRw.jpg",
      "vote_average": 5.144,
      "vote_count": 23,
      "width": 1400
    },
    {
      "aspect_ratio": 0.667,
      "height": 721,
      "iso_639_1": null,
      "file_path": "/ajNaPmXVVMJFg9GWmu6MJzTaXdV.jpg",
      "vote_average": 5.138,
      "vote_count": 75,
      "width": 481
    },
    {
      "aspect_ratio": 0.667,
      "height": 631,
      "iso_639_1": null,
      "file_path": "/w1L55dXNi9UAmw2CURQjQI0DTf2.jpg",
      "vote_average": 5.134,
      "vote_count": 47,
      "width": 421
    },
    {
      "aspect_ratio": 0.666,
      "height": 1572,
      "iso_639_1": null,
      "file_path": "/kU3B75TyRiCgE270EyZnHjfivoq.jpg",
      "vote_average": 5.128,
      "vote_count": 71,
      "width": 1047
    },
    {
      "aspect_ratio": 0.666,
      "height": 2000,
      "iso_639_1": null,
      "file_path": "/uGlfGvB9DzmDaDYErPOZ9071sqt.jpg",
      "vote_average": 5.12,
      "vote_count": 30,
      "width": 1333
    },
    {
      "aspect_ratio":
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | integer |  |  | `287` |
| `profiles` | array[object] |  |  |  |

---

### Latest

```
GET /3/person/latest
```

Get the newest created person. This is a live response and will continuously change.

### Response (200)

**Example Response:**
```json
{
  "adult": false,
  "also_known_as": [],
  "biography": "",
  "birthday": null,
  "deathday": null,
  "gender": 0,
  "homepage": null,
  "id": 4064343,
  "imdb_id": null,
  "known_for_department": null,
  "name": "\u00c1ngel Cruz",
  "place_of_birth": null,
  "popularity": 0.0,
  "profile_path": null
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `adult` | boolean |  |  | `False` |
| `also_known_as` | array |  |  |  |
| `biography` | string |  |  |  |
| `birthday` |  |  |  |  |
| `deathday` |  |  |  |  |
| `gender` | integer |  |  | `0` |
| `homepage` |  |  |  |  |
| `id` | integer |  |  | `4064343` |
| `imdb_id` |  |  |  |  |
| `known_for_department` |  |  |  |  |
| `name` | string |  |  | `Ángel Cruz` |
| `place_of_birth` |  |  |  |  |
| `popularity` | integer |  |  | `0` |
| `profile_path` |  |  |  |  |

---

### Movie Credits

```
GET /3/person/{person_id}/movie_credits
```

Get the movie credits for a person.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `person_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |

### Response (200)

**Example Response:**
```json
{
  "cast": [
    {
      "adult": false,
      "backdrop_path": "/3h1JZGDhZ8nzxdgvkxha0qBqi05.jpg",
      "genre_ids": [
        35,
        18,
        10749
      ],
      "id": 13,
      "original_language": "en",
      "original_title": "Forrest Gump",
      "overview": "A man with a low IQ has accomplished great things in his life and been present during significant historic events\u2014in each case, far exceeding what anyone imagined he could do. But despite all he has achieved, his one true love eludes him.",
      "popularity": 62.225,
      "poster_path": "/arw2vcBveWOVZr6pxd9XTd1TdQa.jpg",
      "release_date": "1994-06-23",
      "title": "Forrest Gump",
      "video": false,
      "vote_average": 8.481,
      "vote_count": 24535,
      "character": "Forrest Gump",
      "credit_id": "52fe420ec3a36847f800074f",
      "order": 0
    },
    {
      "adult": false,
      "backdrop_path": "/vxJ08SvwomfKbpboCWynC3uqUg4.jpg",
      "genre_ids": [
        14,
        18,
        80
      ],
      "id": 497,
      "original_language": "en",
      "original_title": "The Green Mile",
      "overview": "A supernatural tale set on death row in a Southern prison, where gentle giant John Coffey possesses the mysterious power to heal people's ailments. When the cell block's head guard, Paul Edgecomb, recognizes Coffey's miraculous gift, he tries desperately to help stave off the condemned man's execution.",
      "popularity": 58.199,
      "poster_path": "/o0lO84GI7qrG6XFvtsPOSV7CTNa.jpg",
      "release_date": "1999-12-10",
      "title": "The Green Mile",
      "video": false,
      "vote_average": 8.507,
      "vote_count": 15317,
      "character": "Paul Edgecomb",
      "credit_id": "52fe424ac3a36847f8012bc7",
      "order": 0
    },
    {
      "adult": false,
      "backdrop_path": "/32zua2oKjn2EaRk7am3qK8zAlEj.jpg",
      "genre_ids": [
        36,
        18,
        12
      ],
      "id": 568,
      "original_language": "en",
      "original_title": "Apollo
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `cast` | array[object] |  |  |  |
| `crew` | array[object] |  |  |  |
| `id` | integer |  |  | `31` |

---

### TV Credits

```
GET /3/person/{person_id}/tv_credits
```

Get the TV credits that belong to a person.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `person_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |

### Response (200)

**Example Response:**
```json
{
  "cast": [
    {
      "adult": false,
      "backdrop_path": "/ttvojTMgaIN7U8gqB5LlNqO4vPN.jpg",
      "genre_ids": [
        10767
      ],
      "id": 1900,
      "origin_country": [
        "US"
      ],
      "original_language": "en",
      "original_name": "LIVE with Kelly and Mark",
      "overview": "A morning talk show with A-list celebrity guests, top-notch performances and one-of-a-kind segments that are unrivaled on daytime television, plus spontaneous, hilarious and unpredictable talk.",
      "popularity": 700.508,
      "poster_path": "/l5y8egG27p2fSTyq8s21SQMmQLy.jpg",
      "first_air_date": "1988-09-05",
      "name": "LIVE with Kelly and Mark",
      "vote_average": 5.4,
      "vote_count": 25,
      "character": "",
      "credit_id": "52571af019c29571140d5c92",
      "episode_count": 1
    },
    {
      "adult": false,
      "backdrop_path": "/jphrbgfi2Plwp7wyQL0AMHzKrF0.jpg",
      "genre_ids": [
        35
      ],
      "id": 2103,
      "origin_country": [
        "US"
      ],
      "original_language": "en",
      "original_name": "Life with Bonnie",
      "overview": "The host of the local morning talk show Morning Chicago creatively balances family commitment\u2014to her husband John, a hard-working family practice doctor, and their three young children\u2014 and career obligations.",
      "popularity": 3.232,
      "poster_path": "/4VG2dtEL6X3v1Ad3pyzsm8Er0hN.jpg",
      "first_air_date": "2002-09-17",
      "name": "Life with Bonnie",
      "vote_average": 7.0,
      "vote_count": 2,
      "character": "",
      "credit_id": "5257226f760ee3776a222981",
      "episode_count": 1
    },
    {
      "adult": false,
      "backdrop_path": "/7I5VX5Vr1jrUvikA7mTje97dT2e.jpg",
      "genre_ids": [
        10767
      ],
      "id": 2221,
      "origin_country": [
        "US"
      ],
      "original_language": "en",
      "original_name": "The View",
      "overview": "ABC Daytime's morning chatfest, currently featuring Whoopi Goldberg,
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `cast` | array[object] |  |  |  |
| `crew` | array[object] |  |  |  |
| `id` | integer |  |  | `31` |

---

### Tagged Images

```
GET /3/person/{person_id}/tagged_images
```

Get the tagged images for a person.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `person_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `page` | integer |  | *(default: `1`)* |

### Response (200)

**Example Response:**
```json
{
  "id": 31,
  "page": 1,
  "results": [
    {
      "aspect_ratio": 0.6666666666666666,
      "file_path": "/1wY4psJ5NVEhCuOYROwLH2XExM2.jpg",
      "height": 1500,
      "id": "5b235d740e0a265b5d0031d9",
      "iso_639_1": "en",
      "vote_average": 5.456,
      "vote_count": 7,
      "width": 1000,
      "image_type": "poster",
      "media": {
        "adult": false,
        "backdrop_path": "/bdD39MpSVhKjxarTxLSfX6baoMP.jpg",
        "id": 857,
        "title": "Saving Private Ryan",
        "original_language": "en",
        "original_title": "Saving Private Ryan",
        "overview": "As U.S. troops storm the beaches of Normandy, three brothers lie dead on the battlefield, with a fourth trapped behind enemy lines. Ranger captain John Miller and seven men are tasked with penetrating German-held territory and bringing the boy home.",
        "poster_path": "/uqx37cS8cpHg8U35f9U5IBlrCV3.jpg",
        "media_type": "movie",
        "genre_ids": [
          18,
          36,
          10752
        ],
        "popularity": 70.45,
        "release_date": "1998-07-24",
        "video": false,
        "vote_average": 8.208,
        "vote_count": 14134
      },
      "media_type": "movie"
    },
    {
      "aspect_ratio": 0.6666666666666666,
      "file_path": "/23IsAAvjeiScLmK7WIlJTxJKlQO.jpg",
      "height": 2100,
      "id": "5e3a2b14ac8e6b0011c93b21",
      "iso_639_1": "en",
      "vote_average": 5.394,
      "vote_count": 10,
      "width": 1400,
      "image_type": "poster",
      "media": {
        "adult": false,
        "backdrop_path": "/cSJMk9Jar8SibFXL8JAF9p2fhKu.jpg",
        "id": 501907,
        "title": "A Beautiful Day in the Neighborhood",
        "original_language": "en",
        "original_title": "A Beautiful Day in the Neighborhood",
        "overview": "An award-winning cynical journalist, Lloyd Vogel, begrudgingly accepts an assignment to write an Esquire profile piece on the beloved television icon Fred Rogers. After his encounter with Ro
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | integer |  |  | `31` |
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `1` |
| `total_results` | integer |  |  | `13` |