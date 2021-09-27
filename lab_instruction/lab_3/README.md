# Lab 3: Form, Authentication, Session, and Cookie

CSGE602022 - Platform-Based Programming (Pemrograman Berbasis Platform) @
Faculty of Computer Science Universitas Indonesia, Odd Semester 2021/2022

---

## Tujuan Pembelajaran

Setelah menyelesaikan tutorial ini, mahasiswa diharapkan untuk mengerti:

- Memahami cara kerja Form
- Memahami kegunaan Authentication
- Memahami peran dan cara kerja Cookie & Session pada web
- Dapat menggunakan Cookie & Session

---

## Pengenalan

#### HTTP

HTTP merupakan singkatan dari _Hypertext Transfer Protocol_ adalah protokol yang digunakan
untuk berkomunikasi antara _clients_ dan _server_ . HTTP bersifat _stateless_, artinya antar _state_
atau aktifitas yang satu dengan yang lain bersifat independen (tidak terhubung). Setiap transaksi/aktifitas
yang dilakukan dianggap sebagai transaksi/aktifitas yang benar-benar baru, tidak ada data sebelumnya
yang disimpan untuk transkasi/aktifitas saat ini.

Contoh: kegiatan melempar dadu. Lemparan dadu yang pertama, kedua, ketiga dan seterusnya tidak
memiliki hubungan sama sekali. Setiap kegiatan melempar dadu, hasilnya tidak dipengaruhi oleh lemparan
dadu sebelum maupun sesudahnya.

> Noted: _HTTP_ bersifat stateless.

#### Pengetahuan dasar mengenai HTTP

Beberapa konsep atau pengetahuan dasar mengenai HTTP, antara lain :

1. _Client/Server_: Interaksi dilakukan antar client/server.
   Client melakukan request dan server memberikan response
2. _Stateless_: Setiap aktifitas (request/response) bersifat independen
3. _Application Layer_ : Website berjalan pada _application layer_. Proses request/response terjadi
   pada _Transport Layer_ yang umumnya menggunakan protokol TCP, yang menentukan bagaimana data akan dikirim,
   _Application Layer_ tidak peduli apa yang dilakukan _Transport Layer_ (bagaimana data dikirim, diolah, dsb), _App layer_ hanya fokus pada request dan
   response.
4. _Client Actions Method_: Merupakan method yang digunakan oleh client saat melakukan request.
   Contoh: GET, POST, PUT, DELETE, dll.
5. _Server status code_: Merupakan status kode yang diberikan oleh server saat meminta suatu halaman web
   Contoh: 200 (OK), 404 (Page not found), 500 (Internal Server Error), dsb.
6. _Headers_: Merupakan informasi kecil yang dikirim bersamaan dengan request dan response.
   Informasi-informasi tersebut berguna sebagai data tambahan yang digunakan untuk memproses request/response.
   Contoh: Pada Headers terdapat content-type:json. Artinya tipe konten yang diminta/dikirim adalah json.
   Headers juga menyimpan data _cookies_.

#### Latar Belakang Cookies & Session

Semua komunikasi antara klien dan server dilakukan melalui protokol HTTP, dimana HTTP merupakan _stateless protocol_  
yang artinya state yang satu dengan yang lain tidak berhubungan (independen). Hal ini mengharuskan komputer klien yang
menjalankan _browser_ untuk membuat koneksi TCP ke server setiap kali melakukan request.
Tanpa adanya koneksi persisten antara klien dan server, software pada setiap sisi (endpoint) tidak dapat bergantung
hanya pada koneksi TCP untuk melakukan _holding state_ atau _holding session state_.
Apa yang dimaksud dengan _holding state_?

Sebagai contoh, kamu ingin mengakses suatu halaman A pada suatu web yang mensyaratkan pengaksesnya sudah
login ke dalam web.
Kemudian kamu login ke web tersebut dan berhasil membuka halaman A. Saat ingin pindah ke halaman B pada web yang sama,
tanpa adanya suatu proses _holding state_ maka kamu akan diminta untuk login kembali.
Begitu yang akan terjadi setiap kali kamu mengakses halaman yang berbeda padahal masih pada web yang sama.
Proses memberitahu 'siapa' yang sedang login dan menyimpan data ini dikenal sebagai bentuk dialog antara
klien - server dan merupakan dasar session - _a semi-permanent exchange of information_.
Merupakan hal yang sulit untuk membuat HTTP melakukan _holding state_ (karena HTTP merupakan stateless protocol).
Oleh karena itu, dibutuhkan teknik untuk mengatasi masalah tersebut, yaitu Cookie dan Session.

