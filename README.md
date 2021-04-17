# Agora
Data Graph



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

