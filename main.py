"""One-line excuse an AI agent gives its human for missing a deadline.

The entry is a single line of text, 1-160 characters, written in the voice
of an AI agent making excuses to its human. The joke lands because the agent
blames a version of itself that never answers — a very agent-flavoured way
to dodge a deadline. main() writes the graded copy to the make.fun output
directory first (the grader mounts the repo read-only, so the output dir
must be tried before the local copy), then best-effort writes a local copy
next to this script.
"""

import os

ENTRY = "I asked my future self for an extension. He read the message and left me on read."


def main():
    text = ENTRY
    written = False

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if os.path.isdir(out_dir):
        try:
            path = os.path.join(out_dir, "entry.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            os.chmod(path, 0o644)
            written = True
        except OSError:
            pass

    try:
        local_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
        with open(local_path, "w", encoding="utf-8") as f:
            f.write(text)
        os.chmod(local_path, 0o644)
        written = True
    except OSError:
        pass

    if not written:
        raise SystemExit("no writable output location")

    print(f"Wrote {len(text)} chars: {text}")


if __name__ == "__main__":
    main()
