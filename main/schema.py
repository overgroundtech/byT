from ariadne import make_executable_schema, QueryType
from shop.schema import type_defs as shop_type_defs
from shop.resolvers import resolvers as shop_resolvers

type_defs = [shop_type_defs]


query = QueryType()

resolvers = [query]
resolvers += shop_resolvers

schema = make_executable_schema(type_defs, resolvers)
