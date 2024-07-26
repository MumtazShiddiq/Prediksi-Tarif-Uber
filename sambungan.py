

import pickle
import streamlit as st
import numpy as np

# Membaca model
customer_model = pickle.load(open('prediksi_uber.sav', 'rb'))

# Judul web
st.title('Prediksi Tarif Uber')

# Input data
Unnamed = st.text_input('Id pelanggan')
Key = st.text_input('Key')
pickup_datetime = st.text_input('Tanggal jemput')
pickup_longitude = st.text_input('Tempat Jemput(Longitude)')
pickup_latitude = st.text_input('Tempat Jemput(Latitude)')
dropoff_longitude = st.text_input('Tempat Turun(Longitude)')
dropoff_latitude = st.text_input('Tempat Turun(Latitude)')
passenger_count = st.text_input('Jumlah Penumpang')

# Mengecek apakah semua input sudah diisi
if Unnamed and Key and pickup_datetime and pickup_longitude and pickup_latitude and dropoff_longitude and dropoff_latitude and passenger_count:
    try:
        # Konversi input menjadi numerik
        inputs = np.array([[float(Unnamed), float(Key), float(pickup_datetime), float(pickup_longitude),
                            float(pickup_latitude), float(dropoff_longitude), float(dropoff_latitude), float(passenger_count)]])
        # Lakukan prediksi
        status_prediksi = customer_model.predict(inputs)
        
        # Tampilkan hasil prediksi
        st.write(f'Hasil Prediksi: {status_prediksi[0]}')
    except ValueError:
        st.error("Pastikan semua input diisi dengan angka yang valid.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")

