from ariadne import gql

type_defs = gql("""

    scalar Geometry

    type Query {
        
        group (name: String): Group
        groups: [Group]

        country (name: String): Country
        countries: [Country]

        region (name: String): Region
        regions: [Region]

        departement (name: String): Departement
        departements: [Departement]

        commune (name: String): Commune
        communes: [Commune]

    }

    type Mutation {
        createUser (username: String!, email: String!, password: String!, party: String, commune: String): User
        deleteUser (username: String!): User
        updateUser (username: String!, new_username: String!): User
    }

    type Group {
        id: ID
        u_id: String
        code: String 
        level: String 
        name: String 
        geometry: Geometry 
        countries: [Country]
    }
    
    type Country {
        id: ID
        u_id: String 
        code: String 
        level: String 
        name: String 
        geometry: Geometry 
        group: Group
        regions: [Region]
    }

    type Region {
        id: ID!
        u_id: String 
        code: String 
        level: String 
        name: String 
        geometry: Geometry 
        country: Country
        departements: [Departement]
    }
    
    type Departement {
        id: ID
        u_id: String 
        code: String 
        level: String 
        name: String 
        geometry: Geometry 
        region: Region
        communes: [Commune]
    }
    
    type Commune {
        id: ID
        u_id: String 
        code: String 
        level: String 
        name: String 
        geometry: Geometry 
        departement: Departement
    }
    
    type User {
        id: ID
        username: String 
        email: String 
        password: String 
        party: String
        commune: Commune
    }
    
""")
