Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Perbedaan keduanya terletak pada metode dalam pemrograman yang mana sinkronus masih bersifat sekuensial sehingga input perlu di load satu per satu berdasarkan antrian eksekusi program
sedangkan asinkronus proses berjalannya program dapat dilakukan secara bersamaan tanpa harus menunggu proses antrian. 

 Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
 
 Event driven programming adalah sebuah paradigma yang membuat flow dari program bergantung pada event yang dilakukan oleh pengguna. 
 
 seperti saat menekan mouse, scroll, dll yang setiap event yang terjadi dipasangkan dengan sebuah function yang akan jalan dengan otomatis sesuai dengan
 event yang dipasangkan.
 
 Jelaskan penerapan asynchronous programming pada AJAX.
 Browser akan memanggil AJAX javascript untuk mengaktifkan XMLHttpRequest dan mengirimkan HTTP Request ke server.
 
 XMLHttpRequest dibuat untuk proses pertukaran data di server secara asinkron.

Server menerima, memproses, dan mengirimkan data kembali ke browser.

Browser menerima data tersebut dan langsung ditampilkan di halaman website, tanpa perlu reload atau membuat halaman baru.
 
 Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Ajax GET
membuat view baru yaitu show_json untuk menampilkan data dalam bentuk show_json

membuat Url mengarah ke show_json supaya bisa di GET (path('json/', show_json, name="show_json"),) pada url_patterns 

Mengambil data dari /todolist/json/ menggunakan AJAX GET, kemudian membuat card untuk masing-masing data object lalu menambahkan objek tersebut ke dalam container yang 

akan menampilkan seluruh cards.
