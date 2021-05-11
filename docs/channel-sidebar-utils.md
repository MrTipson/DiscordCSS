# channel-sidebar-utils.css
A utility stylesheet that styles the left sidebar (server channels).
Includes some transitions (animations), adjustable margins and colors.

## Variables
`bumper` : Block that appears on hover\
`unread` : Block that appears for channels with unread messages

Name | Description | Default | Type
---- | ----------- | ------- | -
csu-bumper-color  | Color of the bumper | --interactive-active | color
csu-bumper-width  | Width of the bumper | 6px | length
csu-anim-duration | Duration of the transition | .5s | time
csu-unread-width | Width of the unread block | 2px | length
csu-init-margin | Margin when not hovered | --csu-bumper-width | length
csu-anim-transition | Transition function | cubic-bezier(1, 0, 1, 1) | function
csu-bg-hover | Background of channel when hovered | --background-modifier-hover | color
csu-bg-selected | Background of channel when selected | --background-modifier-selected | color

\
`length` : px, %, ...\
`time` : s, ms\
`function` : animation transition function
