from scapy.layers.inet import IP

"""
How to work with IP version 4.
"""

# A given packet with time to live of 10
example_packet1 = IP(ttl=10)
print(example_packet1)

# source IP address of this packet
print(example_packet1.src)

# the time to live of this packet
print(example_packet1.ttl)

# deletes the `ttl` field of our packet which means it no longer has a default ttl value
del example_packet1.ttl

print(example_packet1)

print(example_packet1.ttl)