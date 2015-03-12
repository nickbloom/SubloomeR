import sublime, sublime_plugin
from origami import TravelToPaneCommand

'''
# WHAT IT DOES

One of three things:

1. If only one pane is open, it creates a new pane and initializes the R REPL
2. If two panes are open and no R REPL process is running, it creates a new R REPL in the newest pane
3. If two panes are open and the newest pane contains an R REPL, it makes that REPL view active

# PACKAGE DEPENDENCIES

[Origami](https://github.com/SublimeText/Origami)
[SublimeREPL](https://github.com/wuub/SublimeREPL)

# TO USE

Save this file in '{path to Sublime Packages}/Packages/User'

To add with keybinding ⌘-Shift-R, add this to your User Keybindings file:

```
{
    "keys": ["super+shift+r"],
    "command": "origami_repl"
}
```

'''

class OrigamiReplCommand(sublime_plugin.WindowCommand):
    def run(self):

        awind = sublime.active_window()
        numGroups = awind.num_groups()

        def getNames(x): 
            x.name()

        if numGroups == 1:
            rgroup = awind.active_group()
            gviewsNames = [x.name() for x in awind.views_in_group(rgroup)]
            if any('*REPL* [r]' == x for x in gviewsNames):
                nameIndex = gviewsNames.index('*REPL* [r]')
                self.window.run_command("create_pane", {"direction": "right"})
                view = awind.views_in_group(rgroup)[gviewsNames.index('*REPL* [r]')]
                awind.focus_view(view)
                self.window.run_command("carry_file_to_pane", {"direction":"right"})
            else: 
                self.window.run_command("create_pane", {"direction": "right"})
                self.window.run_command("run_existing_window_command", {"file": "config/R/Main.sublime-menu","id":"repl_r"})
        else:
            rgroup = numGroups-1
            gviewsNames = [x.name() for x in awind.views_in_group(rgroup)]
            allviews = awind.views()
            avn = [x.name() for x in allviews]
            if any('*REPL* [r]' == x for x in gviewsNames):
                nameIndex = gviewsNames.index('*REPL* [r]')
                awind.focus_view(awind.views_in_group(rgroup)[gviewsNames.index('*REPL* [r]')])
            elif any('*REPL* [r]' == x for x in avn):
                view = allviews[avn.index('*REPL* [r]')]
                awind.focus_view(view)
                self.window.run_command("carry_file_to_pane", {"direction":"right"})
            else:
                awind.focus_group(rgroup)
                self.window.run_command("run_existing_window_command", {"file": "config/R/Main.sublime-menu","id":"repl_r"})
