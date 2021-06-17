from ariadne import MutationType, QueryType, convert_kwargs_to_snake_case, snake_case_fallback_resolvers
from django.contrib.auth import get_user_model
from django.conf import settings
from ariadne_jwt import *
from .models import Profile


query = QueryType()
mutation = MutationType()


@query.field("allUsers")
def resolve_all_users(_, info):
    users = get_user_model().objects.all()

    return [
        {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "profile": Profile.objects.get(pk=user.id)
        }for user in users
    ]


@query.field("user")
def resolve_user(_, info, id):
    user = get_user_model().objects.get(pk=id)

    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "profile": Profile.objects.get(pk=user.id)
    }


@query.field('profile')
@convert_kwargs_to_snake_case
def resolve_profile(_, info, user_id):
    prof = Profile.objects.get(user_id=user_id)
    return {
        "id": prof.id,
        "user": prof.user,
        "firstname": prof.firstname,
        "lastname": prof.lastname,
        "phone": prof.phone,
        "image": f'{settings.SITE_DOMAIN_NAME}{prof.image.url}'
    }


@mutation.field("Signup")
def resolve_signup(_, info, username, email, password, password1):
    try:
        if password1 == password:
            user = get_user_model().objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.save()
            return {
                "success": True,
                "error": "none",
                "user": user
            }
        else:
            return {
                "success": False,
                "error": "Passwords did not match",
                "user": None
            }
    except ValueError as err:
        return {
            "success": False,
            "error": err,
            "user": None
        }


mutation.set_field('verifyToken', resolve_verify)
mutation.set_field('refreshToken', resolve_refresh)
mutation.set_field('tokenAuth', resolve_token_auth)

resolvers = [query, mutation, snake_case_fallback_resolvers, GenericScalar]