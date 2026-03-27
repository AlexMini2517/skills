---
title: NavigationBar
description: A library that provides access to various interactions with the native navigation bar on Android.
sourceCodeUrl: 'https://github.com/expo/expo/tree/main/packages/expo-navigation-bar'
packageName: 'expo-navigation-bar'
platforms: ['android', 'expo-go']
---

# Expo NavigationBar

A library that provides access to various interactions with the native navigation bar on Android.
Android, Included in Expo Go

`expo-navigation-bar` enables you to modify and observe the native navigation bar on Android devices. Due to some Android platform restrictions, parts of this API overlap with the `expo-status-bar` API.

The APIs in this package have no impact when "Gesture Navigation" is enabled on the Android device. There is currently no native Android API to detect if "Gesture Navigation" is enabled or not.

## Installation

```sh
npx expo install expo-navigation-bar
```

If you are installing this in an [existing React Native app](/bare/overview), make sure to [install `expo`](/bare/installing-expo-modules) in your project.

## Configuration in app config

You can configure `expo-navigation-bar` using its built-in [config plugin](/config-plugins/introduction) if you use config plugins in your project ([Continuous Native Generation (CNG)](/workflow/continuous-native-generation)). The plugin allows you to configure various properties that cannot be set at runtime and require building a new app binary to take effect. If your app does **not** use CNG, then you'll need to manually configure the library.

### Example app.json with config plugin

```json
{
  "expo": {
    "plugins": [
      [
        "expo-navigation-bar",
        {
          "enforceContrast": true,
          "barStyle": "light",
          "visibility": "visible"
        }
      ]
    ]
  }
}
```

### Configurable properties

| Name | Default | Description |
| --- | --- | --- |
| `enforceContrast` | `true` | Determines whether the operating system should keep the navigation bar translucent to provide contrast between the navigation buttons and app content. |
| `barStyle` | `undefined` | Controls whether Android renders light or dark navigation bar buttons. Accepts `light` and `dark` as values. |
| `visibility` | `undefined` | Determines whether the navigation bar starts visible or hidden. Accepts `visible` to show the bar immediately and `hidden` to hide it until the user reveals it with a system gesture. |

Are you using this library in an existing React Native app?

If you're not using Continuous Native Generation ([CNG](/workflow/continuous-native-generation)) or you're using a native **android** project manually, then you need to add the following configuration to your native project:

-   To apply `visibility` to the navigation bar, add `expo_navigation_bar_visibility` to **android/app/src/main/res/values/strings.xml**:
    
    ```xml
    <resources>
      <!-- ... -->
      <string name="expo_navigation_bar_visibility" translatable="false">visible</string>
    </resources>
    ```

## API

```js
import * as NavigationBar from 'expo-navigation-bar';
```

## Hooks

### `useVisibility()`

Supported platforms: Android.

React hook that statefully updates with the visibility of the system navigation bar.

Returns: `NavigationBarVisibility | null`

Visibility of the navigation bar, `null` during async initialization.

Example

```ts
function App() {
  const visibility = NavigationBar.useVisibility()
  // React Component...
}
```

## Methods

> **Deprecated:** Due to Android edge-to-edge enforcement, getting the navigation bar background color is deprecated and always returns `#00000000` (transparent). This will be removed in a future release.

### `NavigationBar.getBackgroundColorAsync()`

Supported platforms: Android.

Gets the navigation bar's background color.

Returns: `Promise<string>`

Current navigation bar color in hex format. Returns `#00000000` (transparent) on unsupported platforms (iOS, web).

Example

```ts
const color = await NavigationBar.getBackgroundColorAsync();
```

> **Deprecated:** Due to Android edge-to-edge enforcement, getting the navigation bar behavior is deprecated and always returns `inset-touch`. This will be removed in a future release.

### `NavigationBar.getBehaviorAsync()`

Supported platforms: Android.

Gets the behavior of the status and navigation bars when the user swipes or touches the screen.

Returns: `Promise<navigationbarbehavior>`

Navigation bar interaction behavior. Returns `inset-touch` on unsupported platforms (iOS, web).

Example

```ts
await NavigationBar.getBehaviorAsync()
```

> **Deprecated:** Due to Android edge-to-edge enforcement, getting the navigation bar border color is deprecated and always returns `#00000000` (transparent). This will be removed in a future release.

### `NavigationBar.getBorderColorAsync()`

