---
title: VideoThumbnails
description: A library that allows you to generate an image to serve as a thumbnail from a video file.
sourceCodeUrl: 'https://github.com/expo/expo/tree/main/packages/expo-video-thumbnails'
packageName: 'expo-video-thumbnails'
platforms: ['android', 'ios', 'tvos', 'expo-go']
isDeprecated: true
---

# Expo VideoThumbnails

A library that allows you to generate an image to serve as a thumbnail from a video file.
Android, iOS, tvOS, Included in Expo Go

> **Deprecated:** Video Thumbnails library has been deprecated in favor of [`generateThumbnailsAsync`](/versions/latest/sdk/video#generatethumbnailsasynctimes-options) from [`expo-video`](/versions/latest/sdk/video). `expo-video-thumbnails` is not receiving patches and will be removed in SDK 56.

`expo-video-thumbnails` allows you to generate an image to serve as a thumbnail from a video file.

## Installation

```sh
npx expo install expo-video-thumbnails
```

If you are installing this in an [existing React Native app](/bare/overview), make sure to [install `expo`](/bare/installing-expo-modules) in your project.

## Usage

```jsx
import { useState } from 'react';
import { StyleSheet, Button, View, Image, Text } from 'react-native';
import * as VideoThumbnails from 'expo-video-thumbnails';

export default function App() {
  const [image, setImage] = useState(null);

  const generateThumbnail = async () => {
    try {
      const { uri } = await VideoThumbnails.getThumbnailAsync(
        'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4',
        {
          time: 15000,
        }
      );
      setImage(uri);
    } catch (e) {
      console.warn(e);
    }
  };

  return (
    <View style={styles.container}>
      <Button onPress={generateThumbnail} title="Generate thumbnail" />
      {image && <Image source={{ uri: image }} style={styles.image} />}
      <Text>{image}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  image: {
    width: 200,
    height: 200,
  },
});
```

## API

```js
import * as VideoThumbnails from 'expo-video-thumbnails';
```

## Methods

### `VideoThumbnails.getThumbnailAsync(sourceFilename, options)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `sourceFilename` | `string` | An URI of the video, local or remote. |
| `options`(optional) | [VideoThumbnailsOptions](#videothumbnailsoptions) | A map defining how modified thumbnail should be created. Default: `{}` |

  

Create an image thumbnail from video provided via `sourceFilename`.

Returns: `Promise<videothumbnailsresult>`

Returns a promise which fulfils with [`VideoThumbnailsResult`](#videothumbnailsresult).

## Types

### `VideoThumbnailsOptions`

Supported platforms: Android, iOS, tvOS.

| Property | Type | Description |
| --- | --- | --- |
| headers(optional) | `Record<string, string>` | In case `sourceFilename` is a remote URI, `headers` object is passed in a network request. |
| quality(optional) | `number` | A value in range `0.0` - `1.0` specifying quality level of the result image. `1` means no compression (highest quality) and `0` the highest compression (lowest quality). |
| time(optional) | `number` | The time position where the image will be retrieved in ms. |

### `VideoThumbnailsResult`

Supported platforms: Android, iOS, tvOS.

| Property | Type | Description |
| --- | --- | --- |
| height | `number` | Height of the created image. |
| uri | `string` | URI to the created image (usable as the source for an Image/Video element). |
| width | `number` | Width of the created image. |
