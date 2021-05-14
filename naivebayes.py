import pandas as pd
from probaspek import ProbAspek


class NaiveBayes:

    def __init__(self):
        pass

        # TODO: [LANGKAH-2] Buat property untuk menampung data dari file CSV
        self.data_training = None

        # TODO: [Langkah-3] Buat variabel dictionary untuk menampung matriks Probabilitas untuk semua aspek
        self.aspek_cuaca = {'Hujan': None, 'Mendung': None, 'Cerah': None} #Dictionary atau Dict.
        self.aspek_suhu = {'Panas': None, 'Sejuk': None, 'Dingin': None}
        self.aspek_tingkat_malas = {'Tinggi': None, 'Normal': None}
        self.aspek_bangun_siang = {'Tidak': None, 'Ya': None}

        # TODO: [Langkah-4] Buat variabel untuk menampung Prior Probability
        self.prior_probability = {'Bolos': 0, 'Masuk': 0}

    # TODO: [LANGKAH-5] Load data training dari file CSV
    def load_data_training(self):
        self.data_training = pd.read_csv('data_bolos_kuliah.csv', sep=';') # sep --> separator
        print(self.data_training)

    # TODO: [LANGKAH-6] Membuat object ProbAspek untuk semua nilai pada aspek, sekaligus menghitung jumlah masuk dan bolosnya
    def buat_prob_aspek(self, nama_aspek: str, nilai_aspek: str) -> ProbAspek:
        prob_aspek = ProbAspek(nama_aspek, nilai_aspek)
        # Memfulter dari data training yang aspeknya Bolos
        # Kalau pakai SQL seperti ini :
        # SELECT * FROM data_training WHERE cuaca = 'hujan' AND kuliah = 'bolos';
        data_bolos = self.data_training.loc[(self.data_training[nama_aspek] == nilai_aspek) &
                                             (self.data_training['kuliah'] == 'Bolos')]
        # Memfulter dari data training yang aspeknya Masuk
        # Kalau pakai SQL seperti ini :
        # SELECT * FROM data_training WHERE cuaca = 'hujan' AND kuliah = 'masuk';
        data_masuk = self.data_training.loc[(self.data_training[nama_aspek] == nilai_aspek) &
                                             (self.data_training['kuliah'] == 'Masuk')]
        prob_aspek.jml_bolos = len(data_bolos)
        prob_aspek.jml_masuk = len(data_masuk)
        return prob_aspek

    # TODO: [LANGKAH-7] Mengisi semua nilai pada matris probabilitas aspek
    def mulai_training(self):
        # Aspek cuaca
        pc_hujan = self.buat_prob_aspek('cuaca', 'Hujan')
        pc_mendung = self.buat_prob_aspek('cuaca', 'Mendung')
        pc_cerah = self.buat_prob_aspek('cuaca', 'Cerah')
        # Jadikan array
        arr_pc = [pc_hujan, pc_mendung, pc_cerah]
        # Hitung total masing-masing nilai aspek berapa kali muncul di bolos dan masuk
        total_c = ProbAspek.hitung_jml_total_aspek(arr_pc)
        # Hitung probabilitas aspek untuk masing-masing nilai aspek
        pc_hujan.hitung_p_aspek_bolos(total_c['bolos']).hitung_p_aspek_masuk(total_c['masuk'])
        pc_mendung.hitung_p_aspek_bolos(total_c['bolos']).hitung_p_aspek_masuk(total_c['masuk'])
        pc_cerah.hitung_p_aspek_bolos(total_c['bolos']).hitung_p_aspek_masuk(total_c['masuk'])
        # Print matrix probabilitas, tetapi bentuknya vertikal, bukan tabel
        ProbAspek.print_matrix_probabilitas(arr_pc)
        # Simpan ke property class
        self.aspek_cuaca['Hujan'] = pc_hujan
        self.aspek_cuaca['Mendung'] = pc_mendung
        self.aspek_cuaca['Cerah'] = pc_cerah
    #     # TODO: [SOAL-1] Lengkapi fungsi ini untuk semua aspek!
        # Aspek suhu
        ps_panas = self.buat_prob_aspek('suhu', 'Panas')
        ps_dingin = self.buat_prob_aspek('suhu', 'Dingin')
        ps_sejuk = self.buat_prob_aspek('suhu', 'Sejuk')
        # Jadikan array
        arr_ps = [ps_panas, ps_dingin, ps_sejuk]
        # Hitung total masing-masing nilai aspek berapa kali muncul di bolos dan masuk
        total_s = ProbAspek.hitung_jml_total_aspek(arr_ps)
        # Hitung probabilitas aspek untuk masing-masing nilai aspek
        ps_panas.hitung_p_aspek_bolos(total_s['bolos']).hitung_p_aspek_masuk(total_s['masuk'])
        ps_dingin.hitung_p_aspek_bolos(total_s['bolos']).hitung_p_aspek_masuk(total_s['masuk'])
        ps_sejuk.hitung_p_aspek_bolos(total_s['bolos']).hitung_p_aspek_masuk(total_s['masuk'])
        # Print matrix probabilitas, tetapi bentuknya vertikal, bukan tabel
        ProbAspek.print_matrix_probabilitas(arr_ps)
        self.aspek_suhu['Panas'] = ps_panas
        self.aspek_suhu['Dingin'] = ps_dingin
        self.aspek_suhu['Sejuk'] = ps_sejuk

        # Aspek Tingkat Malas
        ptm_tinggi = self.buat_prob_aspek('tingkat_malas', 'Tinggi')
        ptm_normal = self.buat_prob_aspek('tingkat_malas', 'Normal')
        # Jadikan array
        arr_ptm = [ptm_tinggi, ptm_normal]
        # Hitung total masing-masing nilai aspek berapa kali muncul di bolos dan masuk
        total_tm = ProbAspek.hitung_jml_total_aspek(arr_ptm)
        # Hitung probabilitas aspek untuk masing-masing nilai aspek
        ptm_tinggi.hitung_p_aspek_bolos(total_tm['bolos']).hitung_p_aspek_masuk(total_tm['masuk'])
        ptm_normal.hitung_p_aspek_bolos(total_tm['bolos']).hitung_p_aspek_masuk(total_tm['masuk'])
        # Print matrix probabilitas, tetapi bentuknya vertikal, bukan tabel
        ProbAspek.print_matrix_probabilitas(arr_ptm)
        self.aspek_tingkat_malas['Tinggi'] = ptm_tinggi
        self.aspek_tingkat_malas['Normal'] = ptm_normal

        # Aspek Bangun Siang
        pbs_ya = self.buat_prob_aspek('bangun_siang', 'Ya')
        pbs_tidak = self.buat_prob_aspek('bangun_siang', 'Tidak')
        # Jadikan array
        arr_pbs = [pbs_ya, pbs_tidak]
        # Hitung total masing-masing nilai aspek berapa kali muncul di bolos dan masuk
        total_tbs = ProbAspek.hitung_jml_total_aspek(arr_pbs)
        # Hitung probabilitas aspek untuk masing-masing nilai aspek
        pbs_ya.hitung_p_aspek_bolos(total_tbs['bolos']).hitung_p_aspek_masuk(total_tbs['masuk'])
        pbs_tidak.hitung_p_aspek_bolos(total_tbs['bolos']).hitung_p_aspek_masuk(total_tbs['masuk'])
        # Print matrix probabilitas, tetapi bentuknya vertikal, bukan tabel
        ProbAspek.print_matrix_probabilitas(arr_pbs)
        self.aspek_bangun_siang['Ya'] = pbs_ya
        self.aspek_bangun_siang['Tidak'] = pbs_tidak

    # TODO: [LANGKAH-8] Menghitung prior probability
    def hitung_prior_probability(self):
        # self.prior_probability['Bolos'] = 0 #Ini salah
        # self.prior_probability['Masuk'] = 0 #Ini salah
    #     # TODO: [SOAL-2] Prior Probability-nya masih 0, hitunglah prior probability yang sebenarnya!
        pp_bolos = self.buat_prob_aspek('kuliah', 'Bolos')
        pp_masuk = self.buat_prob_aspek('kuliah', 'Masuk')
        arr_pp = (pp_bolos, pp_masuk)
        total_pp = ProbAspek.hitung_jml_total_aspek(arr_pp)
        self.prior_probability['Bolos'] = total_pp['bolos'] / (total_pp['bolos'] + total_pp['masuk'])
        self.prior_probability['Masuk'] = total_pp['masuk'] / (total_pp['bolos'] + total_pp['masuk'])

    # TODO: [LANGKAH-9] Membuat method untuk memprediksi hasil akhir berdasarkan nilai aspek
    def prediksi(self, nilai_cuaca: str, nilai_suhu: str, nilai_tingkat_malas: str, nilai_bangun_siang: str):
        # predict_bolos = p(Bolos) * pc_bolos * ps_bolos * ptm_bolos * pbs_bolos
        self.hitung_prior_probability()
        predict_bolos = self.prior_probability['Bolos'] * \
                        self.aspek_cuaca[nilai_cuaca].p_aspek_bolos * \
                        self.aspek_suhu[nilai_suhu].p_aspek_bolos * \
                        self.aspek_tingkat_malas[nilai_tingkat_malas].p_aspek_bolos * \
                        self.aspek_bangun_siang[nilai_bangun_siang].p_aspek_bolos
        print('Peluang Bolos: {}'.format(predict_bolos))
        # predict_masuk = p(Masuk) * pc_masuk * ps_masuk * ptm_masuk * pbs_masuk
        predict_masuk = self.prior_probability['Masuk'] * \
                        self.aspek_cuaca[nilai_cuaca].p_aspek_masuk * \
                        self.aspek_suhu[nilai_suhu].p_aspek_masuk * \
                        self.aspek_tingkat_malas[nilai_tingkat_malas].p_aspek_masuk * \
                        self.aspek_bangun_siang[nilai_bangun_siang].p_aspek_masuk
        print('Peluang Masuk: {}'.format(predict_masuk))

    #     # TODO: [SOAL-3] hasil prediksi masih '???' dan peluangnya masih 0. Bagaimana agar nilainya benar?
    #     return {'hasil': '???', 'peluang': 0}
        if predict_masuk > predict_bolos:
            hasil = "Masuk"
            peluang = predict_masuk
        else:
            hasil = "Bolos"
            peluang = predict_bolos
        return {'hasil': hasil, 'peluang': peluang}