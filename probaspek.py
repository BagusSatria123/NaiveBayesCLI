class ProbAspek:

    def __init__(self, nama_aspek: str, nilai_aspek: str):
        pass
    # TODO: [LANGKAH-1] Buat class untuk menampung nilai matriks probabilitas

        self.nama_aspek = nama_aspek
        self.nilai_aspek = nilai_aspek
        self.jml_bolos = 0
        self.jml_masuk = 0
        self.p_aspek_bolos = 0
        self.p_aspek_masuk = 0

    def hitung_p_aspek_bolos(self, jml_total_bolos_aspek):
        self.p_aspek_bolos = self.jml_bolos / jml_total_bolos_aspek
        return self

    def hitung_p_aspek_masuk(self, jml_total_masuk_aspek):
        self.p_aspek_masuk = self.jml_masuk / jml_total_masuk_aspek
        return self

    @staticmethod
    def hitung_jml_total_aspek(pa_list: list) -> dict:
        jumlah = {'bolos': 0, 'masuk': 0}
        for pa in pa_list:
            jumlah['bolos'] += pa.jml_bolos
            jumlah['masuk'] += pa.jml_masuk
        return jumlah

    def print(self):
        print('Aspek    : {}'.format(self.nama_aspek))
        print('Nilai    : {}'.format(self.nilai_aspek))
        print('Jml Bolos: {}'.format(self.jml_bolos))
        print('Jml Masuk: {}'.format(self.jml_masuk))
        print('P({}|Bolos): {}'.format(self.nilai_aspek, self.p_aspek_bolos))
        print('P({}|Masuk): {}'.format(self.nilai_aspek, self.p_aspek_masuk))
        print('------------------------------------------')

    @staticmethod
    def print_matrix_probabilitas(pa_list: list):
        for pa in pa_list:
            pa.print()
