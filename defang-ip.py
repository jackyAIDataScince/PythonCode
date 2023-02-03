def ip_address(address):
    new_address = ""
    split_address = address.split(".")
    separator = "[.]"
    new_aadress = separator.join(split_address)
    return address
ipaddress = ip_address("1.1.2.3")
print(ipaddress)
