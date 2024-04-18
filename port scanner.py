import socket

def port_scan(target_host, start_port, end_port):
    for port in range(start_port, end_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target_host, port))
            if result == 0:
                service_name = socket.getservbyport(port)
                print(f"port {port} ({service_name}) is open")
            s.close()
        except socket.error:
            pass

def main():
    target_host = input("Enter the target host: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    port_scan(target_host, start_port, end_port)

if __name__ == "__main__":
    main()