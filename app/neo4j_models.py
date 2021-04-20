from neomodel import StructuredNode, RelationshipTo, RelationshipFrom, UniqueIdProperty, StringProperty, JSONProperty, DateTimeProperty

class World(StructuredNode):
    id_1 = UniqueIdProperty()
    id_2 = UniqueIdProperty()
    code = UniqueIdProperty()	
    name = StringProperty(required = True)	
    validity = DateTimeProperty()
    geometry = JSONProperty(required = True)	
    level = StringProperty(required = True)	

    groups = RelationshipTo('Group', 'GROUP')
    countries = RelationshipTo('Country', 'COUNTRY')

class Group(StructuredNode):
    id_1 = UniqueIdProperty()
    id_2 = UniqueIdProperty()
    code = UniqueIdProperty()	
    name = StringProperty(required = True)	
    validity = DateTimeProperty()
    geometry = JSONProperty(required = True)	
    level = StringProperty(required = True)	

    countries = RelationshipTo('Country', 'COUNTRY')

class Country(StructuredNode):
    id_1 = UniqueIdProperty()
    id_2 = UniqueIdProperty()
    code = UniqueIdProperty()	
    name = StringProperty(required = True)	
    validity = DateTimeProperty()
    geometry = JSONProperty(required = True)	
    level = StringProperty(required = True)	
    
    regions = RelationshipTo('Region', 'REGION')
    collectivites = RelationshipTo('Collectivite', 'COLLECTIVITE')

class Collectivite(StructuredNode):
    id_1 = UniqueIdProperty()
    id_2 = UniqueIdProperty()
    code = UniqueIdProperty()	
    name = StringProperty(required = True)	
    validity = DateTimeProperty()
    geometry = JSONProperty(required = True)	
    level = StringProperty(required = True)	

class Region(StructuredNode):
    id_1 = UniqueIdProperty()
    id_2 = UniqueIdProperty()
    code = UniqueIdProperty()	
    name = StringProperty(required = True)	
    validity = DateTimeProperty()
    geometry = JSONProperty(required = True)	
    level = StringProperty(required = True)	

    departements = RelationshipTo('Departement', 'DEPARTEMENT')

class Subset(StructuredNode):
    id_1 = UniqueIdProperty()
    id_2 = UniqueIdProperty()
    code = UniqueIdProperty()	
    name = StringProperty(required = True)	
    validity = DateTimeProperty()
    geometry = JSONProperty(required = True)	
    level = StringProperty(required = True)	

    departements = RelationshipTo('Departement', 'DEPARTEMENT')
    
class Departement(StructuredNode):
    id_1 = UniqueIdProperty()
    id_2 = UniqueIdProperty()
    code = UniqueIdProperty()	
    name = StringProperty(required = True)	
    validity = DateTimeProperty()
    geometry = JSONProperty(required = True)	
    level = StringProperty(required = True)	

    communes = RelationshipTo('Commune', 'COMMUNE')

class Epci(StructuredNode):
    id_1 = UniqueIdProperty()
    id_2 = UniqueIdProperty()
    code = UniqueIdProperty()	
    name = StringProperty(required = True)	
    validity = DateTimeProperty()
    geometry = JSONProperty(required = True)	
    level = StringProperty(required = True)	

    communes = RelationshipTo('Commune', 'COMMUNE')
    
class Arrondissement(StructuredNode):
    id_1 = UniqueIdProperty()
    id_2 = UniqueIdProperty()
    code = UniqueIdProperty()	
    name = StringProperty(required = True)	
    validity = DateTimeProperty()
    geometry = JSONProperty(required = True)	
    level = StringProperty(required = True)	

    communes = RelationshipTo('Commune', 'COMMUNE')

class Commune(StructuredNode):
    id_1 = UniqueIdProperty()
    id_2 = UniqueIdProperty()
    code = UniqueIdProperty()	
    name = StringProperty(required = True)	
    validity = DateTimeProperty()
    geometry = JSONProperty(required = True)	
    level = StringProperty(required = True)	

    users = RelationshipTo('User', 'USER')

class User(StructuredNode):
    id_1 = UniqueIdProperty()
    id_2 = UniqueIdProperty()
    username = StringProperty(required=True, unique_index=True)
    email = StringProperty(required=True, unique_index=True)
    password = StringProperty(required=True, unique_index=True)
    party = StringProperty()
