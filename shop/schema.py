from ariadne import gql

type_defs = gql("""
    
    type Query {
        all_categories : [Category!]!
        all_products: [Product!]!
        product(id: Int!): Product!
    }
    
    
    type Category {
        id: Int!
        name: String!
        products: [Product!]!
    }
    
    type Product {
        id: Int!
        category: Category!
        name: String!
        description: String!
        image: String!
    }
    
""")