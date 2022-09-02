Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c Run_Windows.bat"
oShell.Run strArgs, 0, false