import os
import platform
import socket
import datetime
import subprocess

# Writing the content of the file
def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

# Getting the local IP Address
def get_ip_address():
    return socket.gethostbyname(socket.gethostname())

# Getting the date and time
def get_current_datetime():
    return datetime.datetime.now()

# Main function of the assignment
def main():
    output_directory = "C:\\temp"
    output_file_path = os.path.join(output_directory, "reporting.txt")

    current_datetime = get_current_datetime()
    ip_address = get_ip_address()
    message = f"{current_datetime} - IP: {ip_address} - hacked!!"

    try:
        # Checking if the directory exists, and creating it if it doesn't already exist
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        write_to_file(output_file_path, message)
        print(f"Writing file to - {output_file_path}")

        if platform.system().lower() == 'windows':
            subprocess.run(["ping", "flemingcollege.ca"], check=True)
        else:
            print("This is not supported on your system...")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()