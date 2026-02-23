
while True:
    print("Silahkan Login")
    username = input("Masukan username : ")
    password = input("Masukan password : ")

    if username == "admin" and password == "admin123":
        print("Login Berhasil")
        break
    else:
        print("Username atau Password Salah, Silahkan Coba Lagi")

    