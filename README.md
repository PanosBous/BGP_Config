# Basic BGP configuration 
I just wanted to learn how to do a basic BGP configuration in yaml

A basic snippet BGP config 
```text
router bgp [AS number]
 neighbor [neighbor IP address] remote-as [neighbor AS number]
 network [network IP address]
 ```

A more realistic example based on the snippet is the following
```text
router bgp 65001
 neighbor 192.168.1.2 remote-as 65002
 network 10.10.10.0 description BGP_PEER

 address-family ipv4
  neighbor 10.0.0.2 activate
 exit-address-family
```
# Next steps I would like to add
the user gives the host ip, ASN number, neighbor ip and neighbor ASN and configure the BGP