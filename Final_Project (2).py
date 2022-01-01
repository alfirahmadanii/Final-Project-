################email_pengirim#########################
email_pengirim = input('masukkan alamat email anda : ')
print(email_pengirim)

#################email_penerima########################
email_penerima1 = input('masukkan email penerima : ')
email_penerima = open("D:/receiver_list.txt", "r")
print(email_penerima.read())

###################Subject#############################
Subject =  input('masukkan subjek : ')
print(Subject)

#######################################################
tulis_pesan = input('tulis pesan anda : ')
print(tulis_pesan)

#######################################################
print("email Terkirim")