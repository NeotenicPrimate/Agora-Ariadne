from ariadne import ObjectType, QueryType, MutationType, make_executable_schema

from neo4j_models import World, Group, Country, Collectivite, Region, Subset, Departement, Epci, Arrondissement, Commune, User
from ariadne_schema import type_defs

query = QueryType()
mutation = MutationType()

world = ObjectType('World')
group = ObjectType('Group')
country = ObjectType('Country')
region = ObjectType('Region')
departement = ObjectType('Departement')
commune = ObjectType('Commune')
user = ObjectType('User')

collectivite = ObjectType('Collectivite')
subset = ObjectType('Subset')
epci = ObjectType('Epci')
arrondissement = ObjectType('Arrondissement')

# Field resolvers

@world.field('countries')
def resolve_world_countries_field(obj, info):
    world = World.nodes.first_or_none(name=obj['name'])
    return [c.__properties__ for c in world.countries]
@world.field('groups')
def resolve_world_groups_field(obj, info):
    world = Group.nodes.first_or_none(name=obj['name'])
    return [c.__properties__ for c in world.groups]

@group.field('world')
def resolve_group_countries_field(obj, info):
    world = World.nodes.first_or_none(name=obj['name'])
    return [c.__properties__ for c in group.world]
@group.field('countries')
def resolve_group_countries_field(obj, info):
    group = Group.nodes.first_or_none(name=obj['name'])
    return [c.__properties__ for c in group.countries]

@country.field('group')
def resolve_country_group_field(obj, info):
    country = Country.nodes.first_or_none(name=obj['name'])
    return country.group[0].__properties__
@country.field('regions')
def resolve_country_regions_field(obj, info):
    country = Country.nodes.first_or_none(name=obj['name'])
    return [r.__properties__ for r in country.regions]
@country.field('collectivites')
def resolve_country_collectivite_field(obj, info):
    country = Country.nodes.first_or_none(name=obj['name'])
    return [c.__properties__ for c in country.collectivites]

@region.field('country')
def resolve_region_country_field(obj, info):
    region = Region.nodes.first_or_none(name=obj['name'])
    return region.country[0].__properties__
@region.field('departements')
def resolve_region_departements_field(obj, info):
    region = Region.nodes.first_or_none(name=obj['name'])
    return [d.__properties__ for d in region.departements]

@departement.field('region')
def resolve_departement_region_field(obj, info):
    departement = Departement.nodes.first_or_none(name=obj['name'])
    return departement.region[0].__properties__
@departement.field('subset')
def resolve_departement_subset_field(obj, info):
    departement = Departement.nodes.first_or_none(name=obj['name'])
    return departement.subset[0].__properties__
@departement.field('communes')
def resolve_departement_communes_field(obj, info):
    departement = Departement.nodes.first_or_none(name=obj['name'])
    return [c.__properties__ for c in departement.communes] 

@commune.field('departement')
def resolve_commune_departement_field(obj, info):
    commune = Commune.nodes.first_or_none(name=obj['name'])
    return commune.departement[0].__properties__
@commune.field('arrondissement')
def resolve_commune_arrondissement_field(obj, info):
    commune = Commune.nodes.first_or_none(name=obj['name'])
    return commune.arrondissement[0].__properties__
@commune.field('epci')
def resolve_commune_epci_field(obj, info):
    commune = Commune.nodes.first_or_none(name=obj['name'])
    return commune.epci[0].__properties__

@collectivite.field('country')
def resolve_collectivite_country_field(obj, info):
    collectivite = Collectivite.nodes.first_or_none(name=obj['name'])
    return collectivite.country[0].__properties__

@subset.field('departements')
def resolve_subset_departements_field(obj, info):
    subset = Subset.nodes.first_or_none(name=obj['name'])
    return [d.__properties__ for d in subset.departements] 

@epci.field('communes')
def resolve_epci_communes_field(obj, info):
    epci = Epci.nodes.first_or_none(name=obj['name'])
    return [c.__properties__ for c in epci.communes] 

@arrondissement.field('communes')
def resolve_epci_communes_field(obj, info):
    arrondissement = Arrondissement.nodes.first_or_none(name=obj['name'])
    return [c.__properties__ for c in arrondissement.communes] 

# Query resolvers

@query.field("world")
def resolve_groups(*_, name):
    return World.nodes.first_or_none(name=name).__properties__
@query.field("worlds")
def resolve_groups(*_):
    return [g.__properties__ for g in World.nodes.all()]

@query.field("group")
def resolve_groups(*_, name):
    return Group.nodes.first_or_none(name=name).__properties__
@query.field("groups")
def resolve_groups(*_):
    return [g.__properties__ for g in Group.nodes.all()]

@query.field("country")
def resolve_countries(*_, name):
    return Country.nodes.first_or_none(name=name).__properties__
@query.field("countries")
def resolve_countries(*_):
    return [c.__properties__ for c in Country.nodes.all()]

@query.field("region")
def resolve_regions(*_, name):
    return Region.nodes.first_or_none(name=name).__properties__
@query.field("regions")
def resolve_regions(*_):
    return [r.__properties__ for r in Region.nodes.all()]

@query.field("departement")
def resolve_departement(*_, name):
    return Departement.nodes.first_or_none(name=name).__properties__
@query.field("departements")
def resolve_departements(*_):
    return [d.__properties__ for d in Departement.nodes.all()]

@query.field("commune")
def resolve_commune(*_, name):
    return Commune.nodes.first_or_none(name=name).__properties__
@query.field("communes")
def resolve_communes(*_):
    return [c.__properties__ for c in Commune.nodes.all()]

@query.field("collectivite")
def resolve_collectivite(*_, name):
    return Collectivite.nodes.first_or_none(name=name).__properties__
@query.field("collectivites")
def resolve_collectivites(*_):
    return [c.__properties__ for c in Collectivite.nodes.all()]

@query.field("subset")
def resolve_subsets(*_, name):
    return Subset.nodes.first_or_none(name=name).__properties__
@query.field("subsets")
def resolve_subsets(*_):
    return [s.__properties__ for s in Subset.nodes.all()]

@query.field("arrondissement")
def resolve_arrondissement(*_, name):
    return Arrondissement.nodes.first_or_none(name=name).__properties__
@query.field("arrondissements")
def resolve_arrondissements(*_):
    return [a.__properties__ for a in Arrondissement.nodes.all()]

@query.field("epci")
def resolve_epci(*_, name):
    return Epci.nodes.first_or_none(name=name).__properties__
@query.field("epcis")
def resolve_epci(*_):
    return [e.__properties__ for e in Epci.nodes.all()]

# Mutations

@mutation.field('createUser')
def resolve_create_user(_, info, username, email, password, party, commune):
    commune = Commune.nodes.first_or_none(name=commune)
    user = User(username=username, email=email, password=password, party=party, commune=commune).save()
    user.commune = commune
    commune.users.connect(user)
    user.save()
    commune.save()
    return user

@mutation.field('deleteUser')
def resolve_delete_user(_, info, username):
    user = User.nodes.first_or_none(username=username)
    user.commune.disconnect_all()
    user.delete()
    return user

@mutation.field('updateUser')
def resolve_update_user(_, info, username, new_username):
    user = User.nodes.first_or_none(username=username)
    user.username = new_username
    user.save()
    return user

schema = make_executable_schema(type_defs, [query, mutation, world, group, country, region, collectivite, departement, arrondissement, epci, commune, user])