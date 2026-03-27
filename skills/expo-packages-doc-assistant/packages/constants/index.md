---
title: Constants
description: An API that provides system information that remains constant throughout the lifetime of your app's installation.
sourceCodeUrl: 'https://github.com/expo/expo/tree/main/packages/expo-constants'
packageName: 'expo-constants'
platforms: ['android', 'ios', 'tvos', 'web', 'expo-go']
---

# Expo Constants

An API that provides system information that remains constant throughout the lifetime of your app's installation.
Android, iOS, tvOS, Web, Included in Expo Go

`expo-constants` provides system information that remains constant throughout the lifetime of your app's installation.

## Installation

```sh
npx expo install expo-constants
```

If you are installing this in an [existing React Native app](/bare/overview), make sure to [install `expo`](/bare/installing-expo-modules) in your project.

## API

```js
import Constants from 'expo-constants';
```

## Types

### `AndroidManifest`

Supported platforms: Android.

Type: `Record<string, any>` extended by:

| Property | Type | Description |
| --- | --- | --- |
| versionCode | `number` | Deprecated: Use expo-application's Application.nativeBuildVersion. . The version code set by `android.versionCode` in app.json. The value is set to `null` in case you run your app in Expo Go. |

### `ClientScopingConfig`

Supported platforms: Android, iOS, tvOS, Web.

