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
 network 10.10.10.0
```
# Next steps I would like to add
separate the jinja2 in a new file
create routers as a group variables