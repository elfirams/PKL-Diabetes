import streamlit as st
import pandas as pd
import numpy as np 
import emoji
import pickle

# Judul dan sidebar
st.title('Gluco Checker 🔍')
st.subheader('Periksa dan Pantau Status Diabetes Anda')

with st.sidebar:
    st.title('Gluco Checker 🔍')
    st.header('Table of Contents')
    st.page_link("https://pkl-diabetes-dyda9xnupeh2utcsxtajcs.streamlit.app/~/+/#3ad77e99", label="Apa itu Diabetes?", icon="🔗")
    st.page_link("https://pkl-diabetes-dyda9xnupeh2utcsxtajcs.streamlit.app/~/+/#tipe-tipe-diabetes", label="Tipe - Tipe Diabetes", icon="🔗")
    st.page_link("https://pkl-diabetes-dyda9xnupeh2utcsxtajcs.streamlit.app/~/+/#7c400abf", label="Jenis - Jenis Tes Diabetes", icon="🔗")
    st.page_link("https://pkl-diabetes-dyda9xnupeh2utcsxtajcs.streamlit.app/~/+/#f07c1f44", label="Seberapa Penting Periksa Diabetes?", icon="🔗")
   
tab1, tab2 = st.tabs(["Tentang Diabetes", "Periksakan Diabetesmu!"])

 # TAB 1
with tab1:
    st.image("diabetes.jpg")

    st.header('🩸 Apa itu Diabetes?')
    st.markdown(
    ''' 
    Dilansir dari *World Health Organization* (WHO), diabetes mellitus adalah penyakit metabolik kronis yang ditandai dengan peningkatan kadar glukosa darah (atau gula darah), yang seiring waktu menyebabkan kerusakan serius pada jantung, pembuluh darah, mata, ginjal, dan saraf.

    Diabetes mellitus merupakan penyakit yang disertai dengan gejala yang dapat dilihat dari beberapa kondisi antara lain seringnya merasa lelah tanpa adanya aktivitas fisik, sering merasa haus padahal sudah minum cukup air, berat badan turun tanpa sebab yang jelas, sering merasa lapar yang ekstrem, sulit sembuhnya luka di tubuh, pandangan kabur, sering buang air kecil, dan sering mengalami infeksi pada kulit, gusi, dan organ intim.
    '''
    )

    st.header('Tipe - Tipe Diabetes')
    col1, col2 = st.columns(2)
 
    with col1:
        st.subheader("🧬 Diabetes Tipe 1")
        with st.container():
            st.image("tipe_1.jpg")
            st.write("Diabetes mellitus tipe 1 terjadi akibat penurunan produksi insulin dan dipercaya faktor genetik dan infeksi virus tertentu menjadi penyebab diabetes mellitus tipe 1.")
 
    with col2:
        st.subheader("🧘🏻‍♀️ Diabetes Tipe 2")
        with st.container():
            st.image("tipe_2.jpg")
            st.write("Umumnya diabetes mellitus tipe 2 disebabkan oleh gaya hidup seperti kurangnya aktivitas fisik, stress, dan konsumsi makanan tinggi gula.")

    st.header('💉 Jenis - Jenis Tes Diabetes')
 
    with st.expander("🔴 Gula Darah Puasa"):
        st.write(
        """
        Kadar gula darah puasa adalah kadar gula dalam darah dimana saat pemeriksaan dilakukan pasien harus puasa atau tidak mendapatkan asupan kalori selama minimal 8 jam. 
        """
        )

    with st.expander("🟡 Gula Darah 2 Jam Setelah Makan"):
        st.write(
        """
        Pemeriksaan gula darah ini bertujuan untuk mendeteksi jumlah dan sensitivitas hormon insulin dalam mengontrol kadar glukosa. Prosedur pemeriksaan gula darah ini ialah setelah cek gula darah puasa, 
        pasien dianjurkan untuk menunggu selama 2 jam kemudian diharuskan mengonsumsi karbohidrat kurang lebih 75 gram. 
        """
        )

    with st.expander("🟢 HbA1C"):
        st.write(
        """
        Pengecekan gula darah (HbA1C) yang bertujuan untuk memantau kadar gula darah dalam tubuh, tes ini juga merupakan tes yang perlu dilakukan apabila pasien mengalami gejala mudah merasa haus padahal sudah minum, 
        peningkatan frekuensi buang air kecil, mudah merasa lelah, dan penglihatan mulai kabur. 
        """
        )

    st.header('🩺 Seberapa Penting Periksa Diabetes?')
    st.markdown(
    ''' 
    Memeriksa diabetes secara rutin sangat penting karena asupan gula yang berlebihan dan kurangnya aktivitas fisik yang sesuai dapat menyebabkan tubuh gagal membakar gula dengan maksimal. Diabetes mellitus juga dapat disebabkan oleh terganggunya respons tubuh terhadap insulin, berkurangnya produksi insulin oleh pankreas, atau kinerja insulin yang terhambat oleh hormon lain. 
    
    Tanpa pemeriksaan rutin, kondisi ini bisa tidak terdeteksi dan mengakibatkan komplikasi serius seperti penyakit jantung, 
    kerusakan saraf, dan masalah penglihatan. Oleh karena itu, pemeriksaan diabetes secara berkala sangat penting untuk menjaga kesehatan dan mencegah komplikasi yang lebih parah.
    '''
    )

