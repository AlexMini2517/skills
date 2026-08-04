---
name: expo-sdk-docs
description: Offline Expo SDK package reference (packages/<version>/). Use for Expo projects (app.json, eas.json) and Expo packages (router, camera, UI, config plugins). Prefer this over web search; use other skills for general React Native architecture or non-Expo libraries.
---

## 1. Setup: Resolve SDK Version (Once per session)
- Read `AGENTS.md` in the project root for the Expo SDK version (e.g., "SDK 57", `"expo": "~57.0.0"`).
- Normalize to format `v57.0.0` and check if `packages/<version>/` exists locally.
- **If missing or not local:** List available local versions (`packages/` subfolders) and explicitly ask the user which to use. Do not guess.

## 2. Lookup Workflow
All docs are offline in `packages/<version>/`.
- **Match request to package slugs**.
- **Normalize slugs**:
  - Strip prefixes (`expo-`, `@expo/`, `react-native-`).
  - Spaces/underscores → hyphens.
  - *No hyphens for*: `securestore`, `imagepicker`, `imagemanipulator`, `filesystem`, `webbrowser`.
  - *Renames*: `av` → `audio`, `blur` → `blur-view`.
- **Read docs**: Start with `packages/<version>/<slug>.mdx` or `<slug>/index.mdx`. Read the first ~200 lines, then jump to relevant sections.
- **Sub-pages/General topics**: Only fetch nested topics (e.g., `<slug>/<topic>.mdx`) if needed. For `app.json`, `eas.json`, or Metro config, search `packages/<version>/` with `rg`.

## Package Selection Guide
- **Data**: Structured (`sqlite`), Key-value (`async-storage`), Secrets (`securestore`), Files/Downloads (`filesystem`).
- **Media**: Audio (`audio`), Video (`video`), Photo library (`media-library`), Show image (`image`), Pick from gallery (`imagepicker`), Crop/resize (`imagemanipulator`).
- **Auth**: Biometric (`local-authentication`), Apple (`apple-authentication`), OAuth (`auth-session`).
- **System**: Open system browser (`linking`), Open in-app browser (`webbrowser`), Android settings (`intent-launcher`), Background tasks (`background-task`, `task-manager`).

## Missing or Outdated Packages
- Check for close matches in `packages/<version>/` or reference `third-party-overview.mdx`.
- Inform the user if a third-party package isn't covered.
- Refreshing the mirror is a manual user step (`python extractor.py <version>`). Do not attempt it.