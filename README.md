# NetPack
NetPack is a Python package that can be used to get information from IP addresses and CIDR ranges. This package uses the whois protocol to fetch the information from the relevant whois server.\
This package is based on my personal use in real environment.

### Usage
For now, it's only one method in here. I hope I can add more function when I develop further.
```
from NetPack import NetPack

# Query information about an IPv4 address
ipv4_address = '8.8.8.8'
response = NetPack.inr(NetPack.ServerLocation.AFRINIC, ipv4_address)
print(response)
```

### Classes and Methods
The NetPack package contains the following classes and methods:


#### func.NetPack.inr(server: str, ipv4v6: str, query_flags: str = None) -> str
* This is a static method that takes the following parameters, and return the check result from the INR whois server:
    * server: The whois server address
      * ##### Pre-set NetPack.ServerLocation
          * AFRINIC: The AFRINIC whois server address
          * ARIN: The ARIN whois server address
          * APNIC: The APNIC whois server address
          * LACNIC: The LACNIC whois server address
          * RIPE_NCC: The RIPE NCC whois server address
          * IANA: The IANA whois server address
          * RADB: The RADB website URL
    * ipv4v6: The IP address or CIDR range
    * query_flags: Optional parameter that specifies query flags for certain whois servers
    * (The method returns the response received from the whois server as a string.)

#### func.NetPack.radb(ip: str) -> str
* This is a static method that takes an IPv4 address as an input and return the result from RADB

#### func.NetPack.ping(host, packet_size=64, ping_type="os", protocol="icmp", interval=0.2, timeout=1, packet_num=5) -> tuple
* The ping() method can be used to ping a single host:
    * Arguments
        * host: the hostname or IP address of the host to ping.
        * packet_size: the size of the packets to send (in bytes). Default is 64.
        * ping_type: using socket to initiate the ping or using inherit from OS
        * protocol: the protocol to use for the ping test. Must be either "icmp" or "tcp". Default is "icmp".
        * interval: the time (in seconds) to wait between sending each packet. Default is 0.2.
        * timeout: the time (in seconds) to wait for a response before considering the packet lost. Default is 1.
        * packet_num: the number of packets to send. Default is 5.

#### func.NetPack.multiple_ping(hosts, packet_size=64, ping_type="os", protocol="icmp", interval=0.2, timeout=1, packet_num=5) -> dict
* The multiple_ping() method can be used to ping multiple hosts in parallel, This will return a dictionary where each key is a host from the hosts list and each value is a dictionary containing the average latency and success rate of the ping test.
    * Arguments
        * The arguments for multiple_ping() are the same as for ping(), except that they are used for all hosts in the hosts list.