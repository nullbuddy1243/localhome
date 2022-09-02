import sys

def main(words, between_char="_"): 
  print(f"---\ninput: {words} \nbetween_char: {between_char} \n---")
  return between_char.join(words.split(" "))

argslen = len(sys.argv)
if argslen == 2:
  print(f"got sys.argv[1] = {sys.argv[1]}")
  between_char = sys.argv[1]
  between_char_len = len(between_char)
  strip = between_char_len + 1
  print(f"{between_char} {between_char_len} {strip}")
  
  output = main(sys.stdin.read(), between_char=sys.argv[1])
  
  print(f"{output[:-strip]}")
  
  print("--- ;) ---")
else:
  print(f"no sys.argv[1] for between_char so using default _")
  between_char = "_"
  between_char_len = len(between_char)
  strip = between_char_len + 1
  print(f"{between_char} {between_char_len} {strip}")

  output = main(sys.stdin.read(), between_char=between_char)
  
  print(f"{output[:-strip]}")
  
  print("--- :) ---")
