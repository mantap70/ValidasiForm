import re

def validate_form(name, phone, email):
    errors = []

    if not name.isalpha():
        errors.append("Nama lengkap harus hanya berisi huruf.")

    if not phone.isdigit():
        errors.append("Nomor telepon harus hanya berisi angka.")

    if "@" not in email or "." not in email:
        errors.append("Email harus mengandung karakter '@' dan '.'.")

    if errors:
        print("Data tidak valid:")
        for error in errors:
            print(f"- {error}")
    else:
        print("Data pendaftaran valid.")

name = input("Masukkan nama lengkap: ")
phone = input("Masukkan nomor telepon: ")
email = input("Masukkan email: ")

validate_form(name, phone, email)
