while True:
  nama = input("masukkan nama: ")
  nim = input("masukkan nim: ")

  print ("Mahasiswa bernama",nama,"dengan nim",nim)

  ulangi = input("Apakah anda ingin melanjutkan? Ya/tidak?")

  if ulangi == "ya":
    continue
  elif ulangi == "tidak":
    print("terimakasih")
    break
  else:
      print("maaf, inputan yang kamu masukkan tidak sesuai!")
      ulangi = input("Apakah anda ingin melanjutkan? y/t?")
  if ulangi == "ya":
    continue
  elif ulangi == "tidak":
    print("terimakasih")
    break