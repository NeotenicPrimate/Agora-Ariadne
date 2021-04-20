from ariadne import gql

type_defs = gql("""

    scalar Geometry

    type Query {
        world (name: String): World
        worlds: [World]

        group (name: String): Group
        groups: [Group]

        country (name: String): Country
        countries: [Country]

        region (name: String): Region
        regions: [Region]

        departement (name: String): Departement
        departements: [Departement]

        collectivite (name: String): Collectivite
        collectivites: [Collectivite]

        subset (name: String): Subset
        subsets: [Subset]

        arrondissement (name: String): Arrondissement
        arrondissements: [Arrondissement]

        epci (name: String): Epci
        epcis: [Epci]
        
        commune (name: String): Commune
        communes: [Commune]

    }

    type Mutation {
        createUser (username: String!, email: String!, password: String!, party: String, commune: String): User
        deleteUser (username: String!): User
        updateUser (username: String!, new_username: String!): User
    }

    type World {
        id: ID
        id_1: String
        code: String 
        level: String 
        name: String 
        geometry: Geometry 
        countries: [Country]
        groups: [Group]
    }

    type Group {
        id: ID
        id_1: String
        code: String 
        level: String 
        name: String 
        geometry: Geometry 
        world: World
        countries: [Country]
    }
    
    type Country {
        id: ID
        id_1: String 
        code: String 
        level: String 
        name: String 
        geometry: Geometry 
        group: Group
        regions: [Region]
        collectivites: [Collectivite]
    }

    type Region {
        id: ID!
        id_1: String 
        code: String 
        level: String 
        name: String 
        geometry: Geometry 
        country: Country
        departements: [Departement]
    }
    
    type Departement {
        id: ID
        id_1: String 
        code: String 
        level: String 
        name: String 
        geometry: Geometry 
        region: Region
        subset: Subset
        communes: [Commune]
    }
    
    type Commune {
        id: ID
        id_1: String 
        code: String 
        level: String 
        name: String 
        geometry: Geometry 
        departement: Departement
        arrondissement: Arrondissement
        epci: Epci
    }
    
    type User {
        id: ID
        username: String 
        email: String 
        password: String 
        party: String
        commune: Commune
    }
  
    type Collectivite {
        id: ID
        id_1: String 
        code: String 
        level: String 
        name: String 
        geometry: Geometry 
        country: Country
    }
    
    type Subset {
        id: ID
        id_1: String 
        code: String 
        level: String 
        name: String 
        geometry: Geometry 
        departements: [Departement]
    }
    
    type Arrondissement {
        id: ID
        id_1: String 
        code: String 
        level: String 
        name: String 
        geometry: Geometry 
        communes: [Commune]
    }
    
    type Epci {
        id: ID
        id_1: String 
        code: String 
        level: String 
        name: String 
        geometry: Geometry 
        communes: [Commune]
    }
    
""")
