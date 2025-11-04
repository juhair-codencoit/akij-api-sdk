from pathlib import Path
import json

def write_response_to_file(response, filename):
    try:
        Path(f"{filename}.json").write_text(json.dumps(response, indent=4))
    except Exception as e:
        print(f"Error writing to file: {e}")