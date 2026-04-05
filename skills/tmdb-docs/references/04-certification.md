## Certification

### Movie Certifications

```
GET /3/certification/movie/list
```

Get an up to date list of the officially supported movie certifications on TMDB.

### Response (200)

**Example Response:**
```json
{
  "certifications": {
    "AU": [
      {
        "certification": "E",
        "meaning": "Exempt from classification. Films that are exempt from classification must not contain contentious material (i.e. material that would ordinarily be rated M or higher).",
        "order": 1
      },
      {
        "certification": "G",
        "meaning": "General. The content is very mild in impact.",
        "order": 2
      },
      {
        "certification": "PG",
        "meaning": "Parental guidance recommended. There are no age restrictions. The content is mild in impact.",
        "order": 3
      },
      {
        "certification": "M",
        "meaning": "Recommended for mature audiences. There are no age restrictions. The content is moderate in impact.",
        "order": 4
      },
      {
        "certification": "MA 15+",
        "meaning": "Mature Accompanied. Unsuitable for children younger than 15. Children younger than 15 years must be accompanied by a parent or guardian. The content is strong in impact.",
        "order": 5
      },
      {
        "certification": "R 18+",
        "meaning": "Restricted to 18 years and over. Adults only. The content is high in impact.",
        "order": 6
      },
      {
        "certification": "X 18+",
        "meaning": "Restricted to 18 years and over. Films with this rating have pornographic content. Films classified as X18+ are banned from being sold or rented in all Australian states and are only legally available in the Australian Capital Territory and the Northern Territory. However, importing X18+ material from the two territories to any of the Australian states is legal.The content is sexually explicit in impact.",
        "order": 7
      },
      {
        "certification": "RC",
        "meaning": "Refused Classification. Banned from sale or hire in Australia; also generally applies to importation (if inspected by and suspicious to Customs). Private Internet viewing is unenforced and attempts to legally censo
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `certifications` | object |  |  |  |
| `AU` | array[object] |  |  |  |
| `BG` | array[object] |  |  |  |
| `BR` | array[object] |  |  |  |
| `CA` | array[object] |  |  |  |
| `CA-QC` | array[object] |  |  |  |
| `DE` | array[object] |  |  |  |
| `DK` | array[object] |  |  |  |
| `ES` | array[object] |  |  |  |
| `FI` | array[object] |  |  |  |
| `FR` | array[object] |  |  |  |
| `GB` | array[object] |  |  |  |
| `HU` | array[object] |  |  |  |
| `IN` | array[object] |  |  |  |
| `IT` | array[object] |  |  |  |
| `LT` | array[object] |  |  |  |
| `MY` | array[object] |  |  |  |
| `NL` | array[object] |  |  |  |
| `NO` | array[object] |  |  |  |
| `NZ` | array[object] |  |  |  |
| `PH` | array[object] |  |  |  |
| `PT` | array[object] |  |  |  |
| `RU` | array[object] |  |  |  |
| `SE` | array[object] |  |  |  |
| `US` | array[object] |  |  |  |
| `KR` | array[object] |  |  |  |
| `SK` | array[object] |  |  |  |
| `TH` | array[object] |  |  |  |
| `MX` | array[object] |  |  |  |
| `ID` | array[object] |  |  |  |
| `TR` | array[object] |  |  |  |
| `AR` | array[object] |  |  |  |
| `GR` | array[object] |  |  |  |
| `TW` | array[object] |  |  |  |
| `ZA` | array[object] |  |  |  |
| `SG` | array[object] |  |  |  |
| `IE` | array[object] |  |  |  |
| `PR` | array[object] |  |  |  |
| `JP` | array[object] |  |  |  |
| `VI` | array[object] |  |  |  |
| `CH` | array[object] |  |  |  |
| `IL` | array[object] |  |  |  |
| `HK` | array[object] |  |  |  |
| `MO` | array[object] |  |  |  |
| `LV` | array[object] |  |  |  |
| `LU` | array[object] |  |  |  |