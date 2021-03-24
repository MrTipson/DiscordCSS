# server-bar.css
A utility stylesheet that moves your servers to the top of the screen.

## Variables
Name | Description | Default | Type
---- | ----------- | ------- | -
bar-toggle-r  | `Toggle for server-folders.css - don't change` | `100%` | `length`
bar-toggle-l  | `Toggle for server-folders.css - don't change` | `none` | `length`
sb-top | `Top offset for everything except servers` | `72px` | `length`
sb-right | `Right offset for everything except servers` | `0px` | `length`
sb-bottom | `Bottom offset for everything except servers` | `0px` | `length`
sb-left | `Left offset for everything except servers` | `0px` | `length`
sb-origin | `Transform origin for servers` | `left top` | `transform-origin`
sb-rotate-bar | `Rotate angle for server bar` | `90deg` | `angle`
sb-rotate-bar-inner | `Rotate angle for server bar inner divs` | `180deg` | `angle`
sb-rotate-servers | `Rotate angle for server icons` | `90deg` | `angle`
sb-bar-top | `Top offset for server bar` | `0` | `length`
sb-bar-left | `Left offset for server bar` | `100%` | `length`
sb-bar-height | `Server bar height/length` | `100vw` | `length`
sb-label-left | `Left offset for server/folder name` | `calc(-50% - 42px)` | `length`
sb-label-top | `Top offset for server/folder name` | `calc(50% + 40px)` | `length`

\
`length` : px, %, ...\
`angle` : deg


## Sample configurations
Default donfiguration is  `top`.
<details>
<summary>Left (revert to discord style)</summary>

```css
--sb-top: 0;
--sb-left: 72px;
--sb-rotate-bar: none;
--sb-rotate-bar-inner: none;
--sb-rotate-servers: none;
--sb-bar-left: 0;
--sb-bar-height: 100vh;
--sb-label-left: 0;
--sb-label-top: 0;
/* These are toggles for server-folders.css */
--bar-toggle-l: 100%;
--bar-toggle-r: none;
```
</details>
<details>
<summary>Top</summary>

```css
--sb-top: 72px;
--sb-right: 0px;
--sb-bottom: 0px;
--sb-left: 0px;

--sb-origin: left top;
--sb-rotate-bar: 90deg;
--sb-rotate-bar-inner: 180deg;
--sb-rotate-servers: 90deg;

--sb-bar-top: 0;
--sb-bar-left: 100%;
--sb-bar-height: 100vw;

--sb-label-left: calc(-50% - 42px);
--sb-label-top: calc(50% + 40px);
/* These are toggles for server-folders.css */
--bar-toggle-r: 100%;
--bar-toggle-l: none;
```
</details>
<details>
<summary>Bottom</summary>

```css
--sb-top: 0;
--sb-bottom: 72px;
--sb-rotate-bar: -90deg;
--sb-rotate-bar-inner: none;

--sb-bar-top: 100%;
--sb-bar-left: 0;

--sb-label-top: calc(-50% - 40px);

/* These are toggles for server-folders.css (if used) */
--bar-toggle-l: 100%;
--bar-toggle-r: none;
```
</details>
<details>
<summary>Right</summary>

```css
--sb-top: 0;
--sb-right: 72px;
--sb-rotate-bar: 180deg;
--sb-rotate-bar-inner: 180deg;
--sb-rotate-servers: none;

--sb-bar-top: calc(100% + 26px);
--sb-bar-left: 100%;
--sb-bar-height: 100vh;
--sb-label-top: 0;
--sb-label-left: calc(-50% - 144px);
```
</details>