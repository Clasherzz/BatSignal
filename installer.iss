[Setup]
AppName=BatSignal
AppVersion=1.0
DefaultDirName={localappdata}\BatSignal
DefaultGroupName=Battery Alert
OutputBaseFilename=BatteryAlertInstaller
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\monitor.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\BatterySettings.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "Clasherzz\Battery Monitor"; Filename: "{app}\monitor.exe"
Name: "Clasherzz\Battery Settings"; Filename: "{app}\BatterySettings.exe"

[Run]
Filename: "BatSignal\monitor.exe"; Description: "Start monitoring battery"; Flags: nowait postinstall skipifsilent
