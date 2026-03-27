---
title: Maps
description: A library that provides access to Google Maps on Android and Apple Maps on iOS.
sourceCodeUrl: 'https://github.com/expo/expo/tree/main/packages/expo-maps'
packageName: 'expo-maps'
platforms: ['ios', 'android']
iconUrl: '/static/images/packages/expo-maps.png'
isAlpha: true
---

# Expo Maps

A library that provides access to Google Maps on Android and Apple Maps on iOS.
Android, iOS

> **This library is currently in alpha and will frequently experience breaking changes.** It is not available in the Expo Go app – use [development builds](/develop/development-builds/introduction) to try it out.

## Installation

```sh
npx expo install expo-maps
```

If you are installing this in an [existing React Native app](/bare/overview), make sure to [install `expo`](/bare/installing-expo-modules) in your project.

  

[Watch: Expo Maps Deep Dive](https://www.youtube.com/watch?v=jDCuaIQ9vd0) — Add Google Maps and Apple Maps to your Expo app with the expo-maps library.

## Configuration

Expo Maps provides access to the platform native map APIs on Android and iOS.

-   **Apple Maps (available on iOS only)**. No additional configuration is required to use it after installing this package.
-   **Google Maps (available on Android only)**. While Google provides a Google Maps SDK for iOS, Expo Maps supports it exclusively on Android. If you want to use Google Maps on iOS, you can look into using an [alternative library](https://reactnative.directory/) or [writing your own](/modules/overview).

### Google Cloud API setup

**Before you can use Google Maps on Android**, you need to register a Google Cloud API project, enable the Maps SDK for Android, and add the associated configuration to your Expo project.

Set up Google Maps on Android

> If you have already registered a project for another Google service on Android, such as Google Sign In, you enable the **Maps SDK for Android** on your project and jump to step 4.

**Register a Google Cloud API project and enable the Maps SDK for Android**

-   Open your browser to the [Google API Manager](https://console.developers.google.com/apis) and create a project.
-   Once it's created, go to the project and enable the **Maps SDK for Android**.

**Copy your app's SHA-1 certificate fingerprint**

-   **If you are deploying your app to the Google Play Store**, you'll need to [upload your app binary to Google Play console](/submit/android) at least once. This is required for Google to generate your app signing credentials.
-   Go to the **[Google Play Console](https://play.google.com/console) > (your app) > Release > Setup > App integrity > App Signing**.
-   Copy the value of **SHA-1 certificate fingerprint**.

**Create an API key**

-   Go to [Google Cloud Credential manager](https://console.cloud.google.com/apis/credentials) and click **Create Credentials**, then **API Key**.
-   In the modal, click **Edit API key**.
-   Under **Key restrictions** > **Application restrictions**, choose **Android apps**.
-   Under **Restrict usage to your Android apps**, click **Add an item**.
-   Add your `android.package` from **app.json** (for example: `com.company.myapp`) to the package name field.
-   Then, add the **SHA-1 certificate fingerprint's** value from step 2.
-   Click **Done** and then click **Save**.

**Add the API key to your project**

-   Copy your **API Key** into your **app.json** under the `android.config.googleMaps.apiKey` field.
-   Create a new development build, and you can now use the Google Maps API on Android with `expo-maps`.

## Permissions

To display the user's location on the map, you need to declare and request location permission beforehand. You can configure this using its built-in [config plugin](/config-plugins/introduction) if you use config plugins in your project ([Continuous Native Generation (CNG)](/workflow/continuous-native-generation)). The plugin allows you to configure various properties that cannot be set at runtime and require building a new app binary to take effect. If your app does **not** use CNG, then you'll need to manually configure the library.

### Example app.json with config plugin

```json
{
  "expo": {
    "plugins": [
      [
        "expo-maps",
        {
          "requestLocationPermission": true,
          "locationPermission": "Allow $(PRODUCT_NAME) to use your location"
        }
      ]
    ]
  }
}
```

### Configurable properties

| Name | Default | Description |
| --- | --- | --- |
| `requestLocationPermission` | `false` | A boolean to add permissions to **AndroidManifest.xml** and **Info.plist**. |
| `locationPermission` | `"Allow $(PRODUCT_NAME) to use your location"` | Only for: iOS. A string to set the [`NSLocationWhenInUseUsageDescription`](#permission-nslocationwheninuseusagedescription) permission message. |

## Usage

```tsx
import { AppleMaps, GoogleMaps } from 'expo-maps';
import { Platform, Text } from 'react-native';

export default function App() {
  if (Platform.OS === 'ios') {
    return <AppleMaps.View style={{ flex: 1 }} />;
  } else if (Platform.OS === 'android') {
    return <GoogleMaps.View style={{ flex: 1 }} />;
  } else {
    return <Text>Maps are only available on Android and iOS</Text>;
  }
}
```

## API

```js
import { AppleMaps, GoogleMaps } from 'expo-maps';

// AppleMaps.View and GoogleMaps.View are the React components
```

## Components

### `AppleMapsView`

Supported platforms: iOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[Component](https://react.dev/reference/react/Component)<[Omit](https://www.typescriptlang.org/docs/handbook/utility-types.html#omittype-keys)<[AppleMapsViewProps](#applemapsviewprops), 'ref'\>\>\>

AppleMapsViewProps

### `annotations`

Supported platforms: iOS.

Optional • Type: [AppleMapsAnnotation[]](#applemapsannotation)

The array of annotations to display on the map.

### `cameraPosition`

Supported platforms: iOS.

Optional • Type: [CameraPosition](/versions/v55.0.0/sdk/maps#cameraposition-2)

The initial camera position of the map.

### `circles`

Supported platforms: iOS.

Optional • Type: [AppleMapsCircle[]](#applemapscircle)

The array of circles to display on the map.

### `colorScheme`

Supported platforms: iOS.

Optional • Type: [AppleMapsColorScheme](#applemapscolorscheme) • Default: `AppleMapsColorScheme.AUTOMATIC`

Controls the color scheme (appearance) of the map. Use this to force the map to display in light or dark mode.

### `markers`

Supported platforms: iOS.

Optional • Type: [AppleMapsMarker[]](#applemapsmarker)

The array of markers to display on the map.

### `onAnnotationClick`

Supported platforms: iOS 18.0+.

Optional • Type: (event: [AppleMapsAnnotation](#applemapsannotation)) => void

Lambda invoked when the annotation is clicked.

### `onCameraMove`

Supported platforms: iOS.

Optional • Type: (event: { bearing: number, coordinates: [Coordinates](#coordinates), latitudeDelta: number, longitudeDelta: number, tilt: number, zoom: number }) => void

Lambda invoked when the map was moved by the user.

### `onCircleClick`

Supported platforms: iOS 18.0+.

Optional • Type: (event: [AppleMapsCircle](#applemapscircle)) => void

Lambda invoked when the circle is clicked.

### `onMapClick`

Supported platforms: iOS.

Optional • Type: (event: { coordinates: [Coordinates](#coordinates) }) => void

Lambda invoked when the user clicks on the map. It won't be invoked if the user clicks on POI or a marker.

### `onMarkerClick`

Supported platforms: iOS 18.0+.

Optional • Type: (event: [AppleMapsMarker](#applemapsmarker)) => void

Lambda invoked when the marker is clicked.

### `onPolygonClick`

Supported platforms: iOS 18.0+.

Optional • Type: (event: [AppleMapsPolygon](#applemapspolygon)) => void

Lambda invoked when the polygon is clicked.

### `onPolylineClick`

Supported platforms: iOS 18.0+.

Optional • Type: (event: [AppleMapsPolyline](#applemapspolyline)) => void

Lambda invoked when the polyline is clicked.

### `polygons`

Supported platforms: iOS.

Optional • Type: [AppleMapsPolygon[]](#applemapspolygon)

The array of polygons to display on the map.

### `polylines`

Supported platforms: iOS.

Optional • Type: [AppleMapsPolyline[]](#applemapspolyline)

The array of polylines to display on the map.

### `properties`

Supported platforms: iOS.

Optional • Type: [AppleMapsProperties](#applemapsproperties)

The properties for the map.

### `ref`

Supported platforms: iOS.

Optional • Type: Ref<[AppleMapsViewType](#applemapsviewtype)\>

### `style`

Supported platforms: iOS.

Optional • Type: StyleProp<[ViewStyle](https://reactnative.dev/docs/view-style-props)\>

### `uiSettings`

Supported platforms: iOS.

Optional • Type: [AppleMapsUISettings](#applemapsuisettings)

The `MapUiSettings` to be used for UI-specific settings on the map.

### `GoogleMapsView`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[Component](https://react.dev/reference/react/Component)<[Omit](https://www.typescriptlang.org/docs/handbook/utility-types.html#omittype-keys)<[GoogleMapsViewProps](#googlemapsviewprops), 'ref'\>\>\>

GoogleMapsViewProps

### `cameraPosition`

Supported platforms: Android.

Optional • Type: [CameraPosition](/versions/v55.0.0/sdk/maps#cameraposition-2)

The initial camera position of the map.

### `circles`

Supported platforms: Android.

Optional • Type: [GoogleMapsCircle[]](#googlemapscircle)

The array of circles to display on the map.

### `colorScheme`

Supported platforms: Android.

Optional • Type: [GoogleMapsColorScheme](#googlemapscolorscheme)

Defines the color scheme for the map.

### `contentPadding`

Supported platforms: Android.

Optional • Type: [GoogleMapsContentPadding](#googlemapscontentpadding)

The padding values used to signal that portions of the map around the edges may be obscured. The map will move the Google logo, etc. to avoid overlapping the padding.

### `mapOptions`

Supported platforms: Android.

Optional • Type: [GoogleMapsMapOptions](#googlemapsmapoptions)

Defines configuration GoogleMapOptions for a GoogleMap

### `markers`

Supported platforms: Android.

Optional • Type: [GoogleMapsMarker[]](#googlemapsmarker)

The array of markers to display on the map.

### `onCameraMove`

Supported platforms: Android.

Optional • Type: (event: { bearing: number, coordinates: [Coordinates](#coordinates), tilt: number, zoom: number }) => void

Lambda invoked when the map was moved by the user.

### `onCircleClick`

Supported platforms: Android.

Optional • Type: (event: [GoogleMapsCircle](#googlemapscircle)) => void

Lambda invoked when the circle is clicked.

### `onMapClick`

Supported platforms: Android.

Optional • Type: (event: { coordinates: [Coordinates](#coordinates) }) => void

Lambda invoked when the user clicks on the map. It won't be invoked if the user clicks on POI or a marker.

### `onMapLoaded`

Supported platforms: Android.

Optional • Type: `() => void`

Lambda invoked when the map is loaded.

### `onMapLongClick`

Supported platforms: Android.

Optional • Type: (event: { coordinates: [Coordinates](#coordinates) }) => void

Lambda invoked when the user long presses on the map.

### `onMarkerClick`

Supported platforms: Android.

Optional • Type: (event: [GoogleMapsMarker](#googlemapsmarker)) => void

Lambda invoked when the marker is clicked

### `onPOIClick`

Supported platforms: Android.

Optional • Type: (event: { coordinates: [Coordinates](#coordinates), name: string }) => void

Lambda invoked when a POI is clicked.

### `onPolygonClick`

Supported platforms: Android.

Optional • Type: (event: [GoogleMapsPolygon](#googlemapspolygon)) => void

Lambda invoked when the polygon is clicked.

### `onPolylineClick`

Supported platforms: Android.

Optional • Type: (event: [GoogleMapsPolyline](#googlemapspolyline)) => void

Lambda invoked when the polyline is clicked.

### `polygons`

Supported platforms: Android.

Optional • Type: [GoogleMapsPolygon[]](#googlemapspolygon)

The array of polygons to display on the map.

### `polylines`

Supported platforms: Android.

Optional • Type: [GoogleMapsPolyline[]](#googlemapspolyline)

The array of polylines to display on the map.

### `properties`

Supported platforms: Android.

Optional • Type: [GoogleMapsProperties](#googlemapsproperties)

The properties for the map.

### `ref`

Supported platforms: Android.

Optional • Type: Ref<[GoogleMapsViewType](#googlemapsviewtype)\>

### `style`

Supported platforms: Android.

Optional • Type: StyleProp<[ViewStyle](https://reactnative.dev/docs/view-style-props)\>

### `uiSettings`

Supported platforms: Android.

Optional • Type: [GoogleMapsUISettings](#googlemapsuisettings)

The `MapUiSettings` to be used for UI-specific settings on the map.

### `userLocation`

Supported platforms: Android.

Optional • Type: [GoogleMapsUserLocation](#googlemapsuserlocation)

User location, overrides default behavior.

### `GoogleStreetView`

Supported platforms: Android.

Type: React.Element<[GoogleStreetViewProps](#googlestreetviewprops)\>

GoogleStreetViewProps

### `isPanningGesturesEnabled`

Supported platforms: Android.

Optional • Type: `boolean`

### `isStreetNamesEnabled`

Supported platforms: Android.

Optional • Type: `boolean`

### `isUserNavigationEnabled`

Supported platforms: Android.

Optional • Type: `boolean`

### `isZoomGesturesEnabled`

Supported platforms: Android.

Optional • Type: `boolean`

### `position`

Supported platforms: Android.

Type: [StreetViewCameraPosition](#streetviewcameraposition)

### `style`

Supported platforms: Android.

Optional • Type: StyleProp<[ViewStyle](https://reactnative.dev/docs/view-style-props)\>

## Hooks

### `useLocationPermissions(options)`

Supported platforms: Android, iOS.

| Parameter | Type |
| --- | --- |
| `options`(optional) | `PermissionHookOptions<object>` |

  

Check or request permissions to access the location. This uses both `requestPermissionsAsync` and `getPermissionsAsync` to interact with the permissions.

Returns: `[PermissionResponse | null, RequestPermissionMethod<permissionresponse>, GetPermissionMethod]</permissionresponse>`

Example

```ts
const [status, requestPermission] = useLocationPermissions();
```

## Methods

### `Maps.getPermissionsAsync()`

Supported platforms: Android, iOS.

Returns: `Promise<permissionresponse>`

### `Maps.requestPermissionsAsync()`

Supported platforms: Android, iOS.

Returns: `Promise<permissionresponse>`

## Types

### `AppleMapsAnnotation`

Supported platforms: iOS.

Type: [AppleMapsMarker](#applemapsmarker) extended by:

| Property | Type | Description |
| --- | --- | --- |
| backgroundColor(optional) | `string` | The background color of the annotation. |
| icon(optional) | [SharedRefType](/versions/v55.0.0/sdk/expo#sharedreftype)<'image'\> | The custom icon to display in the annotation. |
| text(optional) | `string` | The text to display in the annotation. |
| textColor(optional) | `string` | The text color of the annotation. |

### `AppleMapsCircle`

Supported platforms: iOS.

| Property | Type | Description |
| --- | --- | --- |
| center | [Coordinates](#coordinates) | The coordinates of the circle. |
| color(optional) | [ProcessedColorValue](https://reactnative.dev/docs/colors) | string | The color of the circle. |
| id(optional) | `string` | The unique identifier for the circle. This can be used to identify the clicked circle in the `onCircleClick` event. |
| lineColor(optional) | [ProcessedColorValue](https://reactnative.dev/docs/colors) | string | The color of the circle line. |
| lineWidth(optional) | `number` | The width of the circle line. |
| radius | `number` | The radius of the circle (in meters). |
| width(optional) | `number` | The width of the circle. |

### `AppleMapsMarker`

Supported platforms: iOS.

| Property | Type | Description |
| --- | --- | --- |
| coordinates(optional) | [Coordinates](#coordinates) | The coordinates of the marker. |
| id(optional) | `string` | The unique identifier for the marker. This can be used to identify the clicked marker in the `onMarkerClick` event. |
| monogram(optional) | `string` | Supported platforms: iOS 17.0+. A short text (typically initials or 1-2 characters) to display on the marker balloon. This is mutually exclusive with `systemImage`. If both are provided, `systemImage` takes precedence. |
| systemImage(optional) | `string` | The SF Symbol to display for the marker. This is mutually exclusive with `monogram`. If both are provided, `systemImage` takes precedence. |
| tintColor(optional) | `string` | The tint color of the marker. |
| title(optional) | `string` | The title of the marker, displayed in the callout when the marker is clicked. |

### `AppleMapsPointOfInterestCategories`

Supported platforms: iOS.

| Property | Type | Description |
| --- | --- | --- |
| excluding(optional) | [AppleMapPointOfInterestCategory[]](#applemappointofinterestcategory) | The POI categories to exclude. To show all POIs, set this to an empty array. |
| including(optional) | [AppleMapPointOfInterestCategory[]](#applemappointofinterestcategory) | The POI categories to include. To hide all POIs, set this to an empty array. |

### `AppleMapsPolygon`

Supported platforms: iOS.

| Property | Type | Description |
| --- | --- | --- |
| color(optional) | [ProcessedColorValue](https://reactnative.dev/docs/colors) | string | The color of the polygon. |
| coordinates | [Coordinates[]](#coordinates) | The coordinates of the circle. |
| id(optional) | `string` | The unique identifier for the polygon. This can be used to identify the clicked polygon in the `onPolygonClick` event. |
| lineColor(optional) | [ProcessedColorValue](https://reactnative.dev/docs/colors) | string | The color of the polygon. |
| lineWidth(optional) | `number` | The width of the polygon. |

### `AppleMapsPolyline`

Supported platforms: iOS.

| Property | Type | Description |
| --- | --- | --- |
| color(optional) | [ProcessedColorValue](https://reactnative.dev/docs/colors) | string | The color of the polyline. |
| contourStyle(optional) | [AppleMapsContourStyle](#applemapscontourstyle) | The style of the polyline. |
| coordinates | [Coordinates[]](#coordinates) | The coordinates of the polyline. |
| id(optional) | `string` | The unique identifier for the polyline. This can be used to identify the clicked polyline in the `onPolylineClick` event. |
| width(optional) | `number` | The width of the polyline. |

### `AppleMapsProperties`

Supported platforms: iOS.

| Property | Type | Description |
| --- | --- | --- |
| elevation(optional) | [AppleMapsMapStyleElevation](#applemapsmapstyleelevation) | Values you use to determine whether a map renders elevation. |
| emphasis(optional) | [AppleMapsMapStyleEmphasis](#applemapsmapstyleemphasis) | Values that control how the framework emphasizes map features. |
| isMyLocationEnabled(optional) | `boolean` | Whether the user location is shown on the map. Default: `false` |
| isTrafficEnabled(optional) | `boolean` | Whether the traffic layer is enabled on the map. |
| mapType(optional) | [AppleMapsMapType](#applemapsmaptype) | Defines which map type should be used. |
| pointsOfInterest(optional) | [AppleMapsPointOfInterestCategories](#applemapspointofinterestcategories) | A structure you use to define points of interest to include or exclude on a map. |
| polylineTapThreshold(optional) | `number` | The maximum distance in meters from a tap of a polyline for it to be considered a hit. If the distance is greater than the threshold, the polyline is not considered a hit. If a hit occurs, the `onPolylineClick` event will be triggered. Defaults to 20 meters. |
| selectionEnabled(optional) | `boolean` | If true, the user can select a location on the map to get more information. |

### `AppleMapsUISettings`

Supported platforms: iOS.

| Property | Type | Description |
| --- | --- | --- |
| compassEnabled(optional) | `boolean` | Whether the compass is enabled on the map. If enabled, the compass is only visible when the map is rotated. |
| myLocationButtonEnabled(optional) | `boolean` | Whether the my location button is visible. |
| scaleBarEnabled(optional) | `boolean` | Whether the scale bar is displayed when zooming. |
| togglePitchEnabled(optional) | `boolean` | Whether the user is allowed to change the pitch type. |

### `AppleMapsViewType`

Supported platforms: iOS.

| Property | Type | Description |
| --- | --- | --- |
| openLookAroundAsync | (coordinates: [Coordinates](#coordinates)) => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void\> | Opens the look around view at specified coordinates. coordinates: [Coordinates](#coordinates). The coordinates of the location to open the look around view at. |
| selectAnnotation | `(id: string, options: { moveCamera: boolean, zoom: number }) => void` | Supported platforms: iOS 18.0+. Programmatically select an annotation by its ID. `id: string`. The ID of the annotation to select, or `undefined` to clear selection. `options: { moveCamera: boolean, zoom: number }`. Optional configuration for the selection. |
| selectMarker | `(id: string, options: { moveCamera: boolean, zoom: number }) => void` | Supported platforms: iOS 18.0+. Programmatically select a marker by its ID. `id: string`. The ID of the marker to select, or `undefined` to clear selection. `options: { moveCamera: boolean, zoom: number }`. Optional configuration for the selection. |
| setCameraPosition | (config: [CameraPosition](/versions/v55.0.0/sdk/maps#cameraposition-2)) => void | Update camera position. Animation duration is not supported on iOS. config: [CameraPosition](/versions/v55.0.0/sdk/maps#cameraposition-2). New camera postion. |

### `CameraPosition`

Supported platforms: Android, iOS.

| Property | Type | Description |
| --- | --- | --- |
| coordinates(optional) | [Coordinates](#coordinates) | The middle point of the camera. |
| zoom(optional) | `number` | The zoom level of the camera. For some view sizes, lower zoom levels might not be available. |

### `Coordinates`

Supported platforms: Android, iOS.

| Property | Type | Description |
| --- | --- | --- |
| latitude(optional) | `number` | The latitude of the coordinate. |
| longitude(optional) | `number` | The longitude of the coordinate. |

### `GoogleMapsAnchor`

Supported platforms: Android.

| Property | Type | Description |
| --- | --- | --- |
| x | `number` | The normalized horizontal anchor point from 0.0 (left edge) to 1.0 (right edge). |
| y | `number` | The normalized vertical anchor point from 0.0 (top edge) to 1.0 (bottom edge). |

### `GoogleMapsCircle`

Supported platforms: Android.

| Property | Type | Description |
| --- | --- | --- |
| center | [Coordinates](#coordinates) | The coordinates of the circle. |
| clickCoordinates(optional) | [Coordinates](#coordinates) | The geographic coordinates of the click point on the map. |
| color(optional) | [ProcessedColorValue](https://reactnative.dev/docs/colors) | string | The color of the circle. |
| id(optional) | `string` | The unique identifier for the circle. This can be used to identify the clicked circle in the `onCircleClick` event. |
| lineColor(optional) | [ProcessedColorValue](https://reactnative.dev/docs/colors) | string | The color of the circle line. |
| lineWidth(optional) | `number` | The width of the circle line. |
| radius | `number` | The radius of the circle. |

### `GoogleMapsContentPadding`

Supported platforms: Android.

| Property | Type | Description |
| --- | --- | --- |
| bottom(optional) | `number` | The padding on the bottom side of the map. |
| end(optional) | `number` | In LTR contexts, `end` will be applied along the right edge. In RTL contexts, `end` will correspond to the left edge. |
| start(optional) | `number` | In LTR contexts, `start` will be applied along the left edge. In RTL contexts, `start` will correspond to the right edge. |
| top(optional) | `number` | The padding on the top side of the map. |

### `GoogleMapsMapOptions`

Supported platforms: Android.

| Property | Type | Description |
| --- | --- | --- |
| mapId(optional) | `string` | A map ID is a unique identifier that represents Google Map styling and configuration settings that are stored in Google Cloud.See: For more information, see https://developers.google.com/maps/documentation/android-sdk/map-ids/mapid-over |

### `GoogleMapsMapStyleOptions`

Supported platforms: Android.

| Property | Type | Description |
| --- | --- | --- |
| json | `string` | The JSON string of the map style options.See: For creating map style options, see https://mapstyle.withgoogle.com/ |

### `GoogleMapsMarker`

Supported platforms: Android.

| Property | Type | Description |
| --- | --- | --- |
| anchor(optional) | [GoogleMapsAnchor](#googlemapsanchor) | The anchor used to position the anchor relative to its coordinates. Default: `bottom-center of the icon` |
| coordinates(optional) | [Coordinates](#coordinates) | The coordinates of the marker. |
| draggable(optional) | `boolean` | Whether the marker is draggable. |
| icon(optional) | [SharedRefType](/versions/v55.0.0/sdk/expo#sharedreftype)<'image'\> | The custom icon to display for the marker. |
| id(optional) | `string` | The unique identifier for the marker. This can be used to identify the clicked marker in the `onMarkerClick` event. |
| showCallout(optional) | `boolean` | Whether the callout should be shown when the marker is clicked. |
| snippet(optional) | `string` | The snippet of the marker, displayed in the callout when the marker is clicked. |
| title(optional) | `string` | The title of the marker, displayed in the callout when the marker is clicked. |
| zIndex(optional) | `number` | The z-index to use for the marker. Default: `0` |

### `GoogleMapsPolygon`

Supported platforms: Android.

| Property | Type | Description |
| --- | --- | --- |
| color(optional) | [ProcessedColorValue](https://reactnative.dev/docs/colors) | string | The color of the polygon. |
| coordinates | [Coordinates[]](#coordinates) | The coordinates of the circle. |
| id(optional) | `string` | The unique identifier for the polygon. This can be used to identify the clicked polygon in the `onPolygonClick` event. |
| lineColor(optional) | [ProcessedColorValue](https://reactnative.dev/docs/colors) | string | The color of the polygon. |
| lineWidth(optional) | `number` | The width of the polygon. |

### `GoogleMapsPolyline`

Supported platforms: Android.

| Property | Type | Description |
| --- | --- | --- |
| color(optional) | [ProcessedColorValue](https://reactnative.dev/docs/colors) | string | The color of the polyline. |
| coordinates | [Coordinates[]](#coordinates) | The coordinates of the polyline. |
| geodesic(optional) | `boolean` | Whether the polyline is geodesic. |
| id(optional) | `string` | The unique identifier for the polyline. This can be used to identify the clicked polyline in the `onPolylineClick` event. |
| width(optional) | `number` | The width of the polyline. |

### `GoogleMapsProperties`

Supported platforms: Android.

| Property | Type | Description |
| --- | --- | --- |
| isBuildingEnabled(optional) | `boolean` | Whether the building layer is enabled on the map. |
| isIndoorEnabled(optional) | `boolean` | Whether the indoor layer is enabled on the map. |
| isMyLocationEnabled(optional) | `boolean` | Whether finding the user's location is enabled on the map. |
| isTrafficEnabled(optional) | `boolean` | Whether the traffic layer is enabled on the map. |
| mapStyleOptions(optional) | [GoogleMapsMapStyleOptions](#googlemapsmapstyleoptions) | With style options you can customize the presentation of the standard Google map styles, changing the visual display of features like roads, parks, and other points of interest. |
| mapType(optional) | [GoogleMapsMapType](#googlemapsmaptype) | Defines which map type should be used. |
| maxZoomPreference(optional) | `number` | The maximum zoom level for the map. |
| minZoomPreference(optional) | `number` | The minimum zoom level for the map. |
| selectionEnabled(optional) | `boolean` | If true, the user can select a location on the map to get more information. |

### `GoogleMapsUISettings`

Supported platforms: Android.

| Property | Type | Description |
| --- | --- | --- |
| compassEnabled(optional) | `boolean` | Whether the compass is enabled on the map. If enabled, the compass is only visible when the map is rotated. |
| indoorLevelPickerEnabled(optional) | `boolean` | Whether the indoor level picker is enabled . |
| mapToolbarEnabled(optional) | `boolean` | Whether the map toolbar is visible. |
| myLocationButtonEnabled(optional) | `boolean` | Whether the my location button is visible. |
| rotationGesturesEnabled(optional) | `boolean` | Whether rotate gestures are enabled. |
| scaleBarEnabled(optional) | `boolean` | Whether the scale bar is displayed when zooming. |
| scrollGesturesEnabled(optional) | `boolean` | Whether the scroll gestures are enabled. |
| scrollGesturesEnabledDuringRotateOrZoom(optional) | `boolean` | Whether the scroll gestures are enabled during rotation or zoom. |
| tiltGesturesEnabled(optional) | `boolean` | Whether the tilt gestures are enabled. |
| togglePitchEnabled(optional) | `boolean` | Whether the user is allowed to change the pitch type. |
| zoomControlsEnabled(optional) | `boolean` | Whether the zoom controls are visible. |
| zoomGesturesEnabled(optional) | `boolean` | Whether the zoom gestures are enabled. |

### `GoogleMapsUserLocation`

Supported platforms: Android.

| Property | Type | Description |
| --- | --- | --- |
| coordinates | [Coordinates](#coordinates) | User location coordinates. |
| followUserLocation | `boolean` | Should the camera follow the users' location. |

### `GoogleMapsViewType`

Supported platforms: Android.

| Property | Type | Description |
| --- | --- | --- |
| selectMarker | (id: string, options: { moveCamera: boolean, zoom: number }) => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void\> | This is an async operation that animates the camera to the marker. If called rapidly, a previous animation may be cancelled, causing the returned promise to reject. `id: string`. The ID of the marker to select, or `undefined` to clear selection. `options: { moveCamera: boolean, zoom: number }`. Optional configuration for the selection. |
| setCameraPosition | (config: [SetCameraPositionConfig](#setcamerapositionconfig)) => void | Update camera position. config: [SetCameraPositionConfig](#setcamerapositionconfig). New camera position config. |

### `SetCameraPositionConfig`

Supported platforms: Android.

Type: [CameraPosition](/versions/v55.0.0/sdk/maps#cameraposition-2) extended by:

| Property | Type | Description |
| --- | --- | --- |
| duration(optional) | `number` | The duration of the animation in milliseconds. |

### `StreetViewCameraPosition`

Supported platforms: Android.

| Property | Type | Description |
| --- | --- | --- |
| bearing(optional) | `number` | - |
| coordinates | [Coordinates](#coordinates) | - |
| tilt(optional) | `number` | - |
| zoom(optional) | `number` | - |

## Enums

### `AppleMapPointOfInterestCategory`

Supported platforms: iOS.

> **See:** [https://developer.apple.com/documentation/mapkit/AppleMapPointOfInterestCategory](https://developer.apple.com/documentation/mapkit/AppleMapPointOfInterestCategory)

#### `AIRPORT`

`AppleMapPointOfInterestCategory.AIRPORT = "AIRPORT"`

#### `AMUSEMENT_PARK`

`AppleMapPointOfInterestCategory.AMUSEMENT_PARK = "AMUSEMENT_PARK"`

#### `ANIMAL_SERVICE`

`AppleMapPointOfInterestCategory.ANIMAL_SERVICE = "ANIMAL_SERVICE"`

#### `AQUARIUM`

`AppleMapPointOfInterestCategory.AQUARIUM = "AQUARIUM"`

#### `ATM`

`AppleMapPointOfInterestCategory.ATM = "ATM"`

#### `AUTOMOTIVE_REPAIR`

`AppleMapPointOfInterestCategory.AUTOMOTIVE_REPAIR = "AUTOMOTIVE_REPAIR"`

#### `BAKERY`

`AppleMapPointOfInterestCategory.BAKERY = "BAKERY"`

#### `BANK`

`AppleMapPointOfInterestCategory.BANK = "BANK"`

#### `BASEBALL`

`AppleMapPointOfInterestCategory.BASEBALL = "BASEBALL"`

#### `BASKETBALL`

`AppleMapPointOfInterestCategory.BASKETBALL = "BASKETBALL"`

#### `BEACH`

`AppleMapPointOfInterestCategory.BEACH = "BEACH"`

#### `BEAUTY`

`AppleMapPointOfInterestCategory.BEAUTY = "BEAUTY"`

#### `BOWLING`

`AppleMapPointOfInterestCategory.BOWLING = "BOWLING"`

#### `BREWERY`

`AppleMapPointOfInterestCategory.BREWERY = "BREWERY"`

#### `CAFE`

`AppleMapPointOfInterestCategory.CAFE = "CAFE"`

#### `CAMPGROUND`

`AppleMapPointOfInterestCategory.CAMPGROUND = "CAMPGROUND"`

#### `CAR_RENTAL`

`AppleMapPointOfInterestCategory.CAR_RENTAL = "CAR_RENTAL"`

#### `CASTLE`

`AppleMapPointOfInterestCategory.CASTLE = "CASTLE"`

#### `CONVENTION_CENTER`

`AppleMapPointOfInterestCategory.CONVENTION_CENTER = "CONVENTION_CENTER"`

#### `DISTILLERY`

`AppleMapPointOfInterestCategory.DISTILLERY = "DISTILLERY"`

#### `EV_CHARGER`

`AppleMapPointOfInterestCategory.EV_CHARGER = "EV_CHARGER"`

#### `FAIRGROUND`

`AppleMapPointOfInterestCategory.FAIRGROUND = "FAIRGROUND"`

#### `FIRE_STATION`

`AppleMapPointOfInterestCategory.FIRE_STATION = "FIRE_STATION"`

#### `FISHING`

`AppleMapPointOfInterestCategory.FISHING = "FISHING"`

#### `FITNESS_CENTER`

`AppleMapPointOfInterestCategory.FITNESS_CENTER = "FITNESS_CENTER"`

#### `FOOD_MARKET`

`AppleMapPointOfInterestCategory.FOOD_MARKET = "FOOD_MARKET"`

#### `FORTRESS`

`AppleMapPointOfInterestCategory.FORTRESS = "FORTRESS"`

#### `GAS_STATION`

`AppleMapPointOfInterestCategory.GAS_STATION = "GAS_STATION"`

#### `GO_KART`

`AppleMapPointOfInterestCategory.GO_KART = "GO_KART"`

#### `GOLF`

`AppleMapPointOfInterestCategory.GOLF = "GOLF"`

#### `HIKING`

`AppleMapPointOfInterestCategory.HIKING = "HIKING"`

#### `HOSPITAL`

`AppleMapPointOfInterestCategory.HOSPITAL = "HOSPITAL"`

#### `HOTEL`

`AppleMapPointOfInterestCategory.HOTEL = "HOTEL"`

#### `KAYAKING`

`AppleMapPointOfInterestCategory.KAYAKING = "KAYAKING"`

#### `LANDMARK`

`AppleMapPointOfInterestCategory.LANDMARK = "LANDMARK"`

#### `LAUNDRY`

`AppleMapPointOfInterestCategory.LAUNDRY = "LAUNDRY"`

#### `LIBRARY`

`AppleMapPointOfInterestCategory.LIBRARY = "LIBRARY"`

#### `MAILBOX`

`AppleMapPointOfInterestCategory.MAILBOX = "MAILBOX"`

#### `MARINA`

`AppleMapPointOfInterestCategory.MARINA = "MARINA"`

#### `MINI_GOLF`

`AppleMapPointOfInterestCategory.MINI_GOLF = "MINI_GOLF"`

#### `MOVIE_THEATER`

`AppleMapPointOfInterestCategory.MOVIE_THEATER = "MOVIE_THEATER"`

#### `MUSEUM`

`AppleMapPointOfInterestCategory.MUSEUM = "MUSEUM"`

#### `MUSIC_VENUE`

`AppleMapPointOfInterestCategory.MUSIC_VENUE = "MUSIC_VENUE"`

#### `NATIONAL_MONUMENT`

`AppleMapPointOfInterestCategory.NATIONAL_MONUMENT = "NATIONAL_MONUMENT"`

#### `NATIONAL_PARK`

`AppleMapPointOfInterestCategory.NATIONAL_PARK = "NATIONAL_PARK"`

#### `NIGHTLIFE`

`AppleMapPointOfInterestCategory.NIGHTLIFE = "NIGHTLIFE"`

#### `PARK`

`AppleMapPointOfInterestCategory.PARK = "PARK"`

#### `PARKING`

`AppleMapPointOfInterestCategory.PARKING = "PARKING"`

#### `PHARMACY`

`AppleMapPointOfInterestCategory.PHARMACY = "PHARMACY"`

#### `PLANETARIUM`

`AppleMapPointOfInterestCategory.PLANETARIUM = "PLANETARIUM"`

#### `POLICE`

`AppleMapPointOfInterestCategory.POLICE = "POLICE"`

#### `POST_OFFICE`

`AppleMapPointOfInterestCategory.POST_OFFICE = "POST_OFFICE"`

#### `PUBLIC_TRANSPORT`

`AppleMapPointOfInterestCategory.PUBLIC_TRANSPORT = "PUBLIC_TRANSPORT"`

#### `RESTAURANT`

`AppleMapPointOfInterestCategory.RESTAURANT = "RESTAURANT"`

#### `RESTROOM`

`AppleMapPointOfInterestCategory.RESTROOM = "RESTROOM"`

#### `ROCK_CLIMBING`

`AppleMapPointOfInterestCategory.ROCK_CLIMBING = "ROCK_CLIMBING"`

#### `RV_PARK`

`AppleMapPointOfInterestCategory.RV_PARK = "RV_PARK"`

#### `SCHOOL`

`AppleMapPointOfInterestCategory.SCHOOL = "SCHOOL"`

#### `SKATE_PARK`

`AppleMapPointOfInterestCategory.SKATE_PARK = "SKATE_PARK"`

#### `SKATING`

`AppleMapPointOfInterestCategory.SKATING = "SKATING"`

#### `SKIING`

`AppleMapPointOfInterestCategory.SKIING = "SKIING"`

#### `SOCCER`

`AppleMapPointOfInterestCategory.SOCCER = "SOCCER"`

#### `SPA`

`AppleMapPointOfInterestCategory.SPA = "SPA"`

#### `STADIUM`

`AppleMapPointOfInterestCategory.STADIUM = "STADIUM"`

#### `STORE`

`AppleMapPointOfInterestCategory.STORE = "STORE"`

#### `SURFING`

`AppleMapPointOfInterestCategory.SURFING = "SURFING"`

#### `SWIMMING`

`AppleMapPointOfInterestCategory.SWIMMING = "SWIMMING"`

#### `TENNIS`

`AppleMapPointOfInterestCategory.TENNIS = "TENNIS"`

#### `THEATER`

`AppleMapPointOfInterestCategory.THEATER = "THEATER"`

#### `UNIVERSITY`

`AppleMapPointOfInterestCategory.UNIVERSITY = "UNIVERSITY"`

#### `VOLLEYBALL`

`AppleMapPointOfInterestCategory.VOLLEYBALL = "VOLLEYBALL"`

#### `WINERY`

`AppleMapPointOfInterestCategory.WINERY = "WINERY"`

#### `ZOO`

`AppleMapPointOfInterestCategory.ZOO = "ZOO"`

### `AppleMapsColorScheme`

Supported platforms: iOS.

Controls the color scheme (appearance) of the map.

#### `AUTOMATIC`

`AppleMapsColorScheme.AUTOMATIC = "AUTOMATIC"`

The map follows the app's color scheme (light/dark mode).

#### `DARK`

`AppleMapsColorScheme.DARK = "DARK"`

The map is always displayed in dark mode.

#### `LIGHT`

`AppleMapsColorScheme.LIGHT = "LIGHT"`

The map is always displayed in light mode.

### `AppleMapsContourStyle`

Supported platforms: iOS.

The style of the polyline.

#### `GEODESIC`

`AppleMapsContourStyle.GEODESIC = "GEODESIC"`

A geodesic line.

#### `STRAIGHT`

`AppleMapsContourStyle.STRAIGHT = "STRAIGHT"`

A straight line.

### `AppleMapsMapStyleElevation`

Supported platforms: iOS.

#### `AUTOMATIC`

`AppleMapsMapStyleElevation.AUTOMATIC = "AUTOMATIC"`

The default elevation style, that renders a flat, 2D map.

#### `FLAT`

`AppleMapsMapStyleElevation.FLAT = "FLAT"`

A flat elevation style.

#### `REALISTIC`

`AppleMapsMapStyleElevation.REALISTIC = "REALISTIC"`

A value that renders a realistic, 3D map.

### `AppleMapsMapStyleEmphasis`

Supported platforms: iOS.

#### `AUTOMATIC`

`AppleMapsMapStyleEmphasis.AUTOMATIC = "AUTOMATIC"`

The default level of emphasis.

#### `MUTED`

`AppleMapsMapStyleEmphasis.MUTED = "MUTED"`

A muted emphasis style, that deemphasizes the map’s imagery.

### `AppleMapsMapType`

Supported platforms: iOS.

The type of map to display.

#### `HYBRID`

`AppleMapsMapType.HYBRID = "HYBRID"`

A satellite image of the area with road and road name layers on top.

#### `IMAGERY`

`AppleMapsMapType.IMAGERY = "IMAGERY"`

A satellite image of the area.

#### `STANDARD`

`AppleMapsMapType.STANDARD = "STANDARD"`

A street map that shows the position of all roads and some road names.

### `GoogleMapsColorScheme`

Supported platforms: Android.

#### `DARK`

`GoogleMapsColorScheme.DARK = "DARK"`

#### `FOLLOW_SYSTEM`

`GoogleMapsColorScheme.FOLLOW_SYSTEM = "FOLLOW_SYSTEM"`

#### `LIGHT`

`GoogleMapsColorScheme.LIGHT = "LIGHT"`

### `GoogleMapsMapType`

Supported platforms: Android.

The type of map to display.

#### `HYBRID`

`GoogleMapsMapType.HYBRID = "HYBRID"`

Satellite imagery with roads and points of interest overlayed.

#### `NORMAL`

`GoogleMapsMapType.NORMAL = "NORMAL"`

Standard road map.

#### `SATELLITE`

`GoogleMapsMapType.SATELLITE = "SATELLITE"`

Satellite imagery.

#### `TERRAIN`

`GoogleMapsMapType.TERRAIN = "TERRAIN"`

Topographic data.

## Permissions

### Android

To show the user's location on the map, the `expo-maps` library requires the following permissions:

-   `ACCESS_COARSE_LOCATION`: for approximate device location
-   `ACCESS_FINE_LOCATION`: for precise device location

| Android Permission | Description |
| --- | --- |
| `ACCESS_COARSE_LOCATION` | Allows an app to access approximate location. |
| `ACCESS_FINE_LOCATION` | Allows an app to access precise location. |
| `FOREGROUND_SERVICE` | Allows a regular application to use Service.startForeground. |
| `FOREGROUND_SERVICE_LOCATION` | Allows a regular application to use Service.startForeground with the type "location". |
| `ACCESS_BACKGROUND_LOCATION` | Allows an app to access location in the background. |

### iOS

The following usage description keys are used by this library:

| Info.plist Key | Description |
| --- | --- |
| `NSLocationWhenInUseUsageDescription` | A message that tells the user why the app is requesting access to the user’s location information while the app is running in the foreground. |
