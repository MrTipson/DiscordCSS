 # DiscordCSS

DiscordCSS is a set of css stylesheets that make styling discord easier. Each one seeks to provide a unique way to change how discord looks and feels.

The Discord app needs to be patched, my suggestion would be 
[BeautifulDiscord](https://github.com/leovoel/BeautifulDiscord), because it only
injects CSS (no js). If you're using the web version I would suggest trying my 
[browser extension](https://github.com/MrTipson/DiscordCSS-Chromium) (chromium),
but any other CSS injecting extensions should be fine as well.

## A quick word on client mods

*Discord is aware of the existance of client mods (such as BeautifulDiscord; not css stylesheets themselves) but they are technically not allowed. This is something you should be aware of. That being said, BeautifulDiscord is probably the safest one of all, since it interferes the least.*

My hope is that some day, custom themes will be supported officialy, which is
why I try to keep it as simple as possible (plain CSS), but still easy-ish to
maintain (see my github [action](https://github.com/MrTipson/DiscordCSS/blob/master/.github/workflows/validate-selectors.yml) and the stylesheet tracking
[repository](https://github.com/MrTipson/DiscordStylesheetTracker)).

<p align=center>
<img margin=auto width=75% src="https://i.imgur.com/12BIQ9k.png">
</p>

# Stylesheets
All of the stylesheets are modular. Import each one by writing `@import url("<link>");` at the top of your main css file (example: `@import url("https://mrtipson.github.io/DiscordCSS/css/base.css");`.\
Once you have it imported, you can keep the default values or set the variables again to change their values.

Stylesheets are listed, along with images on the wiki page [Stylesheets](docs/stylesheets.md).

*Local files can't be opened due to access policies of browsers and discord itself.*

# Finished themes

Finished themes can be found in the [examples](examples/).\
These are their own stylesheets that provide a unique look incorporating various core stylesheets from this repository.

# Dev tools (windows desktop app)

Dev tools in the desktop app are locked behind a flag in the `%appdata%/discord/settings.json` file (AppData/Roaming).
```json
"DANGEROUS_ENABLE_DEVTOOLS_ONLY_ENABLE_IF_YOU_KNOW_WHAT_YOURE_DOING": true
```


# License

This project is licensed under [the MIT license](https://github.com/MrTipson/DiscordCSS/blob/HEAD/LICENSE).
