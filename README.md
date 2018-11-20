# TriciaCahill_Project
4th Year Software and Electronic Engineering Project

// this command is to capture the packet that are being recieved and if any of the packets were dropped by the kernal. This command has to be run in root user/

tcpdump -nn -i lo -v -w /tmp/packet

// this is how to make a packet
>>> p=IP()
>>> p
<IP  |>
>>> P=IP()/TCP()
>>> send(p)
.
Sent 1 packets.

// this will show you the details of the packet
>>> p.show()
###[ IP ]### 
  version= 4
  ihl= None
  tos= 0x0
  len= None
  id= 1
  flags= 
  frag= 0
  ttl= 64
  proto= ip
  chksum= None
  src= 127.0.0.1
  dst= 127.0.0.1
  \options\



// this will give you a read out of the packets
sr1(p)
Begin emission:
Finished sending 1 packets.
*
Received 1 packets, got 1 answers, remaining 0 packets
<IP  version=4 ihl=5 tos=0x0 len=20 id=1 flags= frag=0 ttl=64 proto=ip chksum=0x7ce7 src=127.0.0.1 dst=127.0.0.1 |>


//this command will send a pack with a message that can be read with wire shark
send(IP(src="192.168.1.107",dst="192.168.1.1")/ICMP()/"hello wireshark")


// this command will send 1000 packets, this is good for an attack on a network
send(IP(src="19.168.1.107", dst="192.168.1.1")/TCP(sport=80, dport=80), count=1000)

