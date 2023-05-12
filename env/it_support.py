def identify_IP(IP_address):
    if IP_address == "192.168.1.1":
        print("This is a private IP address.")
    elif IP_address == "8.8.8.8":
        print("This is a public IP address")
    elif IP_address == "127.0.0.1":
        print("This is a loopback IP address.")
    else:
        print("Unknown")

identify_IP("192.168.1.1")
identify_IP("8.8.8.8")
identify_IP("127.0.0.1")
identify_IP("10.0.0.1")