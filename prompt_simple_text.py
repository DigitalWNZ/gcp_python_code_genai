# REF: https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart-multimodal#gen-ai-sdk-for-python
import os
from google import genai
from google.genai.types import HttpOptions,Part

if __name__ == '__main__':

    path_to_credential = '/Users/wangez/Downloads/GCP_Credentials/agolis-allen-first-13f3be86c3d1.json'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = path_to_credential

    os.environ['GOOGLE_CLOUD_PROJECT']='agolis-allen-first'
    os.environ['GOOGLE_CLOUD_LOCATION']='us-central1'
    os.environ['GOOGLE_GENAI_USE_VERTEXAI']='True'


    client = genai.Client(http_options=HttpOptions(api_version="v1"))
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=[
            "What is shown in this image?",
            Part.from_uri(
                file_uri="gs://cloud-samples-data/generative-ai/image/scones.jpg",
                mime_type="image/jpeg",
            ),
        ],
    )
    print(response.text)

    with open('/Users/wangez/Downloads/Img_Invetory/firebase.png','rb') as f:
        img_bytes=f.read()
    
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=[
            "What is shown in this image?",
            Part.from_bytes(
                data=img_bytes,
                 mime_type='image/jpeg',
            ),
            'Caption this image.'
        ],
    )
    print(response.text)






