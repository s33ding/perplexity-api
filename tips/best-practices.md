# Tips & Best Practices

## Security
- Never commit API keys — use `PERPLEXITY_API_KEY` env var
- Call API from backend only, never expose key in frontend
- Revoke compromised keys in Settings → API

## Models
- `sonar-pro` — search + citations (best for research)
- `sonar` — lighter/faster search
- `mistral-7b-instruct` — general LLM, no web search

## Performance
- `temperature: 0.1-0.2` for factual queries
- `temperature: 0.7+` for creative tasks
- `stream: true` for real-time UX
- Set `max_tokens` to control cost

## Search API (Sonar)
- Use `search_domain_filter` to restrict sources
- Request JSON mode for structured extraction
- Citations come automatically — surface them to users

## Rate Limits
- Monitor usage in Settings → API
- Check rate limits per model tier
