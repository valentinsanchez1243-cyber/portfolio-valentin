import sys

def check_balance(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We only care about style and script blocks
    import re
    blocks = re.findall(r'<(style|script).*?>(.*?)</\1>', content, re.DOTALL | re.IGNORECASE)
    
    for i, (tag, code) in enumerate(blocks):
        open_b = code.count('{')
        close_b = code.count('}')
        if open_b != close_b:
            print(f"Block {i+1} (<{tag}>): Open={open_b}, Close={close_b}")
            # Try to find where it breaks
            level = 0
            for line_num, line in enumerate(code.split('\n'), 1):
                level += line.count('{')
                level -= line.count('}')
                if level < 0:
                    print(f"  Negative level at line {line_num} in block")
                    level = 0
            if level > 0:
                print(f"  Unclosed braces ({level}) at end of block")

if __name__ == "__main__":
    check_balance(sys.argv[1])
