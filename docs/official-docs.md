# Official Documentation Reference

## Authentication

```
Authorization: Bearer ${PERPLEXITY_API_KEY}
Content-Type: application/json
```

## Response Format

```json
{
  "id": "uuid",
  "model": "sonar-pro",
  "choices": [{"index": 0, "finish_reason": "stop", "message": {"role": "assistant", "content": "..."}}],
  "usage": {"prompt_tokens": 40, "completion_tokens": 22, "total_tokens": 62}
}
```

## Models

| Model | Type | Use Case |
|-------|------|----------|
| `sonar-pro` | Search + LLM | Research with citations |
| `sonar` | Search + LLM | Fast search queries |
| `mistral-7b-instruct` | LLM only | General chat |

## Links

- https://docs.perplexity.ai
- https://www.perplexity.ai/settings/api
- https://docs.perplexity.ai/docs/model-cards
- https://docs.perplexity.ai/guides/search
