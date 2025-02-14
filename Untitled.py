#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd

st.title("Aplikasi Penentuan Nama Berdasarkan Aplikasi Operasional")

# Unggah file Excel
uploaded_file = st.file_uploader("Upload file Excel", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    # Definisi kata kunci kategori aplikasi operasional
    dessie_keywords = ["UCR", "OSS", "BSB SMG", "MJP", "APNB", "Socmed APNB", "Development Support"]
    dede_keywords = ["Sosmed Foresta", "Sosmed BSB", "Sosmed SMG", "BSD Reguler", "BCA Express", "SnB", "MO", 
                     "Teknis", "UKP", "Tim Bisnis"]
    dede_other_keywords = ["Video Call", "DRO", "SOLA", "Pemol", "VBK", "QA"]

    # Fungsi untuk menetapkan nama berdasarkan kata kunci
    def assign_name(app):
        if pd.isna(app):  # Cek NaN agar tidak error
            return None  
        if any(keyword in app for keyword in dessie_keywords):
            return "dessie"
        elif any(keyword in app for keyword in dede_keywords):
            return "dede"
        elif any(keyword in app for keyword in dede_other_keywords):
            return "dede"
        return None

    # Tambahkan kolom "Nama"
    df["Nama"] = df["Aplikasi Operasional"].apply(assign_name)

    # Tampilkan DataFrame di Streamlit
    st.write("Hasil Data Setelah Penambahan Kolom 'Nama':")
    st.dataframe(df)

    # Download hasil sebagai file Excel baru
    output_file = "data_pengisian_nama.xlsx"
    df.to_excel(output_file, index=False)

    with open(output_file, "rb") as file:
        st.download_button("Download Hasil", file, file_name="data_pengisian_nama.xlsx")


# In[ ]:




