from ariadne import MutationType, QueryType
from ariadne_jwt import *


query = QueryType()
mutation = MutationType()

mutation.set_field('verifyToken', resolve_verify)
mutation.set_field('refreshToken', resolve_refresh)
mutation.set_field('tokenAuth', resolve_token_auth)

resolvers = [query, mutation, GenericScalar]