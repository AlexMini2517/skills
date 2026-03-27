---
title: Router Color
description: An Expo Router API for accessing platform-specific native colors.
sourceCodeUrl: 'https://github.com/expo/expo/tree/main/packages/expo-router'
packageName: 'expo-router'
platforms: ['android', 'ios']
---

# Expo Router Color

An Expo Router API for accessing platform-specific native colors.
Android, iOS

The Color API provides access to platform-specific native colors.

> See the [Expo Router](/versions/latest/sdk/router/index) reference for installation and configuration.

## Usage

```tsx
import { Color } from 'expo-router';
import { Text, View, useColorScheme } from 'react-native';

export default function MyComponent() {
  useColorScheme();
  return (
    <View style={{ flex: 1, backgroundColor: Color.android.dynamic.primary }}>
      <Text style={{ color: Color.ios.label }}>Hello</Text>
    </View>
  );
}
```

## API

```js
import { Color } from 'expo-router';
```

## Constants

### `Color.Color`

Supported platforms: Android, iOS.

Type: [ColorType](#colortype)

Color utility to access platform-specific colors easily.

On **Android**, it provides access to:

-   System colors, as a type-safe wrapper over `PlatformColor`. For example, `Color.android.background`.
-   Attribute colors, as a type-safe wrapper over `PlatformColor`. For example, `Color.android.attr.colorPrimary`.
-   [Material Design 3 static colors](https://m3.material.io/styles/color/static/baseline). For example, `Color.android.material.primary`.
-   [Material Design 3 dynamic colors](https://m3.material.io/styles/color/dynamic/user-generated-source). For example, `Color.android.dynamic.primary`.

On **iOS**, it is a type-safe wrapper over `PlatformColor`, providing access to system colors. For example, `Color.ios.label`.

> **Note**: To ensure the colors align with the system theme on Android, make sure they are used within a component that responds to theme changes, such as by using the `useColorScheme` hook from React Native. This is especially important when using React Compiler, which can memoize components.

Example

```tsx
import { Color } from 'expo-router';

Color.ios.label; // Access iOS system color
Color.android.background; // Access Android system color
Color.android.attr.colorPrimary; // Access Android attribute color
Color.android.material.primary; // Access Android Material Design 3 static color
Color.android.dynamic.primary; // Access Android Material Design 3 dynamic color
```

Example

```tsx
import { Color } from 'expo-router';
import { View, Text, useColorScheme } from 'react-native';

export default function MyComponent() {
  useColorScheme(); // Ensure the app responds to system theme changes
  return (
    <View style={{ flex: 1, backgroundColor: Color.android.dynamic.primary }}>
      <Text style={{ color: Color.android.dynamic.onPrimary }}>
        Hello, World!
      </Text>
    </View>
  );
}
```

## Interfaces

### `AndroidBaseColorSDK1`

Supported platforms: Android, iOS.

| Property | Type | Description |
| --- | --- | --- |
| background_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/background_dark") |
| background_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/background_light") |
| black | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/black") |
| darker_gray | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/darker_gray") |
| tab_indicator_text | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/tab_indicator_text") |
| transparent | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/transparent") |
| white | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/white") |
| widget_edittext_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/widget_edittext_dark") |

### `AndroidBaseColorSDK14`

Supported platforms: Android, iOS.

| Property | Type | Description |
| --- | --- | --- |
| holo_blue_bright | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/holo_blue_bright") |
| holo_blue_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/holo_blue_dark") |
| holo_blue_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/holo_blue_light") |
| holo_green_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/holo_green_dark") |
| holo_green_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/holo_green_light") |
| holo_orange_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/holo_orange_dark") |
| holo_orange_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/holo_orange_light") |
| holo_purple | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/holo_purple") |
| holo_red_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/holo_red_dark") |
| holo_red_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/holo_red_light") |

### `AndroidBaseColorSDK31`

Supported platforms: Android, iOS.

| Property | Type | Description |
| --- | --- | --- |
| system_accent1_0 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent1_0") |
| system_accent1_10 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent1_10") |
| system_accent1_100 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent1_100") |
| system_accent1_1000 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent1_1000") |
| system_accent1_200 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent1_200") |
| system_accent1_300 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent1_300") |
| system_accent1_400 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent1_400") |
| system_accent1_50 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent1_50") |
| system_accent1_500 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent1_500") |
| system_accent1_600 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent1_600") |
| system_accent1_700 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent1_700") |
| system_accent1_800 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent1_800") |
| system_accent1_900 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent1_900") |
| system_accent2_0 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent2_0") |
| system_accent2_10 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent2_10") |
| system_accent2_100 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent2_100") |
| system_accent2_1000 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent2_1000") |
| system_accent2_200 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent2_200") |
| system_accent2_300 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent2_300") |
| system_accent2_400 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent2_400") |
| system_accent2_50 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent2_50") |
| system_accent2_500 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent2_500") |
| system_accent2_600 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent2_600") |
| system_accent2_700 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent2_700") |
| system_accent2_800 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent2_800") |
| system_accent2_900 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent2_900") |
| system_accent3_0 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent3_0") |
| system_accent3_10 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent3_10") |
| system_accent3_100 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent3_100") |
| system_accent3_1000 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent3_1000") |
| system_accent3_200 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent3_200") |
| system_accent3_300 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent3_300") |
| system_accent3_400 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent3_400") |
| system_accent3_50 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent3_50") |
| system_accent3_500 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent3_500") |
| system_accent3_600 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent3_600") |
| system_accent3_700 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent3_700") |
| system_accent3_800 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent3_800") |
| system_accent3_900 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_accent3_900") |
| system_neutral1_0 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral1_0") |
| system_neutral1_10 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral1_10") |
| system_neutral1_100 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral1_100") |
| system_neutral1_1000 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral1_1000") |
| system_neutral1_200 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral1_200") |
| system_neutral1_300 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral1_300") |
| system_neutral1_400 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral1_400") |
| system_neutral1_50 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral1_50") |
| system_neutral1_500 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral1_500") |
| system_neutral1_600 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral1_600") |
| system_neutral1_700 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral1_700") |
| system_neutral1_800 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral1_800") |
| system_neutral1_900 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral1_900") |
| system_neutral2_0 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral2_0") |
| system_neutral2_10 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral2_10") |
| system_neutral2_100 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral2_100") |
| system_neutral2_1000 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral2_1000") |
| system_neutral2_200 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral2_200") |
| system_neutral2_300 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral2_300") |
| system_neutral2_400 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral2_400") |
| system_neutral2_50 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral2_50") |
| system_neutral2_500 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral2_500") |
| system_neutral2_600 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral2_600") |
| system_neutral2_700 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral2_700") |
| system_neutral2_800 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral2_800") |
| system_neutral2_900 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_neutral2_900") |

### `AndroidBaseColorSDK34`

Supported platforms: Android, iOS.

| Property | Type | Description |
| --- | --- | --- |
| system_background_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_background_dark") |
| system_background_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_background_light") |
| system_control_activated_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_control_activated_dark") |
| system_control_activated_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_control_activated_light") |
| system_control_highlight_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_control_highlight_dark") |
| system_control_highlight_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_control_highlight_light") |
| system_control_normal_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_control_normal_dark") |
| system_control_normal_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_control_normal_light") |
| system_error_container_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_container_dark") |
| system_error_container_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_container_light") |
| system_error_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_dark") |
| system_error_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_light") |
| system_on_background_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_background_dark") |
| system_on_background_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_background_light") |
| system_on_error_container_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_error_container_dark") |
| system_on_error_container_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_error_container_light") |
| system_on_error_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_error_dark") |
| system_on_error_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_error_light") |
| system_on_primary_container_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_primary_container_dark") |
| system_on_primary_container_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_primary_container_light") |
| system_on_primary_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_primary_dark") |
| system_on_primary_fixed | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_primary_fixed") |
| system_on_primary_fixed_variant | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_primary_fixed_variant") |
| system_on_primary_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_primary_light") |
| system_on_secondary_container_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_secondary_container_dark") |
| system_on_secondary_container_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_secondary_container_light") |
| system_on_secondary_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_secondary_dark") |
| system_on_secondary_fixed | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_secondary_fixed") |
| system_on_secondary_fixed_variant | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_secondary_fixed_variant") |
| system_on_secondary_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_secondary_light") |
| system_on_surface_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_surface_dark") |
| system_on_surface_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_surface_light") |
| system_on_surface_variant_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_surface_variant_dark") |
| system_on_surface_variant_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_surface_variant_light") |
| system_on_tertiary_container_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_tertiary_container_dark") |
| system_on_tertiary_container_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_tertiary_container_light") |
| system_on_tertiary_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_tertiary_dark") |
| system_on_tertiary_fixed | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_tertiary_fixed") |
| system_on_tertiary_fixed_variant | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_tertiary_fixed_variant") |
| system_on_tertiary_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_tertiary_light") |
| system_outline_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_outline_dark") |
| system_outline_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_outline_light") |
| system_outline_variant_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_outline_variant_dark") |
| system_outline_variant_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_outline_variant_light") |
| system_palette_key_color_neutral_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_palette_key_color_neutral_dark") |
| system_palette_key_color_neutral_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_palette_key_color_neutral_light") |
| system_palette_key_color_neutral_variant_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_palette_key_color_neutral_variant_dark") |
| system_palette_key_color_neutral_variant_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_palette_key_color_neutral_variant_light") |
| system_palette_key_color_primary_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_palette_key_color_primary_dark") |
| system_palette_key_color_primary_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_palette_key_color_primary_light") |
| system_palette_key_color_secondary_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_palette_key_color_secondary_dark") |
| system_palette_key_color_secondary_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_palette_key_color_secondary_light") |
| system_palette_key_color_tertiary_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_palette_key_color_tertiary_dark") |
| system_palette_key_color_tertiary_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_palette_key_color_tertiary_light") |
| system_primary_container_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_primary_container_dark") |
| system_primary_container_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_primary_container_light") |
| system_primary_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_primary_dark") |
| system_primary_fixed | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_primary_fixed") |
| system_primary_fixed_dim | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_primary_fixed_dim") |
| system_primary_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_primary_light") |
| system_secondary_container_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_secondary_container_dark") |
| system_secondary_container_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_secondary_container_light") |
| system_secondary_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_secondary_dark") |
| system_secondary_fixed | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_secondary_fixed") |
| system_secondary_fixed_dim | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_secondary_fixed_dim") |
| system_secondary_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_secondary_light") |
| system_surface_bright_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_bright_dark") |
| system_surface_bright_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_bright_light") |
| system_surface_container_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_container_dark") |
| system_surface_container_high_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_container_high_dark") |
| system_surface_container_high_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_container_high_light") |
| system_surface_container_highest_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_container_highest_dark") |
| system_surface_container_highest_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_container_highest_light") |
| system_surface_container_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_container_light") |
| system_surface_container_low_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_container_low_dark") |
| system_surface_container_low_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_container_low_light") |
| system_surface_container_lowest_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_container_lowest_dark") |
| system_surface_container_lowest_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_container_lowest_light") |
| system_surface_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_dark") |
| system_surface_dim_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_dim_dark") |
| system_surface_dim_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_dim_light") |
| system_surface_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_light") |
| system_surface_variant_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_variant_dark") |
| system_surface_variant_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_variant_light") |
| system_tertiary_container_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_tertiary_container_dark") |
| system_tertiary_container_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_tertiary_container_light") |
| system_tertiary_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_tertiary_dark") |
| system_tertiary_fixed | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_tertiary_fixed") |
| system_tertiary_fixed_dim | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_tertiary_fixed_dim") |
| system_tertiary_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_tertiary_light") |
| system_text_hint_inverse_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_text_hint_inverse_dark") |
| system_text_hint_inverse_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_text_hint_inverse_light") |
| system_text_primary_inverse_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_text_primary_inverse_dark") |
| system_text_primary_inverse_disable_only_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_text_primary_inverse_disable_only_dark") |
| system_text_primary_inverse_disable_only_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_text_primary_inverse_disable_only_light") |
| system_text_primary_inverse_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_text_primary_inverse_light") |
| system_text_secondary_and_tertiary_inverse_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_text_secondary_and_tertiary_inverse_dark") |
| system_text_secondary_and_tertiary_inverse_disabled_dark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_text_secondary_and_tertiary_inverse_disabled_dark") |
| system_text_secondary_and_tertiary_inverse_disabled_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_text_secondary_and_tertiary_inverse_disabled_light") |
| system_text_secondary_and_tertiary_inverse_light | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_text_secondary_and_tertiary_inverse_light") |

### `AndroidBaseColorSDK35`

Supported platforms: Android, iOS.

| Property | Type | Description |
| --- | --- | --- |
| system_error_0 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_0") |
| system_error_10 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_10") |
| system_error_100 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_100") |
| system_error_1000 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_1000") |
| system_error_200 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_200") |
| system_error_300 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_300") |
| system_error_400 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_400") |
| system_error_50 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_50") |
| system_error_500 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_500") |
| system_error_600 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_600") |
| system_error_700 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_700") |
| system_error_800 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_800") |
| system_error_900 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_error_900") |
| system_on_surface_disabled | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_on_surface_disabled") |
| system_outline_disabled | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_outline_disabled") |
| system_surface_disabled | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("@android:color/system_surface_disabled") |

### `AndroidColorAttrSDK1`

Supported platforms: Android, iOS.

| Property | Type | Description |
| --- | --- | --- |
| colorBackground | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorBackground") |
| colorForeground | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorForeground") |
| colorForegroundInverse | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorForegroundInverse") |

### `AndroidColorAttrSDK14`

Supported platforms: Android, iOS.

| Property | Type | Description |
| --- | --- | --- |
| colorActivatedHighlight | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorActivatedHighlight") |
| colorFocusedHighlight | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorFocusedHighlight") |
| colorLongPressedHighlight | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorLongPressedHighlight") |
| colorMultiSelectHighlight | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorMultiSelectHighlight") |
| colorPressedHighlight | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorPressedHighlight") |

### `AndroidColorAttrSDK21`

Supported platforms: Android, iOS.

| Property | Type | Description |
| --- | --- | --- |
| colorAccent | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorAccent") |
| colorButtonNormal | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorButtonNormal") |
| colorControlActivated | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorControlActivated") |
| colorControlHighlight | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorControlHighlight") |
| colorControlNormal | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorControlNormal") |
| colorEdgeEffect | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorEdgeEffect") |
| colorPrimary | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorPrimary") |
| colorPrimaryDark | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorPrimaryDark") |

### `AndroidColorAttrSDK23`

Supported platforms: Android, iOS.

| Property | Type | Description |
| --- | --- | --- |
| colorBackgroundFloating | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorBackgroundFloating") |

### `AndroidColorAttrSDK25`

Supported platforms: Android, iOS.

| Property | Type | Description |
| --- | --- | --- |
| colorSecondary | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorSecondary") |

### `AndroidColorAttrSDK26`

Supported platforms: Android, iOS.

| Property | Type | Description |
| --- | --- | --- |
| colorError | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorError") |
| colorMode | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorMode") |

### `AndroidColorAttrSDK5`

Supported platforms: Android, iOS.

| Property | Type | Description |
| --- | --- | --- |
| colorBackgroundCacheHint | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("?attr/colorBackgroundCacheHint") |

### `AndroidDeprecatedColor`

Supported platforms: Android, iOS.

| Property | Type | Description |
| --- | --- | --- |
| primary_text_dark | [ColorValue](https://reactnative.dev/docs/colors) | Deprecated: Deprecated in Android SDK 28 . PlatformColor("@android:color/primary_text_dark") |
| primary_text_dark_nodisable | [ColorValue](https://reactnative.dev/docs/colors) | Deprecated: Deprecated in Android SDK 28 . PlatformColor("@android:color/primary_text_dark_nodisable") |
| primary_text_light | [ColorValue](https://reactnative.dev/docs/colors) | Deprecated: Deprecated in Android SDK 28 . PlatformColor("@android:color/primary_text_light") |
| primary_text_light_nodisable | [ColorValue](https://reactnative.dev/docs/colors) | Deprecated: Deprecated in Android SDK 28 . PlatformColor("@android:color/primary_text_light_nodisable") |
| secondary_text_dark | [ColorValue](https://reactnative.dev/docs/colors) | Deprecated: Deprecated in Android SDK 28 . PlatformColor("@android:color/secondary_text_dark") |
| secondary_text_dark_nodisable | [ColorValue](https://reactnative.dev/docs/colors) | Deprecated: Deprecated in Android SDK 28 . PlatformColor("@android:color/secondary_text_dark_nodisable") |
| secondary_text_light | [ColorValue](https://reactnative.dev/docs/colors) | Deprecated: Deprecated in Android SDK 28 . PlatformColor("@android:color/secondary_text_light") |
| secondary_text_light_nodisable | [ColorValue](https://reactnative.dev/docs/colors) | Deprecated: Deprecated in Android SDK 28 . PlatformColor("@android:color/secondary_text_light_nodisable") |
| tertiary_text_dark | [ColorValue](https://reactnative.dev/docs/colors) | Deprecated: Deprecated in Android SDK 28 . PlatformColor("@android:color/tertiary_text_dark") |
| tertiary_text_light | [ColorValue](https://reactnative.dev/docs/colors) | Deprecated: Deprecated in Android SDK 28 . PlatformColor("@android:color/tertiary_text_light") |

### `AndroidDynamicMaterialColorType`

Supported platforms: Android, iOS.

[Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source)

You can find out more about color roles in [official Material Design 3 documentation](https://m3.material.io/styles/color/roles).

You can read about the difference between dynamic and static colors in [official Material Design 3 documentation](https://m3.material.io/styles/color/choosing-a-scheme).

For a detailed definition of each color role, see [material components color documentation](https://github.com/material-components/material-components-android/blob/master/docs/theming/Color.md).

| Property | Type | Description |
| --- | --- | --- |
| background | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. |
| error | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Error color role](https://m3.material.io/styles/color/roles#47a25970-8a80-43be-8307-c12e0f7a2b43) |
| errorContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Error color role](https://m3.material.io/styles/color/roles#47a25970-8a80-43be-8307-c12e0f7a2b43) |
| onBackground | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. |
| onError | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Error color role](https://m3.material.io/styles/color/roles#47a25970-8a80-43be-8307-c12e0f7a2b43) |
| onErrorContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Error color role](https://m3.material.io/styles/color/roles#47a25970-8a80-43be-8307-c12e0f7a2b43) |
| onPrimary | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| onPrimaryContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| onPrimaryFixed | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| onPrimaryFixedVariant | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| onSecondary | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| onSecondaryContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| onSecondaryFixed | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| onSecondaryFixedVariant | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| onSurface | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| onSurfaceInverse | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) . [Read more about Inverse colors](https://m3.material.io/styles/color/roles#7fc6b47e-db22-4e98-8359-7649a099e4a1) |
| onSurfaceVariant | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| onTertiary | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| onTertiaryContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| onTertiaryFixed | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| onTertiaryFixedVariant | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| outline | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Outline color role](https://m3.material.io/styles/color/roles#e7d72e44-72e2-4ce9-a18d-df07b1433d18) |
| outlineVariant | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Outline color role](https://m3.material.io/styles/color/roles#e7d72e44-72e2-4ce9-a18d-df07b1433d18) |
| primary | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| primaryContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| primaryFixed | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| primaryFixedDim | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| primaryInverse | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) . [Read more about Inverse colors](https://m3.material.io/styles/color/roles#7fc6b47e-db22-4e98-8359-7649a099e4a1) |
| secondary | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| secondaryContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| secondaryFixed | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| secondaryFixedDim | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| surface | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceBright | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceContainerHigh | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceContainerHighest | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceContainerLow | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceContainerLowest | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceDim | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceInverse | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) . [Read more about Inverse colors](https://m3.material.io/styles/color/roles#7fc6b47e-db22-4e98-8359-7649a099e4a1) |
| surfaceVariant | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| tertiary | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| tertiaryContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| tertiaryFixed | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| tertiaryFixedDim | [ColorValue](https://reactnative.dev/docs/colors) | [Android Dynamic Material Colors](https://m3.material.io/styles/color/dynamic/user-generated-source) . This color adapts based on the user's wallpaper and theme settings. [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |

### `AndroidStaticMaterialColorType`

Supported platforms: Android, iOS.

[Android Static Material Colors](https://m3.material.io/styles/color/static/baseline)

You can find out more about color roles in [official Material Design 3 documentation](https://m3.material.io/styles/color/roles).

You can read about the difference between dynamic and static colors in [official Material Design 3 documentation](https://m3.material.io/styles/color/choosing-a-scheme).

For a detailed definition of each color role, see [material components color documentation](https://github.com/material-components/material-components-android/blob/master/docs/theming/Color.md).

| Property | Type | Description |
| --- | --- | --- |
| background | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) |
| error | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Error color role](https://m3.material.io/styles/color/roles#47a25970-8a80-43be-8307-c12e0f7a2b43) |
| errorContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Error color role](https://m3.material.io/styles/color/roles#47a25970-8a80-43be-8307-c12e0f7a2b43) |
| onBackground | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) |
| onError | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Error color role](https://m3.material.io/styles/color/roles#47a25970-8a80-43be-8307-c12e0f7a2b43) |
| onErrorContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Error color role](https://m3.material.io/styles/color/roles#47a25970-8a80-43be-8307-c12e0f7a2b43) |
| onPrimary | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| onPrimaryContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| onPrimaryFixed | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| onPrimaryFixedVariant | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| onSecondary | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| onSecondaryContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| onSecondaryFixed | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| onSecondaryFixedVariant | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| onSurface | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| onSurfaceInverse | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) . [Read more about Inverse colors](https://m3.material.io/styles/color/roles#7fc6b47e-db22-4e98-8359-7649a099e4a1) |
| onSurfaceVariant | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| onTertiary | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| onTertiaryContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| onTertiaryFixed | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| onTertiaryFixedVariant | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| outline | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Outline color role](https://m3.material.io/styles/color/roles#e7d72e44-72e2-4ce9-a18d-df07b1433d18) |
| outlineVariant | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Outline color role](https://m3.material.io/styles/color/roles#e7d72e44-72e2-4ce9-a18d-df07b1433d18) |
| primary | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| primaryContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| primaryFixed | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| primaryFixedDim | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) |
| primaryInverse | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Primary color role](https://m3.material.io/styles/color/roles#41f55188-5c63-4107-ac41-822ebca8ae1b) . [Read more about Inverse colors](https://m3.material.io/styles/color/roles#7fc6b47e-db22-4e98-8359-7649a099e4a1) |
| secondary | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| secondaryContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| secondaryFixed | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| secondaryFixedDim | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Secondary color role](https://m3.material.io/styles/color/roles#290bcc49-b728-414c-8cc5-04336c1c799c) |
| surface | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceBright | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceContainerHigh | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceContainerHighest | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceContainerLow | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceContainerLowest | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceDim | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| surfaceInverse | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) . [Read more about Inverse colors](https://m3.material.io/styles/color/roles#7fc6b47e-db22-4e98-8359-7649a099e4a1) |
| surfaceVariant | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Surface color role](https://m3.material.io/styles/color/roles#89f972b1-e372-494c-aabc-69aea34ed591) |
| tertiary | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| tertiaryContainer | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| tertiaryFixed | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |
| tertiaryFixedDim | [ColorValue](https://reactnative.dev/docs/colors) | [Android Static Material Color](https://m3.material.io/styles/color/static/baseline) . [Read more about Tertiary color role](https://m3.material.io/styles/color/roles#727a0bf8-c95f-4f83-bc43-290d20f24e8e) |

### `ColorType`

Supported platforms: Android, iOS.

| Property | Type | Description |
| --- | --- | --- |
| android | [AndroidBaseColorSDK1](#androidbasecolorsdk1) & [AndroidBaseColorSDK14](#androidbasecolorsdk14) & [AndroidBaseColorSDK31](#androidbasecolorsdk31) & [AndroidBaseColorSDK34](#androidbasecolorsdk34) & [AndroidBaseColorSDK35](#androidbasecolorsdk35) & [AndroidDeprecatedColor](#androiddeprecatedcolor) & undefined & { attr: [AndroidBaseColorAttr](#androidbasecolorattr), dynamic: [AndroidDynamicMaterialColor](#androiddynamicmaterialcolor), material: [AndroidMaterialColor](#androidmaterialcolor) } | - |
| ios | [IOSBaseColor](#iosbasecolor) & undefined | - |

### `IOSBaseColor`

Supported platforms: Android, iOS.

| Property | Type | Description |
| --- | --- | --- |
| darkText | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("darkText") |
| label | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("label") |
| lightText | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("lightText") |
| link | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("link") |
| opaqueSeparator | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("opaqueSeparator") |
| placeholderText | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("placeholderText") |
| quaternaryLabel | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("quaternaryLabel") |
| quaternarySystemFill | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("quaternarySystemFill") |
| secondaryLabel | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("secondaryLabel") |
| secondarySystemBackground | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("secondarySystemBackground") |
| secondarySystemFill | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("secondarySystemFill") |
| secondarySystemGroupedBackground | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("secondarySystemGroupedBackground") |
| separator | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("separator") |
| systemBackground | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemBackground") |
| systemBlue | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemBlue") |
| systemBrown | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemBrown") |
| systemCyan | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemCyan") |
| systemFill | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemFill") |
| systemGray | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemGray") |
| systemGray2 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemGray2") |
| systemGray3 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemGray3") |
| systemGray4 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemGray4") |
| systemGray5 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemGray5") |
| systemGray6 | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemGray6") |
| systemGreen | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemGreen") |
| systemGroupedBackground | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemGroupedBackground") |
| systemIndigo | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemIndigo") |
| systemMint | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemMint") |
| systemOrange | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemOrange") |
| systemPink | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemPink") |
| systemPurple | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemPurple") |
| systemRed | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemRed") |
| systemTeal | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemTeal") |
| systemYellow | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("systemYellow") |
| tertiaryLabel | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("tertiaryLabel") |
| tertiarySystemBackground | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("tertiarySystemBackground") |
| tertiarySystemFill | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("tertiarySystemFill") |
| tertiarySystemGroupedBackground | [ColorValue](https://reactnative.dev/docs/colors) | PlatformColor("tertiarySystemGroupedBackground") |

## Types

### `AndroidBaseColor`

Supported platforms: Android, iOS.

Type: [AndroidBaseColorSDK1](#androidbasecolorsdk1) [AndroidBaseColorSDK14](#androidbasecolorsdk14) [AndroidBaseColorSDK31](#androidbasecolorsdk31) [AndroidBaseColorSDK34](#androidbasecolorsdk34) [AndroidBaseColorSDK35](#androidbasecolorsdk35) [AndroidDeprecatedColor](#androiddeprecatedcolor) extended by:

| Property | Type | Description |
| --- | --- | --- |
| key[(index signature)](https://www.typescriptlang.org/docs/handbook/2/objects.html#index-signatures) | [ColorValue](https://reactnative.dev/docs/colors) | - |

### `AndroidBaseColorAttr`

Supported platforms: Android, iOS.

Type: [AndroidColorAttrSDK1](#androidcolorattrsdk1) [AndroidColorAttrSDK5](#androidcolorattrsdk5) [AndroidColorAttrSDK14](#androidcolorattrsdk14) [AndroidColorAttrSDK21](#androidcolorattrsdk21) [AndroidColorAttrSDK23](#androidcolorattrsdk23) [AndroidColorAttrSDK25](#androidcolorattrsdk25) [AndroidColorAttrSDK26](#androidcolorattrsdk26) extended by:

| Property | Type | Description |
| --- | --- | --- |
| key[(index signature)](https://www.typescriptlang.org/docs/handbook/2/objects.html#index-signatures) | [ColorValue](https://reactnative.dev/docs/colors) | - |

### `AndroidDynamicMaterialColor`

Supported platforms: Android, iOS.

Type: [AndroidDynamicMaterialColorType](#androiddynamicmaterialcolortype) extended by:

| Property | Type | Description |
| --- | --- | --- |
| key[(index signature)](https://www.typescriptlang.org/docs/handbook/2/objects.html#index-signatures) | [ColorValue](https://reactnative.dev/docs/colors) | - |

### `AndroidMaterialColor`

Supported platforms: Android, iOS.

Type: [AndroidStaticMaterialColorType](#androidstaticmaterialcolortype) extended by:

| Property | Type | Description |
| --- | --- | --- |
| key[(index signature)](https://www.typescriptlang.org/docs/handbook/2/objects.html#index-signatures) | [ColorValue](https://reactnative.dev/docs/colors) | - |
