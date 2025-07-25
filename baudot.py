
baudot_table = {
    'A': '00011', 'B': '11001', 'C': '01110', 'D': '01001', 'E': '00001',
    'F': '10110', 'G': '11010', 'H': '00100', 'I': '00110', 'J': '10011',
    'K': '01010', 'L': '01100', 'M': '10010', 'N': '10000', 'O': '11000',
    'P': '10100', 'Q': '11100', 'R': '01101', 'S': '01011', 'T': '00101',
    'U': '11110', 'V': '10111', 'W': '01111', 'X': '11011', 'Y': '11101',
    'Z': '10101', ' ': '00000'}
def text_to_baudot(text):
    text = text.upper()
    encoded_text = ''
    for char in text:
        if char in baudot_table:
            encoded_text += baudot_table[char]
    return encoded_text
def baudot_to_text(encoded_text):
    decoded_text = ''
    for i in range(0, len(encoded_text), 5):
        baudot_char = encoded_text[i:i+5]
        for char, code in baudot_table.items():
            if baudot_char == code:
                decoded_text += char
                break
    return decoded_text
mensaje_original = "HELLO"
mensaje_codificado = text_to_baudot(mensaje_original)
mensaje_decodificado = baudot_to_text(mensaje_codificado)
print("Mensaje original: ", mensaje_original)
print("Mensaje codificado en Baudot: ", mensaje_codificado)
print("Mensaje decodificado: ", mensaje_decodificado)