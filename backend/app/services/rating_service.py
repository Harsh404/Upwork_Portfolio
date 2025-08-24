from app.crud import crud_product
from app.schema.schema_product import ReviewSchema


async def add_review_to_product(product_id: str, review: ReviewSchema, user) -> dict:
    product = await crud_product.get_product_by_id(product_id)
    if not product:
        return None

    # Ensure user cannot review twice
    for r in product["reviews"]:
        if r["user_id"] == user["id"]:
            raise ValueError("User already reviewed this product")

    product["reviews"].append(review.dict())

    # Recalculate average rating
    ratings = [r["rating"] for r in product["reviews"]]
    avg_rating = round(sum(ratings) / len(ratings), 2)

    product["average_rating"] = avg_rating

    updated = await crud_product.update_product(product_id, {
        "reviews": product["reviews"],
        "average_rating": avg_rating
    })

    return updated


def calculate_average(ratings: list[int]) -> dict:
    if not ratings:
        return {"average": 0.0, "count": 0}
    avg = sum(ratings) / len(ratings)
    return {"average": round(avg, 2), "count": len(ratings)}
