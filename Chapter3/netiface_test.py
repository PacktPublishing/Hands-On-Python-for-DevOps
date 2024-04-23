import netifaces

def generate_routing_table():
    routing_table = []
    for interface in netifaces.interfaces():
        addresses = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addresses:
            for entry in addresses[netifaces.AF_INET]:
                if 'netmask' in entry and 'addr' in entry:
                    routing_entry = {
                        'interface': interface,
                        'destination': entry['addr'],
                        'netmask': entry['netmask']
                    }
                    routing_table.append(routing_entry)
    return routing_table

if __name__ == "__main__":
    routing_table = generate_routing_table()
    for entry in routing_table:
        print(f"Interface: {entry['interface']}")
        print(f"Destination: {entry['destination']}")
        print(f"Netmask: {entry['netmask']}")
        print("-" * 30)
