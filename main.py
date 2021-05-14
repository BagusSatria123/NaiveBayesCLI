from naivebayes import NaiveBayes


class Main:
    @staticmethod
    def main():
        nb = NaiveBayes()
        nb.load_data_training()
        nb.mulai_training()

        # TODO: [LANGKAH-10] Cobalah untuk melakukan prediksi!
        # Apbila cuacanya 'Hujan', suhunya 'Dingin', tingkat kemalasannya 'tinggi', dan 'Bangun siang',
        # mahasiswanya masuk atau bolos?

        hasil_prediksi = nb.prediksi(nilai_cuaca='Hujan',
                    nilai_suhu='Dingin',
                    nilai_tingkat_malas='Tinggi',
                    nilai_bangun_siang='Ya')
        print('=====================================')
        
        print('Hasil akhir prediksi = {}, dengan peluang sebesar {}%'.format(hasil_prediksi['hasil'], (hasil_prediksi['peluang'] * 100)))

Main.main()
