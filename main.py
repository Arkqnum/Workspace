def brainfuck_encrypt(message, key):
    encrypted = []
    for i, char in enumerate(message):
        # A chave é repetida para cada caractere da mensagem
        key_char = key[i % len(key)]
        # A operação de criptografia: soma o valor ASCII do caractere da mensagem com o da chave
        encrypted_char = chr((ord(char) + ord(key_char)) % 256)
        encrypted.append(encrypted_char)
    return ''.join(encrypted)

def brainfuck_decrypt(encrypted_message, key):
    decrypted = []
    for i, char in enumerate(encrypted_message):
        # A chave é repetida para cada caractere da mensagem
        key_char = key[i % len(key)]
        # A operação de descriptografia: subtrai o valor ASCII da chave do caractere criptografado
        decrypted_char = chr((ord(char) - ord(key_char)) % 256)
        decrypted.append(decrypted_char)
    return ''.join(decrypted)

# Exemplo de uso
if __name__ == "__main__":
    original_message = "Hello, World!"
    key = "secret"

    encrypted_message = brainfuck_encrypt(original_message, key)
    print("Mensagem Criptografada:", encrypted_message)

    decrypted_message = brainfuck_decrypt(encrypted_message, key)
    print("Mensagem Descriptografada:", decrypted_message)