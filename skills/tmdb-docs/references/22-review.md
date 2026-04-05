## Review

### Details

```
GET /3/review/{review_id}
```

Retrieve the details of a movie or TV show review.

### Parameters

**Path Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `review_id` | string | ✓ |  |

### Response (200)

**Example Response:**
```json
{
  "id": "640b2aeecaaca20079decdcc",
  "author": "Ricardo Oliveira",
  "author_details": {
    "name": "Ricardo Oliveira",
    "username": "RSOliveira",
    "avatar_path": "/23Cl7rhsknc7IIAcZZAGKzovjTu.jpg",
    "rating": 9.0
  },
  "content": "\"The Last of Us\" is a post-apocalyptic TV series based on the popular video game of the same name. The story follows the journey of Joel, a smuggler, and Ellie, a teenage girl who may be the key to finding a cure for a deadly fungal infection that has ravaged the world.\r\n\r\nThe series features outstanding performances from Pedro Pascal as Joel, Bella Ramsey as Ellie, and Anna Torv as Tess. The chemistry between the main characters is excellent, and the casting is spot-on.\r\n\r\nThe show's writing is superb, and it captures the essence of the video game while adding a fresh perspective. The narrative is engaging, and the pacing is just right, with each episode leaving you on the edge of your seat, eager to see what happens next.\r\n\r\nThe show's production value is top-notch, with stunning visuals and cinematography that capture the bleak and haunting atmosphere of a post-apocalyptic world. The use of practical effects and makeup is impressive and adds to the overall immersion of the story.\r\n\r\nOverall, \"The Last of Us\" is an outstanding TV series that does justice to the source material. It's a must-watch for fans of the video game and anyone who enjoys gripping and emotional storytelling. I would rate it a 9 out of 10.\r\n\r\n \r\n\r\nWritten and Reviewed by RSOliveira",
  "created_at": "2023-03-10T13:04:46.674Z",
  "iso_639_1": "en",
  "media_id": 100088,
  "media_title": "The Last of Us",
  "media_type": "tv",
  "updated_at": "2023-03-10T13:04:46.734Z",
  "url": "https://www.themoviedb.org/review/640b2aeecaaca20079decdcc"
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | string |  |  | `640b2aeecaaca20079decdcc` |
| `author` | string |  |  | `Ricardo Oliveira` |
| `author_details` | object |  |  |  |
| `name` | string |  |  | `Ricardo Oliveira` |
| `username` | string |  |  | `RSOliveira` |
| `avatar_path` | string |  |  | `/23Cl7rhsknc7IIAcZZAGKzovjTu.jpg` |
| `rating` | integer |  |  | `9` |
| `content` | string |  |  | `"The Last of Us" is a post-apocalyptic TV series based on the popular video game of the same name. The story follows the journey of Joel, a smuggler, and Ellie, a teenage girl who may be the key to finding a cure for a deadly fungal infection that has ravaged the world.

The series features outstanding performances from Pedro Pascal as Joel, Bella Ramsey as Ellie, and Anna Torv as Tess. The chemistry between the main characters is excellent, and the casting is spot-on.

The show's writing is superb, and it captures the essence of the video game while adding a fresh perspective. The narrative is engaging, and the pacing is just right, with each episode leaving you on the edge of your seat, eager to see what happens next.

The show's production value is top-notch, with stunning visuals and cinematography that capture the bleak and haunting atmosphere of a post-apocalyptic world. The use of practical effects and makeup is impressive and adds to the overall immersion of the story.

Overall, "The Last of Us" is an outstanding TV series that does justice to the source material. It's a must-watch for fans of the video game and anyone who enjoys gripping and emotional storytelling. I would rate it a 9 out of 10.

 

Written and Reviewed by RSOliveira` |
| `created_at` | string |  |  | `2023-03-10T13:04:46.674Z` |
| `iso_639_1` | string |  |  | `en` |
| `media_id` | integer |  |  | `100088` |
| `media_title` | string |  |  | `The Last of Us` |
| `media_type` | string |  |  | `tv` |
| `updated_at` | string |  |  | `2023-03-10T13:04:46.734Z` |
| `url` | string |  |  | `https://www.themoviedb.org/review/640b2aeecaaca20079decdcc` |