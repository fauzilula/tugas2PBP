Hasil deploy bisa diakses di https://tugas2pbpfauzil.herokuapp.com/katalog/

**Virtual environment**

_Virtual environment_ berguna ketika membutuhkan suatu _dependency_ berbeda dari suatu projek dengan projek lain agar tidak tercampur. Dengan demikian, _virtual environment_ diperlukan karena di dalam _virtual environment_ mempunyai modul yang terisolasi sehingga jika terdapat perbedaan versi yang diperlukan antara setiap projek tidak menimbulkan masalah. 
Meski demikian, kita tetap bisa menjalankan program tanpa _virtual environment._

![image](https://user-images.githubusercontent.com/88032469/190294154-7f56bc35-521e-4ac0-b5e4-fb5f26881a66.png)

Penjelasan Bagan

User melakukan _request_ dalam bentuk URL, request tersebut akan diterima oleh URL kemudian diarahkan ke views untuk memilih view yang sesuai. Kemudian, views tersebut meminta data yang sudah disimpan di model yang kemudian dikembalikan ke views berisi data yang diambil. Setelah itu, views akan mengarahkan ke html untuk memilih template kemudian akan divisualisasikan ke user.

Penjelasan implementasi poin 1-4

Langkan awal yang saya lakukan yaitu dengan melakukan import data yang ada di dalam models.py. Kemudian membuat fungsi show_katalog yang mereturn fungsi render dari data yang diimport serta penambahan context berupa Nama dan NPM, dan juga html untuk menginstruksikan html agar menampilkan data yang sesuai. Setelah langkah tersebut dijalankan, kemudian saya membuat routing dari katalog di urls.py dengan menghubungkan path dengan fungsi yang sudah dibuat di views.py. Langkah berikutnya yaitu, melakukan konfigurasi di katalog.html yang akan dirender dalam views.py yaitu dengan melakukan iterasi data yang ada di katalog kemudian memanggil attribut dari data agar bisa ditampilkan dalam bentuk table. Langkah terakhir yaitu melakukan deploy ke Heroku dengan membuat secret repository yang berisi nama aplikasi dan key dari Heroku di github.
User melakukan request dalam bentuk URL, request tersebut akan diterima oleh URL kemudian diarahkan ke views untuk memilih view yang sesuai. Kemudian, views tersebut meminta data yang sudah disimpan di model yang kemudian dikembalikan ke views berisi data yang diambil. Setelah itu, views akan mengarahkan ke html untuk memilih template kemudian akan divisualisasikan ke user.

