---
title: Manifests
description: A library that provides types for Expo Manifests.
sourceCodeUrl: 'https://github.com/expo/expo/tree/main/packages/expo-manifests'
packageName: 'expo-manifests'
platforms: ['android', 'ios', 'tvos', 'expo-go']
---

# Expo Manifests

A library that provides types for Expo Manifests.
Android, iOS, tvOS, Included in Expo Go

## Installation

```sh
npx expo install expo-manifests
```

If you are installing this in an [existing React Native app](/bare/overview), make sure to [install `expo`](/bare/installing-expo-modules) in your project.

## API

```js
import * as Manifests from 'expo-manifests';
```

## Types

> **Deprecated:** Renamed to `EmbeddedManifest`, will be removed in a few versions.

### `BareManifest`

Supported platforms: Android, iOS, tvOS.

Type: [EmbeddedManifest](/versions/latest/sdk/manifests#embeddedmanifest)

### `ClientScopingConfig`

Supported platforms: Android, iOS, tvOS.

| Property | Type | Description |
| --- | --- | --- |
| scopeKey(optional) | `string` | An opaque unique string for scoping client-side data to this project. This value will not change when a project is transferred between accounts or renamed. |

### `EASConfig`

Supported platforms: Android, iOS, tvOS.

| Property | Type | Description |
| --- | --- | --- |
| projectId(optional) | `string` | The ID for this project if it's using EAS. UUID. This value will not change when a project is transferred between accounts or renamed. |

### `EmbeddedManifest`

Supported platforms: Android, iOS, tvOS.

An embedded manifest.

Generated during build in **createManifest.js** build step script.

| Property | Type | Description |
| --- | --- | --- |
| assets | `any[]` | - |
| commitTime | `number` | - |
| id | `string` | - |

### `ExpoClientConfig`

Supported platforms: Android, iOS, tvOS.

Type: [ExpoConfig](https://github.com/expo/expo/blob/main/packages/%40expo/config-types/src/ExpoConfig.ts) extended by:

| Property | Type | Description |
| --- | --- | --- |
| hostUri(optional) | `string` | Only present during development using `@expo/cli`. |

### `ExpoGoConfig`

Supported platforms: Android, iOS, tvOS.

| Property | Type | Description |
| --- | --- | --- |
| debuggerHost(optional) | `string` | - |
| developer(optional) | `Record<string, any> & { tool: string }` | - |
| mainModuleName(optional) | `string` | - |
| packagerOpts(optional) | [ExpoGoPackagerOpts](/versions/latest/sdk/manifests#expogopackageropts) | - |

### `ExpoGoPackagerOpts`

Supported platforms: Android, iOS, tvOS.

Type: `Record<string, any>` extended by:

| Property | Type | Description |
| --- | --- | --- |
| dev(optional) | `boolean` | - |
| hostType(optional) | `string` | - |
| lanType(optional) | `string` | - |
| minify(optional) | `boolean` | - |
| strict(optional) | `boolean` | - |
| urlRandomness(optional) | `string` | - |
| urlType(optional) | `string` | - |

### `ExpoUpdatesManifest`

Supported platforms: Android, iOS, tvOS.

A `expo-updates` manifest.

| Property | Type | Description |
| --- | --- | --- |
| assets | [ManifestAsset[]](#manifestasset) | - |
| createdAt | `string` | - |
| extra(optional) | [ManifestExtra](/versions/latest/sdk/manifests#manifestextra) | - |
| id | `string` | - |
| launchAsset | [ManifestAsset](/versions/latest/sdk/manifests#manifestasset) | - |
| metadata | `object` | - |
| runtimeVersion | `string` | - |

### `ManifestAsset`

Supported platforms: Android, iOS, tvOS.

| Property | Type | Description |
| --- | --- | --- |
| url | `string` | - |

### `ManifestExtra`

Supported platforms: Android, iOS, tvOS.

Type: [ClientScopingConfig](/versions/latest/sdk/manifests#clientscopingconfig) extended by:

| Property | Type | Description |
| --- | --- | --- |
| eas(optional) | [EASConfig](/versions/latest/sdk/manifests#easconfig) | - |
| expoClient(optional) | [ExpoClientConfig](/versions/latest/sdk/manifests#expoclientconfig) | - |
| expoGo(optional) | [ExpoGoConfig](/versions/latest/sdk/manifests#expogoconfig) | - |

> **Deprecated:** renamed to `ExpoUpdatesManifest`, will be removed in a few versions.

### `NewManifest`

Supported platforms: Android, iOS, tvOS.

Type: [ExpoUpdatesManifest](/versions/latest/sdk/manifests#expoupdatesmanifest)
