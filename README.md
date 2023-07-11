Python script that creates a straightforward SSH honeypot server is available in this repository. The purpose of the honeypot is to record connection attempts made by potential attackers and collect data on their login attempts.

The honeypot server will begin monitoring port 22 (you can change port) for SSH connection attempts as soon as you launch the honeypot.py script using the: 

python3 honeypot.py 

The client's IP address used to connect to the honeypot server will be printed by the script. The log entry "Connection received from: [client_address]" will include this information and be shown in the console.
