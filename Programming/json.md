# JavaScript Object Notation (JSON)


JSON is another way of storing and transporting structured data like XML but with several advantages over XML.



```json
{"students":[
   {"name":"John", "age":"23", "city":"Agra"},
   {"name":"Steve", "age":"28", "city":"Delhi"},
   {"name":"Peter", "age":"32", "city":"Chennai"},
   {"name":"Chaitanya", "age":"28", "city":"Bangalore"}
]}
```

```xml
<students>
  <student>
    <name>John</name> <age>23</age> <city>Agra</city>
  </student>
  <student>
    <name>Steve</name> <age>28</age> <city>Delhi</city>
  </student>
  <student>
    <name>Peter</name> <age>32</age> <city>Chennai</city>
  </student>
  <student>
    <name>Chaitanya</name> <age>28</age> <city>Bangalore</city>
  </student>
</students>
```

- JSON is much more light-weight than XML
- JSON supports arrays
- JSON is easier to read and write

## Syntax

- Data is in name:value pairs `:`
- Data is separated by commas `,`
- Curly braces hold objects `{ }`
- Square brackets hold arrays `[ ]`
- Keys must be strings, engulfed with double quotes `"key"`
- The file type for JSON files is `.json`
- The MIME type for JSON text is `application/json`

## Data Types

- string `"name":"rick"`
- number `"age": 21`
- object (JSON object) `{"age":21, "name":rick}`
- array `["red", "blue", 6, 4]`
- boolean `true` or `false`
- null `null`

Arrays can hold any type of data, even objects.

## Example JSON data from flickr:
```json
({
    "title": "Talk On Travel Pool",
    "link": "http://www.flickr.com/groups/talkontravel/pool/",
    "description": "Travel and vacation photos from around the world.",
    "modified": "2009-02-02T11:10:27Z",
    "generator": "http://www.flickr.com/",
    "items": [
            {
            "title": "View from the hotel",
            "link": "http://www.flickr.com/photos/33112458@N08/3081564649/in/pool-998875@N22",
            "media": {"m":"http://farm4.static.flickr.com/3037/3081564649_4a6569750c_m.jpg"},
            "date_taken": "2008-12-04T04:43:03-08:00",
            "description": " Talk On Travel< /a> has added a photo to the pool:< /p>
 < /a>< /p> ", "published": "2008-12-04T12:43:03Z", "author": "nobody@flickr.com (Talk On Travel)", "author_id": "33112458@N08", "tags": "spain dolphins tenerife canaries lagomera aqualand playadelasamericas junglepark losgigantos loscristines talkontravel" } ] })
```
