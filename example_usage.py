from client import SlidingWindowSummarizer

history = [
    {"role": "user", "content": "How do we implement Raft leader election?"},
    {"role": "assistant", "content": "Raft uses randomized election timeouts."},
    {"role": "user", "content": "What happens on split vote?"},
    {"role": "assistant", "content": "The timeout triggers a new candidate term."},
    {"role": "user", "content": "Let us implement it now."}
]

res = SlidingWindowSummarizer.condense_dialogue(history, window_size=2)
print("Summary of Past Conversation:", res["summary"])
print("Active Window Count:", len(res["active_window"]))
