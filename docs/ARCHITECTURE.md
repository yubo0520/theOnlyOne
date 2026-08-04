# Architecture

```text
Client
  -> FastAPI conversation service
      -> character pack loader
      -> memory-card retrieval
      -> OpenAI-compatible streaming model
      -> optional external voice service
```

The engine and character content are deliberately separate. A private character pack can contain persona rules, memories, pronunciation dictionaries, and voice metadata without entering this repository.

## Design boundaries

- The LLM provider is replaceable through environment variables.
- Voice inference is a separate service and may be local or remote.
- Character packs are selected by `character_id` and live outside engine code.
- Retrieved memories are evidence, not permission to invent missing canon.
- User conversation memory is not implemented in the public scaffold yet.

