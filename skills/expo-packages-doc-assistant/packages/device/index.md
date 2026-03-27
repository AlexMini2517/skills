---
title: Device
description: A universal library provides access to system information about the physical device.
sourceCodeUrl: 'https://github.com/expo/expo/tree/main/packages/expo-device'
packageName: 'expo-device'
iconUrl: '/static/images/packages/expo-device.png'
platforms: ['android', 'ios', 'tvos', 'web', 'expo-go']
---

# Expo Device

A universal library provides access to system information about the physical device.
Android, iOS, tvOS, Web, Included in Expo Go

`expo-device` provides access to system information about the physical device, such as its manufacturer and model.

## Installation

```sh
npx expo install expo-device
```

If you are installing this in an [existing React Native app](/bare/overview), make sure to [install `expo`](/bare/installing-expo-modules) in your project.

## Usage

```jsx
import { Text, View } from 'react-native';
import * as Device from 'expo-device';

export default function App() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>
        {Device.manufacturer}: {Device.modelName}
      </Text>
    </View>
  );
}
```

## API

```js
import * as Device from 'expo-device';
```

## Constants

### `Device.brand`

Supported platforms: Android, iOS.

Type: `string | null`

The device brand. The consumer-visible brand of the product/hardware. On web, this value is always `null`.

Example

```js
Device.brand; // Android: "google", "xiaomi"; iOS: "Apple"; web: null
```

### `Device.designName`

Supported platforms: Android.

Type: `string | null`

The specific configuration or name of the industrial design. It represents the device's name when it was designed during manufacturing into mass production. On Android, it corresponds to [`Build.DEVICE`](https://developer.android.com/reference/android/os/Build#DEVICE). On web and iOS, this value is always `null`.

Example

```js
Device.designName; // Android: "kminilte"; iOS: null; web: null
```

### `Device.deviceName`

Supported platforms: Android, iOS, tvOS, Web.

Type: `string | null`

The human-readable name of the device, which may be set by the device's user. If the device name is unavailable, particularly on web, this value is `null`.

