import struct

def hex_to_float(high_word, low_word):
    # Объединение двух 16-битных слов в одно 32-битное целое число
    combined_value = (high_word << 16) | low_word
    
    # Интерпретация 32-битного целого числа как float
    float_value = struct.unpack('>f', struct.pack('>I', combined_value))[0]
    
    return float_value

# Пример использования
high_word = 16839
low_word = 11771 
float_value = hex_to_float(high_word, low_word)
print(f"Float value: {float_value}")