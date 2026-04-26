from flask import Flask, render_template, request

app = Flask(__name__)

portfolio_data = {
    "nama": 'Panji Pramudia Bagaskoro',
    "nim": '24225026',
    "kelas": 'Informatics Student',
    "level": '04 (semester)',
    "about": 'Halo! Saya adalah mahasiswa Teknik Informatika dari Tegal. Saya sangat tertarik dengan persimpangan antara teknologi dan pertanian (Agritech). Impian saya adalah mengembangkan sistem Smart Farming menggunakan Computer Vision untuk membantu petani mengklasifikasi kualitas panen secara otomatis. Saya percaya bahwa teknologi dapat menjadi alat yang kuat untuk meningkatkan efisiensi dan keberlanjutan dalam pertanian. Selain itu, saya juga memiliki minat dalam pengembangan aplikasi mobile dan web, serta eksplorasi teknologi baru seperti AI dan IoT. Saya selalu bersemangat untuk belajar dan berkolaborasi dengan orang-orang yang memiliki visi serupa untuk menciptakan solusi inovatif di bidang teknologi.',
    "skills": [
        {
            "nama": "Python",
            "nilai": 65,
            "warna": "is-primary"
        },
        {
            "nama": "HTML/CSS",
            "nilai": 75,
            "warna": "is-success"
        },
        {
            "nama": "Flask",
            "nilai": 65,
            "warna": "is-info"
        },
        {
            "nama": "React",
            "nilai": 45,
            "warna": "is-danger"
        }
    ],
    "quests":[
        {"nama": "Smart To-Do List (Java Swing)", "link": "https://github.com/Jipan-maker", "btn": "is-primary", "teks_btn": "View on GitHub"},
        {"nama": "EcoEarth (Python Flask)", "link": "https://github.com/Jipan-maker", "btn": "is-success", "teks_btn": "View on GitHub"}
    ]
}

@app.route('/')
def home():
    return render_template('index.html', data=portfolio_data)

@app.route('/about')
def about():
    return render_template('about.html', data=portfolio_data)

@app.route('/projects')
def projects():
    return render_template('projects.html', data=portfolio_data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    notif = None
    if request.method == 'POST':
        pengirim = request.form.get('nama_pengirim')
        pesan = request.form.get('pesan_pengirim')

        print(f"PESAN MASUK DARI {pengirim}: {pesan}")
        notif = "Pesan berhasil dikirim! Terima kasih atas pesan Anda."

    return render_template('contact.html', notifikasi=notif)

if __name__ == '__main__':
    app.run(debug=True)