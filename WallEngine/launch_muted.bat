@echo off

wp run mpv ^
--player-operation-mode=pseudo-gui ^
--force-window=yes ^
--terminal=no ^
--no-audio ^
--loop=inf ^
--loop-playlist=inf ^
--input-ipc-server=\\.\pipe\mpvsocket ^
Wallpaper

wp mv --wait --class mpv -x 1920
wp add --wait --fullscreen --class mpv