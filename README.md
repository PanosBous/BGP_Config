# Basic BGP configuration 
I just wanted to learn how to do a basic BGP configuration in yaml

The snippet is the following
```text
router bgp 65001
 neighbor 192.168.1.2 remote-as 65002
 network 10.10.10.0
```
