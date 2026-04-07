import random
import string
import os
import time
import subprocess

def generate_test(filename, length1, length2, alphabet_size=10):
    chars = string.ascii_lowercase[:alphabet_size]
    alphabet = {c: random.randint(1, 100) for c in chars}
    
    s1 = ''.join(random.choice(chars) for _ in range(length1))
    s2 = ''.join(random.choice(chars) for _ in range(length2))
    
    with open(filename, 'w') as f:
        f.write(f"{len(alphabet)}\n")
        for char, val in alphabet.items():
            f.write(f"{char} {val}\n")
        f.write(f"{s1}\n")
        f.write(f"{s2}\n")

os.makedirs('data', exist_ok=True)

test_configs = [
    (25, 25),
    (50, 50),
    (100, 100),
    (200, 200),
    (300, 300),
    (400, 400),
    (500, 500),
    (750, 750),
    (1000, 1000),
    (1500, 1500)
]

print("| Input File | Length A | Length B | Runtime (s) |")
print("|---|---|---|---|")

for i, (l1, l2) in enumerate(test_configs, 1):
    filename = f'data/test{i}.in'
    generate_test(filename, l1, l2)
    
    start_time = time.time()
    subprocess.run(['python', 'src/main.py', filename], capture_output=True)
    end_time = time.time()
    
    print(f"| `test{i}.in` | {l1} | {l2} | {end_time - start_time:.6f} |")
