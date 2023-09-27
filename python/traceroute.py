import subprocess
import platform

def run_traceroute(destination_host):
    try:
        # Determine the operating system
        system = platform.system().lower()

        # Define the traceroute command based on the operating system
        if system == 'linux' or system == 'darwin':  # Linux or macOS
            command = ['traceroute', destination_host]
        elif system == 'windows':  # Windows
            command = ['tracert', destination_host]
        elif system == 'android':  # Android (assuming a Termux-like environment)
            command = ['termux-traceroute', destination_host]
        else:
            print(f"Unsupported operating system: {system}")
            return

        # Run the traceroute command
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Check if the command was successful
        if result.returncode == 0:
            # Print the traceroute results
            print(result.stdout)
        else:
            # Print an error message if the command failed
            print(f"Traceroute failed. Error message:\n{result.stderr}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Replace 'destination_host' with the hostname or IP address you want to trace
destination_host = 'example.com'

run_traceroute(destination_host)
