from openai import OpenAI

client = OpenAI(
  api_key="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"
)

response = client.responses.create(
  model="gpt-5-nano",
  input="write a haiku about ai",
  store=True,
)

print(response.output_text);
