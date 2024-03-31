from pyspark.sql.functions import concat, lit


def get_products(products_df, categories_df, relations_df):
    products_w_cat = relations_df.join(
        products_df, on="product_id"
    ).join(categories_df, on="category_id"
    ).select(
        concat("product_name", lit(' - '),"category_name").alias('Results')
    ).orderBy("product_name")

    products_wo_cat = products_df.join(
        relations_df, on="product_id", how="left_anti"
    ).select("product_name").orderBy("product_name")

    return products_w_cat.union(products_wo_cat)
