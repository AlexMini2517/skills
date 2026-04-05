## Search

### Collection

```
GET /3/search/collection
```

Search for collections by their original, translated and alternative names.

### Parameters

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | string | ✓ |  |
| `include_adult` | boolean |  | *(default: `False`)* |
| `language` | string |  | *(default: `en-US`)* |
| `page` | integer |  | *(default: `1`)* |
| `region` | string |  |  |

### Response (200)

**Example Response:**
```json
{
  "page": 1,
  "results": [
    {
      "adult": false,
      "backdrop_path": "/zuW6fOiusv4X9nnW3paHGfXcSll.jpg",
      "id": 86311,
      "name": "The Avengers Collection",
      "original_language": "en",
      "original_name": "The Avengers Collection",
      "overview": "A superhero film series produced by Marvel Studios based on the Marvel Comics superhero team of the same name, and part of the Marvel Cinematic Universe (MCU).  The series features an ensemble cast from the Marvel Cinematic Universe series films, as they join forces for the peacekeeping organization S.H.I.E.L.D. led by Nick Fury.",
      "poster_path": "/yFSIUVTCvgYrpalUktulvk3Gi5Y.jpg"
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

### Company

```
GET /3/search/company
```

Search for companies by their original and alternative names.

### Parameters

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | string | ✓ |  |
| `page` | integer |  | *(default: `1`)* |

### Response (200)

**Example Response:**
```json
{
  "page": 1,
  "results": [
    {
      "id": 3268,
      "logo_path": "/tuomPhY2UtuPTqqFnKMVHvSb724.png",
      "name": "HBO",
      "origin_country": "US"
    },
    {
      "id": 142414,
      "logo_path": "/tC3oVZvqpwhAG1uSjpMnmj4nW3O.png",
      "name": "HBO Asia",
      "origin_country": "SG"
    },
    {
      "id": 143571,
      "logo_path": null,
      "name": "HBO Showcase",
      "origin_country": ""
    },
    {
      "id": 14914,
      "logo_path": "/1RZBWz53SpHUTLpRcM8BGv2plIP.png",
      "name": "HBO Documentary Films",
      "origin_country": "US"
    },
    {
      "id": 119349,
      "logo_path": null,
      "name": "HBO Central Europe",
      "origin_country": ""
    },
    {
      "id": 48582,
      "logo_path": "/tyoN6zoxMJ71GBddxVkk4dpaeze.png",
      "name": "HBO Europe",
      "origin_country": ""
    },
    {
      "id": 147188,
      "logo_path": null,
      "name": "HBO / Cinemax",
      "origin_country": ""
    },
    {
      "id": 7429,
      "logo_path": "/6in9uMqxXEHx5XgYgkeRBpZ4rPw.png",
      "name": "HBO Films",
      "origin_country": "US"
    },
    {
      "id": 158691,
      "logo_path": "/s5ELD35ShWgVKQxgERHM2iP5bXA.png",
      "name": "HBO Max",
      "origin_country": "US"
    },
    {
      "id": 21222,
      "logo_path": "/baMruKL2uRhJ1Soi4flSHVzXIH2.png",
      "name": "HBO Independent Productions",
      "origin_country": "US"
    },
    {
      "id": 27289,
      "logo_path": null,
      "name": "HBO Bulgaria",
      "origin_country": ""
    },
    {
      "id": 128608,
      "logo_path": null,
      "name": "H-Bomb Films",
      "origin_country": ""
    },
    {
      "id": 89525,
      "logo_path": null,
      "name": "HBO Family",
      "origin_country": ""
    },
    {
      "id": 37659,
      "logo_path": "/zfouUSOEq718TbB9YqN9OylPtD7.png",
      "name": "HBO Polska",
      "origin_country": "PL"
    },
    {
      "id": 136561,
      "logo_path": "/mReKmOZLemFcWlMocCwiq3XbsbB.png",
      "name": "HBO Europe",
   
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `2` |
| `total_results` | integer |  |  | `22` |

---

### Keyword

```
GET /3/search/keyword
```

Search for keywords by their name.

### Parameters

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | string | ✓ |  |
| `page` | integer |  | *(default: `1`)* |

### Response (200)

**Example Response:**
```json
{
  "page": 1,
  "results": [
    {
      "id": 262419,
      "name": "lost"
    },
    {
      "id": 5930,
      "name": "getting lost"
    },
    {
      "id": 249351,
      "name": "lost wallet"
    },
    {
      "id": 213077,
      "name": "lost youth"
    },
    {
      "id": 41309,
      "name": "lost of friend"
    },
    {
      "id": 215483,
      "name": "lost daughter"
    },
    {
      "id": 251248,
      "name": "paradise lost"
    },
    {
      "id": 215583,
      "name": "lost colony"
    },
    {
      "id": 215678,
      "name": "partially lost film"
    },
    {
      "id": 163088,
      "name": "lost tribe"
    },
    {
      "id": 222130,
      "name": "lost continent"
    },
    {
      "id": 223620,
      "name": "lost in the woods"
    },
    {
      "id": 169953,
      "name": "lost treasure"
    },
    {
      "id": 170333,
      "name": "innocence lost"
    },
    {
      "id": 225280,
      "name": "partly lost"
    },
    {
      "id": 227948,
      "name": "lost children"
    },
    {
      "id": 288632,
      "name": "lost girl"
    },
    {
      "id": 179553,
      "name": "lost pet"
    },
    {
      "id": 179578,
      "name": "lost at sea"
    },
    {
      "id": 181429,
      "name": "lost film"
    }
  ],
  "total_pages": 5,
  "total_results": 84
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `5` |
| `total_results` | integer |  |  | `84` |

---

### Movie

```
GET /3/search/movie
```

Search for movies by their original, translated and alternative titles.

### Parameters

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | string | ✓ |  |
| `include_adult` | boolean |  | *(default: `False`)* |
| `language` | string |  | *(default: `en-US`)* |
| `primary_release_year` | string |  |  |
| `page` | integer |  | *(default: `1`)* |
| `region` | string |  |  |
| `year` | string |  |  |

### Response (200)

**Example Response:**
```json
{
  "page": 1,
  "results": [
    {
      "adult": false,
      "backdrop_path": "/hZkgoQYus5vegHoetLkCJzb17zJ.jpg",
      "genre_ids": [
        18,
        53,
        35
      ],
      "id": 550,
      "original_language": "en",
      "original_title": "Fight Club",
      "overview": "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground \"fight clubs\" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.",
      "popularity": 73.433,
      "poster_path": "/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg",
      "release_date": "1999-10-15",
      "title": "Fight Club",
      "video": false,
      "vote_average": 8.433,
      "vote_count": 26279
    },
    {
      "adult": false,
      "backdrop_path": "/1VqE5z4VIOcNcajJuHLk4fDkY9G.jpg",
      "genre_ids": [
        28,
        27
      ],
      "id": 289732,
      "original_language": "zh",
      "original_title": "\u5c4d\u57ce",
      "overview": "It's the end of the century at a corner of the city in a building riddled with crime - Everyone in the building has turned into zombies. After Jenny's boyfriend is killed in a zombie attack, she faces the challenge of surviving in the face of adversity. In order to stay alive, she struggles with Andy to flee danger.",
      "popularity": 15.263,
      "poster_path": "/u8u3KVq0qfJYmNDsaTVOXy4So6f.jpg",
      "release_date": "2014-10-23",
      "title": "Zombie Fight Club",
      "video": false,
      "vote_average": 4.721,
      "vote_count": 52
    },
    {
      "adult": false,
      "backdrop_path": null,
      "genre_ids": [
        35,
        18
      ],
      "id": 323667,
      "original_language": "ru",
      "original_title": "\u0412\u0441\u0442\u0430\u0432\u0430\u0439 \u0438 \u0431\u0435\u0439\u0441\u044f",
      "overview": "Intertwined stories from the gladiator/athletes participating to the Calcio S
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `2` |
| `total_results` | integer |  |  | `39` |

---

### Multi

```
GET /3/search/multi
```

Use multi search when you want to search for movies, TV shows and people in a single request.

### Parameters

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | string | ✓ |  |
| `include_adult` | boolean |  | *(default: `False`)* |
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
      "backdrop_path": "/aDYSnJAK0BTVeE8osOy22Kz3SXY.jpg",
      "id": 11,
      "title": "Star Wars",
      "original_language": "en",
      "original_title": "Star Wars",
      "overview": "Princess Leia is captured and held hostage by the evil Imperial forces in their effort to take over the galactic Empire. Venturesome Luke Skywalker and dashing captain Han Solo team together with the loveable robot duo R2-D2 and C-3PO to rescue the beautiful princess and restore peace and justice in the Empire.",
      "poster_path": "/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg",
      "media_type": "movie",
      "genre_ids": [
        12,
        28,
        878
      ],
      "popularity": 78.047,
      "release_date": "1977-05-25",
      "video": false,
      "vote_average": 8.208,
      "vote_count": 18528
    },
    {
      "adult": false,
      "backdrop_path": "/iflKt34Ck2JpY2PY9wW1zwdJgJi.jpg",
      "id": 782054,
      "title": "Doraemon: Nobita's Little Star Wars 2021",
      "original_language": "ja",
      "original_title": "\u6620\u753b\u30c9\u30e9\u3048\u3082\u3093 \u306e\u3073\u592a\u306e\u5b87\u5b99\u5c0f\u6226\u4e89 2021",
      "overview": "One day during summer vacation, a palm-sized alien named Papi appears from a small rocket that Nobita picks up. He is the president of Pirika, a small planet in outer space, and has come to Earth to escape the rebels. Doraemon and his friends are puzzled by Papi\u2019s small size, but as they play together using the secret tool \u201cSmall Light\u201d, they gradually become friends. However, a whale-shaped space battleship comes to earth and attacks Doraemon, Nobita and the others in order to capture Papi. Feeling responsible for getting everyone involved, Papi tries to stand up to the rebels. Doraemon and his friends leave for the planet Pirika to protect their dear friend and his home.",
      "poster_path": "/48gKZioIDeUOI0afbYv3kh9u9RQ.jpg",
      "media_type": "movie",
  
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `11` |
| `total_results` | integer |  |  | `201` |

---

### Person

```
GET /3/search/person
```

Search for people by their name and also known as names.

### Parameters

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | string | ✓ |  |
| `include_adult` | boolean |  | *(default: `False`)* |
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
      "gender": 2,
      "id": 31,
      "known_for_department": "Acting",
      "name": "Tom Hanks",
      "original_name": "Tom Hanks",
      "popularity": 84.631,
      "profile_path": "/xndWFsBlClOJFRdhSt4NBwiPq2o.jpg",
      "known_for": [
        {
          "adult": false,
          "backdrop_path": "/3h1JZGDhZ8nzxdgvkxha0qBqi05.jpg",
          "id": 13,
          "title": "Forrest Gump",
          "original_language": "en",
          "original_title": "Forrest Gump",
          "overview": "A man with a low IQ has accomplished great things in his life and been present during significant historic events\u2014in each case, far exceeding what anyone imagined he could do. But despite all he has achieved, his one true love eludes him.",
          "poster_path": "/arw2vcBveWOVZr6pxd9XTd1TdQa.jpg",
          "media_type": "movie",
          "genre_ids": [
            35,
            18,
            10749
          ],
          "popularity": 67.209,
          "release_date": "1994-06-23",
          "video": false,
          "vote_average": 8.481,
          "vote_count": 24525
        },
        {
          "adult": false,
          "backdrop_path": "/3Rfvhy1Nl6sSGJwyjb0QiZzZYlB.jpg",
          "id": 862,
          "title": "Toy Story",
          "original_language": "en",
          "original_title": "Toy Story",
          "overview": "Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.",
          "poster_path": "/uXDfjJbdP4ijW5hWSBrPrlKpxab.jpg",
          "media_type": "movie",
          "genre_ids": [
            16,
            12,
            10751,
            35
          ],
          "popularity": 119.802,
          "release_date": "1995-10-30",
         
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `1` |
| `total_results` | integer |  |  | `1` |

---

### TV

```
GET /3/search/tv
```

Search for TV shows by their original, translated and also known as names.

### Parameters

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `query` | string | ✓ |  |
| `first_air_date_year` | integer |  | Search only the first air date. Valid values are: 1000..9999 |
| `include_adult` | boolean |  | *(default: `False`)* |
| `language` | string |  | *(default: `en-US`)* |
| `page` | integer |  | *(default: `1`)* |
| `year` | integer |  | Search the first air date and all episode air dates. Valid values are: 1000..9999 |

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
      "popularity": 298.884,
      "poster_path": "/ggFHVNu6YYI5L9pCfOacjizRGt.jpg",
      "first_air_date": "2008-01-20",
      "name": "Breaking Bad",
      "vote_average": 8.879,
      "vote_count": 11536
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