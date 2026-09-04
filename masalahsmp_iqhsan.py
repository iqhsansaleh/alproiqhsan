def hitung_rasio_uang():
    print("=== PROGRAM HITUNG RASIO UANG SAKU ===")
    try:
        rasio_ani = int(input("Masukkan rasio bagian pertama (Ani): "))
        rasio_budi = int(input("Masukkan rasio bagian kedua (Budi): "))
        total_uang = float(input("Masukkan total uang (Rp): "))
        
        total_rasio = rasio_ani + rasio_budi
        
        uang_ani = (rasio_ani / total_rasio) * total_uang
        uang_budi = (rasio_budi / total_rasio) * total_uang
        
        print("\n--- HASIL PERHITUNGAN ---")
        print(f"Total Uang      : Rp {total_uang:,.0f}")
        print(f"Uang Ani ({rasio_ani})   : Rp {uang_ani:,.0f}")
        print(f"Uang Budi ({rasio_budi})   : Rp {uang_budi:,.0f}")
        
    except ValueError:
        print("Kesalahan: Mohon masukkan angka yang valid.")

if __name__ == "__main__":
    hitung_rasio_uang()