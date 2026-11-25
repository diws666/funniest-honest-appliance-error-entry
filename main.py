import os

LINE = "Error 404: Ice not found. The freezer gave up, and honestly, so did I."  # verified: 70 chars

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
output_path = os.path.join(output_dir, "entry.txt")

with open(output_path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

print(len(LINE))
