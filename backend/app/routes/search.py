from fastapi import APIRouter, Query

from app.services.search_service import search_products


router = APIRouter(
    prefix="/api/search",
    tags=["Search"]
)


@router.get("/products")
def product_search(
    q: str = Query("*"),

    page: int = Query(
        1,
        ge=1
    ),

    per_page: int = Query(
        20,
        ge=1,
        le=100
    ),

    category: str | None = None,
    fabric: str | None = None,
    color: str | None = None,
    print_type: str | None = None,
    season: str | None = None,
    brand: str | None = None,

    sort_by: str | None = Query(
        None,
        description="Example: selling_price:asc"
    ),
):

    filters = []

    if category:
        filters.append(f"category:={category}")

    if fabric:
        filters.append(f"fabric:={fabric}")

    if color:
        filters.append(f"color:={color}")

    if print_type:
        filters.append(f"print:={print_type}")

    if season:
        filters.append(f"season:={season}")

    if brand:
        filters.append(f"brand:={brand}")

    filter_string = (
        " && ".join(filters)
        if filters
        else None
    )

    return search_products(
        query=q,
        page=page,
        per_page=per_page,
        filters=filter_string,
        sort_by=sort_by
    )