# app.py
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import random

app = Flask(__name__)

# Inisialisasi Database
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS motivasi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            teks TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            likes INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

# Halaman Utama
@app.route('/')
def index():
    return render_template('index.html')

# Dapatkan Motivasi Harian
@app.route('/motivasi')
def motivasi_harian():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    # Ambil motivasi acak
    c.execute('SELECT teks FROM motivasi ORDER BY RANDOM() LIMIT 1')
    result = c.fetchone()
    
    conn.close()
    
    if result:
        motivasi = result[0]
    else:
        motivasi = "Tidak ada motivasi tersedia. Silakan tambahkan motivasi baru!"
    
    return render_template('motivasi.html', motivasi=motivasi)

# Tambah Motivasi Baru
@app.route('/tambah', methods=['GET', 'POST'])
def tambah_motivasi():
    if request.method == 'POST':
        motivasi = request.form['motivasi'].strip()
        
        if not motivasi:
            return render_template('tambah.html', error='Motivasi tidak boleh kosong!')
        
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('INSERT INTO motivasi (teks) VALUES (?)', (motivasi,))
        conn.commit()
        conn.close()
        
        return redirect(url_for('motivasi_harian'))
    
    return render_template('tambah.html')

# Daftar Semua Motivasi
@app.route('/daftar')
def daftar_motivasi():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT id, teks, likes FROM motivasi ORDER BY created_at DESC')
    motivasi_list = c.fetchall()
    conn.close()
    
    return render_template('daftar_motivasi.html', motivasi_list=motivasi_list)

# Like Motivasi
@app.route('/like/<int:motivasi_id>')
def like_motivasi(motivasi_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('UPDATE motivasi SET likes = likes + 1 WHERE id = ?', (motivasi_id,))
    conn.commit()
    conn.close()
    
    return redirect(url_for('daftar_motivasi'))

# Hapus Motivasi
@app.route('/hapus/<int:motivasi_id>')
def hapus_motivasi(motivasi_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('DELETE FROM motivasi WHERE id = ?', (motivasi_id,))
    conn.commit()
    conn.close()
    
    return redirect(url_for('daftar_motivasi'))

# Edit Motivasi
@app.route('/edit/<int:motivasi_id>', methods=['GET', 'POST'])
def edit_motivasi(motivasi_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    if request.method == 'POST':
        motivasi_baru = request.form['motivasi'].strip()
        
        if not motivasi_baru:
            conn.close()
            return render_template('edit_motivasi.html', 
                                   motivasi_id=motivasi_id, 
                                   error='Motivasi tidak boleh kosong!')
        
        c.execute('UPDATE motivasi SET teks = ? WHERE id = ?', (motivasi_baru, motivasi_id))
        conn.commit()
        conn.close()
        
        return redirect(url_for('daftar_motivasi'))
    
    # Ambil motivasi yang akan diedit
    c.execute('SELECT teks FROM motivasi WHERE id = ?', (motivasi_id,))
    motivasi = c.fetchone()
    conn.close()
    
    if not motivasi:
        return redirect(url_for('daftar_motivasi'))
    
    return render_template('edit_motivasi.html', 
                           motivasi_id=motivasi_id, 
                           motivasi=motivasi[0])

if __name__ == '__main__':
    init_db()
    app.run(debug=True)