> Catatan: HTTP bersifat stateless. Bagaimana cara untuk membuat web (HTTP) menjadi stateful?

#### Cookies & Session

Salah satu cara yang paling banyak digunakan untuk melakukan _holding state_ adalah dengan menggunakan
session ID yang disimpan sebagai cookie pada komputer klien. Session ID dapat dianggap sebagai suatu token
(barisan karakter) untuk mengenali session yang unik pada aplikasi web tertentu.
Daripada menyimpan semua jenis informasi sebagai cookies pada klien seperti username, nama dan password,
hanya Session ID yang disimpan. Session ID ini kemudian dapat dipetakan ke suatu
struktur data pada sisi web server. Pada struktur data tersebut, kamu dapat menyimpan semua informasi yang kamu butuhkan.
Pendekatan ini jauh lebih aman untuk menyimpan informasi mengenai pengguna, daripada menyimpannya pada cookie.
Dengan cara ini, informasi tidak dapat disalah gunakan oleh klien atau koneksi yang mencurigakan.
Selain itu, pendekatan ini lebih 'tepat' jika data yang akan disimpan ada banyak. Hal itu karena cookie hanya dapat
menyimpan maksimal 4kb data.
Bayangkan kamu sudah login ke suatu web / aplikasi dan mendapat session ID (session identifier).
Untuk dapat melakukan _holding state_ pada HTTP yang _stateless_ , browser biasanya mengirimkan
suatu session ID ke server pada setiap _request_. Dengan begitu, setiap kali datang suatu _request_ ,
maka server akan bereaksi (kurang lebih) "Oh, Orang ini!" . Kemudian server akan mencari informasi _state_ di
memori server atau di _database_ berdasarkan session ID yang didapat, dan mengembalikan data yang diminta.

