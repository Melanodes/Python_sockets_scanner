import socket
# This function is the end function that scans the ports of given ip
def scan_port(target_ip,port):
    try:
        # Create a TCP socker
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt to prevent hanging
        sock.settimeout(1)
        # Attempt to connect to target IP and Ports
        result = sock.connect_ex((target_ip, port)) # connect_ex returns an error code instead of raising an exception if the connection fails.
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


# This function takes multiple parameters for ports and splits them into set and returns
def parse_ports(*port_args):
    ports = set()
    for arg in port_args:
        if '-' in arg:
            start, end = map(int, arg.split('-')) # Splits if range seperated by hyphen
            ports.update(range(start, end + 1)) # Creates range from the user's input and adds 1 to ensure correct working of range function
        else:
            ports.add(int(arg)) # Changes the single port into int and adds to the set
    return sorted(ports)


def main():
    ip = input("Ip or domain to scan")
    port = input("Port or ports to scan")
    # Example usage
    t = parse_ports(port)

    for x in t:
        scan_port(ip,x)  

main()
