def galat_absolut(hasil, acuan):
    
    return abs(hasil - acuan)

def galat_relatif(hasil, acuan):
    
    if acuan == 0:
        raise ValueError("Nilai acuan tidak boleh nol (0).")
    
    
    absolut = galat_absolut(hasil, acuan)
    return (absolut / acuan) * 100



if __name__ == "__main__":
   
    rata_rata_program = 13.58 
    nilai_acuan = 13.5714
    toleransi = 0.5 

    g_absolut = galat_absolut(rata_rata_program, nilai_acuan)
    g_relatif = galat_relatif(rata_rata_program, nilai_acuan)

   
    if g_relatif <= toleransi:
        status = "LULUS"
    else:
        status = "TIDAK LULUS"

    print(f"Galat absolut: {g_absolut:.4f}")
    print(f"Galat relatif (%): {g_relatif:.4f}%")
    print(f"Status: {status}")