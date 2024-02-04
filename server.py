import socket

def receive_message(port=8000):
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set the server address and port
    server_address = ('', port)

    try:
        # Bind the socket to the server address and port
        server_socket.bind(server_address)

        # Listen for incoming connections
        server_socket.listen(5)

        print(f"Server is listening for incoming messages on port {port}...")

        # Wait for a connection
        client_socket, client_address = server_socket.accept()

        # Receive data from the client
        data = client_socket.recv(1024)

        # Print the received message
        message = data.decode()
        print(f"Received message from {client_address}: {message}")

    except Exception as e:
        print(f"Error receiving message: {e}")

    finally:
        # Close the sockets
        client_socket.close()
        server_socket.close()

def merge_changes(base_text, incoming_changes):
    """
    Merges incoming_changes into base_text.

    Args:
    - base_text (str): The original text.
    - incoming_changes (str): The changes to be merged.

    Returns:
    - str: The merged text.
    """
    # Split the text into lines
    base_lines = base_text.splitlines()
    incoming_lines = incoming_changes.splitlines()

    # Merge the changes
    merged_lines = []
    i, j = 0, 0

    while i < len(base_lines) or j < len(incoming_lines):
        if i < len(base_lines) and j < len(incoming_lines):
            # Compare lines from both texts
            if base_lines[i] == incoming_lines[j]:
                # Lines are the same, include either
                merged_lines.append(base_lines[i])
                i += 1
                j += 1
            else:
                # Lines are different, include both
                merged_lines.append(f"<<<<<<< Base\n{base_lines[i]}\n=======\n{incoming_lines[j]}\n>>>>>>> Incoming")
                i += 1
                j += 1
        elif i < len(base_lines):
            # No more incoming lines, include remaining base lines
            merged_lines.append(base_lines[i])
            i += 1
        elif j < len(incoming_lines):
            # No more base lines, include remaining incoming lines
            merged_lines.append(incoming_lines[j])
            j += 1

    # Join the merged lines back into text
    merged_text = '\n'.join(merged_lines)

    return merged_text

# Example usage:
base_text = "This is the original text.\nSome more content here."
incoming_changes = "This is the modified text.\nAdditional changes."

merged_result = merge_changes(base_text, incoming_changes)
print("Merged Result:")
print(merged_result)

# Example usage:
receive_message(8000)

