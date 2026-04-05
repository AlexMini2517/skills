## Watch

### Available Regions

```
GET /3/watch/providers/regions
```

Get the list of the countries we have watch provider (OTT/streaming) data for.

### Parameters

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |

### Response (200)

**Example Response:**
```json
{
  "results": [
    {
      "iso_3166_1": "AD",
      "english_name": "Andorra",
      "native_name": "Andorra"
    },
    {
      "iso_3166_1": "AE",
      "english_name": "United Arab Emirates",
      "native_name": "United Arab Emirates"
    },
    {
      "iso_3166_1": "AG",
      "english_name": "Antigua and Barbuda",
      "native_name": "Antigua & Barbuda"
    },
    {
      "iso_3166_1": "AL",
      "english_name": "Albania",
      "native_name": "Albania"
    },
    {
      "iso_3166_1": "AR",
      "english_name": "Argentina",
      "native_name": "Argentina"
    },
    {
      "iso_3166_1": "AT",
      "english_name": "Austria",
      "native_name": "Austria"
    },
    {
      "iso_3166_1": "AU",
      "english_name": "Australia",
      "native_name": "Australia"
    },
    {
      "iso_3166_1": "BA",
      "english_name": "Bosnia and Herzegovina",
      "native_name": "Bosnia & Herzegovina"
    },
    {
      "iso_3166_1": "BB",
      "english_name": "Barbados",
      "native_name": "Barbados"
    },
    {
      "iso_3166_1": "BE",
      "english_name": "Belgium",
      "native_name": "Belgium"
    },
    {
      "iso_3166_1": "BG",
      "english_name": "Bulgaria",
      "native_name": "Bulgaria"
    },
    {
      "iso_3166_1": "BH",
      "english_name": "Bahrain",
      "native_name": "Bahrain"
    },
    {
      "iso_3166_1": "BM",
      "english_name": "Bermuda",
      "native_name": "Bermuda"
    },
    {
      "iso_3166_1": "BO",
      "english_name": "Bolivia",
      "native_name": "Bolivia"
    },
    {
      "iso_3166_1": "BR",
      "english_name": "Brazil",
      "native_name": "Brazil"
    },
    {
      "iso_3166_1": "BS",
      "english_name": "Bahamas",
      "native_name": "Bahamas"
    },
    {
      "iso_3166_1": "CA",
      "english_name": "Canada",
      "native_name": "Canada"
    },
    {
      "iso_3166_1": "CH",
      "english_name": "Switzerland",
      "native_name": "Switzerland"
    },
    {
      "iso_3166_1": "CI",
     
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `results` | array[object] |  |  |  |

---

### Movie Providers

```
GET /3/watch/providers/movie
```

Get the list of streaming providers we have for movies.

### Parameters

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |
| `watch_region` | string |  |  |

### Response (200)

**Example Response:**
```json
{
  "results": [
    {
      "display_priorities": {
        "CA": 6,
        "AE": 1,
        "AR": 3,
        "AT": 4,
        "AU": 10,
        "BE": 6,
        "BO": 6,
        "BR": 8,
        "BG": 2,
        "CH": 4,
        "CL": 3,
        "CO": 4,
        "CR": 5,
        "CZ": 3,
        "DE": 4,
        "DK": 7,
        "EC": 7,
        "EE": 3,
        "EG": 2,
        "ES": 4,
        "FI": 10,
        "FR": 5,
        "GB": 5,
        "GR": 2,
        "GT": 7,
        "HK": 5,
        "HN": 7,
        "HU": 3,
        "ID": 4,
        "IE": 4,
        "IN": 8,
        "IT": 4,
        "JP": 7,
        "LT": 3,
        "LV": 3,
        "MX": 4,
        "MY": 4,
        "NL": 8,
        "NO": 6,
        "NZ": 4,
        "PE": 3,
        "PH": 4,
        "PL": 1,
        "PT": 4,
        "PY": 7,
        "RU": 2,
        "SA": 1,
        "SE": 8,
        "SG": 5,
        "SK": 3,
        "TH": 4,
        "TR": 6,
        "TW": 7,
        "US": 4,
        "VE": 4,
        "ZA": 2,
        "SI": 31,
        "CV": 13,
        "GH": 17,
        "MU": 15,
        "MZ": 16,
        "UG": 16,
        "IL": 28
      },
      "display_priority": 2,
      "logo_path": "/peURlLlr8jggOwK53fJ5wdQl05y.jpg",
      "provider_name": "Apple TV",
      "provider_id": 2
    },
    {
      "display_priorities": {
        "CA": 8,
        "AE": 3,
        "AR": 6,
        "AT": 8,
        "AU": 14,
        "BE": 7,
        "BO": 22,
        "BR": 16,
        "CH": 5,
        "CL": 4,
        "CO": 3,
        "CR": 22,
        "CZ": 4,
        "DE": 8,
        "DK": 8,
        "EC": 11,
        "EE": 4,
        "EG": 4,
        "ES": 13,
        "FI": 11,
        "FR": 7,
        "GB": 12,
        "GR": 3,
        "GT": 22,
        "HK": 13,
        "HN": 22,
        "HR": 3,
        "HU": 4,
        "ID": 6,
        "IE": 7,
        "IN": 10,
        "IS": 4,
        "IT": 7,
        "JP": 9,
        "KR": 7,
        "LT": 4,
        "LV": 4,
        "MX": 15,
        "MY": 5
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `results` | array[object] |  |  |  |

---

### TV Providers

```
GET /3/watch/providers/tv
```

Get the list of streaming providers we have for TV shows.

### Parameters

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |
| `watch_region` | string |  |  |

### Response (200)

**Example Response:**
```json
{
  "results": [
    {
      "display_priorities": {
        "CA": 6,
        "AE": 1,
        "AR": 3,
        "AT": 4,
        "AU": 10,
        "BE": 6,
        "BO": 6,
        "BR": 8,
        "BG": 2,
        "CH": 4,
        "CL": 3,
        "CO": 4,
        "CR": 5,
        "CZ": 3,
        "DE": 4,
        "DK": 7,
        "EC": 7,
        "EE": 3,
        "EG": 2,
        "ES": 4,
        "FI": 10,
        "FR": 5,
        "GB": 5,
        "GR": 2,
        "GT": 7,
        "HK": 5,
        "HN": 7,
        "HU": 3,
        "ID": 4,
        "IE": 4,
        "IN": 8,
        "IT": 4,
        "JP": 7,
        "LT": 3,
        "LV": 3,
        "MX": 4,
        "MY": 4,
        "NL": 8,
        "NO": 6,
        "NZ": 4,
        "PE": 3,
        "PH": 4,
        "PL": 1,
        "PT": 4,
        "PY": 7,
        "RU": 2,
        "SA": 1,
        "SE": 8,
        "SG": 5,
        "SK": 3,
        "TH": 4,
        "TR": 6,
        "TW": 7,
        "US": 4,
        "VE": 4,
        "ZA": 2,
        "SI": 31,
        "CV": 13,
        "GH": 17,
        "MU": 15,
        "MZ": 16,
        "UG": 16,
        "IL": 28
      },
      "display_priority": 2,
      "logo_path": "/peURlLlr8jggOwK53fJ5wdQl05y.jpg",
      "provider_name": "Apple TV",
      "provider_id": 2
    },
    {
      "display_priorities": {
        "CA": 8,
        "AE": 3,
        "AR": 6,
        "AT": 8,
        "AU": 14,
        "BE": 7,
        "BO": 22,
        "BR": 16,
        "CH": 5,
        "CL": 4,
        "CO": 3,
        "CR": 22,
        "CZ": 4,
        "DE": 8,
        "DK": 8,
        "EC": 11,
        "EE": 4,
        "EG": 4,
        "ES": 13,
        "FI": 11,
        "FR": 7,
        "GB": 12,
        "GR": 3,
        "GT": 22,
        "HK": 13,
        "HN": 22,
        "HR": 3,
        "HU": 4,
        "ID": 6,
        "IE": 7,
        "IN": 10,
        "IS": 4,
        "IT": 7,
        "JP": 9,
        "KR": 7,
        "LT": 4,
        "LV": 4,
        "MX": 15,
        "MY": 5
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `results` | array[object] |  |  |  |