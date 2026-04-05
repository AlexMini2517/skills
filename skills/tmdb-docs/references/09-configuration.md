## Configuration

### Details

```
GET /3/configuration
```

Query the API configuration details.

### Response (200)

**Example Response:**
```json
{
  "images": {
    "base_url": "http://image.tmdb.org/t/p/",
    "secure_base_url": "https://image.tmdb.org/t/p/",
    "backdrop_sizes": [
      "w300",
      "w780",
      "w1280",
      "original"
    ],
    "logo_sizes": [
      "w45",
      "w92",
      "w154",
      "w185",
      "w300",
      "w500",
      "original"
    ],
    "poster_sizes": [
      "w92",
      "w154",
      "w185",
      "w342",
      "w500",
      "w780",
      "original"
    ],
    "profile_sizes": [
      "w45",
      "w185",
      "h632",
      "original"
    ],
    "still_sizes": [
      "w92",
      "w185",
      "w300",
      "original"
    ]
  },
  "change_keys": [
    "adult",
    "air_date",
    "also_known_as",
    "alternative_titles",
    "biography",
    "birthday",
    "budget",
    "cast",
    "certifications",
    "character_names",
    "created_by",
    "crew",
    "deathday",
    "episode",
    "episode_number",
    "episode_run_time",
    "freebase_id",
    "freebase_mid",
    "general",
    "genres",
    "guest_stars",
    "homepage",
    "images",
    "imdb_id",
    "languages",
    "name",
    "network",
    "origin_country",
    "original_name",
    "original_title",
    "overview",
    "parts",
    "place_of_birth",
    "plot_keywords",
    "production_code",
    "production_companies",
    "production_countries",
    "releases",
    "revenue",
    "runtime",
    "season",
    "season_number",
    "season_regular",
    "spoken_languages",
    "status",
    "tagline",
    "title",
    "translations",
    "tvdb_id",
    "tvrage_id",
    "type",
    "video",
    "videos"
  ]
}
```

**Response Fields:**

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `images` | object |  |  |  |
| `base_url` | string |  |  | `http://image.tmdb.org/t/p/` |
| `secure_base_url` | string |  |  | `https://image.tmdb.org/t/p/` |
| `backdrop_sizes` | array[string] |  |  |  |
| `logo_sizes` | array[string] |  |  |  |
| `poster_sizes` | array[string] |  |  |  |
| `profile_sizes` | array[string] |  |  |  |
| `still_sizes` | array[string] |  |  |  |
| `change_keys` | array[string] |  |  |  |

---

### Countries

```
GET /3/configuration/countries
```

Get the list of countries (ISO 3166-1 tags) used throughout TMDB.

### Parameters

**Query Parameters**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `language` | string |  | *(default: `en-US`)* |

### Response (200)

**Example Response:**
```json
[
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
    "iso_3166_1": "AF",
    "english_name": "Afghanistan",
    "native_name": "Afghanistan"
  },
  {
    "iso_3166_1": "AG",
    "english_name": "Antigua and Barbuda",
    "native_name": "Antigua & Barbuda"
  },
  {
    "iso_3166_1": "AI",
    "english_name": "Anguilla",
    "native_name": "Anguilla"
  },
  {
    "iso_3166_1": "AL",
    "english_name": "Albania",
    "native_name": "Albania"
  },
  {
    "iso_3166_1": "AM",
    "english_name": "Armenia",
    "native_name": "Armenia"
  },
  {
    "iso_3166_1": "AN",
    "english_name": "Netherlands Antilles",
    "native_name": "Netherlands Antilles"
  },
  {
    "iso_3166_1": "AO",
    "english_name": "Angola",
    "native_name": "Angola"
  },
  {
    "iso_3166_1": "AQ",
    "english_name": "Antarctica",
    "native_name": "Antarctica"
  },
  {
    "iso_3166_1": "AR",
    "english_name": "Argentina",
    "native_name": "Argentina"
  },
  {
    "iso_3166_1": "AS",
    "english_name": "American Samoa",
    "native_name": "American Samoa"
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
    "iso_3166_1": "AW",
    "english_name": "Aruba",
    "native_name": "Aruba"
  },
  {
    "iso_3166_1": "AZ",
    "english_name": "Azerbaijan",
    "native_name": "Azerbaijan"
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
    "iso_3166_1": "BD",
    "english_name": "Bangladesh",
    "native_name": "Bangladesh"
  },
  {
    "iso_3166_1": "BE",
    "english_name": "Belgium",
    "native_name": "Belg
```

---

### Jobs

```
GET /3/configuration/jobs
```

Get the list of the jobs and departments we use on TMDB.

### Response (200)

