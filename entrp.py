import math
from collections import Counter

def calculate_entropy(text):
    freq_table = Counter(text)
    total_chars = len(text)
    probabilities = [count / total_chars for count in freq_table.values()]
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return entropy

text = "алиевасланбекмагомедович"
entropy = calculate_entropy(text)
print(f"Энтропия текста '{text}': {entropy:.4f} бит/символ")
