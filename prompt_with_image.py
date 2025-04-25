# REF: https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart-multimodal#gen-ai-sdk-for-python
import os
from google import genai
from google.genai.types import HttpOptions

if __name__ == '__main__':

    path_to_credential = '/Users/wangez/Downloads/GCP_Credentials/agolis-allen-first-13f3be86c3d1.json'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = path_to_credential

    os.environ['GOOGLE_CLOUD_PROJECT']='agolis-allen-first'
    os.environ['GOOGLE_CLOUD_LOCATION']='us-central1'
    os.environ['GOOGLE_GENAI_USE_VERTEXAI']='True'


    client = genai.Client(http_options=HttpOptions(api_version="v1"))
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents="How does AI work?",
    )
    print(response.text)



