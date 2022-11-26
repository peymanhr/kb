# JavaScript Object Notation (JSON)


JSON is another way of storing and transporting structured data like XML but with several advantages over XML.



```json
{"students":[
   {"name":"Ali", "age":"23", "city":"Tehran"},
   {"name":"Mina", "age":"28", "city":"Rasht"},
   {"name":"Reza", "age":"32", "city":"Abadan"},
   {"name":"Abbass", "age":"27", "city":"Shiraz"}
]}
```

```xml
<students>
  <student>
    <name> Ali </name> <age>23</age> <city>Tehran</city>
  </student>
  <student>
    <name>Mina</name> <age>28</age> <city>Rasht</city>
  </student>
  <student>
    <name>Reza</name> <age>32</age> <city>Abadan</city>
  </student>
  <student>
    <name>Abbass</name> <age>27</age> <city>Shiraz</city>
  </student>
</students>
```

- JSON is much more light-weight than XML
- JSON supports arrays
- JSON is easier to read and write

## Syntax

- Curly braces hold objects `{ }`
- Data is in name:value pairs `:`
- Keys must be strings, engulfed with double quotes `"key"`
- Data is separated by commas `,`
- Square brackets hold arrays `[ ]`
- The file type for JSON files is `.json`
- The MIME type for JSON text is `application/json`

## Data Types

- string `"name":"rick"`
- number `"age": 21`
- object (JSON object) `{"age":21, "name":"rick"}`
- array `["red", "blue", 6, 4]`
- boolean `true` or `false`
- null `null`

Arrays can hold any type of data, even objects.
