---
title: Router
description: A file-based routing library for React Native and web applications.
sourceCodeUrl: 'https://github.com/expo/expo/tree/main/packages/expo-router'
packageName: 'expo-router'
platforms: ['android', 'ios', 'tvos', 'web', 'expo-go']
---

# Expo Router

A file-based routing library for React Native and web applications.
Android, iOS, tvOS, Web, Included in Expo Go

`expo-router` is a routing library for React Native and web apps. It enables navigation management using a file-based routing system and provides native navigation components and is built on top of [React Navigation](https://reactnavigation.org/).

[Expo Router guides](/router/introduction) — Learn about Expo Router basics, navigation patterns, core concepts, and more.

## Installation

To use Expo Router in your project, you need to install. Follow the instructions from the Expo Router's installation guide:

[Install Expo Router](/router/installation) — Learn how to install Expo Router in your project.

## Configuration in app config

If you are using the [default](/more/create-expo#--template) template to create a new project, `expo-router`'s [config plugin](/config-plugins/introduction) is already configured in your app config.

### Example app.json with config plugin

```json
{
  "expo": {
    "plugins": ["expo-router"]
  }
}
```

### Configurable properties

| Name | Default | Description |
| --- | --- | --- |
| `root` | `"app"` | Changes the routes directory from `app` to another value. Avoid using this property unless you have a specific need. |
| `origin` | `undefined` | Production origin URL where assets in the public folder are hosted. The fetch function is polyfilled to support relative requests from this origin in production. The development origin is inferred using the Expo CLI development server. |
| `headOrigin` | `undefined` | A more specific origin URL used in the `expo-router/head` module for iOS handoff. Defaults to `origin`. |
| `asyncRoutes` | `undefined` | Enable async routes (lazy loading). Can be a boolean, a string (`"development"` or `"production"`), or an object with platform-specific values (`{ android, ios, web, default }`). `production` is currently web-only and will be disabled on native. |
| `platformRoutes` | `true` | Enable or disable platform-specific routes (for example, **index.android.tsx** and **index.ios.tsx**). |
| `sitemap` | `true` | Enable or disable the automatically generated sitemap at **/_sitemap**. |
| `partialRouteTypes` | `true` | Enable partial typed routes generation. This allows TypeScript to provide type checking for routes without requiring all routes to be statically known. |
| `redirects` | `undefined` | An array of static redirect rules. Each rule should have `source`, `destination`, and optionally `permanent` (defaults to `false`) and `methods` (HTTP methods to redirect). |
| `rewrites` | `undefined` | An array of static rewrite rules. Each rule should have `source`, `destination`, and optionally `methods` (HTTP methods to rewrite). |
| `headers` | `undefined` | A list of headers that are set on every route response from the server. The value can be a string or an array of strings. |
| `disableSynchronousScreensUpdates` | `false` | Disable synchronous layout updates for native screens. This can help with performance in some cases. |
| `unstable_useServerMiddleware` | `false` | , Experimental. Enable server middleware support with a `+middleware.ts` file. Requires `web.output: "server"` to be set in app config. |
| `unstable_useServerDataLoaders` | `false` | , Experimental. Enable data loader support. This is only supported for `web.output: "static"` outputs at the moment. |
| `unstable_useServerRendering` | `false` | , Experimental. Enable server-side rendering. When enabled with `web.output: "server"`, HTML is rendered at request time instead of being pre-rendered at build time. |

## Usage

For information core concepts, notation patterns, navigation layouts, and common navigation patterns, start with Router 101 section:

[Router 101](/router/basics/core-concepts)

## APIs

| API | Description |
| --- | --- |
| [Stack](/versions/latest/sdk/router/stack) | Stack navigator, toolbar, and screen components |
| [Link](/versions/latest/sdk/router/link) | Link and Redirect components |
| [Color](/versions/latest/sdk/router/color) | Platform color utilities |
| [Native Tabs](/versions/latest/sdk/router/native-tabs) | Native tab navigation |
| [Split View](/versions/latest/sdk/router/split-view) | Split view layout |
| [UI](/versions/latest/sdk/router/ui) | Headless tab components |

## API

```js
import { useRouter, Tabs, Navigator, Slot } from 'expo-router';
```

## Components

### `Tabs`

Supported platforms: Android, iOS, tvOS, Web.

Renders a tabs navigator.

### `Badge`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[BadgeProps](#badgeprops)\>

BadgeProps

#### Inherited Props

-   [NativeTabsTriggerBadgeProps](/versions/v55.0.0/sdk/router/native-tabs#nativetabstriggerbadgeprops)
-   [StackToolbarBadgeProps](#stacktoolbarbadgeprops)

### `ErrorBoundary`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ErrorBoundaryProps](#errorboundaryprops)\>

Props passed to a page's `ErrorBoundary` export.

ErrorBoundaryProps

### `error`

Supported platforms: Android, iOS, tvOS, Web.

Type: [Error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)

The error that was thrown.

### `retry`

Supported platforms: Android, iOS, tvOS, Web.

Type: () => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void\>

A function that will re-render the route component by clearing the `error` state.

### `Icon`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[IconProps](#iconprops)\>

IconProps

#### Inherited Props

-   [NativeTabsTriggerIconProps](/versions/v55.0.0/sdk/router/native-tabs#nativetabstriggericonprops)
-   [StackToolbarIconProps](#stacktoolbariconprops)

### `Label`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[LabelProps](#labelprops)\>

LabelProps

#### Inherited Props

-   [NativeTabsTriggerLabelProps](/versions/v55.0.0/sdk/router/native-tabs#nativetabstriggerlabelprops)
-   [StackToolbarLabelProps](#stacktoolbarlabelprops)

### `Slot`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[Omit](https://www.typescriptlang.org/docs/handbook/utility-types.html#omittype-keys)<NavigatorProps<any\>, 'children'\>\>

Renders the currently selected content.

There are actually two different implementations of `<Slot/>`:

-   Used inside a `_layout` as the `Navigator`
-   Used inside a `Navigator` as the content

Since a custom `Navigator` will set the `NavigatorContext.contextKey` to the current `_layout`, you can use this to determine if you are inside a custom navigator or not.

### `VectorIcon`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[VectorIconProps](/versions/v55.0.0/sdk/router#vectoriconprops)<NameT\>\>

Helper component for loading vector icons.

Prefer using the `md` and `sf` props on `Icon` rather than using this component directly. Only use this component when you need to load a specific icon from a vector icon family.

Example

```tsx
import { Icon, VectorIcon } from 'expo-router';
import MaterialCommunityIcons from '@expo/vector-icons/MaterialCommunityIcons';

<Icon src={<VectorIcon family={MaterialCommunityIcons} name="home" />} />
```

VectorIconProps

### `family`

Supported platforms: Android, iOS, tvOS, Web.

Type: { getImageSource: (name: NameT, size: number, color: [ColorValue](https://reactnative.dev/docs/colors)) => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[ImageSourcePropType](https://reactnative.dev/docs/image#imagesource) | null\> }

The family of the vector icon.

Example

```tsx
import MaterialCommunityIcons from '@expo/vector-icons/MaterialCommunityIcons';
```

### `name`

Supported platforms: Android, iOS, tvOS, Web.

Type: `NameT`

The name of the vector icon.

### `Tabs.Screen`

Supported platforms: Android, iOS, tvOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ScreenProps](#screenprops)<[TabsProps](/versions/v55.0.0/sdk/router/ui#tabsprops), [TabNavigationState](https://reactnavigation.org/docs/custom-navigators/#type-checking-navigators)<ParamListBase\>, BottomTabNavigationEventMap\>\>

## Constants

### `unstable_navigationEvents`

Supported platforms: Android, iOS, tvOS, Web.

Type: `{ addListener: (eventType: EventType, callback: (event: Payload<EventType>) => void) => () => void, emit: (type: EventType, event: Payload<EventType>) => void, enable: () => void, isEnabled: () => boolean, saveCurrentPathname: () => void, }`

## Hooks

### `useFocusEffect(effect, do_not_pass_a_second_prop)`

Supported platforms: Android, iOS, tvOS, Web.

| Parameter | Type | Description |
| --- | --- | --- |
| `effect` | [EffectCallback](#effectcallback) | Memoized callback containing the effect, should optionally return a cleanup function. |
| `do_not_pass_a_second_prop`(optional) | `undefined` | - |

  

Hook to run an effect whenever a route is **focused**. Similar to [`React.useEffect`](https://react.dev/reference/react/useEffect).

This can be used to perform side-effects such as fetching data or subscribing to events. The passed callback should be wrapped in [`React.useCallback`](https://react.dev/reference/react/useCallback) to avoid running the effect too often.

Returns: `void`

Example

```tsx
import { useFocusEffect } from 'expo-router';
import { useCallback } from 'react';

export default function Route() {
  useFocusEffect(
    // Callback should be wrapped in `React.useCallback` to avoid running the effect too often.
    useCallback(() => {
      // Invoked whenever the route is focused.
      console.log("Hello, I'm focused!");

      // Return function is invoked whenever the route gets out of focus.
      return () => {
        console.log('This route is now unfocused.');
      };
    }, []),
   );

 return </>;
}
```

### `useGlobalSearchParams()`

Supported platforms: Android, iOS, tvOS, Web.

Returns URL parameters for globally selected route, including dynamic path segments. This function updates even when the route is not focused. Useful for analytics or other background operations that don't draw to the screen.

Route URL example: `acme://profile/baconbrix?extra=info`.

When querying search params in a stack, opt-towards using [`useLocalSearchParams`](#uselocalsearchparams) because it will only update when the route is focused.

> **Note:** For usage information, see [Local versus global search parameters](/router/reference/url-parameters#local-versus-global-url-parameters).

Returns: `RouteParams<troute> & TParams</troute>`

Example

```tsx
import { Text } from 'react-native';
import { useGlobalSearchParams } from 'expo-router';

export default function Route() {
  // user=baconbrix & extra=info
  const { user, extra } = useGlobalSearchParams();

  return <Text>User: {user}</Text>;
}
```

### `useLoaderData()`

Supported platforms: Android, iOS, tvOS, Web.

Returns the result of the `loader` function for the calling route.

Returns: `LoaderFunctionResult<t>`

Example

```tsx
import { Text } from 'react-native';
import { useLoaderData } from 'expo-router';

export function loader() {
  return Promise.resolve({ foo: 'bar' }};
}

export default function Route() {
 const data = useLoaderData<typeof loader>(); // { foo: 'bar' }

 return <Text>Data: {JSON.stringify(data)}</Text>;
}
```

### `useLocalSearchParams()`

Supported platforms: Android, iOS, tvOS, Web.

Returns the URL parameters for the contextually focused route. Useful for stacks where you may push a new screen that changes the query parameters. For dynamic routes, both the route parameters and the search parameters are returned.

Route URL example: `acme://profile/baconbrix?extra=info`.

To observe updates even when the invoking route is not focused, use [`useGlobalSearchParams`](#useglobalsearchparams).

> **Note:** For usage information, see [Local versus global search parameters](/router/reference/url-parameters#local-versus-global-url-parameters).

Returns: `RouteParams<troute> & TParams</troute>`

Example

```tsx
import { Text } from 'react-native';
import { useLocalSearchParams } from 'expo-router';

export default function Route() {
 // user=baconbrix & extra=info
 const { user, extra } = useLocalSearchParams();

 return <Text>User: {user}</Text>;
}
```

### `useNavigation(parent)`

Supported platforms: Android, iOS, tvOS, Web.

| Parameter | Type | Description |
| --- | --- | --- |
| `parent`(optional) | string | [HrefObject](#hrefobject) | Provide an absolute path such as `/(root)` to the parent route or a relative path like `. /. /` to the parent route. |

  

Returns the underlying React Navigation [`navigation` object](https://reactnavigation.org/docs/navigation-object) to imperatively access layout-specific functionality like `navigation.openDrawer()` in a [Drawer](/router/advanced/drawer) layout.

Returns: `T`

The navigation object for the current route.

> **See:** React Navigation documentation on [navigation dependent functions](https://reactnavigation.org/docs/navigation-object/#navigator-dependent-functions) for more information.

Example

```tsx
import { useNavigation } from 'expo-router';

export default function Route() {
  // Access the current navigation object for the current route.
  const navigation = useNavigation();

  return (
    <View>
      <Text onPress={() => {
        // Open the drawer view.
        navigation.openDrawer();
      }}>
        Open Drawer
      </Text>
    </View>
  );
}
```

When using nested layouts, you can access higher-order layouts by passing a secondary argument denoting the layout route. For example, `/menu/_layout.tsx` is nested inside `/app/orders/`, you can use `useNavigation('/orders/menu/')`.

Example

```tsx
import { useNavigation } from 'expo-router';

export default function MenuRoute() {
  const rootLayout = useNavigation('/');
  const ordersLayout = useNavigation('/orders');

  // Same as the default results of `useNavigation()` when invoked in this route.
  const parentLayout = useNavigation('/orders/menu');
}
```

If you attempt to access a layout that doesn't exist, an error such as `Could not find parent navigation with route "/non-existent"` is thrown.

### `useNavigationContainerRef()`

Supported platforms: Android, iOS, tvOS, Web.

Returns: `NavigationContainerRefWithCurrent<rootparamlist>`

The root `<NavigationContainer />` ref for the app. The `ref.current` may be `null` if the `<NavigationContainer />` hasn't mounted yet.

### `usePathname()`

Supported platforms: Android, iOS, tvOS, Web.

Returns the currently selected route location without search parameters. For example, `/acme?foo=bar` returns `/acme`. Segments will be normalized. For example, `/[id]?id=normal` becomes `/normal`.

Returns: `string`

Example

```tsx
import { Text } from 'react-native';
import { usePathname } from 'expo-router';

export default function Route() {
  // pathname = "/profile/baconbrix"
  const pathname = usePathname();

  return <Text>Pathname: {pathname}</Text>;
}
```

> **Deprecated:** Use [`useNavigationContainerRef`](#usenavigationcontainerref) instead, which returns a React `ref`.

### `useRootNavigation()`

Supported platforms: Android, iOS, tvOS, Web.

Returns: `NavigationContainerRef<rootparamlist> | null</rootparamlist>`

### `useRootNavigationState()`

Supported platforms: Android, iOS, tvOS, Web.

Returns the [navigation state](https://reactnavigation.org/docs/navigation-state/) of the navigator which contains the current screen.

Returns: `Readonly<undefined>`

Example

```tsx
import { useRootNavigationState } from 'expo-router';

export default function Route() {
 const { routes } = useRootNavigationState();

 return <Text>{routes[0].name}</Text>;
}
```

### `useRouter()`

Supported platforms: Android, iOS, tvOS, Web.

Returns the [Router](#router) object for imperative navigation.

Returns: `Router`

Example

```tsx
import { useRouter } from 'expo-router';
import { Text } from 'react-native';

export default function Route() {
 const router = useRouter();

 return (
  <Text onPress={() => router.push('/home')}>Go Home</Text>
 );
}
```

### `useSegments()`

Supported platforms: Android, iOS, tvOS, Web.

Returns a list of selected file segments for the currently selected route. Segments are not normalized, so they will be the same as the file path. For example, `/[id]?id=normal` becomes `["[id]"]`.

Returns: `RouteSegments<tsegments>`

Example

```tsx
import { Text } from 'react-native';
import { useSegments } from 'expo-router';

export default function Route() {
  // segments = ["profile", "[user]"]
  const segments = useSegments();

  return <Text>Hello</Text>;
}
```

`useSegments` can be typed using an abstract. Consider the following file structure:

```md
- app
  - [user]
    - index.tsx
    - followers.tsx
  - settings.tsx
```

This can be strictly typed using the following abstract with `useSegments` hook:

```tsx
const [first, second] = useSegments<['settings'] | ['[user]'] | ['[user]', 'followers']>()
```

### `useSitemap()`

Supported platforms: Android, iOS, tvOS, Web.

Returns: `SitemapType | null`

## Methods

### `Sitemap()`

Supported platforms: Android, iOS, tvOS, Web.

Returns: `Element`

### `withLayoutContext(Nav, processor, useOnlyUserDefinedScreens)`

Supported platforms: Android, iOS, tvOS, Web.

| Parameter | Type | Description |
| --- | --- | --- |
| `Nav` | `T` | The navigator component to wrap. |
| `processor`(optional) | (options: [ScreenProps[]](#screenprops)) => [ScreenProps[]](#screenprops) | A function that processes the screens before passing them to the navigator. |
| `useOnlyUserDefinedScreens`(optional) | `boolean` | If true, all screens not specified as navigator's children will be ignored. Default: `false` |

  

Returns a navigator that automatically injects matched routes and renders nothing when there are no children. Return type with `children` prop optional.

Enables use of other built-in React Navigation navigators and other navigators built with the React Navigation custom navigator API.

Returns: `Component<propswithoutref>> & { Protected: FunctionComponent, Screen: (props: ScreenProps) => null }</propswithoutref`

Example

```tsx
import { ParamListBase, TabNavigationState } from "@react-navigation/native";
import {
  createMaterialTopTabNavigator,
  MaterialTopTabNavigationOptions,
  MaterialTopTabNavigationEventMap,
} from "@react-navigation/material-top-tabs";
import { withLayoutContext } from "expo-router";

const MaterialTopTabs = createMaterialTopTabNavigator();

const ExpoRouterMaterialTopTabs = withLayoutContext<
  MaterialTopTabNavigationOptions,
  typeof MaterialTopTabs.Navigator,
  TabNavigationState<ParamListBase>,
  MaterialTopTabNavigationEventMap
>(MaterialTopTabs.Navigator);

export default function TabLayout() {
  return <ExpoRouterMaterialTopTabs />;
}
```

## Types

### `EffectCallback()`

Supported platforms: Android, iOS, tvOS, Web.

Memoized callback containing the effect, should optionally return a cleanup function.

Returns:

`undefined | void | () => void`

### `ExternalPathString`

Supported platforms: Android, iOS, tvOS, Web.

Literal Type: `union`

Acceptable values are: `{string}:{string}` | `//{string}`

### `Href<T>`

Supported platforms: Android, iOS, tvOS, Web.

The main routing type for Expo Router. It includes all available routes with strongly typed parameters. It can either be:

-   **string**: A full path like `/profile/settings` or a relative path like `../settings`.
-   **object**: An object with a `pathname` and optional `params`. The `pathname` can be a full path like `/profile/settings` or a relative path like `../settings`. The params can be an object of key-value pairs.

An Href can either be a string or an object.

Generic: `T`

Type: T ? T[href] : string | [HrefObject](#hrefobject)

### `HrefObject`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| params(optional) | `UnknownInputParams` | Optional parameters for the route. |
| pathname | `string` | The path of the route. |

### `NativeIntent`

Supported platforms: Android, iOS, tvOS, Web.

Created by using a special file called `+native-intent.tsx` at the top-level of your project's **app** directory. It exports `redirectSystemPath` or `legacy_subscribe` functions, both methods designed to handle URL/path processing.

Useful for re-writing URLs to correctly target a route when unique/referred URLs are incoming from third-party providers or stale URLs from previous versions.

> **See:** For more information on how to use `NativeIntent`, see [Customizing links](/router/advanced/native-intent).

| Property | Type | Description |
| --- | --- | --- |
| legacy_subscribe(optional) | `(listener: (url: string) => void) => undefined | void | () => void` | Useful as an alternative API when a third-party provider doesn't support Expo Router but has support for React Navigation via `Linking.subscribe()` for existing projects. Using this API is not recommended for newer projects or integrations since it is incompatible with Server Side Routing and [Static Rendering](/router/reference/static-rendering), and can become challenging to manage while offline or in a low network environment. |
| redirectSystemPath(optional) | (event: { initial: boolean, path: string }) => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<string | null\> | string | null | A special method used to process URLs in native apps. When invoked, it receives an `options` object with the following properties:
-   **path**: represents the URL or path undergoing processing.
-   **initial**: a boolean indicating whether the path is the app's initial URL.

. Its return value should be a `string`, a `Promise<string | null>`, or `null`. When a falsy value is returned (for example, `null`), no redirection occurs and the app stays on the current path. Note that throwing errors within this method may result in app crashes. It's recommended to wrap your code inside a `try/catch` block and utilize `.catch()` when appropriate.See: For usage information, see Redirecting system paths. |

### `PickPartial`

Supported platforms: Android, iOS, tvOS, Web.

Literal Type: `union`

The list of input keys will become optional, everything else will remain the same.

Acceptable values are: [Omit](https://www.typescriptlang.org/docs/handbook/utility-types.html#omittype-keys)<T, K\> | [Partial](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype)<[Pick](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)<T, K\>\>

### `RedirectConfig`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| destination | `string` | - |
| destinationContextKey | `string` | - |
| external(optional) | `boolean` | - |
| methods(optional) | `string[]` | - |
| permanent(optional) | `boolean` | - |
| source | `string` | - |

### `RelativePathString`

Supported platforms: Android, iOS, tvOS, Web.

Literal Type: `union`

Acceptable values are: `./{string}` | `../{string}` | `'..'`

### `ResultState`

Supported platforms: Android, iOS, tvOS, Web.

Type: PartialState<[NavigationState](https://reactnavigation.org/docs/navigation-state)\> extended by:

| Property | Type | Description |
| --- | --- | --- |
| state(optional) | [ResultState](#resultstate) | - |

### `Route`

Supported platforms: Android, iOS, tvOS, Web.

Type: [Exclude](https://www.typescriptlang.org/docs/handbook/utility-types.html#excludeuniontype-excludedmembers)<Extract[pathname], [RelativePathString](#relativepathstring) | [ExternalPathString](#externalpathstring)\>

### `Router`

Supported platforms: Android, iOS, tvOS, Web.

Returns `router` object for imperative navigation API.

Example

```tsx
import { router } from 'expo-router';
import { Text } from 'react-native';

export default function Route() {

 return (
  <Text onPress={() => router.push('/home')}>Go Home</Text>
 );
}
```

| Property | Type | Description |
| --- | --- | --- |
| back | `() => void` | Goes back in the navigation history. |
| canDismiss | `() => boolean` | Checks if it is possible to dismiss the current screen. Returns `true` if the router is within the stack with more than one screen in stack's history. |
| canGoBack | `() => boolean` | Navigates to a route in the navigator's history if it supports invoking the `back` function. |
| dismiss | `(count: number) => void` | Navigates to the a stack lower than the current screen using the provided count if possible, otherwise 1. If the current screen is the only route, it will dismiss the entire stack. |
| dismissAll | `() => void` | Returns to the first screen in the closest stack. This is similar to [`popToTop`](https://reactnavigation.org/docs/stack-actions/#poptotop) stack action. |
| dismissTo | (href: [Href](/versions/v55.0.0/sdk/router#hreft), options: [NavigationOptions](https://reactnavigation.org/docs/screen-options/)) => void | Dismisses screens until the provided href is reached. If the href is not found, it will instead replace the current screen with the provided `href`. |
| navigate | (href: [Href](/versions/v55.0.0/sdk/router#hreft), options: [NavigationOptions](https://reactnavigation.org/docs/screen-options/)) => void | Navigates to the provided [`href`](#href). |
| prefetch | (name: [Href](/versions/v55.0.0/sdk/router#hreft)) => void | Prefetch a screen in the background before navigating to it |
| push | (href: [Href](/versions/v55.0.0/sdk/router#hreft), options: [NavigationOptions](https://reactnavigation.org/docs/screen-options/)) => void | Navigates to the provided [`href`](#href) using a push operation if possible. |
| replace | (href: [Href](/versions/v55.0.0/sdk/router#hreft), options: [NavigationOptions](https://reactnavigation.org/docs/screen-options/)) => void | Navigates to route without appending to the history. Can be used with [`useFocusEffect`](#usefocuseffecteffect-do_not_pass_a_second_prop) to redirect imperatively to a new screen.See: Using useRouter() hook to redirect. |
| setParams | (params: [Partial](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype)<RouteInputParams<T\>\>) => void | Updates the current route's query params. |

### `ScreenProps`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| dangerouslySingular(optional) | [SingularOptions](#singularoptions) | - |
| getId(optional) | `({ params }: { params: Record<string, any> }) => string | undefined` | - |
| initialParams(optional) | `Record<string, any>` | - |
| listeners(optional) | ScreenListeners<TState, TEventMap\> | (prop: { navigation: any, route: [RouteProp](https://reactnavigation.org/docs/glossary-of-terms/#route-object)<ParamListBase, string\> }) => ScreenListeners<TState, TEventMap\> | - |
| name(optional) | `string` | Name is required when used inside a Layout component. |
| options(optional) | TOptions | (prop: { navigation: any, route: [RouteProp](https://reactnavigation.org/docs/glossary-of-terms/#route-object)<ParamListBase, string\> }) => TOptions | - |
| redirect(optional) | `boolean` | Redirect to the nearest sibling route. If all children are `redirect={true}`, the layout will render `null` as there are no children to render. |

### `SearchOrHash`

Supported platforms: Android, iOS, tvOS, Web.

Literal Type: `union`

Acceptable values are: `?{string}` | `#{string}`

### `SingularOptions`

Supported platforms: Android, iOS, tvOS, Web.

Type: `boolean` or `object` shaped as below:

#### `` (name, params) => `string | undefined` ``

| Parameter | Type | Description |
| --- | --- | --- |
| name[(index signature)](https://www.typescriptlang.org/docs/handbook/2/objects.html#index-signatures) | `string` | - |
| params[(index signature)](https://www.typescriptlang.org/docs/handbook/2/objects.html#index-signatures) | `UnknownOutputParams` | - |

### `SitemapType`

Supported platforms: Android, iOS, tvOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| children | [SitemapType[]](#sitemaptype) | - |
| contextKey | `string` | - |
| filename | `string` | - |
| href | string | [Href](/versions/v55.0.0/sdk/router#hreft) | - |
| isGenerated | `boolean` | - |
| isInitial | `boolean` | - |
| isInternal | `boolean` | - |
