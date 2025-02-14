{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c61e2476",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-02-14 15:25:34.602 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-14 15:25:36.488 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\lenovo\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-02-14 15:25:36.488 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-14 15:25:36.488 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-14 15:25:36.499 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-14 15:25:36.501 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-14 15:25:36.504 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-14 15:25:36.506 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "\n",
    "st.title(\"Aplikasi Penentuan Nama Berdasarkan Aplikasi Operasional\")\n",
    "\n",
    "# Unggah file Excel\n",
    "uploaded_file = st.file_uploader(\"Upload file Excel\", type=[\"xlsx\"])\n",
    "\n",
    "if uploaded_file is not None:\n",
    "    df = pd.read_excel(uploaded_file)\n",
    "\n",
    "    # Definisi kata kunci kategori aplikasi operasional\n",
    "    dessie_keywords = [\"UCR\", \"OSS\", \"BSB SMG\", \"MJP\", \"APNB\", \"Socmed APNB\", \"Development Support\"]\n",
    "    dede_keywords = [\"Sosmed Foresta\", \"Sosmed BSB\", \"Sosmed SMG\", \"BSD Reguler\", \"BCA Express\", \"SnB\", \"MO\", \n",
    "                     \"Teknis\", \"UKP\", \"Tim Bisnis\"]\n",
    "    dede_other_keywords = [\"Video Call\", \"DRO\", \"SOLA\", \"Pemol\", \"VBK\", \"QA\"]\n",
    "\n",
    "    # Fungsi untuk menetapkan nama berdasarkan kata kunci\n",
    "    def assign_name(app):\n",
    "        if pd.isna(app):  # Cek NaN agar tidak error\n",
    "            return None  \n",
    "        if any(keyword in app for keyword in dessie_keywords):\n",
    "            return \"dessie\"\n",
    "        elif any(keyword in app for keyword in dede_keywords):\n",
    "            return \"dede\"\n",
    "        elif any(keyword in app for keyword in dede_other_keywords):\n",
    "            return \"dede\"\n",
    "        return None\n",
    "\n",
    "    # Tambahkan kolom \"Nama\"\n",
    "    df[\"Nama\"] = df[\"Aplikasi Operasional\"].apply(assign_name)\n",
    "\n",
    "    # Tampilkan DataFrame di Streamlit\n",
    "    st.write(\"Hasil Data Setelah Penambahan Kolom 'Nama':\")\n",
    "    st.dataframe(df)\n",
    "\n",
    "    # Download hasil sebagai file Excel baru\n",
    "    output_file = \"data_pengisian_nama.xlsx\"\n",
    "    df.to_excel(output_file, index=False)\n",
    "\n",
    "    with open(output_file, \"rb\") as file:\n",
    "        st.download_button(\"Download Hasil\", file, file_name=\"data_pengisian_nama.xlsx\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1b79bbda",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.19"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
