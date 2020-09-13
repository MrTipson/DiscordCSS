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

Some stylesheets have screenshots of examples for the theme. They can be found in the [examples](examples/).

## base.css
`https://mrtipson.github.io/DiscordCSS/banter.css`\
The core stylesheet to any of my other themes.
<details>
 <summary>Image</summary>
 
 ![Dark](https://i.imgur.com/12BIQ9k.png)
 ![Light](https://i.imgur.com/BF8gmbI.png)
</details>

## candy-land.css
`https://mrtipson.github.io/DiscordCSS/candy-land.cs`\
A theme centered around rounded edges, compartmentalised feel and translucent backgrounds.
<details>
 <summary>Image</summary>
 
 ![Dark](https://i.imgur.com/UG1WMs7.png)
 ![Light](https://i.imgur.com/fT6Eomk.png)
 (the screenshot is from the premade stylesheet for the theme - things dont look well with default values)
</details>

## server-bar.css
`https://mrtipson.github.io/DiscordCSS/server-bar.css`\
Move your servers to the top of the screen.
<details>
 <summary>Image</summary>
 
 ![Server-bar](https://i.imgur.com/5e3Hqee.png)
</details>

## server-folders.css
`https://mrtipson.github.io/DiscordCSS/server-folders.css`\
Servers in a folder no longer display as a row, but pop out as a folder.
<details>
 <summary>Image</summary>
 
 ![Server folders](https://i.imgur.com/OFLLMwL.png)
 ![Server folders - with server bar](https://i.imgur.com/F4xdPX9.png)
</details>

## reverse-chat.css
`https://mrtipson.github.io/DiscordCSS/reverse-chat.css`\
Latest messages are on top.\
**! Janky implementation**\
*(Flex direction didnt work out well so I used transforms. Makes scrolling go the wrong way.)*\
**! Compact messages almost obligatory**
<details>
 <summary>Image</summary>
 
 ![Reverse chat](https://i.imgur.com/trhkOS0.png)
</details>

## banter.css
`https://mrtipson.github.io/DiscordCSS/banter.css`\
A stylesheet dedicated to me exploring dumb shit i can make with css in discord.\
Not meant for everyday use but checking out what i've been up to could be fun from time to time.

# License

This project is licensed under [the MIT license](https://github.com/MrTipson/DiscordCSS/blob/HEAD/LICENSE).
