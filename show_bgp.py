import yaml
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException
from jinja2 import Environment, FileSystemLoader

# define routers
routers = [
    {"device_type": "cisco_ios",
     "host": "192.168.1.1",
     "username": "admin",
     "password": "password",
     "secret": "enable_password",
     "bgp_as": 65001,
     "neighbor_ip": "10.0.0.2",
     "neighbor_as": 65002
     },
    {"device_type": "cisco_ios",
     "host": "192.168.1.2",
     "username": "admin",
     "password": "password",
     "secret": "enable_password",
     "bgp_as": 65002,
     "neighbor_ip": "10.0.0.1",
     "neighbor_as": 65001
     }
]

# helper function to load the YAML file
def load_yaml(file_path):
    # to do
    with open(file_path) as f:
        return yaml.safe_load(f)

# helper function to push configs
def push_config(device, config):
    #to do
    connection = ConnectHandler(
            device_type = router["device_type"],
            host = router["host"],
            username = router["username"],
            password = router["password"],
            secret = router["secret"]
    )

    connection.enable()

    # convert rendered config into command line
    config_commands = config.splitlines()

    output = connection.send_config_set(config_commands)

    print(f"\n --- Config output from {device['host']} ---")
    print(output)

    print("\n --- Saving config ---")
    print(connection.save_config())

    print("\n --- BGP Status ---")
    print(connection.send_command("show ip bgp summary"))

    connection.disconnect()



for router in routers:
    try:
        print(f"\n Connecting to {router['host']}...")


        # BGP config
        bgp_config = [
            f"router bgp {router['bgp_as']}",
            f"neighbor {router['neighbor_ip']} remote-as {router['neighbor_as']}",
            f"neighbor {router['neighbor_ip']} description BGP_PEER",
            "address-family ipv4",
            f"neighbor {router['neighbor_ip']} activate",
            "exit-address-family"
        ]

        output = connection.send_config_set(bgp_config)

        print("configuration applied")
        print(output)

        # save config
        save_output = connection.save_config()
        print(save_output)

        # to verify bgp
        print("\n BGP Summary:")
        verification = connection.send_command("show ip bgp summary")
        print(verification)

        connection.disconnect()

    except NetmikoAuthenticationException:
        print(f"Authentication failed on {router['host']}")

    except NetmikoTimeoutException:
        print(f"Timeout connecting to {router['host']}")

    except Exception as e:
        print(f"Error on {router['host']}: {e}")


if __name__ == "__main__":
    main()