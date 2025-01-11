import socket
import os

def list_files_in_directory(base_path):
    """
    Lists all files in the specified directory and its subdirectories
    to verify the path and its contents.
    """
    print(f"Checking files in directory and subdirectories: {base_path}")
    if os.path.exists(base_path):
        found_files = []
        for root, dirs, files in os.walk(base_path):
            for file in files:
                found_files.append(os.path.join(root, file))
        if found_files:
            print("Files found:")
            for file in found_files:
                print(f"- {file}")
        else:
            print("The directory and its subdirectories are empty.")
    else:
        print("Error: The specified path does not exist.")

def server_b():
    """
    Server B listens on port 9090 and sends files to the client upon request.
    Files are stored in a drive or directory specified by base_path.
    """
    host = '0.0.0.0'  # Accept connections from any IP address
    port = 9090       # Port where the server will listen

    # Update this to the directory or drive path where the files are stored
    base_path = "/storage/emulated/0/server_b_data"  # Example path for Android
    # Example for external drive: "/storage/<drive_name>/server_b_data"

    # Verify the directory and log available files
    list_files_in_directory(base_path)

    # Create the socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((host, port))  # Bind the server to the port
        server.listen(5)  # Allow up to 5 pending connections
        print(f"Server B is running on {host}:{port}")
        print(f"Serving files from: {base_path}")

        while True:
            # Accept a connection from a client
            conn, addr = server.accept()
            with conn:
                print(f"Connected by {addr}")

                # Receive the file name from the client
                file_name = conn.recv(1024).decode()
                print(f"Client requested: {file_name}")

                # Build the file path
                full_path = os.path.join(base_path, file_name)

                # Check if the file exists
                if os.path.exists(full_path):
                    # Send the file content to the client
                    with open(full_path, 'rb') as file:
                        conn.sendfile(file)
                    print(f"File sent: {file_name}")
                else:
                    # Send an error message if the file doesn't exist
                    conn.send(b"ERROR: File not found")
                    print(f"File not found: {file_name}")

if __name__ == "__main__":
    server_b()
