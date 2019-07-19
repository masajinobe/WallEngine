Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c launch_muted.bat"
oShell.Run strArgs, 0, false