from ariadne import make_executable_schema, QueryType, load_schema_from_path
from shop.resolvers import resolvers as shop_resolvers
from users.resolvers import resolvers as users_resolvers


type_defs = [
    load_schema_from_path("schema/schema.graphql")
]


query = QueryType()

resolvers = [query]
resolvers += shop_resolvers
resolvers += users_resolvers

schema = make_executable_schema(type_defs, resolvers)
