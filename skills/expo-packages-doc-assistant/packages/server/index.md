---
title: Server
description: Server-side API and runtime for Expo Router projects.
sourceCodeUrl: 'https://github.com/expo/expo/tree/main/packages/expo-server'
packageName: 'expo-server'
platforms: ['server']
---

# Expo Server

Server-side API and runtime for Expo Router projects.
Server

`expo-server` is a server-side API and runtime library for Expo Router. It provides helpers you can use in your Expo Router API routes or other server code, and contains adapters to run Expo Router server exports.

## Installation

```sh
npx expo install expo-server
```

To use `expo-server` in your project, you need to configure your Expo Router project to export in `server` mode. Follow the instructions from Expo Router's API Routes guide:

[API Routes](/router/web/api-routes) — Learn how to create server endpoints with Expo Router.

## Usage

`expo-server`'s runtime APIs can only be used in server-side code and give you access to the server-side runtime environment. The runtime API exposes functions that can be called within the async context of request handlers and give you information about the current request or schedule tasks that run concurrently to the incoming request.

### Accessing request metadata

```ts
import { origin, environment } from 'expo-server';

export async function GET() {
  return Response.json({
    isProduction: environment() == null,
    isStaging: environment() === 'staging',
    origin: origin(),
  });
}
```

### Scheduling tasks

```ts
import { runTask, deferTask } from 'expo-server';

export async function GET() {
  runTask(async () => {
    console.log('will run immediately.');
  });

  deferTask(async () => {
    console.log('will run after the response resolved.');
  });

  return Response.json({ success: true });
}
```

## Adapters

