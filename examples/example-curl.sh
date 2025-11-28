bash
#!/bin/bash
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Write a poem about AI",
    "max_tokens": 100,
    "temp": 0.8
  }'
