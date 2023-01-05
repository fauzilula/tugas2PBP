link deploy
https://tugas2pbpfauzil.herokuapp.com/todolist

Apa kegunaan {% csrf_token %} pada elemen form? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?
  
{% csrf_token %} diperlukan untuk menghindari Cross Site Request Forgery (CSRF) attack yang membuat penyerang dapat mengirimkan permintaan palsu (request forgery) pada aplikasi website yang sedang diakses. Efek apa bila tidak ada potongan kode tersebut maka siapapun bisa mengubah data termasuk data sensitif seperti email password dll sehingga sangat diperlukan.

Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat form secara manual.

  Kita bisa membuat elemen form secara manual tanpa generator {{ form.as_table }} dan keuntungannya kita lebih bebas mengubah style dengan css, bootstrap dll pada form tersebut. Cara membuatnya yaitu pertama membuat html lalu pada section html membuat setiap field beserta label secara manual dan button agar bisa memproses data yang dimasukkan. Referensi: https://www.geeksforgeeks.org/render-django-form-fields-manually/

Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
 
  pengguna melakukan submisi dengan menekan button yang sudah dihubungkan dengan suatu function pada views.py kemudian views.py akan memproses data dengan semua logika
  dan fungsi yang telah dibuat.Kemudian data yang diberikan user tersimpan diambil dan ditampilkan pada html.
  
  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!
  
 langkah pertama yaitu buat app todolist dengan menggunakan python manage.py startapp todolist, kemudian tambahkan path todolist di settings.py dan di urls.py (urlpattern) 
  kemudian membuat model yang berupa class berisi field sesuai permintaan kemudian membuat berbagai fungsi di views.py seperti login register addtask dll yang mana fungsi show_todolist dan addtodo direstriksi agar bisa diakses hanya ketika user melakukan login terlebih dahulu
  Setelah itu, membuat beberapa html sesuai yang ada di views.py agar bisa dirender di views.py. Lalu menambahkan routing agar fungsi bisa terhubung dengan fungsi yang telah dibuat seperti register login todolist dll. Terakhir, melakukan deploy ke github dan heroku dan membuat 2 akun pengguna serta 3 dummy data dengan rincian sebagai berikut:
  
username: fauzil2
  
password: tes12345
  
username: fauzil1
  
password: tes12345
  
