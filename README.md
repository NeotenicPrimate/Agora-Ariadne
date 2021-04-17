# Agora
• European Data Graph
• GraphQL

## Navigating the Graph
Navigating the graph from and to any point, and gathering the relevant data on the way.


```
uvicorn main:app --reload
```

Down:
```
query {
  country(name: "France") {
    type
    id
    name
    gdp
    children {
      type
      id
      name
      unemployement_rate
      children {
          id
          name
          population
          average_income
      }
    }
  }
}
```

Up:
```
query {
  commune(name: "Vauvenargues") {
    type
    id
    name
    population
    average_income
    parent {
      type
      id
      name
      unemployement_rate
      parent {
          id
          name
          average_education
      }
    }
  }
}
```

Nodes and links:
```
{
  "nodes": [ 
      { 
        "id": "id1",
        "name": "name1",
        "val": 1 
      },
      { 
        "id": "id2",
        "name": "name2",
        "val": 10 
      },
      (...)
  ],
  "links": [
      {
          "source": "id1",
          "target": "id2"
      },
      (...)
  ]
}
```

Tree:
```
{
    "id": "id1",
    "children": [
        {
            "id": "id1.1",
            "children": [
                {
                    "id": "id1.1.1",
                    "children": [
                        (...)
                    ]
                },
                {
                    "id": "id1.1.2"",
                    "children": [
                        (...)
                    ]
                }
            ]
        },
        {
            "id": "id1.2",
            "children": [
                {
                    "id": "id1.2.1"",
                    "children": [
                        (...)
                    ]
                },
                {
                   "id": "id1.2.2"",
                    "children": [
                        (...)
                    ]
                }
            ]
        }
}
```
