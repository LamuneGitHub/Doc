#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

^+d::
	FormatTime, CurrentDateTime,, (yyyy-MM-dd)  ; It will look like 20050918-1553
	SendInput %CurrentDateTime%{space}
Return

^!+d::
	FormatTime, CurrentDateTime,, (yyyy-MM-dd_HHmmss)  ; It will look like 20050918-1553
	SendInput %CurrentDateTime%{space}
Return
