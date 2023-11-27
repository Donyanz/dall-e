import openai
from config import OPENAI_API_KEY
from params import SELECT_SIZE
import telegram

async def dall_e(message):
    openai.api_key = OPENAI_API_KEY
    response = openai.images.generate(
    model="dall-e-3",
    prompt=message,
    size="1024x1024",
    quality="standard",
    n=1,
    )

    image_url = response.data[0].url
    return image_url

