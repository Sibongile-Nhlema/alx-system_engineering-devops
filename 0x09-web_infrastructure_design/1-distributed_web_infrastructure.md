# 1-distributed_web_infrastructure

## Link :
https://imgur.com/a/chA9Jv0

## Description :

This Load Balancer in this model uses the Round Robin Algorithm. This means that it divides the requests evenly between the two servers.

The load balancer has an Active - Active setup which would require that both servers run simultaneously.

(An Active-Passive setup is one where  one server acts as the active node, handling incoming requests, while the other server remains passive, ready to take over in case of a failure)

## Issues with this Infrastructure:

### Single Point of Failure (SPOF):

We are using a single load-balancer so if it fails it will result in the website not being accessible. The implementation of a back up load balancer.

### Security Issues:

The lack of a firewall leaves this model vulnerable to unauthorized access and attacks. To mitigate this risk firewalls can be added at the network level and on the client-end level. The lack of HTTPS (secured HTTP) leaves the model susceptible to data interception and tampering.
 .
### Monitoring:

The lack of monitoring makes maintenance difficult as it will require extensive resources to identify issues. Monitoring can provide real-time insights into the infrastructure's health, performance, and resource utilization, enabling proactive troubleshooting and optimization..

### Primary Replica Cluster:

This is a design that has a central Database that handles all read and write operations. It has a number of other replica dabases that perform read operation and can serve as a replacement to the main Database should a failover occur.