from decimal import Decimal, getcontext

def arithmetic_encode(text):
    getcontext().prec = 70
    freq_table = {}
    for char in text:
        freq_table[char] = freq_table.get(char, 0) + 1
    total_chars = len(text)
    for char in freq_table:
        freq_table[char] /= total_chars
    intervals = {}
    low = Decimal(0.0)
    for char, freq in freq_table.items():
        high = low + Decimal(freq)
        intervals[char] = (low, high)
        low = high
    print("Таблица интервалов:")
    print("| Символ | Левая граница | Правая граница |")
    print("|--------|---------------|----------------|")
    for char, (low, high) in intervals.items():
        print(f"| {char}      | {low:.10f}       | {high:.10f}       |")
    low = Decimal(0.0)
    high = Decimal(1.0)
    for symbol in text:
        symbol_low, symbol_high = intervals[symbol]
        range_size = high - low
        high = low + range_size * symbol_high
        low = low + range_size * symbol_low
    encoded_value = (low + high) / 2
    formatted_value = f"{encoded_value:.65f}"
    binary_value = ""
    decimal_value = encoded_value
    for _ in range(65):
        decimal_value *= 2
        bit = int(decimal_value)
        binary_value += str(bit)
        decimal_value -= bit
    return formatted_value, binary_value

text = "алиевасланбекмагомедович"
encoded_value, binary_value = arithmetic_encode(text)
print(f"\nEncoded value for '{text}': {encoded_value}")
print(f"Binary representation: {binary_value}")
