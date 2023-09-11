transform_table = {0b000:0b010, 
                       0b001:0b110,
                       0b010:0b000,
                       0b011:0b111,
                       0b100:0b101,
                       0b101:0b100,
                       0b110:0b001,
                       0b111:0b011}

def print_bin(plain: int, ciph):
    print("{:03b}".format(plain) + " " + "{:03b}".format(ciph))

def peel_lsb_three(num: int) -> int:
    mask = 0b111
    return num & mask

def shift_by_three(num: int) -> int:
    return num >> 3

def apply_cbc(ciph_text: int, p_text: int) -> int:
    scramble =  ciph_text ^ p_text
    scramble = transform_table[scramble]
    return scramble

def main():
    iv = 0b110
    code_length = 3
    plaintext_str: str = input("Enter plaintext: ")
    plaintext_length = len(plaintext_str) * 8
    length_check = plaintext_length / code_length
    if (length_check != int(length_check)):
        raise ValueError("the number of characters in your plain text must be divisible by 3")
    plaintext_code = 0
    for c in plaintext_str:
        plaintext_code *= 256
        plaintext_code += ord(c)

    plaintext_list = []
    for i in range(plaintext_length//code_length):
        three_bits = peel_lsb_three(plaintext_code)
        plaintext_list.insert(0, three_bits)
        plaintext_code = shift_by_three(plaintext_code)
    
    ciph = apply_cbc(iv,plaintext_list[0])
    print_bin(plaintext_list[0], ciph)
    for plaintext in plaintext_list[1:]:
        ciph = apply_cbc(ciph, plaintext)
        print_bin(plaintext, ciph)

if __name__ == "__main__":
    main()