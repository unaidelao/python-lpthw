import sys
script, input_encoding, error = sys.argv


def main(languaje_file, encoding, errors):
	line = languaje_file.readline()
	
	if line:
		print_line(line, encoding, errors)
		return main(languaje_file, encoding, errors)
		

# Truco mnemotécnico: DBES (Decode Bytes, Encode Strings)
def print_line(line, encoding, errors):
	next_lang = line.strip()
	raw_bytes = next_lang.encode(encoding, errors=errors)
	# En verdad, cooked_string es lo mismo que next_lang
	cooked_string = raw_bytes.decode(encoding, errors=errors)
	
	print(raw_bytes, "<===>", cooked_string)
	
	
languajes = open("languages.txt", encoding="utf-8")

main(languajes, input_encoding, error)