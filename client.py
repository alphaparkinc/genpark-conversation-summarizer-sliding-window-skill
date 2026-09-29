"""Conversation Summarizer Sliding Window Engine.
100% Python Standard Library.
"""

import re

class SlidingWindowSummarizer:
    """Condenses past conversational dialogue outside the active sliding window."""
    @staticmethod
    def condense_dialogue(messages, window_size=4):
        if len(messages) <= window_size:
            return {"active_window": messages, "summary": None}
        past = messages[:-window_size]
        active = messages[-window_size:]
        key_topics = set()
        for m in past:
            for w in re.findall(r'\b[A-Za-z]{4,}\b', m.get("content", "")):
                if w.lower() not in {"this", "that", "with", "have", "from", "will"}:
                    key_topics.add(w.lower())
        summary = f"Prior dialogue covered: {', '.join(sorted(list(key_topics))[:8])}."
        return {"active_window": active, "summary": summary}
