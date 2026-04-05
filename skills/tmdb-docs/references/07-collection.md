## Collection

### Details

```
GET /3/collection/{collection_id}
```

Get collection details by ID.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `collection_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |

### Response (200)

**Example Response:**
```json
{
  "id": 10,
  "name": "Star Wars Collection",
  "original_language": "en",
  "original_name": "Star Wars Collection",
  "overview": "An epic space-opera theatrical film series, which depicts the adventures of various characters \"a long time ago in a galaxy far, far away\u2026.\"",
  "poster_path": "/22dj38IckjzEEUZwN1tPU5VJ1qq.jpg",
  "backdrop_path": "/4z9ijhgEthfRHShoOvMaBlpciXS.jpg",
  "parts": [
    {
      "adult": false,
      "backdrop_path": "/2w4xG178RpB4MDAIfTkqAuSJzec.jpg",
      "id": 11,
      "name": "Star Wars",
      "original_name": "Star Wars",
      "overview": "Princess Leia is captured and held hostage by the evil Imperial forces in their effort to take over the galactic Empire. Venturesome Luke Skywalker and dashing captain Han Solo team together with the loveable robot duo R2-D2 and C-3PO to rescue the beautiful princess and restore peace and justice in the Empire.",
      "poster_path": "/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg",
      "media_type": "movie",
      "original_language": "en",
      "genre_ids": [
        12,
        28,
        878
      ],
      "popularity": 15.8557,
      "release_date": "1977-05-25",
      "video": false,
      "vote_average": 8.205,
      "vote_count": 21522
    },
    {
      "adult": false,
      "backdrop_path": "/dMZxEdrWIzUmUoOz2zvmFuutbj7.jpg",
      "id": 1891,
      "name": "The Empire Strikes Back",
      "original_name": "The Empire Strikes Back",
      "overview": "The epic saga continues as Luke Skywalker, in hopes of defeating the evil Galactic Empire, learns the ways of the Jedi from aging master Yoda. But Darth Vader is more determined than ever to capture Luke. Meanwhile, rebel leader Princess Leia, cocky Han Solo, Chewbacca, and droids C-3PO and R2-D2 are thrown into various stages of capture, betrayal and despair.",
      "poster_path": "/nNAeTmF4CtdSgMDplXTDPOpYzsX.jpg",
      "media_type": "movie",
      "original_language": "en",
      "genre_ids": [
        12,
        28,
        878
    
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | integer |  |  | `10` |
| `name` | string |  |  | `Star Wars Collection` |
| `original_language` | string |  |  | `en` |
| `original_name` | string |  |  | `Star Wars Collection` |
| `overview` | string |  |  | `An epic space-opera theatrical film series, which depicts the adventures of various characters "a long time ago in a galaxy far, far away…."` |
| `poster_path` | string |  |  | `/22dj38IckjzEEUZwN1tPU5VJ1qq.jpg` |
| `backdrop_path` | string |  |  | `/4z9ijhgEthfRHShoOvMaBlpciXS.jpg` |
| `parts` | array[object] |  |  |  |

---

### Images

```
GET /3/collection/{collection_id}/images
```

Get the images that belong to a collection.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `collection_id` | integer | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `include_image_language` | string |  | specify a comma separated list of ISO-639-1 values to query, for example: `en-US,null` |
| `language` | string |  |  |

### Response (200)

**Example Response:**
```json
{
  "id": 10,
  "backdrops": [
    {
      "aspect_ratio": 1.778,
      "height": 1080,
      "iso_639_1": null,
      "file_path": "/d8duYyyC9J5T825Hg7grmaabfxQ.jpg",
      "vote_average": 5.464,
      "vote_count": 30,
      "width": 1920
    },
    {
      "aspect_ratio": 1.778,
      "height": 720,
      "iso_639_1": null,
      "file_path": "/zZDkgOmFMVYpGAkR9Tkxw0CRnxX.jpg",
      "vote_average": 5.454,
      "vote_count": 3,
      "width": 1280
    },
    {
      "aspect_ratio": 1.778,
      "height": 1080,
      "iso_639_1": "en",
      "file_path": "/trf3Hi3tPOJARsCBoVMDBlpjPC4.jpg",
      "vote_average": 5.376,
      "vote_count": 6,
      "width": 1920
    },
    {
      "aspect_ratio": 1.778,
      "height": 1080,
      "iso_639_1": null,
      "file_path": "/sGxcMvC6mfCzEir0c1tldsPhZEF.jpg",
      "vote_average": 5.356,
      "vote_count": 22,
      "width": 1920
    },
    {
      "aspect_ratio": 1.778,
      "height": 1080,
      "iso_639_1": "en",
      "file_path": "/h3JDR9iruHqwGC4Dm8UbYkY9paK.jpg",
      "vote_average": 5.326,
      "vote_count": 7,
      "width": 1920
    },
    {
      "aspect_ratio": 1.778,
      "height": 2160,
      "iso_639_1": null,
      "file_path": "/eO3PyZbDe7UlkyypMgfHWdeo9VZ.jpg",
      "vote_average": 5.322,
      "vote_count": 5,
      "width": 3840
    },
    {
      "aspect_ratio": 1.778,
      "height": 1080,
      "iso_639_1": "en",
      "file_path": "/benqmUIQGqU7iMYrDl8aUxhXWC.jpg",
      "vote_average": 5.318,
      "vote_count": 3,
      "width": 1920
    },
    {
      "aspect_ratio": 1.778,
      "height": 2160,
      "iso_639_1": null,
      "file_path": "/5PqKzRkcPZOsKy1sqAC8IrYkeyc.jpg",
      "vote_average": 5.318,
      "vote_count": 3,
      "width": 3840
    },
    {
      "aspect_ratio": 1.778,
      "height": 1080,
      "iso_639_1": "en",
      "file_path": "/itH1Wlzwf6yTNa7fVkYMVUwXlhR.jpg",
      "vote_average": 5.318,
      "vote_count": 3,
      "width": 1920
    },
    {
      "aspect_ratio
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | integer |  |  | `10` |
| `backdrops` | array[object] |  |  |  |
| `posters` | array[object] |  |  |  |

---

### Translations

```
GET /3/collection/{collection_id}/translations
```

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `collection_id` | integer | ✓ |  |

### Response (200)

**Example Response:**
```json
{
  "id": 10,
  "translations": [
    {
      "iso_3166_1": "AE",
      "iso_639_1": "ar",
      "name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
      "english_name": "Arabic",
      "data": {
        "title": "",
        "overview": "",
        "homepage": ""
      }
    },
    {
      "iso_3166_1": "BG",
      "iso_639_1": "bg",
      "name": "\u0431\u044a\u043b\u0433\u0430\u0440\u0441\u043a\u0438 \u0435\u0437\u0438\u043a",
      "english_name": "Bulgarian",
      "data": {
        "title": "\u041c\u0435\u0436\u0434\u0443\u0437\u0432\u0435\u0437\u0434\u043d\u0438 \u0432\u043e\u0439\u043d\u0438 (\u043f\u043e\u0440\u0435\u0434\u0438\u0446\u0430)",
        "overview": "\u041c\u0435\u0436\u0434\u0443\u0437\u0432\u0435\u0437\u0434\u043d\u0438 \u0432\u043e\u0439\u043d\u0438 \u0435 \u043f\u043e\u0440\u0435\u0434\u0438\u0446\u0430 \u043e\u0442 \u0448\u0435\u0441\u0442 \u0444\u0438\u043b\u043c\u0430 \u043f\u0440\u043e\u0441\u043b\u0435\u0434\u044f\u0432\u0430\u0449\u0438 \u0436\u0438\u0432\u043e\u0442\u0430 \u043d\u0430 \u0410\u043d\u0430\u043a\u0438\u043d \u0421\u043a\u0430\u0439\u0443\u043e\u043a\u044a\u0440. \u041e\u0442\u043a\u0440\u0438\u0442 \u043e\u0442 \u0434\u0436\u0435\u0434\u0430\u044f \u041a\u0443\u0430\u0439-\u0413\u043e\u043d \u0414\u0436\u0438\u043d \u043d\u0430 \u043f\u0443\u0441\u0442\u0438\u043d\u043d\u0430\u0442\u0430 \u043f\u043b\u0430\u043d\u0435\u0442\u0430 \u0422\u0430\u0442\u0443\u0438\u043d \u0410\u043d\u0430\u043a\u0438\u043d \u0435 \u0432\u0441\u0435 \u043e\u0449\u0435 \u0434\u0435\u0442\u0435, \u043d\u043e \u043f\u043e\u0441\u0442\u0435\u043f\u0435\u043d\u043d\u043e \u0441\u0435 \u043f\u0440\u0435\u0432\u0440\u044a\u0449\u0430 \u0432 \u0441\u0438\u043b\u043d\u0438\u044f \u0414\u0430\u0440\u0442 \u0412\u0435\u0439\u0434\u044a\u0440, \u0434\u044f\u0441\u043d\u0430\u0442\u0430 \u0440\u044a\u043a\u0430 \u043d\u0430 \u0418\u043c\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u044a\u0442, \u043a\u043e\u0439\u0442\u043e \u043f\u043e\u0447\u0442\u0438 
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | integer |  |  | `10` |
| `translations` | array[object] |  |  |  |