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


#### NetPack.inr(server: str, ipv4v6: str, query_flags: str = None) -> str
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

#### NetPack.radb(ip: str) -> str
* This is a static method that takes an IPv4 address as an input and return the result from RADB