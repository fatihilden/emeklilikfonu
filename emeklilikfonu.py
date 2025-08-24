import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
yillik_getiri_ortalama = 0.08
yillik_getiri_std = 0.15
simulasyon_sayisi = 5000

aylik_yatirim = st.number_input("Her ay yatıracağınız tutarı giriniz (TL) : ", min_value=0)
yil_sayisi = st.number_input("Kaç yıl yatırım yapacaksınız?: ", min_value=1)

ay_sayisi = yil_sayisi * 12
sonuclar = []
for s in range(simulasyon_sayisi):
    toplam = 0
    yillik_getiriler = np.random.normal(yillik_getiri_ortalama, yillik_getiri_std, yil_sayisi)
    for yil in range (yil_sayisi):
        aylik_getiri = (1 + yillik_getiriler[yil])**(1/12) - 1
        for ay in range(12):
            toplam = toplam * (1 + aylik_getiri) + aylik_yatirim
            
    sonuclar.append(toplam)
sonuclar = np.array(sonuclar)

st.write(f"Ortalama varlık: {sonuclar.mean():.0f} TL")
st.write(f"En düşük birikim: {np.percentile(sonuclar, 5):.0f} TL")
st.write(f"En yüksek birikim: {np.percentile(sonuclar, 95):.0f} TL")

plt.figure(figsize=(10,6))
plt.hist(sonuclar, bins=30, color="seagreen", edgecolor="black")
plt.title("Emeklilik Fonunun Monte Carlo Simülasyon Sonuçları")
plt.xlabel("Toplam Varlık(TL)")
plt.ylabel("Simülasyon tekrarı")

plt.axvline(sonuclar.mean(), color="red", linestyle="dashed", linewidth=2, label=f"ortalama: {sonuclar.mean():.0f} TL")
plt.axvline(np.percentile(sonuclar, 5), color="orange", linestyle="dashed", linewidth=2, label=f"En düşük birikim: {np.percentile(sonuclar, 5):.0f} TL")
plt.axvline(np.percentile(sonuclar, 95), color="green", linestyle="dashed", linewidth=2, label=f"En yüksek birikim: {np.percentile(sonuclar, 95):.0f} TL")

st.caption("Bu simulasyon olasılıklara dayalıdır, kesin yatırım tavsiyesi değildir.")
plt.legend()

st.pyplot(plt)