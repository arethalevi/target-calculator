#meminta input dari pengguna
harga_target = int(input("Masukkan total harga rumah yang anda inginkan: "))
gaji_bulanan = int(input("Masukkan Gaji bulanan anda: "))
persen_untuk_ditabung = int(input("Berapa persen yang anda sisihkan untuk ditabung? "))
persen_untuk_investasi = int(input("Berapa persen yang anda sisihkan untuk investasi? "))


#kenaikan gaji tahun pertama dan tahun kedua berbeda, sehingga perulangan akan dimulai pada balance setelah dua tahun
gaji_tahun1 = (gaji_bulanan*12)
gaji_tahun2 = gaji_tahun1 + (gaji_tahun1*0.1)
gaji_tabung_2thn = (gaji_tahun1+gaji_tahun2)*(persen_untuk_ditabung/100) #gajitabung2tahun

ir = persen_untuk_investasi/100
gaji_invest_tahun1 = (gaji_tahun1*ir)+((gaji_tahun1*ir)*0.05)
gaji_invest_tahun2 = gaji_invest_tahun1 +(gaji_invest_tahun1*0.05)
gaji_invest_2thn = gaji_invest_tahun1+gaji_invest_tahun2

balance = gaji_tabung_2thn+gaji_invest_2thn #balance selama 2tahun
month = 24 #2tahun

for i in range(1,100):
    gaji_dengan_inflasi = (gaji_tahun2)*((1+0.15)**i)
    gaji_yang_ditabung = gaji_dengan_inflasi*(persen_untuk_ditabung/100) #gaji tabung ditambah inflasi
    gaji_yang_diinvest = (gaji_dengan_inflasi*ir)+((gaji_dengan_inflasi*ir)*0.05) #gaji invest ditambah return
    totali = gaji_yang_ditabung+gaji_yang_diinvest #total pendapatan pertahun
    for j in range(12):
        permonth = totali/12 #total pendapatan perbulan
        balance+=permonth
        month+=1
        if balance< harga_target:
            continue
        else:
            hasil = month
            break
    else:
        continue
    break

print("Jumlah Bulan untuk mencapai jumlah tabungan demi target rumah impian anda:",hasil,"bulan")