# 0. Simple web stack

## Link :
https://imgur.com/a/flvgmSk

## Description :

## Server

    A server is a computer or system that provides services or resources to other computers. (known as clients)

## What type of DNS record www is in www.foobar.com:
    It is a subdomain.

## Roles:

The role of the domain name is to identify Internet resources, such as computers, networks, and services.

The role of the web server is to handle HTTP requests from clients and serve web pages.

The role of the application server is to execute the application logic and generating dynamic content. It processes requests received from the web server and interacts with the database.

The role of the database is to store and manage the website's data.

## Issues with this infrastructure:

Single Point of Failure (SPOF):  We are using a single server and a single database so any failure or downtime of the server or database will result in the website not being accessible. The implementation of a back up server, back up database or load balancer would minimize this risk.

Downtime during maintenance: The website might be inaccessible when performing maintenance tasks, such as updating the web server, the website may experience downtime. To minimize this risk, scheduled maintenance can happen during off-peak hours.

Scalability limitations:  As the number of incoming requests increases, the server may become overloaded, leading to performance degradation and crashes. To avoid this, we can add more servers and distribute the load using load balancers.