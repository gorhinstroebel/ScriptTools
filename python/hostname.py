import socket

def get_hostname():
    try:
        # Get the hostname of the current system
        hostname = socket.gethostname()
        return hostname
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    hostname = get_hostname()
    print(f"Hostname: {hostname}")
