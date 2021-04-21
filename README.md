# Agora
• European Data Graph <br>
• GraphQL <br>


![Alt text](/images/schema.png?raw=true "Schema")

## Todo
• Interfaces - GraphQL <br>
• Filtering - GraphQL <br>
• Input root node - Networkx/Cypher <br>
• Query parent-child with property - Cypher <br>
• Query subset {departement} not working - Cypher <br>

## Navigating the Graph
Navigating the graph from and to any point, and gathering the relevant data on the way.


```
uvicorn main:app --reload
```

Top Down:
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

Bottom Up:
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
                type
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
    ]
}
```