# TAB 2
with tab2:
    st.header("🧪 Periksa Diabetes")
    st.markdown(
        '''
    Formulir ini dirancang untuk membantu Anda memantau dan mengelola kesehatan terkait diabetes. Dengan mengisi data yang diperlukan, Anda dapat memperoleh gambaran mengenai risiko diabetes Anda, serta mendapatkan rekomendasi tindakan pencegahan atau penanganan lebih lanjut. 
        '''
    )
    st.image("tab_2.jpg")

# Definisikan kelas convert_data
    class convert_data:
        def __init__(self, df):
            self.df = df

        def usia(self, row):
            usia = row['usia_tahun']
            if usia == '< 45':
                return 1
            else:
                return 2

        def imt(self, row):
            bmi = row['IMT']
            if bmi == '< 18.5':
                return 1
            elif bmi == '> 25.0':
                return 3
            else:
                return 2

        def gender(self, row):
            jk = row['gender']
            if jk == 'P':
                return 1
            else:
                return 2

        def gdp(self, row):
            glupu = row['Glukosa Puasa']
            if glupu >= 126:
                return 1
            else:
                return 2

        def gd2pp(self, row):
            glupp = row['Glukosa 2 Jam PP']
            if glupp >= 200:
                return 1
            else:
                return 2

        def hba1c(self, row):
            a1c = row['HbA1C']
            if a1c >= 6.5:
                return 1
            else:
                return 2

        def transform_columns(self):
            self.df['usia_tahun'] = self.df.apply(self.usia, axis=1)
            self.df['IMT'] = self.df.apply(self.imt, axis=1)
            self.df['gender'] = self.df.apply(self.gender, axis=1)
            self.df['Glukosa Puasa'] = self.df.apply(self.gdp, axis=1)
            self.df['Glukosa 2 Jam PP'] = self.df.apply(self.gd2pp, axis=1)
            self.df['HbA1C'] = self.df.apply(self.hba1c, axis=1)

        def process(self):
            self.transform_columns()
            return self.df

    usia_tahun = st.radio("Inputkan data usia berdasarkan pilihan yang ada", ["Di bawah 45", "45 tahun ke atas"])
    gender = st.radio("Inputkan data jenis kelamin berdasarkan pilihan yang ada", options=["L", "P"])
    imt = st.selectbox("Inputkan data IMT berdasarkan pilihan yang ada",["< 18.5", "18.5 - 25.0", "> 25.0"])
    glukosa_puasa = st.number_input("Glukosa Puasa (mg/dL)", min_value=0)
    glukosa_2jampp = st.number_input("Glukosa 2 Jam PP (mg/dL)", min_value=0)
    hba1c = st.number_input("HbA1C (%)", min_value=0.0, max_value=20.0)

    # Panggil Model
    model = pickle.load(open(r"naive_bayes_model.pkl", "rb"))

    if st.button("Submit"):
    # Mengumpulkan input data ke dalam list
        data_dict = {
            'gender':[gender],
            'usia_tahun':[usia_tahun],
            'IMT':[imt],
            'Glukosa 2 Jam PP':[glukosa_2jampp],
            'Glukosa Puasa':[glukosa_puasa],
            'HbA1C':[hba1c]
        }
    # Membuat DataFrame dari input pengguna
        df = pd.DataFrame(data_dict)
    # Menerapkan kelas convert_data pada DataFrame
        converter = convert_data(df)
        df_transformed = converter.process()
        y_pred = model.predict(df_transformed)

        # Output result
        st.header("Status Diabetes Anda:")
        st.subheader("Diabetes" if y_pred == 'Diabetes' else "Non-Diabetes")
        if y_pred == 'Diabetes':
            st.markdown(
                '''
            Rekomendasi Kegiatan:
            🚫 Kurangi Minuman Manis
            🥗 Ganti Sumber Karbohidrat
            🍛 Perhatikan Porsi Makan
            💊 Minum Obat Sesuai Instruksi Dokter
            🏃🏽 Rutin Olahraga
            🚭 Hindari Merokok
            🩺 Kontrol Gula Darah
            🦵🏻 Selalu Periksa Kondisi Kaki (Luka & Lecet yang tidak biasa)
            
            Dilansir dari *halodoc.com*
                '''
            )
        else:
            st.markdown(
                '''
            Rekomendasi Kegiatan: 
            🏃🏽 Rutin Olahraga
            💧 Rajin Minum Air Putih
            🥗 Menerapkan Pola Makan Sehat
            💪🏼 Menjaga Berat Badan Tetap Ideal
            🩺 Kontrol Gula Darah Berkala
            🚭 Hindari Merokok

            Dilansir dari *siloamhospitals.com*
                '''
            )
        
        st.header("🔰 For Your Information:")
        st.markdown(
            '''
        💠 Jenis kelamin perempuan lebih berisiko terkena Diabetes tipe 2 karena secara fisiologis perempuan berpeluang dalam peningkatan IMT yang lebih besar. 
        
        💠 Umumnya pada usia 45 tahun ke atas terjadi penurunan fungsi pada organ tubuh hingga bahkan kegagalan bagi organ untuk menjalankan fungsinya. 
            '''
        )

        st.header("🪟 Tabel Klasifikasi Diabetes")
        st.image("hba1c.png")
