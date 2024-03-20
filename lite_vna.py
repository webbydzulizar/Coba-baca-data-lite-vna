# import pyvisa
# import numpy as np
# import time

# def read_data(resource_manager, timeout=10000):
#     # Open connection to Nano VNA
#     try:
#         nano_vna = resource_manager.open_resource("ASRL3::INSTR")
#         nano_vna.timeout = timeout
#     except Exception as e:
#         print("Failed to connect to Nano VNA:", e)
#         return None

#     # Send SCPI command to trigger sweep and wait for it to complete
#     nano_vna.write(":CALC1:PAR1:SEL")  # Select S11 parameter
#     nano_vna.write(":CALC1:FORM SLOG")  # Set the format to log magnitude
#     nano_vna.write(":CALC1:MARK1 ON")   # Turn on marker 1
#     nano_vna.write(":CALC1:MARK1:FUNC:TYPE MAX")  # Set marker 1 to find maximum
#     nano_vna.write(":CALC1:MARK1:FUNC ON")  # Turn on marker 1 function
#     nano_vna.write(":INIT1:CONT ON")  # Set continuous measurement mode
#     time.sleep(1)  # Wait for measurement to stabilize

#     # Read frequency and S11 data
#     nano_vna.write(":CALC1:MARK1:Y?")  # Query S11 marker data
#     response = nano_vna.read()
#     data_str = response.strip().split(',')
#     frequencies = np.array([float(freq) for freq in data_str[::2]])
#     s11_db = np.array([float(val) for val in data_str[1::2]])

#     # Close connection
#     nano_vna.close()

#     return frequencies, s11_db

# def main():
#     rm = pyvisa.ResourceManager()
#     freq, s11 = read_data(rm)
#     if freq is not None and s11 is not None:
#         print("Frequencies:", freq)
#         print("S11 (dB):", s11)
#     else:
#         print("Failed to read data from Nano VNA.")

# if __name__ == "__main__":
#     main()


# import pyvisa
# import numpy as np
# import time

# def baca_data(resource_manager, timeout=10000):
#     # Buka koneksi ke Lite VNA
#     try:
#         lite_vna = resource_manager.open_resource("ASRL3::INSTR")
#         lite_vna.timeout = timeout
#     except Exception as e:
#         print("Gagal terhubung ke Lite VNA:", e)
#         return None

#     # Kirim perintah SCPI untuk mengambil data dan tunggu hingga selesai
#     lite_vna.write(":CALC1:PAR1:SEL")  # Pilih parameter S11
#     lite_vna.write(":CALC1:FORM SLOG")  # Atur format menjadi logaritmik
#     lite_vna.write(":CALC1:MARK1 ON")   # Hidupkan penanda 1
#     lite_vna.write(":CALC1:MARK1:FUNC:TYPE MAX")  # Atur penanda 1 untuk mencari nilai maksimum
#     lite_vna.write(":CALC1:MARK1:FUNC ON")  # Hidupkan fungsi penanda 1
#     lite_vna.write(":INIT1:CONT ON")  # Atur mode pengukuran berkelanjutan
#     time.sleep(1)  # Tunggu hingga pengukuran stabil

#     # Baca data frekuensi dan S11
#     lite_vna.write(":CALC1:MARK1:Y?")  # Kueri data penanda S11
#     respons = lite_vna.read()
#     data_str = respons.strip().split(',')
#     frekuensi = np.array([float(freq) for freq in data_str[::2]])
#     s11_db = np.array([float(val) for val in data_str[1::2]])

#     # Tutup koneksi
#     lite_vna.close()

#     return frekuensi, s11_db

# def utama():
#     rm = pyvisa.ResourceManager()
#     frekuensi, s11 = baca_data(rm)
#     if frekuensi is not None and s11 is not None:
#         print("Frekuensi:", frekuensi)
#         print("S11 (dB):", s11)
#     else:
#         print("Gagal membaca data dari Lite VNA.")

# if __name__ == "__main__":
#     utama()


# import pyvisa

# # Buat objek pengelola sumber daya (resource manager)
# rm = pyvisa.ResourceManager('@py')

# # Tampilkan sumber daya yang tersedia
# print(f"Daftar Sumber Daya yang Tersedia: {rm.list_resources()}")

# try:
#     # Buka sumber daya VNA menggunakan nama sumber daya
#     # Ganti "ASRL9::INSTR" dengan nama sumber daya yang sesuai
#     vna = rm.open_resource("ASRL3::INSTR", timeout=10000)

#     # Kirim permintaan sederhana untuk memeriksa respons komunikasi
#     response = vna.query('*IDN?')

#     # Periksa respons untuk memastikan koneksi berhasil
#     if response is not None and len(response) > 0:
#         print("VNA terhubung dan merespons.")
#     else:
#         print("VNA tidak merespons.")
# except Exception as e:
#     print(f"Kesalahan saat menghubungkan ke VNA: {e}")
# finally:
#     # Tutup sumber daya VNA jika sudah dibuka
#     if vna is not None:
#         vna.close()


# import pyvisa
# rm = pyvisa.ResourceManager('@py')
# rm.list_resources()
# inst = rm.open_resource('ASRL3::INSTR')
# print(inst.query("*IDN?"))

# Impor kelas Vna dari paket rohdeschwarz
# from rohdeschwarz.instruments.vna import Vna

# # Buat instance dari kelas Vna
# vna = Vna()

# # Buka koneksi ke perangkat VNA menggunakan VISA
# visa_address = "COM3"  # Ganti dengan alamat VISA perangkat Anda
# vna.open('VISA', visa_address)

# # Buka file log untuk menyimpan perintah SCPI dan tanggapannya
# log_file_path = 'D:\Coding\Python\Coba baca data lite vna\Hasil\log.txt'  # Ganti dengan jalur yang sesuai
# vna.open_log(log_file_path)

# # Lakukan operasi (kirim perintah SCPI) di sini...
# print(inst.query("*IDN?"))

# # Tutup file log
# vna.close_log()

# # Tutup koneksi ke perangkat VNA
# vna.close()

import serial
import time

def read_from_nanovna(ser):
    # Kirim perintah untuk memulai pengukuran
    ser.write(b's21\n')  # Misalnya, untuk membaca S11

    # Tunggu sebentar agar NanoVNA merespons
    time.sleep(1)

    # Baca data yang dikirimkan oleh NanoVNA
    data = ser.readline().decode().strip()
    return data

def main():
    # Konfigurasi port serial
    serial_port = 'COM3'  # Ganti dengan port serial yang sesuai
    baud_rate = 115200  # Sesuaikan dengan baud rate NanoVNA

    # Buat objek serial
    ser = serial.Serial(serial_port, baud_rate, timeout=1)

    try:
        while True:
            # Baca data dari NanoVNA
            measurement_data = read_from_nanovna(ser)
            print("Measurement Data:", measurement_data)

            # Tunggu beberapa detik sebelum membaca data lagi
            time.sleep(2)
    except KeyboardInterrupt:
        print("Program terminated by user.")
    finally:
        # Tutup koneksi serial
        ser.close()

if __name__ == "__main__":
    main()
