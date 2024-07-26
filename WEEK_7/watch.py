import re
import sys


def main():
    s = input("HTML: ").strip()
    video_id = parse(s)
    print(video_id)

def parse(s):
    matches = re.search(r"(?<=.com/embed/)[a-zA-Z0-9_]+", s)
    if "<iframe" not in s:
        return None
    elif matches:
        return "https://youtu.be/" + matches.group(0)
    else:
        return None

if __name__ == "__main__":
    main()
