# mengimpor Flask
from flask import Flask, render_template, request, jsonify

# mengimpor ChatBot dari chatterbot
from chatterbot import ChatBot

# mengimpor trainer
from chatterbot.trainers import ListTrainer

# membuat aplikasi flask
app = Flask(__name__)

# membuat chatbot
chatbot = ChatBot('MyChatBot')

# membuat trainer
trainer = ListTrainer(chatbot)

# melatih chatbot
trainer.train([

    'Hai',
    'Halo!',

    'Apa kabar?',
    'Saya baik, terima kasih!',

    'Siapa nama kamu?',
    'Saya Tasia, asisten dari Auto Marsa.',

    'informasi sekolah',
    'Auto Marsa adalah sekolah berbasis teknologi dan kreativitas digital.',

    'daftar jurusan',
    'Jurusan yang tersedia adalah TKR, TSM, AKL, PPLG dan KULINER.',

    'Sampai jumpa!',
    'Sampai jumpa juga!',

    'keluar',
    'Terima kasih sudah menghubungi Auto Marsa.'
])

# halaman utama
@app.route('/')
def home():
    return render_template('index.html')

# route chatbot
@app.route('/get_response', methods=['POST'])
def get_bot_response():

    # mengambil pesan dari user
    user_message = request.json['message'].lower()

    # pilihan informasi sekolah
    if user_message == '1' or user_message == 'informasi sekolah':

        response = '''
Auto Marsa adalah sekolah berbasis teknologi dan kreativitas digital.
'''

    # pilihan daftar jurusan
    elif user_message == '2' or user_message == 'daftar jurusan':

        response = '''
<b>Jurusan yang tersedia:</b>
<br><br>
1. TKR (Teknik Kendaraan Ringan)<br>
2. TSM (Teknik Sepeda Motor)<br>
3. AKL (Akuntansi dan Keuangan Lembaga)<br>
4. PPLG (Pengembangan Perangkat Lunak dan Gim)<br>
5. Kuliner
'''

    # pilihan informasi pendaftaran
    elif user_message == '3' or user_message == 'informasi pendaftaran':

        response = """
Pendaftaran dapat dilakukan secara online maupun langsung ke sekolah.

<br><br><b>Online:</b><br>
<a href="https://www.marsa9.com/berita/resmi-dibuka-ayo-bergabung-di-spmb-smk-ma-arif-9-kebumen-2026" target="_blank">
Klik untuk daftar online
</a>

<br><br><b>Offline:</b><br>
Ruang TU SMK Ma'arif 9 Kebumen<br>
Jl. Raya, Klirong, Klegenwonosari,<br>
Kec. Klirong, Kabupaten Kebumen,<br>
Jawa Tengah 54381
"""

    else:

        # daftar input yang dikenali chatbot
        known_inputs = [
            'hai',
            'halo!',
            'apa kabar?',
            'siapa nama kamu?',
            'sampai jumpa!',
            'keluar'
        ]

        # jika input dikenal
        if user_message in known_inputs:
            response = str(chatbot.get_response(user_message))

        # jika tidak dikenal
        else:
            response = "Pesan tidak dimengerti."

    # mengirim respon ke web
    return jsonify({'response': response})

# menjalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)