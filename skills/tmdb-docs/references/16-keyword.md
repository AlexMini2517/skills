## Keyword

### Details

```
GET /3/keyword/{keyword_id}
```

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `keyword_id` | integer | ✓ |  |

### Response (200)

**Example Response:**
```json
{
  "id": 1701,
  "name": "hero"
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | integer |  |  | `1701` |
| `name` | string |  |  | `hero` |

---

### Movies

```
GET /3/keyword/{keyword_id}/movies
```

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `keyword_id` | string | ✓ |  |

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `include_adult` | boolean |  | *(default: `False`)* |
| `language` | string |  | *(default: `en-US`)* |
| `page` | integer |  | *(default: `1`)* |

### Response (200)

**Example Response:**
```json
{
  "id": 1701,
  "page": 1,
  "results": [
    {
      "adult": false,
      "backdrop_path": "/3CxUndGhUcZdt1Zggjdb2HkLLQX.jpg",
      "genre_ids": [
        28,
        12,
        878
      ],
      "id": 640146,
      "original_language": "en",
      "original_title": "Ant-Man and the Wasp: Quantumania",
      "overview": "Das Superhelden-Duo Scott Lang und Hope Van Dyne erkundet zusammen mit Hopes Eltern Hank Pym und Janet Van Dyne das Quantenreich, interagiert mit seltsamen neuen Kreaturen und begibt sich auf ein Abenteuer, das sie \u00fcber die Grenzen dessen hinaustreiben wird, was sie f\u00fcr m\u00f6glich gehalten haben.",
      "popularity": 9200.005,
      "poster_path": "/nA5otwVxAfpBP4PVgeuBk3qHcLY.jpg",
      "release_date": "2023-02-15",
      "title": "Ant-Man and the Wasp: Quantumania",
      "video": false,
      "vote_average": 6.5,
      "vote_count": 2079
    },
    {
      "adult": false,
      "backdrop_path": "/xDMIl84Qo5Tsu62c9DGWhmPI67A.jpg",
      "genre_ids": [
        28,
        12,
        878
      ],
      "id": 505642,
      "original_language": "en",
      "original_title": "Black Panther: Wakanda Forever",
      "overview": "Der K\u00f6nig ist tot! K\u00f6nig T'Challa, der als Black Panther auch Mitglied der Avengers-Heldentruppe war, stirbt an einer unbekannten Krankheit und ganz Wakanda ist in Trauer. Die Weltgemeinschaft sieht ihre Chance gekommen, um das vermeintlich geschw\u00e4chte K\u00f6nigreich endlich zu Zugest\u00e4ndnissen bei der Lieferung des m\u00e4chtigen Minerals Vibranium zu bewegen - und scheut dabei auch vor bewaffneten \u00dcberf\u00e4llen nicht zur\u00fcck. Doch K\u00f6nigin Ramonda bleibt standhaft und weist die Staatsoberh\u00e4upter in ihre Schranken. Wakanda wird auch ohne K\u00f6nig T'Challa und den Black Panther weiter existieren und nicht vor anderen Nationen buckeln. Zur selben Zeit haben die USA mithilfe der erst 19 Jahre alten MIT-Studentin Riri Williams ein Ger\u00e4t zur Aufsp\u00fcrung von Vibr
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | integer |  |  | `1701` |
| `page` | integer |  |  | `1` |
| `results` | array[object] |  |  |  |
| `total_pages` | integer |  |  | `11` |
| `total_results` | integer |  |  | `211` |