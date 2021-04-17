# Agora
Data Graph


Navigating the graph from and to any point, and gathering the relevant data on the way.

```
query {
  Country(name: "France") {
    id
    name
    regions {
      id
      name
      departements {
          id
          name
      }
    }
  }
}
```
