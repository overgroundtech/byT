from ariadne import QueryType, MutationType, convert_kwargs_to_snake_case, upload_scalar, snake_case_fallback_resolvers
from .models import Product, Category
from django.conf import settings


query = QueryType()
mutation = MutationType()


@query.field("allCategories")
def resolve_all_categories(_, info):
    categories = [
        {
            "id": cat.id,
            "name": cat.name,
            "products": [
                {
                    "id": prod.id,
                    "name": prod.name,
                    "description": prod.description,
                    "image": f'{settings.SITE_DOMAIN_NAME}{prod.image.url}'
                } for prod in Product.objects.filter(category_id=cat.id)
            ]
        }for cat in Category.objects.all()
    ]

    return categories


@query.field('allProducts')
def resolve_all_products(_, info):
    products = [
        {
            "id": prod.id,
            "name": prod.name,
            "description": prod.description,
            "price": prod.price,
            "image": f'{settings.SITE_DOMAIN_NAME}{prod.image.url}',
            "category": prod.category
        } for prod in Product.objects.all()
    ]
    return products


@query.field('product')
def resolve_product(_, info, id):
    prod = Product.objects.get(pk=id)

    return {
        "id": prod.id,
        "name": prod.name,
        "description": prod.description,
        "price": prod.price,
        "image": f'{settings.SITE_DOMAIN_NAME}{prod.image.url}',
        "category": prod.category
    }


@mutation.field('createCategory')
def resolve_create_category(_, info, name):
    try:
        category = Category.objects.create(name=name)
        category.save()
        return {
            "error": "No Error",
            "success": True,
            "category": category
        }
    except ValueError as error:
        return {
            "error": error,
            "success": False,
            "category": None
        }


@mutation.field("createProduct")
@convert_kwargs_to_snake_case
def resolve_create_product(_, info, name, description, price, image, category_id):
    try:
        product = Product.objects.create(
            category_id=category_id,
            name=name,
            price=price,
            description=description,
            image=image
        )
        product.save()
        return {
            "success": True,
            "error": "no errors",
            "product": product
        }
    except ValueError as error:
        return {
            "error": error,
            "success": False,
            "product": None
        }


resolvers = [query, mutation, snake_case_fallback_resolvers, upload_scalar]
