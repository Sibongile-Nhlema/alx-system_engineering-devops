# 2-secured_and_monitored_web_infrastructure

## Link :
https://imgur.com/WBpYITC

## Description :

Firewalls act as a barrier between a trusted internal network and an untrusted external network. They monitor and control incoming and outgoing network traffic based on predetermined security rules.

Serving traffic over HTTPS (Hypertext Transfer Protocol Secure) is crucial for ensuring the security and integrity of data transmitted between a client and a server. It encrypts the data exchanged between the client and the server, uses cryptographic algorithms to ensure data integrity, provides authentication and improves trust and confidence.

Monitoring is used to ensure the optimal performance of an operation and identifies any potential bottlenecks or issues.

The monitoring tool (Datadog) collects data by deploying an agent on the web server or by using integrations with popular web server software

o monitor your web server QPS, you need to Choose a monitoring tool, Install and configure the monitoring tool, Set up data collection, Visualize and analyze the data, Set up alerts and Continuously monitor and optimize

## Issues with the Infrastructure

Terminating SSL at the Load Balancer Level: Terminating SSL at the load balancer can simplify the configuration and offload the SSL decryption process from the web servers. However, it can introduce a single point of failure and limit the ability to inspect and filter traffic at the server level. To mitigate this, we can consider implementing end-to-end encryption by using SSL/TLS between the load balancer and the web servers.

Single MySQL Server Capable of Accepting Writes: Having only one MySQL server capable of accepting writes can be a performance bottleneck and a single point of failure. To address this, we can implement database replication, as mentioned earlier, to distribute the write load and ensure high availability.

Servers with Identical Components: Using servers with identical components can be a problem if there is a vulnerability or issue that affects all the servers simultaneously. It is recommended to have a diverse set of server configurations, software versions, and security measures to minimize the impact of such issues. Additionally, regular patching and updates should be performed to address any known vulnerabilities.