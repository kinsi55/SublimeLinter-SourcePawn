**Warning:** This plugin is by no means complete, as i have mainly created it for personal use. If you'd like to improve it, feel free to send a PR :)

=> If used in combination with [SourcePawnCompletitions](https://github.com/ppalex7/SourcePawnCompletions) with a set-up Build system, it works. Thats to say the least.

SublimeLinter-SourcePawn
================================

This linter plugin for [SublimeLinter][http://www.sublimelinter.com/en/latest/index.html] provides an interface to [spcomp](https://www.sourcemod.net/). It will be used with files that have the “Pawn / [SourcePawn](https://github.com/Dillonb/SublimeSourcePawn)” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][http://www.sublimelinter.com/en/latest/installation.html].

### Linter installation
Before using this plugin, you must ensure that `spcomp` is installed on your system. To install `spcomp`, do the following:

1. Download a Recent version of SourceMod

1. Extract the included Compiler

**Note:** Use of the plugin [SourcePawnCompletitions](https://github.com/ppalex7/SourcePawnCompletions) is recommended as the linter will use its build settings (Include path, etc.)

### Linter configuration
In order for `spcomp` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `spcomp`, you can proceed to install the SublimeLinter-contrib-spcomp plugin if it is not yet installed.

### Plugin installation

Clone this repo to your Sublime's Packages folder.