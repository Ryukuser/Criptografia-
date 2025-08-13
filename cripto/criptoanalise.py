#Esse programa para faz a criptoanálise e decifra um texto cifrado usando análise de frequências 
# Frequências esperadas (português brasileiro):

#freq_portuguese = { 'A': 14.634, 'B': 1.043, 'C': 3.882, 'D': 4.992, 'E': 12.494, 'F': 1.023, 'G': 1.302, 'H': 1.279, 'I': 6.186, 'J': 0.397, 'K': 0.024, 'L': 2.777, 'M': 2.474, 'N': 4.439, 'O': 9.744, 'P': 2.523, 'Q': 0.204, 'R': 6.532, 'S': 7.755, 'T': 4.717, 'U': 4.035, 'V': 1.666, 'W': 0.037, 'X': 0.215, 'Y': 0.039, 'Z': 0.744 }(em Português BR ou Inglês).



# (texto exemplo ) SquiqhsyfxuhCujxetydmxysxuqsxbujjuhydjxufbqydjunjyihufbqsutroqbujjuhiecuvynutdkcruh evfeiyjyeditemdjxuqbfxqrujJxucujxetyidqcutqvjuhZkbykiSquiqhmxekiutyjydxyifhylqjusehhu ifedtudsu

def cesar_decipher(key, text):
    result = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in text:
        if char.isupper() and char in alphabet:
            index = alphabet.index(char)
            new_index = (index - key) % 26
            result += alphabet[new_index]
        else:
            result += char
    return result

def calculate_frequency(text):
    freq = {}
    total_letters = 0
    for char in text:
        if char.isupper() and char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            freq[char] = freq.get(char, 0) + 1
            total_letters += 1
    return {char: (count / total_letters * 100) if total_letters > 0 else 0 for char, count in freq.items()}

def frequency_analysis(ciphertext):
    freq_portuguese = {
    'A': 14.634, 'B': 1.043, 'C': 3.882, 'D': 4.992, 'E': 12.494, 'F': 1.023,
    'G': 1.302, 'H': 1.279, 'I': 6.186, 'J': 0.397, 'K': 0.024, 'L': 2.777,
    'M': 2.474, 'N': 4.439, 'O': 9.744, 'P': 2.523, 'Q': 0.204, 'R': 6.532,
    'S': 7.755, 'T': 4.717, 'U': 4.035, 'V': 1.666, 'W': 0.037, 'X': 0.215,
    'Y': 0.039, 'Z': 0.744
}
    best_key = 0
    best_score = float('inf')
    best_text = ""

    for key in range(26):
        decrypted = cesar_decipher(key, ciphertext)
        freq = calculate_frequency(decrypted)
        score = sum((freq.get(char, 0) - freq_portuguese[char]) ** 2 for char in freq_portuguese)
        if score < best_score:
            best_score = score
            best_key = key
            best_text = decrypted
    return best_key, best_text

def main():
    ciphertext = input("Digite o texto cifrado: ")
    key, decrypted = frequency_analysis(ciphertext)
    print(f"Chave estimada: {key}")
    print(f"Texto decifrado: {decrypted}")

if __name__ == "__main__":
    main()