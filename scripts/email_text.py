#!/usr/bin/env python3
"""
Print the full plain text of every message in a saved Superhuman get_thread result.

Superhuman returns receipt emails as raw HTML (100k+ characters for one Uber thread),
which is too big to read inline. This strips markup only: every word of visible text
is kept, so nothing in the receipt is lost.

Usage:
    python3 email_text.py THREAD_RESULT.json
"""

import html
import json
import re
import sys


def to_text(body: str) -> str:
    body = re.sub(r"<(style|script|head)\b.*?</\1>", " ", body, flags=re.S | re.I)
    body = re.sub(r"<br\s*/?>|</(p|div|tr|td|li|h\d)>", "\n", body, flags=re.I)
    body = re.sub(r"<[^>]+>", " ", body)
    body = html.unescape(body)
    lines = [re.sub(r"[ \t ‌]+", " ", l).strip() for l in body.splitlines()]
    return "\n".join(l for l in lines if l)


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    with open(sys.argv[1]) as f:
        thread = json.load(f)
    for m in thread.get("messages", []):
        print(f"=== message {m.get('message_id')} | {m.get('sent_at')} | {m.get('from')}")
        print(f"Subject: {m.get('subject')}")
        print(to_text(m.get("body") or ""))
        print()


if __name__ == "__main__":
    main()
