from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

def ambil_motivasi():
    with open('motivasi.txt', 'r', encoding='utf-8') as file:
        motivasi = file.readlines()
    return random.choice(motivasi).strip()

def simpan_motivasi(motivasi_baru):
    with open('motivasi.txt', 'a', encoding='utf-8') as file:
        file.write(f"\n{motivasi_baru}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/motivasi')
def motivasi_harian():
    motivasi = ambil_motivasi()
    return render_template('motivasi.html', motivasi=motivasi)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah_motivasi():
    if request.method == 'POST':
        motivasi_baru = request.form['motivasi']
        
        # Validasi sederhana
        if motivasi_baru and len(motivasi_baru) > 5:
            simpan_motivasi(motivasi_baru)
            return redirect(url_for('index'))
        else:
            error = "Motivasi terlalu pendek. Minimal 5 karakter."
            return render_template('tambah.html', error=error)
    
    return render_template('tambah.html')

if __name__ == '__main__':
    app.run(debug=True)