Supported platforms: Android.

Gets the navigation bar's top border color, also known as the "divider color".

Returns: `Promise<string>`

Navigation bar top border color in hex format. Returns `#00000000` (transparent) on unsupported platforms (iOS, web).

Example

```ts
const color = await NavigationBar.getBorderColorAsync();
```

> **Deprecated:** Due to Android edge-to-edge enforcement, getting the navigation bar button color style is deprecated and always returns `light`. This will be removed in a future release.

### `NavigationBar.getButtonStyleAsync()`

Supported platforms: Android.

Gets the navigation bar's button color style.

Returns: `Promise<navigationbarbuttonstyle>`

Navigation bar foreground element color settings. Returns `light` on unsupported platforms (iOS, web).

Example

```ts
const style = await NavigationBar.getButtonStyleAsync();
```

### `NavigationBar.getVisibilityAsync()`

Supported platforms: Android.

Get the navigation bar's visibility.

Returns: `Promise<navigationbarvisibility>`

Navigation bar's current visibility status. Returns `hidden` on unsupported platforms (iOS, web).

Example

```ts
const visibility = await NavigationBar.getVisibilityAsync();
```

> **Deprecated:** Due to Android edge-to-edge enforcement, setting the navigation bar background color is deprecated and has no effect. This will be removed in a future release.

### `NavigationBar.setBackgroundColorAsync(color)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `color` | `string` | Any valid [CSS 3 (SVG) color](http://www.w3.org/TR/css3-color/#svg-color). |

  

Changes the navigation bar's background color.

Returns: `Promise<void>`

Example

```ts
NavigationBar.setBackgroundColorAsync("white");
```

> **Deprecated:** Due to Android edge-to-edge enforcement, setting the navigation bar behavior is deprecated and has no effect. This will be removed in a future release.

### `NavigationBar.setBehaviorAsync(behavior)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `behavior` | [NavigationBarBehavior](#navigationbarbehavior) | Dictates the interaction behavior of the navigation bar. |

  

Sets the behavior of the status bar and navigation bar when they are hidden and the user wants to reveal them.

For example, if the navigation bar is hidden (`setVisibilityAsync(false)`) and the behavior is `'overlay-swipe'`, the user can swipe from the bottom of the screen to temporarily reveal the navigation bar.

-   `'overlay-swipe'`: Temporarily reveals the System UI after a swipe gesture (bottom or top) without insetting your App's content.
-   `'inset-swipe'`: Reveals the System UI after a swipe gesture (bottom or top) and insets your App's content (Safe Area). The System UI is visible until you explicitly hide it again.
-   `'inset-touch'`: Reveals the System UI after a touch anywhere on the screen and insets your App's content (Safe Area). The System UI is visible until you explicitly hide it again.

Returns: `Promise<void>`

Example

```ts
await NavigationBar.setBehaviorAsync('overlay-swipe')
```

> **Deprecated:** Due to Android edge-to-edge enforcement, setting the navigation bar border color is deprecated and has no effect. This will be removed in a future release.

### `NavigationBar.setBorderColorAsync(color)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `color` | `string` | Any valid [CSS 3 (SVG) color](http://www.w3.org/TR/css3-color/#svg-color). |

  

Changes the navigation bar's border color.

Returns: `Promise<void>`

Example

```ts
NavigationBar.setBorderColorAsync("red");
```

> **Deprecated:** Use `setStyle` instead. This will be removed in a future release.

### `NavigationBar.setButtonStyleAsync(style)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `style` | [NavigationBarButtonStyle](#navigationbarbuttonstyle) | Dictates the color of the foreground element color. |

  

Changes the navigation bar's button colors between white (`light`) and a dark gray color (`dark`).

Returns: `Promise<void>`

Example

```ts
NavigationBar.setButtonStyleAsync("light");
```

> **Deprecated:** Due to Android edge-to-edge enforcement, setting the navigation bar position is deprecated and has no effect. This will be removed in a future release.

### `NavigationBar.setPositionAsync(position)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `position` | [NavigationBarPosition](#navigationbarposition) | Based on CSS position property. |

  

Sets positioning method used for the navigation bar (and status bar). Setting position `absolute` will float the navigation bar above the content, whereas position `relative` will shrink the screen to inline the navigation bar.

When drawing behind the status and navigation bars, ensure the safe area insets are adjusted accordingly.

Returns: `Promise<void>`

