from ariadne import QueryType, MutationType
from .models import Product, Category
from django.conf import settings


query = QueryType()


@query.field("all_categories")
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

@query.field('all_products')
def resolve_all_products(_, info):
    return Product.objects.all()


@query.field('product')
def resolve_product(_, info, id):
    return Product.objects.get(pk=id)


resolvers = [query]

