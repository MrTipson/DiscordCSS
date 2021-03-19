# base.css
A core stylesheet to any theme. Adds variables for hardcoded colors and 
splits certain discord variables. Hides the download button on the online client.

## Variables
Name | Description | Default | Type
---- | ----------- | ------- | -
color-main  | `Add/explore servers and home` | `#7289da` | `color`
progress-track-full  | `User volume adjust - bar filled` | `rgb(114 118 125)` | `color`
progress-track-empty | `User volume adjust - bar empty` | `rgb(182 184 188)` | `color`
progress-thumb | `User volume adjust - thumb` | `rgb(48 51 56)` | `color`
background-image | `Image in the background` | `none` | `image`
background-color | `Color in the background` | `none` | `color`
background-filter | `Filter for the background` | `none` | `filter`
background-markup | `Color behind markup blocks` | `--background-secondary` | `color`
background-embed | `Background for embedded content` | `--background-secondary` | `color`
background-modal | `Background of modal popups` | `--background-primary` | `color`
background-floating | `Background of not so modal popups` | `--background-primary` | `color`
background-dropdown | `Dropdown menu` | `--background-primary` | `color`
background-primary-extra | `Override background-primary` | `--background-primary` | `color`
background-mentioned-before | `Color of border in front of mention` | `#faa61a` | `color`

\
`image` : background-image tag\
`filter` : filter tag\
`color` : background-color tag