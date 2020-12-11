# palladin
A mighty knight to keep your .config clean

## Idea
Someday I got tired about numerous `.config` subfolders in my system, so I decided to write a simple script to put my attention on configs that may be unneeded.

## Usage
Just run `palladin` from your shell. It will ask you about suspicious configs if they are needed. You can also tell `palladin` to remember the config you need - you will be never asked about it again. If you want to undo this, just remove the respective line from `~/.config/palladin/mercy.list`.

## Side effects
- `palladin` **does remove** the unneeded configs. Just keep it in mind.
- `palladin` creates `.config` subfolder `palladin` with a single file `mercy.list` in it. Yes, it have become the very thing it swore to destroy.