**Example Response:**
```json
[
  {
    "department": "Production",
    "jobs": [
      "Casting",
      "Line Producer",
      "Co-Producer",
      "Accounting Trainee",
      "Assistant Extras Casting",
      "First Assistant Accountant",
      "General Manager",
      "Head of Production",
      "Locale Casting Director",
      "Location Assistant",
      "Location Coordinator",
      "Post Production Technical Engineer",
      "Location Manager",
      "Production Accountant",
      "Supervising Producer",
      "Production Manager",
      "Consulting Producer",
      "Assistant Production Manager",
      "Other",
      "Finance",
      "Character Technical Supervisor",
      "Development Manager",
      "Production Coordinator",
      "ADR Voice Casting",
      "Additional Post-Production Supervisor",
      "Art Department Production Assistant",
      "Back-up Truck Production Assistant",
      "Accounting Clerk Assistant",
      "Broadcast Producer",
      "Extras Casting Coordinator",
      "Grip Production Assistant",
      "Key Set Production Assistant",
      "Musical Casting",
      "Post Production Accountant",
      "Development Producer",
      "Key Accountant",
      "Production Assistant",
      "Production Consultant",
      "Second Assistant Production Coordinator",
      "Truck Production Assistant",
      "Executive Consultant",
      "Accounting Supervisor",
      "Assistant Location Manager",
      "Director of Operations",
      "Executive Assistant",
      "Insert Unit Location Manager",
      "Key Grip Production Assistant",
      "Location Casting",
      "Unit Swing",
      "Executive Producer",
      "Producer",
      "Executive In Charge Of Production",
      "Senior Executive Consultant",
      "Unit Manager",
      "Additional Casting",
      "Assistant Accountant",
      "Contract Manager",
      "Extras Casting",
      "Production Driver",
      "Production Trainee",
      "Associate Producer",
      "Attorney",
      "Casting Coordinator",
      "Casting Consult
```

---

### Languages

```
GET /3/configuration/languages
```

Get the list of languages (ISO 639-1 tags) used throughout TMDB.

### Response (200)

**Example Response:**
```json
[
  {
    "iso_639_1": "bi",
    "english_name": "Bislama",
    "name": ""
  },
  {
    "iso_639_1": "cs",
    "english_name": "Czech",
    "name": "\u010cesk\u00fd"
  },
  {
    "iso_639_1": "ba",
    "english_name": "Bashkir",
    "name": ""
  },
  {
    "iso_639_1": "ae",
    "english_name": "Avestan",
    "name": ""
  },
  {
    "iso_639_1": "av",
    "english_name": "Avaric",
    "name": ""
  },
  {
    "iso_639_1": "de",
    "english_name": "German",
    "name": "Deutsch"
  },
  {
    "iso_639_1": "mt",
    "english_name": "Maltese",
    "name": "Malti"
  },
  {
    "iso_639_1": "om",
    "english_name": "Oromo",
    "name": ""
  },
  {
    "iso_639_1": "rm",
    "english_name": "Raeto-Romance",
    "name": ""
  },
  {
    "iso_639_1": "so",
    "english_name": "Somali",
    "name": "Somali"
  },
  {
    "iso_639_1": "ts",
    "english_name": "Tsonga",
    "name": ""
  },
  {
    "iso_639_1": "vi",
    "english_name": "Vietnamese",
    "name": "Ti\u1ebfng Vi\u1ec7t"
  },
  {
    "iso_639_1": "gn",
    "english_name": "Guarani",
    "name": ""
  },
  {
    "iso_639_1": "ig",
    "english_name": "Igbo",
    "name": ""
  },
  {
    "iso_639_1": "it",
    "english_name": "Italian",
    "name": "Italiano"
  },
  {
    "iso_639_1": "ki",
    "english_name": "Kikuyu",
    "name": ""
  },
  {
    "iso_639_1": "ku",
    "english_name": "Kurdish",
    "name": ""
  },
  {
    "iso_639_1": "la",
    "english_name": "Latin",
    "name": "Latin"
  },
  {
    "iso_639_1": "ln",
    "english_name": "Lingala",
    "name": ""
  },
  {
    "iso_639_1": "lb",
    "english_name": "Letzeburgesch",
    "name": ""
  },
  {
    "iso_639_1": "ny",
    "english_name": "Chichewa; Nyanja",
    "name": ""
  },
  {
    "iso_639_1": "pl",
    "english_name": "Polish",
    "name": "Polski"
  },
  {
    "iso_639_1": "si",
    "english_name": "Sinhalese",
    "name": "\u0dc3\u0dd2\u0d82\u0dc4\u0dbd"
  },
  {
    "iso_639_1": "to",
    "english_name": "Tonga",
    "name": ""
  },
  {
    "iso_63
```

---

### Primary Translations

```
GET /3/configuration/primary_translations
```

