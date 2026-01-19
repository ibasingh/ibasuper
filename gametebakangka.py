import random

def game_tebak_angka():
    """
    Game tebak angka - pemain menebak angka dari 1 hingga 100
    """
    angka_rahasia = random.randint(1, 100)
    kesempatan = 10
    tebakan = 0
    
    print("=" * 50)
    print("SELAMAT DATANG DI GAME TEBAK ANGKA!")
    print("=" * 50)
    print(f"Saya sudah memilih sebuah angka antara 1 hingga 100")
    print(f"Anda punya {kesempatan} kesempatan untuk menebaknya!")
    print("=" * 50)
    
    while kesempatan > 0:
        try:
            tebakan = int(input(f"\nKesempatan tersisa: {kesempatan} | Masukkan tebakan Anda: "))
            
            # Validasi input
            if tebakan < 1 or tebakan > 100:
                print("❌ Masukkan angka antara 1 hingga 100!")
                continue
            
            kesempatan -= 1
            
            if tebakan == angka_rahasia:
                print("\n" + "=" * 50)
                print(f"🎉 SELAMAT! Anda berhasil menebak angka {angka_rahasia}!")
                print(f"Sisa kesempatan: {kesempatan}")
                print("=" * 50)
                return True
            
            elif tebakan < angka_rahasia:
                print(f"📈 Terlalu KECIL! Angka yang dicari lebih besar dari {tebakan}")
            
            else:
                print(f"📉 Terlalu BESAR! Angka yang dicari lebih kecil dari {tebakan}")
        
        except ValueError:
            print("❌ Input tidak valid! Masukkan angka saja!")
            continue
    
    print("\n" + "=" * 50)
    print(f"😢 GAME OVER! Kesempatan habis.")
    print(f"Angka yang benar adalah: {angka_rahasia}")
    print("=" * 50)
    return False

def main():
    """
    Fungsi utama untuk menjalankan game
    """
    while True:
        hasil = game_tebak_angka()
        
        print("\n")
        lagi = input("Ingin bermain lagi? (ya/tidak): ").lower().strip()
        
        if lagi != 'ya' and lagi != 'y':
            print("Terima kasih telah bermain! Sampai jumpa lagi! 👋")
            break

if __name__ == "__main__":
    main()

