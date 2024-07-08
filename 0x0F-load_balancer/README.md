## LOAD BALANCER

On a high level, there are two types of load balancers, which implements different types of scheduling algorithms and routing mechanisms.

Software load balancer
Hardware load balancer
I. Software Load Balancers
Software load balancers generally implements a combination of one or more scheduling algorithms.

The following are the three different basic algorithms used by load balancers. Most modern load balancers use combination of these algorithms to reach high performance and to set a trade off between various parameters.

1. Weighted Scheduling Algorithm
Work is assigned to the server according to the weight assigned to the server. For different types of the server in the group different weights are assigned thus the load gets distributed.

he diagram below depicts a generic scenario where a load balancer is used and how the weighted scheduling will work if there are total of 10 request ( R1, R2…… R10 ) coming to the server farm/cluster.

As you see, the request will be assigned to the server as per its weight. This weight is determined by the administrators wisely by considering the hardware capabilities of each server. Assuming that we have different weights assigned to each server as you can see in the figure below.

The load balancer will compute the percentage of traffic to be sent to a particular server according to the weight assigned to it.

When is this algorithm mostly used?: This is used when there is a considerable difference between the capabilities and specification of the servers present in the farm or cluster.

This algorithm stands out to be efficient in managing the load without swarming the low capability servers the most and efficiently utilizing the available server resource at any instant of time

2. Round Robin Scheduling
Requests are served by the server sequentially one after another. After sending the request to the last server, it starts from the first server again.

The diagram below depicts this approach. Sequentially each request gets assigned to each server one by one and the round goes on. The change in the request assigned can be easily understood by looking into the diagram below.

3. Least Connection First Scheduling
Requests are served first to the server which is currently handling least number of persistent connections.

In the diagram above, if we are using the least connection first scheduling algorithm, the request R5 can be assigned randomly to any of the server as when R5 will be coming every server will be having same number of connections.

Lets say when request R5 comes, request R3 got completed and server S3 is free now. Then, in that case, the request R5 will be assigned to server S3 instead of any other server as server S3 is having least no of connection at that instant of time.

When is this algorithm used?: When we have large number of persistent connections in the traffic unevenly distributed between the servers. It is often coupled with Sticky Session or Session aware load balancing. In this, all the request related to a session is sent to the same server to maintain the session state and syncronization.

Now, load balancing softwares can have the smart implementation of the combination of the above three basic scheduling algorithm. Such implementations are Weighted round robin scheduling and Weighted least connection scheduling.Now, load balancing softwares can have the smart implementation of the combination of the above three basic scheduling algorithm. Such implementations are Weighted round robin scheduling and Weighted least connection scheduling.