`expo-server` exposes adapters to run Expo Router server-side exports in different environments or on different cloud provider serverless functions. Typically, every runtime needs its own adapter to function with the `expo-server` runtime. Before deploying to these providers, it is good to be familiar with the basics of [`npx expo export`](/more/expo-cli#exporting) command.

| Adapter | Provider |
| --- | --- |
| `expo-server/adapter/bun` | [Bun](https://bun.com/docs) |
| `expo-server/adapter/express` | [Express](https://expressjs.com/en/5x/api.html) |
| `expo-server/adapter/http` | [Node.js](https://nodejs.org/api/http.html) |
| `expo-server/adapter/netlify` | [Netlify Functions](https://docs.netlify.com/build/functions/overview/) |
| `expo-server/adapter/vercel` | [Vercel Functions](https://vercel.com/docs/functions) |
| `expo-server/adapter/workerd` | [Cloudflare Workers](https://developers.cloudflare.com/pages/functions/) |

To learn how to host API routes on different third-party services, follow the instructions from Expo Router's API Routes guide:

[API Routes](/router/web/api-routes#hosting-on-third-party-services) — Learn how to host API Routes on third-party services.

By convention, all adapters export a `createRequestHandler` function that accepts a parameters object. This accepts a `build` parameter that must be set to the relative path to the `dist/server` output directory that `npx expo export` created. Some adapters may also accept more values to configure the runtime API.

```ts
import path from 'node:path';
import { createRequestHandler } from 'expo-server/adapter/http';

const onRequest = createRequestHandler({
  build: path.join(process.cwd(), 'dist/server'),
  environment: process.env.NODE_ENV,
});
```

## API

## Classes

### `StatusError`

Supported platforms: Server.

Type: Class extends [Error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)

An error response representation which can be thrown anywhere in server-side code.

A `StatusError` can be thrown by a request handler and will be caught by the `expo-server` runtime and replaced by a `Response` with the `status` and `body` that's been passed to the `StatusError`.

Example

```ts
import { StatusError } from 'expo-server';

export function GET(request, { postId }) {
  if (!postId) {
    throw new StatusError(400, 'postId parameter is required');
  }
}
```

StatusError Properties

### `body`

Supported platforms: Server.

Type: `string`

### `status`

Supported platforms: Server.

Type: `number`

## Methods

### `deferTask(fn)`

Supported platforms: Server.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | () => void | [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<unknown\> | A task function to execute after the request handler has finished. |

  

Defers a task until after a response has been sent.

This only calls the task function once the request handler has finished resolving a `Response` and keeps the request handler alive until the task is completed. This is useful to run non-critical tasks after the request handler, for example to log analytics datapoints. If the request handler rejects with an error, deferred tasks won't be executed.

Returns: `void`

### `environment()`

Supported platforms: Server.

Returns the request's environment, if the server runtime supports this.

In EAS Hosting, the returned environment name is the [alias or deployment identifier](https://docs.expo.dev/eas/hosting/deployments-and-aliases/), but the value may differ for other providers.

Returns: `string | null`

A request environment name, or `null` for production.

### `origin()`

Supported platforms: Server.

Returns the current request's URL.

This typically returns the request's URL, or on certain platform, the origin of the request. This does not use the `Origin` header in development as it may contain an untrusted value.

Returns: `string | null`

A request origin

### `requestHeaders()`

Supported platforms: Server.

Returns an immutable copy of the current request's headers.

Returns: `ImmutableHeaders`

### `runTask(fn)`

Supported platforms: Server.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | () => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<unknown\> | A task function to execute. The request handler will be kept alive until this task finishes. |

  

Runs a task immediately and instructs the runtime to complete the task.

A request handler may be terminated as soon as the client has finished the full `Response` and unhandled promise rejections may not be logged properly. To run tasks concurrently to a request handler and keep the request alive until the task is completed, pass a task function to `runTask` instead. The request handler will be kept alive until the task completes.

Returns: `void`

### `setResponseHeaders(updateHeaders)`

Supported platforms: Server.

| Parameter | Type | Description |
| --- | --- | --- |
| `updateHeaders` | [Headers](https://developer.mozilla.org/en-US/docs/Web/API/Headers) | Record<string, string | string[]\> | (headers: [Headers](https://developer.mozilla.org/en-US/docs/Web/API/Headers)) => void | [Headers](https://developer.mozilla.org/en-US/docs/Web/API/Headers) | A `Headers` object, a record of headers, or a function that receives `Headers` to be updated or can return a `Headers` object that will be merged into the response headers. |

  

Sets headers on the `Response` the current request handler will return.

This only updates the headers once the request handler has finished and resolved a `Response`. It will either receive a set of `Headers` or an equivalent object containing headers, which will be merged into the response's headers once it's returned.

Returns: `void`

## Interfaces

### `ImmutableHeaders`

Supported platforms: Server.

Extends: `_ImmutableHeaders`

An immutable version of the Fetch API's `Headers` object. It cannot be mutated or modified.

### `ImmutableRequest`

Supported platforms: Server.

Extends: `_ImmutableRequest`

An immutable version of the Fetch API's `Request` object. It cannot be mutated or modified, its headers are immutable, and you won't have access to the request body.

| Property | Type | Description |
| --- | --- | --- |
| method | `string` | The **`method`** read-only property of the `POST`, etc.) A String indicating the method of the request. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Request/method) |
| url | `string` | The **`url`** read-only property of the Request interface contains the URL of the request. [MDN Reference](https://developer.mozilla.org/docs/Web/API/Request/url) |

### `MiddlewareMatcher`

Supported platforms: Server.

Middleware matcher settings that restricts the middleware to run conditionally.

| Property | Type | Description |
| --- | --- | --- |
| methods(optional) | `string[]` | Set this to a list of HTTP methods to conditionally run middleware on. By default, middleware will match all HTTP methods. . Example. `['POST', 'PUT', 'DELETE']` |
| patterns(optional) | (string | [RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp))[] | Set this to a list of path patterns to conditionally run middleware on. This may be exact paths, paths containing parameter or catch-all segments (`'/posts/[postId]'` or `'/blog/[. .slug]'`), or regular expressions matching paths. . Example. `['/api', '/posts/[id]', '/blog/[. .slug]']` |

### `MiddlewareSettings`

Supported platforms: Server.

Exported from a `+middleware.ts` file to configure the server-side middleware function.

> **See:** [https://docs.expo.dev/router/reference/middleware/](https://docs.expo.dev/router/reference/middleware/)

Example

```ts
import type { MiddlewareSettings } from 'expo-server';

export const unstable_settings: MiddlewareSettings = {
  matcher: {
    methods: ['GET'],
    patterns: ['/api', '/admin/[...path]'],
  },
};
```

| Property | Type | Description |
| --- | --- | --- |
| matcher(optional) | [MiddlewareMatcher](#middlewarematcher) | Matcher definition that restricts the middleware to run conditionally. |

## Types

### `LoaderFunction(request, params)`

Supported platforms: Server.

Function type for route loaders. Loaders are executed on the server during SSR/SSG to fetch data required by a route.

During SSG (Static Site Generation), the `request` parameter will be `undefined` as there is no HTTP request at build time.

> **See:** [Data loaders](/router/web/data-loaders) for more information.

Example

```ts
import type { LoaderFunction } from 'expo-server';

export const loader: LoaderFunction = async (request, params) => {
  const data = await fetchData(params.id);
  return { data };
};
```

| Parameter | Type | Description |
| --- | --- | --- |
| `request` | [ImmutableRequest](#immutablerequest) | undefined | An `ImmutableRequest` with read-only headers and no body access. In SSG, this is `undefined` |
| `params` | `Record<string, string | string[]>` | Route parameters extracted from the URL path |

Returns:

[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<T\> | T

### `MiddlewareFunction(request)`

Supported platforms: Server.

Middleware function type. Middleware run for every request in your app, or on specified conditionally matched methods and path patterns, as per [`MiddlewareMatcher`](#middlewarematcher).

> **See:** [Server middleware](https://docs.expo.dev/router/web/middleware/) for more information.

Example

```ts
import type { MiddlewareFunction } from 'expo-server';

const middleware: MiddlewareFunction = async (request) => {
  console.log(`Middleware executed for: ${request.url}`);
};

export default middleware;
```

| Parameter | Type | Description |
| --- | --- | --- |
| `request` | [ImmutableRequest](#immutablerequest) | An `ImmutableRequest` with read-only headers and no body access |

Returns:

[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[Response](https://developer.mozilla.org/en-US/docs/Web/API/Response) | void\> | [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response) | void
