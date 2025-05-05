#!/bin/sh
set -e

# Start Ollama server in background
ollama serve &

# Wait until Ollama is ready
echo "🕒 Waiting for Ollama to start..."
until curl -s http://localhost:11434/api/tags >/dev/null; do
  sleep 1
done

# Pull the model you want (change "mistral" if needed)
echo "📦 Pulling mistral model..."
ollama pull mistral

# Confirm model is there
echo "✅ Available models:"
curl -s http://localhost:11434/api/tags

# Keep container alive
tail -f /dev/null
