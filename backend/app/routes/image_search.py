import os
import tempfile

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.image_search_service import search_similar_images


router = APIRouter(
    prefix="/api/image-search",
    tags=["Image Search"]
)


@router.post("")
async def image_search(
    file: UploadFile = File(...),
):

    if not file.content_type:
        raise HTTPException(
            status_code=400,
            detail="File type could not be determined."
        )

    if not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail="Please upload an image file."
        )

    suffix = os.path.splitext(file.filename or "")[1]

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix
    ) as temp_file:

        contents = await file.read()

        temp_file.write(contents)

        temp_path = temp_file.name

    try:

        results = search_similar_images(
            temp_path,
            match_count=10
        )

        return {
            "results": results
        }

    finally:

        if os.path.exists(temp_path):
            os.remove(temp_path)