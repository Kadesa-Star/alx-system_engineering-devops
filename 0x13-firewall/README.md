0x13. Firewall

Description
This project involves configuring firewall rules to secure network traffic on Ubuntu servers. The firewall rules are implemented using `ufw` (Uncomplicated Firewall) to control incoming and outgoing traffic based on special policies.

A firewall is a network security system that monitors and controls incoming and outgoing traffic based on predetermined security rules.

Firewalls are categorized as network based or host based system. Network based firewalls are positioned between two or more networks. Typically between LAN and WAN. Their basic function is to control the flow of data between connected networks.  

They are either;
a) Software appliacne runnint on general purpose hardware
b) Hardware appliance running on special purpose hardware 
c) Virtual appliance running on virtual host controlled by a hypervisor.

Host based firewalls are deployed directly on the host itself to control network traffic or other computing resources. This can be a daemon or service as a part of the OS or an agent applicatiion for protection.

Types of firewall
1. Packet filter - this inspects packets transfered between computers.   This firewall maintains an access-control list which dictated what packets will be looked at and what action shouold be applied, if any, with the default action set to silent discard.
   Actons with regard to packets consist of; silent discard, discard with Internet Control Message Protocol or TCP reset response to the sender and forward to the next hop.

2. Connection tracking - Stateful firewall. This second generation of firewalls was called circuit level gateways. they perform the work of first generation predecessors but also maintain knowledge of specific conversations between endpoitns by remembering which port number the two IPs are using at layer 4 for the ir conversation.

3. Application layer - application firewall
The key benefit of application filtering is that it can understand certain applications and protocols such as File Transfer Protocol (FTP), DNS, or HTTP. This allows it to identify unwanted applications or services using a nonstandard port or detect if an allowed port is being abused. 

4. Endpoint specific - these function by determining whether a proces should accept any given connection. They filter connections by examining the process ID of data packets against a rule set for the local process involved in the data transmission. 
These firewaslls accomplish their funtion by hoking into socket calls to filter the connections between the application layer and the lower layes. 