Example

```ts
// enables edge-to-edge mode
await NavigationBar.setPositionAsync('absolute')
// transparent backgrounds to see through
await NavigationBar.setBackgroundColorAsync('#ffffff00')
```

### `NavigationBar.setStyle(style)`

Supported platforms: Android.

| Parameter | Type |
| --- | --- |
| `style` | [NavigationBarStyle](#navigationbarstyle) |

  

Sets the style of the navigation bar.

> This will have an effect when the following conditions are met:
> 
> -   The `enforceContrast` option of the `expo-navigation-bar` plugin is set to `false`.
> -   The device is using the three-button navigation bar.

> Due to a bug in the Android 15 emulator this function may have no effect. Try a physical device or an emulator with a different version of Android.

Returns: `void`

### `NavigationBar.setVisibilityAsync(visibility)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `visibility` | [NavigationBarVisibility](#navigationbarvisibility) | Based on CSS visibility property. |

  

Set the navigation bar's visibility.

Returns: `Promise<void>`

Example

```ts
NavigationBar.setVisibilityAsync("hidden");
```

> **Deprecated:** Due to Android edge-to-edge enforcement, getting the navigation bar position is deprecated and always returns `relative`. This will be removed in a future release.

### `NavigationBar.unstable_getPositionAsync()`

Supported platforms: Android.

Whether the navigation and status bars float above the app (absolute) or sit inline with it (relative). This value can be incorrect if `androidNavigationBar.visible` is used instead of the config plugin `position` property.

This method is unstable because the position can be set via another native module and get out of sync. Alternatively, you can get the position by measuring the insets returned by `react-native-safe-area-context`.

Returns: `Promise<navigationbarposition>`

Navigation bar positional rendering mode. Returns `relative` on unsupported platforms (iOS, web).

Example

```ts
await NavigationBar.unstable_getPositionAsync()
```

## Event Subscriptions

### `NavigationBar.addVisibilityListener(listener)`

Supported platforms: Android.

| Parameter | Type |
| --- | --- |
| `listener` | (event: [NavigationBarVisibilityEvent](#navigationbarvisibilityevent)) => void |

  

Observe changes to the system navigation bar. Due to platform constraints, this callback will also be triggered when the status bar visibility changes.

Returns: `EventSubscription`

Example

```ts
NavigationBar.addVisibilityListener(({ visibility }) => {
  // ...
});
```

## Types

> **Deprecated:** This will be removed in a future release.

### `NavigationBarBehavior`

Supported platforms: Android.

Literal Type: `string`

Interaction behavior for the system navigation bar.

Acceptable values are: `'overlay-swipe'` | `'inset-swipe'` | `'inset-touch'`

### `NavigationBarButtonStyle`

Supported platforms: Android.

Literal Type: `string`

Appearance of the foreground elements in the navigation bar, i.e. the color of the menu, back, home button icons.

-   `dark` makes buttons **darker** to adjust for a mostly light nav bar.
-   `light` makes buttons **lighter** to adjust for a mostly dark nav bar.

Acceptable values are: `'light'` | `'dark'`

> **Deprecated:** This will be removed in a future release.

### `NavigationBarPosition`

Supported platforms: Android.

Literal Type: `string`

Navigation bar positional mode.

Acceptable values are: `'relative'` | `'absolute'`

### `NavigationBarStyle`

Supported platforms: Android.

Literal Type: `string`

Navigation bar style.

-   `auto` will automatically adjust based on the current theme.
-   `light` a light navigation bar with dark content.
-   `dark` a dark navigation bar with light content.
-   `inverted` the bar colors are inverted in relation to the current theme.

Acceptable values are: `'auto'` | `'inverted'` | `'light'` | `'dark'`

### `NavigationBarVisibility`

Supported platforms: Android.

Literal Type: `string`

Visibility of the navigation bar.

Acceptable values are: `'visible'` | `'hidden'`

### `NavigationBarVisibilityEvent`

Supported platforms: Android.

Current system UI visibility state. Due to platform constraints, this will return when the status bar visibility changes as well as the navigation bar.

| Property | Type | Description |
| --- | --- | --- |
| rawVisibility | `number` | Native Android system UI visibility state, returned from the native Android `setOnSystemUiVisibilityChangeListener` API. |
| visibility | [NavigationBarVisibility](#navigationbarvisibility) | Current navigation bar visibility. |