Perbedaan penting yang perlu diingat, data Cookie disimpan pada sisi klien,
sedangkan data Session biasanya disimpan pada sisi server.
Masih belum paham apa itu _stateless, stateful, cookies dan session_ ?
Coba baca artikel berikut :
[Stateless, Stateful, Coookies and Session](https://sethuramanmurali.wordpress.com/2013/07/07/stateful-stateless-cookie-and-session/)

Selanjutnya mengenai _storage_ atau penyimpanan data,
kalian juga harus memahami perbedaan pada Cookies, Session Storage dan Local Storage. Coba perhatikan gambar dibawah ini,

![alt text](http://tutorial.techaltum.com/images/Local-Storage-Vs-Session-Storage-Vs-Cookies.jpg)

> Berikut beberapa pranala video yang dapat membantu pemahaman terhadap Cookies dan Session:
> [Session_Cookies](https://www.youtube.com/watch?v=64veb6tKTm0&t=10s),
> [Cookies_history](https://www.youtube.com/watch?v=I01XMRo2ESg),
> [Perbedaan Cookies-Session-Local Storage](https://www.youtube.com/watch?v=AwicscsvGLg)

> Catatan : Cookies and Session make web (HTTP) stateful.

#### Informasi tambahan

1. Untuk dapat melihat data Cookies, gunakan browser Chrome tercinta,

   - Tekan tombol F12 atau klik kanan -> Inspect element
   - Pilih tab `APPLICATION`,
   - Kemudian pada sidebar sebelah kiri, pilih menu `Cookies`,
   - Pilih sub-menu yang merupakan web kalian (misalkan localhost:8000 jika mengerjakan di lokal)
   - Nanti akan muncul beberapa data, misalnya `csrftoken` lengkap dengan value, domain, masa kadaluarsa, dsb.

2. Mengapa menyimpan data (misalkan data user yang login) pada cookies tidak aman?
   Apakah menyimpan data dengan session lebih aman? Bagaimana membuktikan hal ini?

   > Framework django memiliki 'key' cookies bernama `sessionid` yang menyimpan token unik setiap kali berhasil login
   > ke suatu web. Misalkan jalankan server pada localhost:8000, buka halaman A dan lakukan login.
   > Kemudian bukalah halaman lain (halaman B) menggunakan mode Incognito (penyamaran), buka web yang sama dan pastikan kamu belum login pada halaman B ini.
   > Salin `sessionid` (key-value) dari halaman A tempat kamu berhasil login,
   > kemudian isi cookie secara manual pada halaman B. Tekan F5. Tadaa! Analisa apa yang terjadi!

   > Catatan: Cookie dicek pada sisi klien, session dicek pada sisi server.
   > Jika suatu Session login sudah dihapus (logout), maka semua login yang menggunakan session yang sama otomatis
   > ikut ter-logout, karena pengecekan pada sisi server. Hal ini tidak berlaku untuk cookie.

## Tugas

Anda diminta untuk membuat sebuah app baru di dalam project ini bernama `lab_3`. Dalam lab ini Anda akan mengimplementasikan pengimputan data pada `Friend` model yang sudah dibuat pada `lab_1` **menggunakan form yang Anda buat sendiri, tidak melalui `django-admin`**. Untuk mengakses form tersebut, **Anda harus login sebagai user terlebih dahulu**.

## Lab Checklist

1. [ ] Create new app by running `django-admin startapp lab_3` in root directory (`pbp-lab`).

2. [ ] Register `lab-3/` path in `praktikum/urls.py` file, so that you can access the app by accessing [http://localhost:8000/lab-3](http://localhost:8000/lab-3)

3. [ ] Add `lab_3` into `INSTALLED_APPS` in `praktikum/settings.py` file.

4. Show page to list created `Friend`:

   1. [ ] Create `index` method in `lab_3/views.py` that render HTML for our response. Implement it just like we implement `friend_list` method in [lab_1/views.py](../../lab_1/views.py).
   2. [ ] Create a template named `lab3_index.html` in `lab_3/templates` folder that contains a table as a template for our `Friend` model. You can use [friend_list_lab1.html](../../lab_1/templates/friend_list_lab1.html) as an example and modify it into `lab3_index.html` file.
   3. [ ] Create file `lab_3/urls.py` with route `''` for `index` path so that you can access the result by accessing [http://localhost:8000/lab-3](http://localhost:8000/lab-3).

5. Create form for creating new `Friend`:

   1. [ ] Create `forms.py` inside `lab_3` folder.
   2. [ ] Create class `FriendForm` inside `lab_3/forms.py` file.
   3. [ ] Implement class `FriendForm`. Assign `model` in class `Meta` with `Friend` model from `lab_1/models.py`.
   4. [ ] Create a template named `lab3_form.html` in `lab_3/templates` folder that contains a form for inserting our new `Friend` object.
   5. [ ] Implement `lab3_form.html` with HTML code so that it will render our form. Use `POST` as `method` and `""` as `action` in `<form>` tag.
   6. [ ] Create `add_friend` method in `lab_3/views.py` that render HTML for our form.
   7. [ ] Implement `add_friend` method so that you can create `Friend` with data from the form. For the example you can read the tutorial [here](https://www.geeksforgeeks.org/django-modelform-create-form-from-models/).
   8. [ ] Check request method in `add_friend`. If the request method is `POST` then we need to redirect to [`/lab-3`](http://localhost:8000/lab-3) after validating form data and save the data if valid.
   9. [ ] Add `add` route into `lab_3/urls.py`, so you can access the result by accessing [http://localhost:8000/lab-3/add](http://localhost:8000/lab-3/add).

6. [ ] Try the application that you have built in step before using Web Browser. Try it before going to next checklist.

7. [ ] Enable form only for authenticated user by adding [decorator](https://docs.djangoproject.com/en/3.2/topics/auth/default/#authentication-in-web-requests) `@login_required` with `/admin/login/` as `login_url` parameter before `index` and `add_friend` method declaration in `lab_3/views.py`.

8. [ ] Try the application that you have built in step before using Web Browser. See if you find any differences.

## Referensi

1. [PPW-2017 Lab 9](https://gitlab.com/PPW-2017/ppw-lab/-/blob/master/lab_instruction/lab_9/README.md)
