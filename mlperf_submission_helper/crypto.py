from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

def encrypt_file(public_key, src_file, dest_file):
    try:
        data = None
        with open(src_file) as f:
            data = f.read()
    except Exception as e:
        print("Unable to read source file.")
        raise e

    try:
        rsa_key = RSA.import_key(open(public_key).read())
        session_key = get_random_bytes(16)
        # Encrypt the session key with the public RSA key
        cipher_rsa = PKCS1_OAEP.new(rsa_key)
        enc_session_key = cipher_rsa.encrypt(session_key)
        # Encrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)
    except Exception as e:
        print("Unable to encrypt file.")
        raise e

    try:
        with open(dest_file, "wb") as f:
            for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext):
                f.write(x)
    except Exception as e:
        print("Unable to write output file.")
        raise e


def decrypt_file(private_key, src_file, dest_file):
    try:
        with open(src_file, "rb") as f:
            rsa_key = RSA.import_key(open(private_key).read())
            enc_session_key = f.read(rsa_key.size_in_bytes())
            nonce = f.read(16)
            tag = f.read(16)
            ciphertext = f.read(-1)
    except Exception as e:
        print("Unable to read source file.")
        raise e

    try:
        # Decrypt the session key with the private RSA key
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)
        # Decrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
        data = data.decode("utf-8")
    except Exception as e:
        print("Unable to decrypt file.")
        raise e

    try:
        with open(dest_file, "w") as f:
            f.write(data)
    except Exception as e:
        print("Unable to write output file.")
        raise e


def encrypt_submission(public_key, src_dir, dest_dir):
    raise NotImplementedError

def decrypt_submission(private_key, src_dir, dest_dir):
    raise NotImplementedError
