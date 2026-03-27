---
title: Router Link
description: An Expo Router API that provides Link, Redirect, preview, and zoom transition components.
sourceCodeUrl: 'https://github.com/expo/expo/tree/main/packages/expo-router'
packageName: 'expo-router'
platforms: ['android', 'ios', 'tvos', 'web', 'expo-go']
---

# Expo Router Link

An Expo Router API that provides Link, Redirect, preview, and zoom transition components.
Android, iOS, tvOS, Web, Included in Expo Go

An Expo Router API that provides components for navigating between routes, including link, redirect, preview, and zoom transitions.

> See the [Expo Router](/versions/latest/sdk/router/index) reference for installation and configuration.

## Usage

```tsx
import { Link } from 'expo-router';

export default function Page() {
  return <Link href="/about">About</Link>;
}
```

For more information about navigating between routes, read the navigation guide:

[Navigate between pages](/router/basics/navigation) — Learn how to navigate between pages in Expo Router.

## API

```js
import { Link, Redirect } from 'expo-router';
```

## Components

### `Link`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[LinkProps](#linkprops)\>

Component that renders a link using [`href`](#href) to another route. By default, it accepts children and wraps them in a `<Text>` component.

Uses an anchor tag (`<a>`) on web and performs a client-side navigation to preserve the state of the website and navigate faster. The web-only attributes such as `target`, `rel`, and `download` are supported and passed to the anchor tag on web. See [`WebAnchorProps`](#webanchorprops) for more details.

> **Note**: Client-side navigation works with both single-page apps, and [static-rendering](/router/reference/static-rendering).

Example

```tsx
import { Link } from 'expo-router';
import { View } from 'react-native';

export default function Route() {
 return (
  <View>
   <Link href="/about">About</Link>
  </View>
 );
}
```

LinkProps

### `asChild`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

Used to customize the `Link` component. It will forward all props to the first child of the `Link`. Note that the child component must accept `onPress` or `onClick` props. The `href` and `role` are also passed to the child.

Example

```tsx
import { Link } from 'expo-router';
import { Pressable, Text } from 'react-native';

export default function Route() {
 return (
  <View>
   <Link href="/home" asChild>
     <Pressable>
      <Text>Home</Text>
     </Pressable>
   </Link>
  </View>
 );
}
```

### `className`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `string`

On native, this can be used with CSS interop tools like Nativewind. On web, this sets the HTML `class` directly.

### `dangerouslySingular`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: [SingularOptions](#singularoptions)

When navigating in a Stack, if the target is valid then screens in the history that matches the uniqueness constraint will be removed.

If used with `push`, the history will be filtered even if no navigation occurs.

### `dismissTo`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

While in a stack, this will dismiss screens until the provided `href` is reached. If the href is not found, it will instead replace the current screen with the provided `href`.

Example

```tsx
import { Link } from 'expo-router';
import { View } from 'react-native';

export default function Route() {
 return (
  <View>
    <Link dismissTo href="/feed">Close modal</Link>
  </View>
 );
}
```

### `href`

Supported platforms: Android, iOS, tvOS, Web.

Literal type: `union`

The path of the route to navigate to. It can either be:

-   **string**: A full path like `/profile/settings` or a relative path like `../settings`.
-   **object**: An object with a `pathname` and optional `params`. The `pathname` can be a full path like `/profile/settings` or a relative path like `../settings`. The params can be an object of key-value pairs.

Example

```tsx
import { Link } from 'expo-router';
import { View } from 'react-native';

export default function Route() {
 return (
  <View>
   <Link href="/about">About</Link>
   <Link
    href={{
      pathname: '/user/[id]',
      params: { id: 'bacon' }
    }}>
      View user
   </Link>
  </View>
 );
}
```

Acceptable values are: `string` | [HrefObject](#hrefobject)

### `onPress`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: (event: [MouseEvent](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent)<[HTMLAnchorElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAnchorElement), [MouseEvent](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent)\> | GestureResponderEvent) => void

This function is called on press. Text intrinsically supports press handling with a default highlight state (which can be disabled with suppressHighlighting).

### `prefetch`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

Prefetches the route when the component is rendered on a focused screen.

### `push`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

Always pushes a new route, and never pops or replaces to existing route. You can push the current route multiple times or with new parameters.

Example

```tsx
import { Link } from 'expo-router';
import { View } from 'react-native';

export default function Route() {
 return (
  <View>
    <Link push href="/feed">Login</Link>
  </View>
 );
}
```

### `ref`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: Ref<[Text](https://reactnative.dev/docs/text)\>

### `relativeToDirectory`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

Relative URL references are either relative to the directory or the document. By default, relative paths are relative to the document.

> **See:** [Resolving relative references in Mozilla's documentation](https://developer.mozilla.org/en-US/docs/Web/API/URL_API/Resolving_relative_references).

### `replace`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

Removes the current route from the history and replace it with the specified URL. This is useful for [redirects](/router/reference/redirects).

Example

```tsx
import { Link } from 'expo-router';
import { View } from 'react-native';

export default function Route() {
 return (
  <View>
    <Link replace href="/feed">Login</Link>
  </View>
 );
}
```

### `withAnchor`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

Replaces the initial screen with the current route.

#### Inherited Props

-   [Omit](https://www.typescriptlang.org/docs/handbook/utility-types.html#omittype-keys)<[TextProps](https://reactnative.dev/docs/text#props), 'href'\>
-   [WebAnchorProps](#webanchorprops)

### `Redirect`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[RedirectProps](#redirectprops)\>

Redirects to the `href` as soon as the component is mounted.

Example

```tsx
import { View, Text } from 'react-native';
import { Redirect } from 'expo-router';

export default function Page() {
 const { user } = useAuth();

 if (!user) {
   return <Redirect href="/login" />;
 }

 return (
   <View>
     <Text>Welcome Back!</Text>
   </View>
 );
}
```

RedirectProps

### `href`

Supported platforms: Android, iOS, tvOS, Web.

Type: [Href](/versions/v55.0.0/sdk/router#hreft)

The path of the route to navigate to. It can either be:

-   **string**: A full path like `/profile/settings` or a relative path like `../settings`.
-   **object**: An object with a `pathname` and optional `params`. The `pathname` can be a full path like `/profile/settings` or a relative path like `../settings`. The params can be an object of key-value pairs.

Example

```tsx
import { Redirect } from 'expo-router';

export default function RedirectToAbout() {
 return (
   <Redirect href="/about" />
 );
}
```

### `relativeToDirectory`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

Relative URL references are either relative to the directory or the document. By default, relative paths are relative to the document.

> **See:** [Resolving relative references in Mozilla's documentation](https://developer.mozilla.org/en-US/docs/Web/API/URL_API/Resolving_relative_references).

### `withAnchor`

Supported platforms: Android, iOS, tvOS, Web.

Optional • Type: `boolean`

Replaces the initial screen with the current route.

### `Link.AppleZoom`

Supported platforms: iOS 18+.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[LinkAppleZoomProps](#linkapplezoomprops)\>

When this component is used inside a Link, [zoom transition](https://developer.apple.com/documentation/uikit/enhancing-your-app-with-fluid-transitions?language=objc) will be used when navigating to the link's href.

LinkAppleZoomProps

### `alignmentRect`

Supported platforms: iOS 18+.

Optional • Type: `{ height: number, width: number, x: number, y: number }`

Defines the rectangle used for the zoom transition's alignment. This rectangle is specified in the zoomed screen's coordinate space.

#### Inherited Props

-   `PropsWithChildren`

### `Link.AppleZoomTarget`

Supported platforms: iOS 18+.

Type: React.Iterable<{ children: [ReactNode](https://reactnative.dev/docs/react-node) }\>

Defines the target for an Apple zoom transition.

Example

```tsx
import { Link } from 'expo-router';

export default function Screen() {
 return (
  <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
   <Link.AppleZoomTarget>
     <Image source={require('../assets/image.png')} style={{ width: 200, height: 200 }} />
   </Link.AppleZoomTarget>
  </View>
 );
}
```

### `Link.Menu`

Supported platforms: iOS.

Type: React.Element<[LinkMenuProps](#linkmenuprops)\>

Groups context menu actions for a link.

If multiple `Link.Menu` components are used within a single `Link`, only the first will be rendered. Only `Link.MenuAction` and `Link.Menu` components are allowed as children.

Example

```tsx
<Link.Menu>
  <Link.MenuAction title="Action 1" onPress={() => {}} />
  <Link.MenuAction title="Action 2" onPress={() => {}} />
</Link.Menu>
```

LinkMenuProps

### `children`

Supported platforms: iOS.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

### `destructive`

Supported platforms: iOS.

Optional • Type: `boolean`

If `true`, the menu item will be displayed as destructive.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenu/options-swift.struct/destructive) for more information.

> **Deprecated:** Use `palette` prop instead.

### `displayAsPalette`

Supported platforms: iOS.

Optional • Type: `boolean`

> **Deprecated:** Use `inline` prop instead.

### `displayInline`

Supported platforms: iOS.

Optional • Type: `boolean`

### `elementSize`

Supported platforms: iOS 16.0+.

Optional • Literal type: `string`

The preferred size of the menu elements. `elementSize` property is ignored when `palette` is used.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenu/preferredelementsize) for more information.

Acceptable values are: `'small'` | `'auto'` | `'medium'` | `'large'`

### `icon`

Supported platforms: iOS.

Optional • Type: [SFSymbols7_0](https://github.com/nandorojo/sf-symbols-typescript)

Optional SF Symbol displayed alongside the menu item.

### `image`

Supported platforms: iOS.

Optional • Literal type: `union`

Custom image loaded using `useImage()` hook from `expo-image`. Takes priority over `icon` (SF Symbol) when both are provided.

Example

```tsx
import { useImage } from 'expo-image';
import { Link } from 'expo-router';

const customIcon = useImage('https://simpleicons.org/icons/expo.svg', {
  maxWidth: 24,
  maxHeight: 24,
});

<Link.Menu image={customIcon} title="Menu">
  <Link.MenuAction title="Action" onPress={() => {}} />
</Link.Menu>
```

Acceptable values are: `ImageRef` | `null`

### `inline`

Supported platforms: iOS.

Optional • Type: `boolean`

If `true`, the menu will be displayed inline. This means that the menu will not be collapsed

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenu/options-swift.struct/displayinline) for more information.

### `palette`

Supported platforms: iOS.

Optional • Type: `boolean`

If `true`, the menu will be displayed as a palette. This means that the menu will be displayed as one row. The `elementSize` property is ignored when palette is used, all items will be `elementSize="small"`. Use `elementSize="medium"` instead of `palette` to display actions with titles horizontally.

> **Note**: Palette menus are only supported in submenus.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenu/options-swift.struct/displayaspalette) for more information.

### `subtitle`

Supported platforms: iOS.

Optional • Type: `string`

An optional subtitle for the submenu. Does not appear on `inline` menus.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenuelement/subtitle) for more information.

### `title`

Supported platforms: iOS.

Optional • Type: `string`

The title of the menu item

### `Link.MenuAction`

Supported platforms: iOS.

Type: React.Element<[LinkMenuActionProps](#linkmenuactionprops)\>

This component renders a context menu action for a link. It should only be used as a child of `Link.Menu` or `LinkMenu`.

LinkMenuActionProps

### `children`

Supported platforms: iOS.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

The title of the menu item.

### `destructive`

Supported platforms: iOS.

Optional • Type: `boolean`

If `true`, the menu item will be displayed as destructive.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenuelement/attributes/destructive) for more information.

### `disabled`

Supported platforms: iOS.

Optional • Type: `boolean`

If `true`, the menu item will be disabled and not selectable.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenuelement/attributes/disabled) for more information.

### `discoverabilityLabel`

Supported platforms: iOS.

Optional • Type: `string`

An elaborated title that explains the purpose of the action.

### `hidden`

Supported platforms: iOS.

Optional • Type: `boolean` • Default: `false`

Whether the menu element should be hidden.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenuelement/attributes/hidden) for more information.

### `icon`

Supported platforms: iOS.

Optional • Type: [SFSymbols7_0](https://github.com/nandorojo/sf-symbols-typescript)

SF Symbol displayed alongside the menu item.

### `image`

Supported platforms: iOS.

Optional • Literal type: `union`

Custom image loaded using `useImage()` hook from `expo-image`. Takes priority over `icon` (SF Symbol) when both are provided.

Example

```tsx
import { useImage } from 'expo-image';
import { Link } from 'expo-router';

const customIcon = useImage('https://simpleicons.org/icons/expo.svg', {
  maxWidth: 24,
  maxHeight: 24,
});

<Link.Menu title="Menu">
  <Link.MenuAction image={customIcon} title="Action" onPress={() => {}} />
</Link.Menu>
```

Acceptable values are: `ImageRef` | `null`

### `imageRenderingMode`

Supported platforms: iOS.

Optional • Literal type: `string`

Controls how image-based icons are rendered on iOS.

-   `'template'`: iOS applies tint color to the icon
-   `'original'`: Preserves original icon colors

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uiimage/renderingmode-swift.enum) for more information.

Acceptable values are: `'template'` | `'original'`

### `isOn`

Supported platforms: iOS.

Optional • Type: `boolean`

If `true`, the menu item will be displayed as selected.

### `onPress`

Supported platforms: iOS.

Optional • Type: `() => void`

### `subtitle`

Supported platforms: iOS.

Optional • Type: `string`

An optional subtitle for the menu item.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenuelement/subtitle) for more information.

> **Deprecated:** Use `children` prop instead.

### `title`

Supported platforms: iOS.

Optional • Type: `string`

The title of the menu item.

### `unstable_keepPresented`

Supported platforms: iOS.

Optional • Type: `boolean`

If `true`, the menu will be kept presented after the action is selected.

This is marked as unstable, because when action is selected it will recreate the menu, which will close all opened submenus and reset the scroll position.

> **See:** [Apple documentation](https://developer.apple.com/documentation/uikit/uimenuelement/attributes/keepsmenupresented) for more information.

### `Link.Preview`

Supported platforms: iOS.

Type: React.Element<[LinkPreviewProps](#linkpreviewprops)\>

A component used to render and customize the link preview.

If `Link.Preview` is used without any props, it will render a preview of the `href` passed to the `Link`.

If multiple `Link.Preview` components are used within a single `Link`, only the first one will be rendered.

To customize the preview, you can pass custom content as children.

Example

```tsx
<Link href="/about">
  <Link.Preview>
    <Text>Custom Preview Content</Text>
  </Link.Preview>
</Link>
```

Example

```tsx
<Link href="/about">
  <Link.Preview />
</Link>
```

LinkPreviewProps

### `children`

Supported platforms: iOS.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

### `style`

Supported platforms: iOS.

Optional • Type: `LinkPreviewStyle`

Custom styles for the preview container.

Note that some styles may not work, as they are limited or reset by the native view

### `Link.Trigger`

Supported platforms: iOS.

Type: React.Iterable<[LinkTriggerProps](#linktriggerprops)\>

Serves as the trigger for a link. The content inside this component will be rendered as part of the base link.

If multiple `Link.Trigger` components are used within a single `Link`, only the first will be rendered.

Example

```tsx
<Link href="/about">
  <Link.Trigger>
    Trigger
  </Link.Trigger>
</Link>
```

LinkTriggerProps

### `withAppleZoom`

Supported platforms: iOS 18+.

Optional • Type: `boolean`

A shorthand for enabling the Apple Zoom Transition on this link trigger.

When set to `true`, the trigger will be wrapped with `Link.AppleZoom`. If another `Link.AppleZoom` is already used inside `Link.Trigger`, an error will be thrown.

#### Inherited Props

-   `PropsWithChildren`

## Hooks

### `useIsPreview()`

Supported platforms: Android, iOS, tvOS, Web.

Hook to determine if the current route is rendered inside a preview.

Returns: `boolean`

-   True if the current route is rendered inside a preview, false otherwise.

### `usePreventZoomTransitionDismissal(_options)`

Supported platforms: iOS.

| Parameter | Type |
| --- | --- |
| `_options`(optional) | [UsePreventZoomTransitionDismissalOptions](#usepreventzoomtransitiondismissaloptions) |

  

Limits the screen area where interactive dismissal gestures are allowed for zoom transitions.

This hook must be called from the destination screen of a zoom transition (the screen you navigate to, not the source). It restricts where app users can start swipe gestures to dismiss the screen and return to the previous screen.

When a dismissal gesture starts inside the bounds, the screen can be dismissed. When a dismissal gesture starts outside the bounds, dismissal is blocked completely. Undefined coordinates place no restriction on that dimension.

> **Note**: Only one instance of this hook should be used per screen. If multiple instances exist, the last one to render will take effect.

Returns: `void`

Example

```tsx
// In your destination screen (e.g., app/image.tsx)
import { usePreventZoomTransitionDismissal } from 'expo-router';
import { useWindowDimensions } from 'react-native';
import { Image } from 'expo-image';

export default function ImageScreen() {
  const dimensions = useWindowDimensions();
  // Only allow dismissal from the bottom 200px of the screen
  usePreventZoomTransitionDismissal({
    unstable_dismissalBoundsRect: {
      minY: dimensions.height - 200
    }
  });

  return <Image source={...} style={{ flex: 1 }} />;
}
```

## Interfaces

### `DismissalBoundsRect`

Supported platforms: iOS.

Defines the screen bounds where interactive dismissal gestures are allowed for zoom transitions.

| Property | Type | Description |
| --- | --- | --- |
| maxX(optional) | `number` | Maximum X coordinate (right edge) where dismissal gestures are allowed. |
| maxY(optional) | `number` | Maximum Y coordinate (bottom edge) where dismissal gestures are allowed. |
| minX(optional) | `number` | Minimum X coordinate (left edge) where dismissal gestures are allowed. |
| minY(optional) | `number` | Minimum Y coordinate (top edge) where dismissal gestures are allowed. |

### `UsePreventZoomTransitionDismissalOptions`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| unstable_dismissalBoundsRect(optional) | [DismissalBoundsRect](#dismissalboundsrect) | Defines the screen bounds where interactive dismissal gestures are allowed. Each coordinate is optional. Undefined coordinates place no restriction on that dimension. For example, if only `minY` and `maxY` are defined, horizontal gestures are unrestricted while vertical gestures must stay within the Y bounds.See: Apple documentation for more information. |

## Types

### `WebAnchorProps`

Supported platforms: Web.

| Property | Type | Description |
| --- | --- | --- |
| download(optional) | `string` | Specifies that the [`href`](#href) should be downloaded when the user clicks on the link, instead of navigating to it. It is typically used for links that point to files that the user should download, such as PDFs, images, documents, and more. The value of the `download` property, which represents the filename for the downloaded file. This property is passed to the underlying anchor (`<a>`) tag. . Example
```jsx
<Link href="/image.jpg" download="my-image.jpg">Download image</Link>
```

 |
| rel(optional) | `string` | Specifies the relationship between the [`href`](#href) and the current route. Common values:

-   **nofollow**: Indicates to search engines that they should not follow the `href`. This is often used for user-generated content or links that should not influence search engine rankings.
-   **noopener**: Suggests that the `href` should not have access to the opening window's `window.opener` object, which is a security measure to prevent potentially harmful behavior in cases of links that open new tabs or windows.
-   **noreferrer**: Requests that the browser does not send the `Referer` HTTP header when navigating to the `href`. This can enhance user privacy.

. The `rel` property is primarily used for informational and instructive purposes, helping browsers and web crawlers make better decisions about how to handle and interpret the links on a web page. It is important to use appropriate `rel` values to ensure that links behave as intended and adhere to best practices for web development and SEO (Search Engine Optimization). This property is passed to the underlying anchor (`<a>`) tag. . Example

```jsx
<Link href="https://expo.dev" rel="nofollow">Go to Expo</Link>
```

 |
| target(optional) | `'_self' | '_blank' | '_parent' | '_top' | string & object` | Specifies where to open the [`href`](#href).

-   **_self**: the current tab.
-   **_blank**: opens in a new tab or window.
-   **_parent**: opens in the parent browsing context. If no parent, defaults to **_self**.
-   **_top**: opens in the highest browsing context ancestor. If no ancestors, defaults to **_self**.

. This property is passed to the underlying anchor (`<a>`) tag. Default: `'_self'`. Example

```jsx
<Link href="https://expo.dev" target="_blank">Go to Expo in new tab</Link>
```

 |
