# Agora
Data Graph


Navigating the graph from and to any point, and gathering the relevant data on the way.

```
query {
  Country(name: "France") {
    id
    name
    gdp
    regions {
      id
      name
      unemployement_rate
      departements {
          id
          name
          population
          average_income
      }
    }
  }
}
```
