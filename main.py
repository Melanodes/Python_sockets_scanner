import socket

def scan_port(target_ip, port):
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt to prevent hanging
        sock.settimeout(1)

        # Attempt to connect to the target IP and port
        result = sock.connect_ex((target_ip, port))
        
        # Check if the connection was successful (result == 0 means port is open)
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed or filtered")
        
        # Close the socket after the connection attempt
        sock.close()

    except Exception as e:
        # Print any errors encountered during the scan
        print(f"Error scanning port {port}: {e}")

def scan_ports(target_ip, ports):
    # Print the target IP being scanned
    print(f"Scanning ports on {target_ip}...")
    # Iterate through the list of ports to scan
    for port in ports:
        # Call the scan_port function for each port
        scan_port(target_ip, port)

# Define the target IP address to scan
target_ip = "google.com"
# Define the range of ports to scan (from 20 to 1024)
ports_to_scan = range(20, 1025)

# Start the port scan by calling scan_ports
scan_ports(target_ip, ports_to_scan)
