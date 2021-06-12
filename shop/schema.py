from ariadne import gql

type_defs = gql("""
    
    scalar Upload
    
    type Query {
        allCategories : [Category!]!
        allProducts: [Product!]!
        product(id: Int!): Product!
    }
    
    type Mutation {
        createCategory(
            name: String!
        ): createCategoryPayload!
        
        createProduct(
            categoryId: Int!
            name: String!
            description: String!
            price: Float!
            image: Upload!
        ): createProductPayload!
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
    
    type createCategoryPayload {
        error: String!
        success: Boolean!
        category: Category
    }
    
    type createProductPayload {
        success: Boolean!
        error: String!
        product: Product!
    }
    
""")