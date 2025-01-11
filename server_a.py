import socket
import os


def list_files_in_directory(base_path):
    """
    Lists all files in the specified directory to verify the path and its contents.
    """
    print(f"Checking files in directory: {base_path}")
    if os.path.exists(base_path):
        files = os.listdir(base_path)
        if files:
            print("Files in the directory:")
            for file in files:
                print(f"- {file}")
        else:
            print("The directory exists but is empty.")
    else:
        print("Error: The specified path does not exist.")

def server_a():
    """
    Server that listens on a port and sends files to the client.
    """
    host = '0.0.0.0'  # Accepts connections from any IP address
    port = 8080       # Port where the server will listen
    base_path = r"/αρχεία - τμήματα"  # Path to the files

    # Call the directory check before starting the server
    #list_files_in_directory(base_path)

    # Create the socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((host, port))  # Bind the server to the port
        server.listen(5)  # Allow up to 5 pending connections
        print(f"Server A is running on {host}:{port} (Wireless Connection)")
        print(f"Serving files from: {base_path}")

        while True:
            # Accept a connection from a client
            conn, addr = server.accept()
            with conn:
                print(f"Connected by {addr}")
                # Receive the file request from the client
                file_name = conn.recv(1024).decode()
                print(f"Client requested: {file_name}")

                # Create the full path to the requested file
                full_path = os.path.join(base_path, file_name)

                # Check if the file exists
                if os.path.exists(full_path):
                    with open(full_path, 'rb') as file:
                        # Send the file to the client
                        conn.sendfile(file)
                    print(f"File sent: {file_name}")
                else:
                    # If the file doesn't exist, send an error message
                    conn.send(b"ERROR: File not found")
                    print(f"File not found: {file_name}")

if __name__ == "__main__":
    server_a()
