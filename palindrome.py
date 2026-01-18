import sys
import math
def pal(text):
    return text == text[::-1]
if __name__ == "__main__":
    if len(sys.argv)==2:
        script_name = sys.argv[0]
        text = sys.argv[1]
    else:
        script_name = sys.argv[0]
        text = "madam"
        print(f"Palindrome: {pal(text)}")