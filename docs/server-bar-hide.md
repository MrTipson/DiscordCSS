# server-bar-hide.css
A utility stylesheet that hides the server bar unless hovered.

## Variables
Name | Description | Default | Type
---- | ----------- | ------- | -
sb-collapsed-width | Width of the collapsed server bar | 10px | length
sb-transition-duration | Duration of the animation | .5s | time
sb-collapsed-left | Space on the left when collapsed | sb-collapsed-width | length
sb-collapsed-top | Space on the top when collapsed | sb-collapsed-width | length
sb-collapsed-bottom | Space on the bottom when collapsed | sb-collapsed-width | length
sb-collapsed-right | Space on the right when collapsed | sb-collapsed-width | length
sb-transition-property | Side of transition | left | property [top, left, right, bottom]

## Configuration
Similar to server-bar.css, some tweaks are necessary, depending on the side of the server bar.

Default: left

`Up` sets up automatically with server-bar.css.

<details>
<summary>Right</summary>

```css
--sb-collapsed-right: 10px;
--sb-collapsed-top:0px;
--sb-transition-property: right;
```
</details>
<details>
<summary>Bottom</summary>

```css
--sb-collapsed-bottom: 10px;
--sb-collapsed-top:0px;
--sb-transition-property: bottom;
```
</details>