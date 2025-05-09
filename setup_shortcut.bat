@echo off
set STARTUP=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
set TARGET=%~dp0dist\battery_checker\battery_checker.exe

echo Creating shortcut in startup folder...
powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%STARTUP%\BatteryMonitor.lnk');$s.TargetPath='%TARGET%';$s.Save()"
echo Done.
pause
