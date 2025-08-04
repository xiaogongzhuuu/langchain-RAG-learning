# OpenAI API Documentation (Sample)

## Introduction
The OpenAI API provides access to powerful language models that can understand and generate natural language. It can be used for tasks such as chatbots, summarization, content generation, and more.

## Authentication
All API requests must be authenticated using your OpenAI API key. You can set your key as an environment variable `OPENAI_API_KEY`.

## Chat Completions
The Chat Completions endpoint is used to interact with models like `gpt-3.5-turbo` and `gpt-4`. You must provide a list of messages, where each message has a `role` (`system`, `user`, or `assistant`) and `content`.

## Parameters
- `model`: The name of the model to use (e.g., `gpt-4`)
- `messages`: An array of message objects
- `temperature`: Controls randomness (0.0 = deterministic, 1.0 = creative)

## Embeddings
The embeddings endpoint allows you to convert text into numeric vectors for tasks like semantic search and clustering.

## Rate Limits
Your rate limits depend on your account and the type of model you're using. Check the dashboard for your limits.

## Pricing
Pricing is based on the number of tokens processed by the model. Refer to the [pricing page](https://openai.com/pricing) for details.