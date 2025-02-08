from netmiko import ConnectHandler

# Define the device details
device = {
    "device_type": "cisco_ios",  # Adjust for your device type
    "host": "192.168.1.1",      # Replace with device IP
    "username": "admin",        # Replace with your username
    "password": "password",     # Replace with your password
}

# MAC address to search for
mac_address_to_find = "00:1A:2B:3C:4D:5E"

try:
    # Establish SSH connection to the device
    connection = ConnectHandler(**device)

    # Run the command to retrieve the MAC address table
    output = connection.send_command("show mac address-table")

    # Search for the MAC address in the output
    if mac_address_to_find.lower() in output.lower():
        print(f"MAC Address {mac_address_to_find} found!")
        lines = output.split("\n")
        for line in lines:
            if mac_address_to_find.lower() in line.lower():
                print(f"Details: {line}")
    else:
        print(f"MAC Address {mac_address_to_find} not found.")

    # Close the connection
    connection.disconnect()

except Exception as e:
    print(f"An error occurred: {e}")
