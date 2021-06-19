# border-utils.css
A utility stylesheet that provides selectors for important borders in the discord layout.

## Variables
Name | Description | Default | Type
---- | ----------- | ------- | -
bu-border  | Border between divs | none | border shorthand
bu-image-src  | Image to use | none | image
bu-image-slice  | Slice sections | 100% | border-image-slice
bu-image-width  | Width of image border | 1 | border-image-width
bu-image-outset  | Slice sections | 0 | border-image-outset
bu-image-repeat  | Slice sections | round | border-image-repeat
  
## Notes
If you wish to use the `bu-image` tags, `bu-border` should be set to a trivial value which cant be none (something like `3px solid`). Note that the `bu-border` width still impacts how the border image looks.

If you only wish to use `border`, `bu-image-src` can be set to `none`.

## Examples
```
--bu-border: 3px solid;
--bu-image-src: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' viewBox='0 0 100 100' width='100' height='100'%3E%3Cpath d='m 0 0 h 100 v 100 h -100 v -101 M 33 0 L 0 33 M 66 0 L 0 66 M 100 0 L 0 100 M 33 100 L 100 33 M 66 100 L 100 66' fill='transparent' stroke='red' stroke-width='3'%3E%3C/path%3E%3C/svg%3E");
--bu-image-slice: 10%;
```

```
--bu-border: 3px solid;
--bu-image-src: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' viewBox='0 0 100 100' width='100' height='100'%3E%3Cpath d='m 0 0 h 100 v 100 h -100 v -100 q 16 8 33 0 q 16 8 33 0 q 16 8 34 0 q -8 16 0 33 q -8 16 0 33 q -8 16 0 34 q -16 -8 -33 0 q -16 -8 -33 0 q -16 -8 -34 0 q 8 -16 0 -33 q 8 -16 0 -33 q 8 -16 0 -34' fill='transparent' stroke='%23717171' stroke-width='3'%3E%3C/path%3E%3C/svg%3E");
--bu-image-slice: 6%;
```
>Note: tweaking the slice values/border width can vastly impact the look of borders.