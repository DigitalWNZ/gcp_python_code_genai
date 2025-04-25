# Run on VM instead of local because of IP contraint
from openai import OpenAI
import os,json

# path_to_credential = '/Users/wangez/Downloads/GCP_Credentials/agolis-allen-first-13f3be86c3d1.json'
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = path_to_credential

# os.environ['GOOGLE_CLOUD_PROJECT']='agolis-allen-first'
# os.environ['GOOGLE_CLOUD_LOCATION']='us-central1'
# os.environ['GOOGLE_GENAI_USE_VERTEXAI']='True'

with open('/Users/wangez/Downloads/Customer_Manus/raw_example.json', 'r') as file:
    request_data = file.read()
request_json =json.loads(request_data)

messages=request_json['messages'] if 'messages' in request_json else None
model=request_json['model'] if 'model' in request_json else None
audio=request_json['audio'] if 'audio' in request_json else None
frequency_penalty=request_json['frequency_penalty'] if 'frequency_penalty' in request_json else None
function_call=request_json['function_call'] if 'function_call' in request_json else None
functions=request_json['functions'] if 'functions' in request_json else None
logit_bias=request_json['logit_bias'] if 'logit_bias' in request_json else None
logprobs=request_json['logprobs'] if 'logprobs' in request_json else None
max_completion_tokens=request_json['max_completion_tokens'] if 'max_completion_tokens' in request_json else None
max_tokens=request_json['max_tokens'] if 'max_tokens' in request_json else None
metadata=request_json['metadata'] if 'metadata' in request_json else None
modalities=request_json['modalities'] if 'modalities' in request_json else None
n=request_json['n'] if 'n' in request_json else None
parallel_tool_calls=request_json['parallel_tool_calls'] if 'parallel_tool_calls' in request_json else None
prediction=request_json['prediction'] if 'prediction' in request_json else None
presence_penalty=request_json['presence_penalty'] if 'presence_penalty' in request_json else None
reasoning_effort=request_json['reasoning_effort'] if 'reasoning_effort' in request_json else None
response_format=request_json['response_format'] if 'response_format' in request_json else None
seed=request_json['seed'] if 'seed' in request_json else None
service_tier=request_json['service_tier'] if 'service_tier' in request_json else None
stop=request_json['stop'] if 'stop' in request_json else None
store=request_json['store'] if 'store' in request_json else None
stream=request_json['stream'] if 'stream' in request_json else None
stream_options=request_json['stream_options'] if 'stream_options' in request_json else None
temperature=request_json['temperature'] if 'temperature' in request_json else None
tool_choice=request_json['tool_choice'] if 'tool_choice' in request_json else None
tools=request_json['tools'] if 'tools' in request_json else None
top_logprobs=request_json['top_logprobs'] if 'top_logprobs' in request_json else None
top_p=request_json['top_p'] if 'top_p' in request_json else None
user=request_json['user'] if 'user' in request_json else None
web_search_options=request_json['web_search_options'] if 'web_search_options' in request_json else None
extra_headers=request_json['extra_headers'] if 'extra_headers' in request_json else None
extra_query=request_json['extra_query'] if 'extra_query' in request_json else None
extra_body=request_json['extra_body'] if 'extra_body' in request_json else None
timeout=request_json['timeout'] if 'timeout' in request_json else None

print(stop)


client = OpenAI(
    api_key="AIzaSyA_K32ztwsjoXbowwexZ2cAr1QEFUg6_ZI",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.0-flash",
    messages=messages,
    # audio=audio,
    # max_completion_tokens=max_completion_tokens,
    max_tokens=max_tokens,
    # modalities=modalities,
    # n=n,
    # parallel_tool_calls=parallel_tool_calls,
    # presence_penalty=presence_penalty,
    # reasoning_effort=reasoning_effort,
    # response_format=response_format,
    # stop=stop,
    # stream=stream,
    # stream_options=stream_options,
    # temperature=temperature,
    # tool_choice=tool_choice,
    # tools=tools,
    # top_p=top_p,
    # user=user,
    # extra_headers=extra_headers,
    # extra_query=extra_query,
    # extra_body=extra_body,
    # timeout=timeout

    # frequency_penalty=frequency_penalty,
    # function_call=function_call,
    # functions=functions,
    # logit_bias=logit_bias,
    # logprobs=logprobs,
    # metadata=metadata,
    # prediction=prediction,
    # seed=seed,
    # service_tier=service_tier,
    # store=store,
    # top_logprobs=top_logprobs,
    # web_search_options=web_search_options,
)

print(response.choices[0].message)