Get a list of the officially supported translations on TMDB.

### Response (200)

**Example Response:**
```json
[
  "af-ZA",
  "ar-AE",
  "ar-SA",
  "be-BY",
  "bg-BG",
  "bn-BD",
  "ca-ES",
  "ch-GU",
  "cn-CN",
  "cs-CZ",
  "cy-GB",
  "da-DK",
  "de-AT",
  "de-CH",
  "de-DE",
  "el-GR",
  "en-AU",
  "en-CA",
  "en-GB",
  "en-IE",
  "en-NZ",
  "en-US",
  "eo-EO",
  "es-ES",
  "es-MX",
  "et-EE",
  "eu-ES",
  "fa-IR",
  "fi-FI",
  "fr-CA",
  "fr-FR",
  "ga-IE",
  "gd-GB",
  "gl-ES",
  "he-IL",
  "hi-IN",
  "hr-HR",
  "hu-HU",
  "id-ID",
  "it-IT",
  "ja-JP",
  "ka-GE",
  "kk-KZ",
  "kn-IN",
  "ko-KR",
  "ky-KG",
  "lt-LT",
  "lv-LV",
  "ml-IN",
  "mr-IN",
  "ms-MY",
  "ms-SG",
  "nb-NO",
  "nl-BE",
  "nl-NL",
  "no-NO",
  "pa-IN",
  "pl-PL",
  "pt-BR",
  "pt-PT",
  "ro-RO",
  "ru-RU",
  "si-LK",
  "sk-SK",
  "sl-SI",
  "sq-AL",
  "sr-RS",
  "sv-SE",
  "ta-IN",
  "te-IN",
  "th-TH",
  "tl-PH",
  "tr-TR",
  "uk-UA",
  "vi-VN",
  "zh-CN",
  "zh-HK",
  "zh-SG",
  "zh-TW",
  "zu-ZA"
]
```

---

### Timezones

```
GET /3/configuration/timezones
```

Get the list of timezones used throughout TMDB.

### Response (200)

**Example Response:**
```json
[
  {
    "iso_3166_1": "AD",
    "zones": [
      "Europe/Andorra"
    ]
  },
  {
    "iso_3166_1": "AE",
    "zones": [
      "Asia/Dubai"
    ]
  },
  {
    "iso_3166_1": "AF",
    "zones": [
      "Asia/Kabul"
    ]
  },
  {
    "iso_3166_1": "AG",
    "zones": [
      "America/Puerto_Rico"
    ]
  },
  {
    "iso_3166_1": "AI",
    "zones": [
      "America/Puerto_Rico"
    ]
  },
  {
    "iso_3166_1": "AL",
    "zones": [
      "Europe/Tirane"
    ]
  },
  {
    "iso_3166_1": "AM",
    "zones": [
      "Asia/Yerevan"
    ]
  },
  {
    "iso_3166_1": "AO",
    "zones": [
      "Africa/Lagos"
    ]
  },
  {
    "iso_3166_1": "AQ",
    "zones": [
      "Antarctica/Casey",
      "Antarctica/Davis",
      "Antarctica/Mawson",
      "Antarctica/Palmer",
      "Antarctica/Rothera",
      "Antarctica/Troll",
      "Asia/Urumqi",
      "Pacific/Auckland",
      "Pacific/Port_Moresby",
      "Asia/Riyadh"
    ]
  },
  {
    "iso_3166_1": "AR",
    "zones": [
      "America/Argentina/Buenos_Aires",
      "America/Argentina/Cordoba",
      "America/Argentina/Salta",
      "America/Argentina/Jujuy",
      "America/Argentina/Tucuman",
      "America/Argentina/Catamarca",
      "America/Argentina/La_Rioja",
      "America/Argentina/San_Juan",
      "America/Argentina/Mendoza",
      "America/Argentina/San_Luis",
      "America/Argentina/Rio_Gallegos",
      "America/Argentina/Ushuaia"
    ]
  },
  {
    "iso_3166_1": "AS",
    "zones": [
      "Pacific/Pago_Pago"
    ]
  },
  {
    "iso_3166_1": "AT",
    "zones": [
      "Europe/Vienna"
    ]
  },
  {
    "iso_3166_1": "AU",
    "zones": [
      "Australia/Lord_Howe",
      "Antarctica/Macquarie",
      "Australia/Hobart",
      "Australia/Melbourne",
      "Australia/Sydney",
      "Australia/Broken_Hill",
      "Australia/Brisbane",
      "Australia/Lindeman",
      "Australia/Adelaide",
      "Australia/Darwin",
      "Australia/Perth",
      "Australia/Eucla"
    ]
  },
  {
    "iso_3166_1": "AW",
    "zones": [
      "
```