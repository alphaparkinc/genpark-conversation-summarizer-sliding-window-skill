# genpark-conversation-summarizer-sliding-window-skill

Agent Skill implementing **Conversation History Summarization & Sliding Window Compression** in 100% Python standard library.

## Architectural Flow
```mermaid
flowchart TD
    Messages["Long Dialogue History (M_1 .. M_T)"] --> Partition["Partition at Window Boundary (T - W)"]
    Partition --> Old["Past Messages (1 .. T - W)"]
    Partition --> Active["Active Window Messages (T - W + 1 .. T)"]
    Old --> Summarizer["Key Topic Extraction & Semantic Compactor"]
    Summarizer --> Summary["Concise Summary Sentence"]
    Summary & Active --> Prompt["Compressed High-Retention Prompt"]
```
