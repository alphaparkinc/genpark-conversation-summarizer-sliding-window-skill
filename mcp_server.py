import sys
import json
from client import SlidingWindowSummarizer

def handle_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-conversation-summarizer-sliding-window-skill", "version": "1.0.0"}
            }
        }
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "compress_dialogue_history",
                        "description": "Compress long dialogue history into sliding active window and summarized prefix",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "messages": {
                                    "type": "array",
                                    "items": {"type": "object"},
                                    "description": "Conversation message history"
                                },
                                "window_size": {"type": "integer", "default": 4}
                            },
                            "required": ["messages"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        
        if tool_name == "compress_dialogue_history":
            m = args.get("messages", [])
            w = args.get("window_size", 4)
            res = SlidingWindowSummarizer.condense_dialogue(m, w)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
