import random
import google.generativeai as genai
from django.conf import settings
from openai import OpenAI


def get_summary(text: str) -> str:
    provider = getattr(settings, 'AI_PROVIDER', 'manual')

    match provider:
        case "manual":
            return generate_random_summary(text)
        case "gemini":
            return get_gemini_summary(text)
        case "openai":
            return get_openai_summary(text)
        case _:
            return "Invalid provider."



def get_gemini_summary(text: str) -> str:
    genai.configure(api_key=settings.GEMINI_API_KEY)
    print(settings.GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f"Resume el siguiente texto de forma concisa: {text}")
    return response.text

def get_openai_summary(text: str) -> str:
    client = OpenAI(api_key=settings.OPENAI_API_KEY)

    response = client.chat.completions.create(
        model="gpt-4o-mini", # O el modelo que prefieras
        messages=[
            {"role": "user", "content": f"Resume el siguiente texto de forma concisa: {text}"}
        ]
    )
    return response.choices[0].message.content

def generate_random_summary(text: str) -> str:
    texts = [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In vestibulum tortor sollicitudin justo tempor accumsan. Pellentesque non feugiat quam, in aliquam felis.",
        "Duis quis dictum libero. Pellentesque elementum magna ut turpis elementum eleifend. Nam eu nibh nibh. Suspendisse id enim sit amet massa aliquam viverra.",
        "Nam eu sollicitudin tortor, eleifend dapibus velit. Pellentesque aliquam sodales velit non blandit. Proin feugiat lacinia rutrum.",
        "Phasellus et nunc quis erat maximus blandit ac sit amet enim. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras est eros, feugiat at nisi at, varius pellentesque enim.",
        "Ut faucibus, enim fringilla scelerisque pulvinar, orci purus ultrices neque, nec tincidunt diam dui quis purus. Sed rhoncus, dui ac pharetra lobortis, lorem magna tincidunt nibh, non sagittis ante mi cursus orci.",
    ]

    index = random.randint(0, len(texts)-1)
    return texts[index]