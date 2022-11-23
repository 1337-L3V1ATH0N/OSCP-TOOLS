print("== Endian Byte Flipper ==\nDeveloped with <3 by Akash Pandey")
endian=input("\n[+] Enter your jump ESP address: ")
increment=0
if len(endian)==8:
    end=endian[::-2]
    ian=endian[-2::-2]
    while increment != 4:
        print("\\x"+ian[increment]+end[increment],end="")
        increment+=1
            
               
else:
    print("Check Address")
