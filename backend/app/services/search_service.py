import typesense

from app.config import (
    TYPESENSE_HOST,
    TYPESENSE_PORT,
    TYPESENSE_PROTOCOL,
    TYPESENSE_API_KEY,
)


client = typesense.Client({
    "nodes": [{
        "host": TYPESENSE_HOST,
        "port": TYPESENSE_PORT,
        "protocol": TYPESENSE_PROTOCOL,
    }],
    "api_key": TYPESENSE_API_KEY,
    "connection_timeout_seconds": 5,
})

def search_products(
    query: str,
    page: int = 1,
    per_page: int = 20,
    filters: str | None = None,
    sort_by: str | None = None,
):

    search_parameters = {
        "q": query,
        "query_by": (
            "style_number,"
            "style_name,"
            "category,"
            "fabric,"
            "color,"
            "print,"
            "season,"
            "brand,"
            "supplier"
        ),
        "page": page,
        "per_page": per_page,

        # Return facet information
        "facet_by": (
            "category,"
            "fabric,"
            "color,"
            "print,"
            "season,"
            "brand,"
            "supplier"
        ),
    }

    if filters:
        search_parameters["filter_by"] = filters

    if sort_by:
        search_parameters["sort_by"] = sort_by

    return client.collections[
        "finished_goods"
    ].documents.search(search_parameters)