import codecs

def ascii_to_ebcdic(text):
    try:
        # Codificación ASCII a EBCDIC (usando el mapeo CP500 de EBCDIC)
        ebcdic_text = codecs.encode(text, 'cp500')
        return ebcdic_text
    except Exception as e:
        print("Error:", e)
        return None

# Cadena de texto en formato ASCII
texto_ascii = "Hola, esto es un ejemplo de EBCDIC!"

# Convertir a EBCDIC
texto_ebcdic = ascii_to_ebcdic(texto_ascii)

if texto_ebcdic:
    print("Texto en formato EBCDIC:", texto_ebcdic)
else:
    print("La conversión a EBCDIC no pudo realizarse.")
