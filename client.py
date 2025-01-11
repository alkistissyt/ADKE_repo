import socket
import sys
import time  # Import time module for measuring elapsed time

def client(server_a_addr, server_b_addr, n_a, n_b):
    """
    Connects to two servers and requests files based on the parameters n_a and n_b.
    Measures the total time to download all 160 files.
    """
    file_count = 1  # The number of the first file to be requested
    total_files = 160  # Total number of files to download

    print(f"Starting to download {total_files} files...")

    # Start the timer
    start_time = time.time()

    while file_count <= total_files:
        # Requests for Server A
        for _ in range(n_a):
            if file_count > total_files:
                break
            file_name = f"s{str(file_count).zfill(3)}.m4s"
            print(f"Requesting {file_name} from Server A ({server_a_addr[0]}:{server_a_addr[1]})...")
            if not request_file(server_a_addr, file_name):
                print("Server A disconnected or file transfer failed.")
                return
            file_count += 1

        # Requests for Server B
        for _ in range(n_b):
            if file_count > total_files:
                break
            file_name = f"s{str(file_count).zfill(3)}.m4s"
            print(f"Requesting {file_name} from Server B ({server_b_addr[0]}:{server_b_addr[1]})...")
            if not request_file(server_b_addr, file_name):
                print("Server B disconnected or file transfer failed.")
                return
            file_count += 1

    # Stop the timer
    end_time = time.time()

    # Calculate and display total time taken
    total_time = end_time - start_time
    print(f"Downloaded all {total_files} files.")
    print(f"Total time taken: {total_time:.2f} seconds")

def request_file(server_addr, file_name):
    """
    Connects to the server and requests a specific file.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect(server_addr)
            client.send(file_name.encode())  # Send file request

            # Create a local file for saving the received data
            with open(file_name, 'wb') as file:
                while True:
                    data = client.recv(1024)
                    if not data:
                        break
                    file.write(data)
            print(f"Downloaded: {file_name}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    # Check if the correct parameters are provided
    if len(sys.argv) != 5:
        print("Usage: python client.py <n_A> <n_B> <IP_A> <IP_B>")
        sys.exit(1)

    # Parameters from the command line
    n_a = int(sys.argv[1])  # Number of files to request from Server A per round
    n_b = int(sys.argv[2])  # Number of files to request from Server B per round
    ip_a = sys.argv[3]      # IP address of Server A
    ip_b = sys.argv[4]      # IP address of Server B

    # Server addresses and ports
    server_a_addr = (ip_a, 8080)  # IP and port for Server A
    server_b_addr = (ip_b, 9090)  # IP and port for Server B

    # Execute the client
    client(server_a_addr, server_b_addr, n_a, n_b)