Type: [ClientScopingConfigForReExport](/versions/latest/sdk/manifests#clientscopingconfigforreexport)

### `EASConfig`

Supported platforms: Android, iOS, tvOS, Web.

Type: [ManifestsEASConfig](/versions/latest/sdk/manifests#manifestseasconfig)

### `ExpoGoConfig`

Supported platforms: Android, iOS, tvOS, Web.

Type: [ManifestsExpoGoConfig](/versions/latest/sdk/manifests#manifestsexpogoconfig)

### `ExpoGoPackagerOpts`

Supported platforms: Android, iOS, tvOS, Web.

Type: [ExpoGoPackagerOptsForReExport](/versions/latest/sdk/manifests#expogopackageroptsforreexport)

### `IOSManifest`

Supported platforms: iOS.

Type: `Record<string, any>` extended by:

| Property | Type | Description |
| --- | --- | --- |
| buildNumber | `string | null` | The build number specified in the embedded **Info.plist** value for `CFBundleVersion` in this app. In a standalone app, you can set this with the `ios.buildNumber` value in **app.json**. This may differ from the value in `Constants.expoConfig.ios.buildNumber` because the manifest can be updated, whereas this value will never change for a given native binary. The value is set to `null` in case you run your app in Expo Go. |
| model | `string | null` | Deprecated: Moved to expo-device as Device.modelName. . The human-readable model name of this device. For example, `"iPhone 7 Plus"` if it can be determined, otherwise will be `null`. |
| platform | `string` | Deprecated: Use expo-device's Device.modelId. . The Apple internal model identifier for this device. . Example. `iPhone1,1` |
| systemVersion | `string` | Deprecated: Use expo-device's Device.osVersion. . The version of iOS running on this device. . Example. `10.3` |
| userInterfaceIdiom | [UserInterfaceIdiom](#userinterfaceidiom) | Deprecated: Use expo-device's Device.getDeviceTypeAsync(). . The user interface idiom of the current device, such as whether the app is running on an iPhone, iPad, Mac or Apple TV. |

### `Manifest`

Supported platforms: Android, iOS, tvOS, Web.

Type: [ExpoUpdatesManifest](/versions/latest/sdk/manifests#expoupdatesmanifest)

### `ManifestAsset`

Supported platforms: Android, iOS, tvOS, Web.

Type: [ManifestAssetForReExport](/versions/latest/sdk/manifests#manifestassetforreexport)

### `ManifestExtra`

Supported platforms: Android, iOS, tvOS, Web.

Type: [ManifestExtraForReExport](/versions/latest/sdk/manifests#manifestextraforreexport)

### `NativeConstants`

Supported platforms: Android, iOS, tvOS, Web.

Type: `Record<string, any>` extended by:

| Property | Type | Description |
| --- | --- | --- |
| appOwnership | [AppOwnership](#appownership) | null | Deprecated: Use Constants.executionEnvironment instead. . Returns `expo` when running in Expo Go, otherwise `null`. |
| debugMode | `boolean` | Returns `true` when the app is running in debug mode (`__DEV__`). Otherwise, returns `false`. |
| deviceName(optional) | `string` | A human-readable name for the device type. |
| deviceYearClass | `number | null` | Deprecated: Moved to expo-device as Device.deviceYearClass. . The [device year class](https://github.com/facebook/device-year-class) of this device. |
| easConfig | [ManifestsEASConfig](/versions/latest/sdk/manifests#manifestseasconfig) | null | The standard EAS config object populated when using EAS. |
| executionEnvironment | [ExecutionEnvironment](#executionenvironment) | Returns the current execution environment. |
| experienceUrl | `string` | - |
| expoConfig | [ExpoConfig](https://github.com/expo/expo/blob/main/packages/%40expo/config-types/src/ExpoConfig.ts) & { hostUri: string } | null | The standard Expo config object defined in **app.json** and **app.config.js** files. For both classic and modern manifests, whether they are embedded or remote. |
| expoGoConfig | [ManifestsExpoGoConfig](/versions/latest/sdk/manifests#manifestsexpogoconfig) | null | The standard Expo Go config object populated when running in Expo Go. |
| expoRuntimeVersion | `string | null` | Nullable only on the web. |
| expoVersion | `string | null` | The version string of the Expo Go app currently running. Returns `null` in bare workflow and web. |
| getWebViewUserAgentAsync | () => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<string | null\> | Gets the user agent string which would be included in requests sent by a web view running on this device. This is probably not the same user agent you might be providing in your JS `fetch` requests. |
| intentUri(optional) | `string` | - |
| isDetached(optional) | `boolean` | - |
| isHeadless | `boolean` | Returns `true` if the app is running in headless mode. Otherwise, returns `false`. |
| linkingUri | `string` | - |
| manifest2 | [ExpoUpdatesManifest](/versions/latest/sdk/manifests#expoupdatesmanifest) | null | Manifest for Expo apps using modern Expo Updates from a remote source, such as apps that use EAS Update. `Constants.expoConfig` should be used for accessing the Expo config object. |
| platform(optional) | [PlatformManifest](#platformmanifest) | Returns the specific platform manifest object. Note: This is distinct from the manifest and manifest2. |
| sessionId | `string` | A string that is unique to the current session of your app. It is different across apps and across multiple launches of the same app. |
| statusBarHeight | `number` | The default status bar height for the device. Does not factor in changes when location tracking is in use or a phone call is active. |
| systemFonts | `string[]` | A list of the system font names available on the current device. |
| systemVersion(optional) | `number` | - |

### `PlatformManifest`

Supported platforms: Android, iOS, tvOS, Web.

Type: `Record<string, any>` extended by:

| Property | Type | Description |
| --- | --- | --- |
| android(optional) | [AndroidManifest](#androidmanifest) | - |
| detach(optional) | `{ scheme: string }` | - |
| developer(optional) | `string` | - |
| hostUri(optional) | `string` | - |
| ios(optional) | [IOSManifest](#iosmanifest) | - |
| scheme(optional) | `string` | - |
| web(optional) | [WebManifest](#webmanifest) | - |

### `WebManifest`

Supported platforms: Web.

Type: `Record<string, any>`

## Enums

### `AppOwnership`

Supported platforms: Android, iOS, tvOS, Web.

> **Deprecated:** Use [`Constants.executionEnvironment`](#executionenvironment) instead.

#### `Expo`

`AppOwnership.Expo = "expo"`

The experience is running inside the Expo Go app.

### `ExecutionEnvironment`

Supported platforms: Android, iOS, tvOS, Web.

Identifies where the app's JavaScript bundle is currently running.

#### `Bare`

`ExecutionEnvironment.Bare = "bare"`

A project that includes native project directories that you maintain directly in your [existing (bare) React Native app](https://docs.expo.dev/bare/overview/).

#### `Standalone`

`ExecutionEnvironment.Standalone = "standalone"`

Production/release build created with or without EAS Build.

#### `StoreClient`

`ExecutionEnvironment.StoreClient = "storeClient"`

Expo Go or a development build built with `expo-dev-client`.

### `UserInterfaceIdiom`

Supported platforms: Android, iOS, tvOS, Web.

Current supported values are `handset`, `tablet`, `desktop` and `tv`. CarPlay will show up as `unsupported`.

#### `Desktop`

`UserInterfaceIdiom.Desktop = "desktop"`

#### `Handset`

`UserInterfaceIdiom.Handset = "handset"`

#### `Tablet`

`UserInterfaceIdiom.Tablet = "tablet"`

#### `TV`

`UserInterfaceIdiom.TV = "tv"`

#### `Unsupported`

`UserInterfaceIdiom.Unsupported = "unsupported"`
