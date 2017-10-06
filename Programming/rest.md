# Representational State Transfer (REST)

REST is not a protocol. It is a style of programming and the applications that are built with this style are often called **RESTful**

## So what is REST exactly?

In a RESTful Web service, HTTP requests are made to a resource's URL and a response that may be in XML, JSON or some other defined format are returned.

- REST is more like normal web browsing but the audience is a software instead of a human being.
    * It us based on HTTP protocol
    * It uses URLs for different resources
    * The output format is usually **JSON** or **XML** instead of HTML because the intended audience is a software

- Many *web-services* around the world use REST therefore they are RESTful

## REST is stateless

It means it treats each request as an independent transaction that is unrelated to any previous request so that the communication consists of independent pairs of request and response.

HTTP itself is an stateless protocol and people use a trick called **cookies** to keep track of a session.

A disadvantage of statelessness is that it may be necessary to include additional information like a **TOKEN** in every request.

## REST API

[Twitter](https://dev.twitter.com/rest/public) is a messaging application and apart from it's mobile app or website that people normally use, It offers a decent REST API which enables a softwares to twit instead of a human being. or through another URL it enables a software to query top twits for a specific hashtag.

So a REST API is **a collection of RESTful web-services plus documents on how to use the API that allows a developer to integrate his own application with it.**
