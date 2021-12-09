# code by utari

print("WELCOME TO PALINDROM CHECK")

def kata():
    a = str(input("Masukkan kata : "))
    b = a[::-1]
    if a == b:
        print("Kata ini adalah kata Palindrom")
    else:
        print("Kata ini bukan kata Palindrom")

kata()
q = input("Apakah anda ingin melanjutkan? (y/n) : ")

if q == "y":
    while q == "y":
        kata()
        q = input("Apakah anda ingin melanjutkan? (y/n) : ")
    if q == "n":
        print("Thank you!")
else:
    print("Thank you")


# code by utari8