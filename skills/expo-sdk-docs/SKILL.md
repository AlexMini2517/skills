---
name: expo-sdk-docs
description: "On-demand Expo SDK package reference. Use when working in an Expo project, or when the user asks about Expo SDK APIs/packages (expo-router, expo-camera, etc.). Determines the SDK version from AGENTS.md in the project root. If missing, repeatedly asks the user until a version is provided. Fetches only the required .mdx/.md docs directly from the Expo GitHub repository."
---

## SDK Version Resolution

1. Read `AGENTS.md` in the current project root.
2. Look for an explicit Expo SDK version (e.g., `Expo SDK: 57`, `SDK 57`, `expo: ~57.0.0`).
3. Normalize the version to the exact GitHub folder format (e.g., `v57.0.0`, `v56.0.0`, `v55.0.0`, `v54.0.0`, `unversioned`).  
   *Note*: `latest` does not exist as a folder on GitHub; map it to the most recent stable version (e.g., `v57.0.0`) or ask the user to clarify the exact version number.
4. **If `AGENTS.md` does not exist or the SDK version is missing/ambiguous**, ask the user:
   > "Quale Expo SDK sta usando questo progetto? (es. 57, 56, unversioned)"
5. **CRITICAL**: If the user does not answer or refuses to provide the version, **do not proceed**. Keep asking for the version until the user provides it. Do not guess, do not use fallbacks, and do not download any docs without knowing the exact version.

## Docs Retrieval Workflow

Once the exact version (e.g., `v57.0.0`) is known:
1. Fetch the top-level index of available packages for that version using the GitHub API:
```http
https://api.github.com/repos/expo/expo/contents/docs/pages/versions/{version}/sdk?ref=main
```
*Example for SDK 57:*
```http
https://api.github.com/repos/expo/expo/contents/docs/pages/versions/v57.0.0/sdk?ref=main
```
2. Identify the relevant package slug from the index using the slug normalization rules below.
3. Fetch **only** the specific `.mdx` or `.md` file needed for the user's request directly from raw GitHub:
   ```http
   https://raw.githubusercontent.com/expo/expo/main/docs/pages/versions/{version}/sdk/{slug}.mdx
   ```
   *Example:*
   ```http
   https://raw.githubusercontent.com/expo/expo/main/docs/pages/versions/v57.0.0/sdk/camera.mdx
   ```
4. If the package has a folder instead of a single file, fetch the folder index first, then fetch only the required nested files (e.g., `index.mdx`).
5. Do not download the entire `sdk` docs tree. Fetch only the smallest possible set of docs needed for the current question.

## Package Slug Normalization

When the user mentions a package name, normalize it to find the file in the GitHub index:
- Strip prefixes: `expo-`, `@expo/`, `react-native-`, `@react-native-community/`, `@shopify/`
- Convert spaces and underscores to hyphens
- ⚠️ Watch out — these slugs drop the hyphen: `secure-store` → `securestore`, `image-picker` → `imagepicker`, `image-manipulator` → `imagemanipulator`, `file-system` → `filesystem`, `web-browser` → `webbrowser`
- These rename entirely: `av` → `audio`, `blur` → `blur-view`

## Decision Trees for Common Scenarios

When the user's request could map to multiple packages, use these trees to pick the right one(s):
- **"Save data locally":**
  - Structured/queryable data → `sqlite`
  - Simple key-value pairs → `async-storage`
  - Sensitive data (tokens, passwords) → `securestore`
  - Binary files (images, PDFs) → `filesystem`
- **"Show an image":**
  - Display a static/network image → `image`
  - Pick from photo gallery → `imagepicker` (then display with `image`)
  - Crop, resize, or rotate → `imagemanipulator`
- **"Play media":**
  - Audio playback/recording → `audio`
  - Video playback → `video`
  - Access saved photos/videos → `media-library`
- **"Authenticate the user":**
  - Biometric → `local-authentication`
  - Apple Sign-In → `apple-authentication`
  - OAuth/OpenID → `auth-session`
- **"Open something external":**
  - Open URL in system browser → `linking`
  - Open URL in in-app browser → `webbrowser`
- **"Background work":**
  - Background fetch → `background-task`
  - Register tasks → `task-manager`

## How to Use the Docs in Practice

Use the fetched docs to:
- Write correct code (check method signatures, required props, import paths).
- Fix bugs (look up the correct API usage).
- Choose the right API when multiple approaches exist.
- Get config right (plugin configs, `app.json` fields, permissions).

When referencing information, don't just dump the docs. Use them to inform your code changes naturally.

## If a Package Isn't Found
- Check the fetched index for close matches.
- For third-party packages not in the Expo ecosystem, say so explicitly. Do not pretend the Expo docs cover them.