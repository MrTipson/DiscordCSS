 # DiscordCSS

DiscordCSS is a set of css stylesheets that aims to create a more pleasant Discord experience.
It's modularity means that you can mix and match whichever parts you want.

The Discord app needs to be patched, instructions can be found on the project [wiki](https://github.com/MrTipson/DiscordCSS/wiki).
If you're using the web version it should be available via an extension to your browser. Something like [Amino](https://chrome.google.com/webstore/detail/amino-live-css-editor/pbcpfbcibpcbfbmddogfhcijfpboeaaf) will do, but you can use anything you 
want.

If you would like me to add a certain functionality, you can make an issue or fork the repo and make a pull request

# Stylesheets

All of the stylesheets are modular. Import each one by writing `@import url("<link>");` at the top of your main css file (example: `@import url("https://mrtipson.github.io/DiscordCSS/theme.css");`.\
Once you have it imported, you can keep the default values or set the variables again to change their values.

*Modern browsers disallow opening local files, so to use a stylesheet, you have to link to an externally hosted file.*

## theme.css

`https://mrtipson.github.io/DiscordCSS/theme.css`\
As the centerpiece of this project, **theme.css** changes up the look and feel of discord the most, affecting these elements:
- the background
- context (right click) menus
- scrollbars
- icons
- buttons
- gradients, borders, and more...

## layout.css

`https://mrtipson.github.io/DiscordCSS/layout.css`\
As another major change to how things behave, **layout.css** turns things around a bit:
- server bar
- server folders 

## banter.css

`https://mrtipson.github.io/DiscordCSS/banter.css`\
A stylesheet dedicated to me exploring dumb shit i can make with css in discord.\
Not meant for everyday use but checking out what i've been up to could be fun from time to time.

# License

This project is licensed under [the MIT license](https://github.com/MrTipson/DiscordCSS/blob/HEAD/LICENSE).
