# SuBloom Peek

A (pseudo-) fork of [SublimePeek](https://github.com/jlegewie/SublimePeek). Updated with Mavericks-compatible Quicklook (broken in 10.10.2) and HTML Popups.

## To install:

1. Move `popup.app` to your applications folder (or leave it where it is if you want), and update the path on like 129 of `SublimePeek.py` accordingly.
2. Unzip `htmlstatic.zip` and rename the folder `html` if you want to use my pre-compiled static documentation. Info on compiling your own is in `rhelp.R`.
3. If you want to use HTML popups for R's `help` documentation, add these two lines to your .Rprofile file:

```
options("help_type"="html")

options('browser' ='open {path-to-popup}/popup.app --args')

```

4. Add the following to your User Keybinding file:

```
{ "keys": ["super+shift+/"], "command": "sublime_peek" }
```

5. I'll update the Quicklook functionality once its fixed. The popup does essentially the same thing, but is (slightly) more persistent and fancy.