> On iOS 16 and newer, this value will be set to generic "iPhone" until you add the correct entitlement, see [iOS Capabilities page](/build-reference/ios-capabilities) to learn how to add one and check out [Apple documentation](https://developer.apple.com/documentation/uikit/uidevice/1620015-name#discussion) for more details on this change.

Example

```js
Device.deviceName; // "Vivian's iPhone XS"
```

### `Device.deviceType`

Supported platforms: Android, iOS, tvOS, Web.

Type: [DeviceType](#devicetype) | null

The type of the device as a [`DeviceType`](#devicetype) enum value.

On Android, for devices other than TVs, the device type is determined by the screen resolution (screen diagonal size), so the result may not be completely accurate. If the screen diagonal length is between 3" and 6.9", the method returns `DeviceType.PHONE`. For lengths between 7" and 18", the method returns `DeviceType.TABLET`. Otherwise, the method returns `DeviceType.UNKNOWN`.

Example

```js
Device.deviceType; // UNKNOWN, PHONE, TABLET, TV, DESKTOP
```

### `Device.deviceYearClass`

Supported platforms: Android, iOS, tvOS, Web.

Type: `number | null`

The [device year class](https://github.com/facebook/device-year-class) of this device. On web, this value is always `null`.

### `Device.isDevice`

Supported platforms: Android, iOS, tvOS, Web.

Type: `boolean`

`true` if the app is running on a real device and `false` if running in a simulator or emulator. On web, this is always set to `true`.

### `Device.manufacturer`

Supported platforms: Android, iOS, tvOS, Web.

Type: `string | null`

The actual device manufacturer of the product or hardware. This value of this field may be `null` if it cannot be determined.

To view difference between `brand` and `manufacturer` on Android see [official documentation](https://developer.android.com/reference/android/os/Build).

Example

```js
Device.manufacturer; // Android: "Google", "xiaomi"; iOS: "Apple"; web: "Google", null
```

### `Device.modelId`

Supported platforms: iOS.

Type: `any`

The internal model ID of the device. This is useful for programmatically identifying the type of device and is not a human-friendly string. On web and Android, this value is always `null`.

Example

```js
Device.modelId; // iOS: "iPhone7,2"; Android: null; web: null
```

### `Device.modelName`

Supported platforms: Android, iOS, tvOS, Web.

Type: `string | null`

The human-friendly name of the device model. This is the name that people would typically use to refer to the device rather than a programmatic model identifier. This value of this field may be `null` if it cannot be determined.

Example

```js
Device.modelName; // Android: "Pixel 2"; iOS: "iPhone XS Max"; web: "iPhone", null
```

### `Device.osBuildFingerprint`

Supported platforms: Android.

Type: `string | null`

A string that uniquely identifies the build of the currently running system OS. On Android, it follows this template:

-   `$(BRAND)/$(PRODUCT)/$(DEVICE)/$(BOARD):$(VERSION.RELEASE)/$(ID)/$(VERSION.INCREMENTAL):$(TYPE)/\$(TAGS)` On web and iOS, this value is always `null`.

Example

```js
Device.osBuildFingerprint;
// Android: "google/sdk_gphone_x86/generic_x86:9/PSR1.180720.075/5124027:user/release-keys";
// iOS: null; web: null
```

### `Device.osBuildId`

Supported platforms: Android, iOS, tvOS, Web.

Type: `string | null`

The build ID of the OS that more precisely identifies the version of the OS. On Android, this corresponds to `Build.DISPLAY` (not `Build.ID`) and currently is a string as described [here](https://source.android.com/setup/start/build-numbers). On iOS, this corresponds to `kern.osversion` and is the detailed OS version sometimes displayed next to the more human-readable version. On web, this value is always `null`.

Example

```js
Device.osBuildId; // Android: "PSR1.180720.075"; iOS: "16F203"; web: null
```

### `Device.osInternalBuildId`

Supported platforms: Android, iOS, tvOS, Web.

Type: `string | null`

The internal build ID of the OS running on the device. On Android, this corresponds to `Build.ID`. On iOS, this is the same value as [`Device.osBuildId`](#deviceosbuildid). On web, this value is always `null`.

Example

```js
Device.osInternalBuildId; // Android: "MMB29K"; iOS: "16F203"; web: null,
```

### `Device.osName`

Supported platforms: Android, iOS, tvOS, Web.

Type: `string | null`

The name of the OS running on the device.

Example

```js
Device.osName; // Android: "Android" or fingerprint string; iOS: "iOS" or "iPadOS"; web: "iOS", "Android", "Windows"
```

On Android this option maps directly to [`android.os.Build.VERSION.BASE_OS`](https://developer.android.com/reference/android/os/Build.VERSION#BASE_OS) which on some devices is set to "Android" and on others is a build fingerprint.

For example on Xiaomi Poco X3 Pro the `Device.osName` is set to `POCO/vayu_eea/vayu:11/RKQ1.200826.002/V12.5.4.0.RJUEUXM:user/release-keys`

If you want to differentiate between Android and iOS consider using [`Platform.OS`](https://reactnative.dev/docs/platform#os) from `react-native`.

### `Device.osVersion`

Supported platforms: Android, iOS, tvOS, Web.

Type: `string | null`

The human-readable OS version string. Note that the version string may not always contain three numbers separated by dots.

Example

```js
Device.osVersion; // Android: "4.0.3"; iOS: "12.3.1"; web: "11.0", "8.1.0"
```

### `Device.platformApiLevel`

Supported platforms: Android.

Type: `number | null`

The Android SDK version of the software currently running on this hardware device. This value never changes while a device is booted, but it may increase when the hardware manufacturer provides an OS update. See [here](https://developer.android.com/reference/android/os/Build.VERSION_CODES.html) to see all possible version codes and corresponding versions. On iOS and web, this value is always `null`.

Example

```js
Device.platformApiLevel; // Android: 19; iOS: null; web: null
```

### `Device.productName`

Supported platforms: Android.

Type: `string | null`

The device's overall product name chosen by the device implementer containing the development name or code name of the device. Corresponds to [`Build.PRODUCT`](https://developer.android.com/reference/android/os/Build#PRODUCT). On web and iOS, this value is always `null`.

Example

```js
Device.productName; // Android: "kminiltexx"; iOS: null; web: null
```

### `Device.supportedCpuArchitectures`

Supported platforms: Android, iOS, tvOS, Web.

Type: `string[] | null`

A list of supported processor architecture versions. The device expects the binaries it runs to be compiled for one of these architectures. This value is `null` if the supported architectures could not be determined, particularly on web.

Example

```js
Device.supportedCpuArchitectures; // ['arm64 v8', 'Intel x86-64h Haswell', 'arm64-v8a', 'armeabi-v7a", 'armeabi']
```

### `Device.totalMemory`

Supported platforms: Android, iOS, tvOS, Web.

Type: `number | null`

The device's total memory, in bytes. This is the total memory accessible to the kernel, but not necessarily to a single app. This is basically the amount of RAM the device has, not including below-kernel fixed allocations like DMA buffers, RAM for the baseband CPU, etc… On web, this value is always `null`.

Example

```js
Device.totalMemory; // 17179869184
```

## Methods

### `Device.getDeviceTypeAsync()`

Supported platforms: Android, iOS, tvOS, Web.

Checks the type of the device as a [`DeviceType`](#devicetype) enum value.

On Android, for devices other than TVs, the device type is determined by the screen resolution (screen diagonal size), so the result may not be completely accurate. If the screen diagonal length is between 3" and 6.9", the method returns `DeviceType.PHONE`. For lengths between 7" and 18", the method returns `DeviceType.TABLET`. Otherwise, the method returns `DeviceType.UNKNOWN`.

Returns: `Promise<devicetype>`

Returns a promise that resolves to a [`DeviceType`](#devicetype) enum value.

Example

```js
await Device.getDeviceTypeAsync();
// DeviceType.PHONE
```

### `Device.getMaxMemoryAsync()`

Supported platforms: Android.

Returns the maximum amount of memory that the Java VM will attempt to use. If there is no inherent limit then `Number.MAX_SAFE_INTEGER` is returned.

Returns: `Promise<number>`

Returns a promise that resolves to the maximum available memory that the Java VM will use, in bytes.

Example

```js
await Device.getMaxMemoryAsync();
// 402653184
```

### `Device.getPlatformFeaturesAsync()`

Supported platforms: Android.

Gets a list of features that are available on the system. The feature names are platform-specific. See [Android documentation](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures\(\)) to learn more about this implementation.

Returns: `Promise<string[]>`

Returns a promise that resolves to an array of strings, each of which is a platform-specific name of a feature available on the current device. On iOS and web, the promise always resolves to an empty array.

Example

```js
await Device.getPlatformFeaturesAsync();
// [
//   'android.software.adoptable_storage',
//   'android.software.backup',
//   'android.hardware.sensor.accelerometer',
//   'android.hardware.touchscreen',
// ]
```

### `Device.getUptimeAsync()`

Supported platforms: Android, iOS.

Gets the uptime since the last reboot of the device, in milliseconds. Android devices do not count time spent in deep sleep.

Returns: `Promise<number>`

Returns a promise that resolves to a `number` that represents the milliseconds since last reboot.

Example

```js
await Device.getUptimeAsync();
// 4371054
```

### `Device.hasPlatformFeatureAsync(feature)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `feature` | `string` | The platform-specific name of the feature to check for on the device. You can get all available system features with `Device.getSystemFeatureAsync()`. See [Android documentation](https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature\(java.lang.String\)) to view acceptable feature strings. |

  

Tells if the device has a specific system feature.

Returns: `Promise<boolean>`

Returns a promise that resolves to a boolean value indicating whether the device has the specified system feature. On iOS and web, the promise always resolves to `false`.

Example

```js
await Device.hasPlatformFeatureAsync('amazon.hardware.fire_tv');
// true or false
```

### `Device.isRootedExperimentalAsync()`

Supported platforms: Android, iOS, tvOS, Web.

> This method is experimental and is not completely reliable. See description below.

Checks whether the device has been rooted (Android) or jailbroken (iOS). This is not completely reliable because there exist solutions to bypass root-detection on both [iOS](https://www.theiphonewiki.com/wiki/XCon) and [Android](https://tweakerlinks.com/how-to-bypass-apps-root-detection-in-android-device/). Further, many root-detection checks can be bypassed via reverse engineering.

-   On Android, it's implemented in a way to find all possible files paths that contain the `"su"` executable but some devices that are not rooted may also have this executable. Therefore, there's no guarantee that this method will always return correctly.
-   On iOS, [these jailbreak checks](https://www.theiphonewiki.com/wiki/Bypassing_Jailbreak_Detection) are used to detect if a device is rooted/jailbroken. However, since there are closed-sourced solutions such as [xCon](https://www.theiphonewiki.com/wiki/XCon) that aim to hook every known method and function responsible for informing an application of a jailbroken device, this method may not reliably detect devices that have xCon or similar packages installed.
-   On web, this always resolves to `false` even if the device is rooted.

Returns: `Promise<boolean>`

Returns a promise that resolves to a `boolean` that specifies whether this device is rooted.

Example

```js
await Device.isRootedExperimentalAsync();
// true or false
```

### `Device.isSideLoadingEnabledAsync()`

Supported platforms: Android.

**Using this method requires you to [add the `REQUEST_INSTALL_PACKAGES` permission](/versions/latest/config/app#permissions).** Returns whether applications can be installed for this user via the system's [`ACTION_INSTALL_PACKAGE`](https://developer.android.com/reference/android/content/Intent.html#ACTION_INSTALL_PACKAGE) mechanism rather than through the OS's default app store, like Google Play.

Returns: `Promise<boolean>`

Returns a promise that resolves to a `boolean` that represents whether the calling package is allowed to request package installation.

Example

```js
await Device.isSideLoadingEnabledAsync();
// true or false
```

## Enums

### `DeviceType`

Supported platforms: Android, iOS, tvOS, Web.

An enum representing the different types of devices supported by Expo.

#### `UNKNOWN`

`DeviceType.UNKNOWN = 0`

An unrecognized device type.

#### `PHONE`

`DeviceType.PHONE = 1`

Mobile phone handsets, typically with a touch screen and held in one hand.

#### `TABLET`

`DeviceType.TABLET = 2`

Tablet computers, typically with a touch screen that is larger than a usual phone.

#### `DESKTOP`

`DeviceType.DESKTOP = 3`

Desktop or laptop computers, typically with a keyboard and mouse.

#### `TV`

`DeviceType.TV = 4`

Device with TV-based interfaces.

## Error codes

| Code | Description |
| --- | --- |
| ERR_DEVICE_ROOT_DETECTION | Error code thrown for `isRootedExperimentalAsync`. This may be thrown if there's no read access to certain system files. |
