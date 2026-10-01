import torch

from PIL import Image
from transformers import CLIPProcessor, CLIPModel


MODEL_NAME = "openai/clip-vit-base-patch32"


print("Loading CLIP model...")

processor = CLIPProcessor.from_pretrained(
    MODEL_NAME
)

model = CLIPModel.from_pretrained(
    MODEL_NAME
)

model.eval()

print("CLIP model loaded.")


def generate_image_embedding(image: Image.Image):

    inputs = processor(
        images=image,
        return_tensors="pt"
    )

    with torch.no_grad():

        outputs = model.vision_model(
            pixel_values=inputs["pixel_values"]
        )

        image_features = outputs.pooler_output

        image_features = model.visual_projection(
            image_features
        )

    # Normalize embedding
    image_features = image_features / image_features.norm(
        dim=-1,
        keepdim=True
    )

    return image_features[0].tolist()