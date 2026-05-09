# Perplexity API

Utilities, tips, and documentation for using the Perplexity API (pplx-api + Sonar/Search).

## Overview

- **pplx-api**: Chat endpoint compatible with OpenAI client
- **Sonar / Search API**: Web search + LLM with citations and structured JSON

**Base URL**: `https://api.perplexity.ai`  
**Endpoint**: `POST /chat/completions`

## Structure

```
utils/   - Python and Bash utility scripts
tips/    - Best practices and usage tips
docs/    - Official documentation references
```

## Quick Start

```bash
export PERPLEXITY_API_KEY="pplx-..."
python utils/chat.py "Your question here"
# or
bash utils/chat.sh "Your question here"
```

## API Key Setup

1. [Perplexity Settings → API](https://www.perplexity.ai/settings/api)
2. Generate key
3. `export PERPLEXITY_API_KEY="pplx-..."`

## Official Docs

- [API Docs](https://docs.perplexity.ai)
- [Model Cards](https://docs.perplexity.ai/docs/model-cards)
- [Sonar / Search](https://docs.perplexity.ai/guides/search)
