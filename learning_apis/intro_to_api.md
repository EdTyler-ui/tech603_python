# API

## What is an API
- application programming interface, interface for software to talk to each other
- Access to resources like;
  - data
  - images
  - videos
  - web pages
- Also allow to ask for certain action to be done e.g. require the cloud 

## Why might devops need APIs
- automate interactions with clouds services + infrastructure
- integrate and manage devop tools and platforms
- retrieve and manipulate data from systems + services

## RESTful services
- REST - representational state transfer
- type of architecture used for API
- primarily used to build web services that are lightweight, maintainable and scalable
- RESTful services use HTTP
- properties: representation adn data flow, messages, URIs, statelessness, caching

## HTTP messages and vers

- HTTP is protocol for internet communication
- HTTPS is secured version
- request/response system

<br>

- GET: read
- POST: create
- PUT: complete replacement of a certain record
- PATCH: modify specific piece of data
- DELETE: DELETE

## HTTP request structure
- top layer: VERB, URL, version 
  - GET (url) 1.1
- next later: Header, key value pairs
  - Content- type, date, accept-charset
- body: text, JSON, XML but body not always present

## API REST: stateful vs stateless
- stateful: client request has limited info in HTTP, moves to server which requests additional info from state storage. Keeps track of old request for next customer
- stateless: client request has all information in HTTP that goes to load balancer. Every request treated independently, allows high scalability and easier load balancing

