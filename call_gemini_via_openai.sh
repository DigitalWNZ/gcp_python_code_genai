# 以下的三个export可能没啥作用
export GOOGLE_CLOUD_PROJECT='agolis-allen-first'
export GOOGLE_CLOUD_LOCATION='us-central1'
export GOOGLE_GENAI_USE_VERTEXAI='True'

# 通过OpenAI的方式走AI Studio调用gemini模型
# https://ai.google.dev/gemini-api/docs/openai

curl "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
-H "Content-Type: text/xml" \
-H "Authorization: Bearer AIzaSyA_K32ztwsjoXbowwexZ2cAr1QEFUg6_ZI" \
--data-binary "@raw_example.json"



# 通过OpenAI的方式走Vertex AI调用gemini模型， 注意MODEL_ID 前面必须有google/
# https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/call-vertex-using-openai-library?hl=zh-cn

export PROJECT_ID='agolis-allen-first'
export LOCATION='us-central1'
export MODEL_ID='google/gemini-2.5-pro-preview-03-25'

curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: text/xml" \
https://${LOCATION}-aiplatform.googleapis.com/v1beta1/projects/${PROJECT_ID}/locations/${LOCATION}/endpoints/openapi/chat/completions \
--data-binary "@tool-with-response.json"