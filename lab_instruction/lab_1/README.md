# Lab 1: Introduction to Django Framework

CSGE602022 - Platform-Based Programming (Pemrograman Berbasis Platform) @
Faculty of Computer Science Universitas Indonesia, Odd Semester 2021/2022

---

## Tujuan Pembelajaran

Setelah menyelesaikan tutorial ini, mahasiswa diharapkan untuk mengerti :

- Mengerti Struktur _Django Project_
- Mengerti bagaimana alur _Django_ menampilkan sebuah _webpage_ (_Django MTV Architecture_)
- Mengerti konfigurasi yang ada pada _settings.py_

---

## Pengenalan

_Django_ merupakan salah satu _framework_ yang menggunakan bahasa pemrograman _python_.
_Framework_ sangat berguna dalam pengembangan web karena sudah menyediakan komponen-komponen
yang dibutuhkan untuk membuat dan menjalankan suatu web, tanpa harus mulai dari nol.
Sebelum memulai pengembangan web menggunakan Django, penting untuk memahami apa itu `virtual environemnt` (virtualenv).
Virtual environment (lingkungan virtual) berfungsi untuk memisahkan pengaturan dan _package_ yang di _install_  
pada setiap _Django project_ sehingga perubahan yang dilakukan pada satu _project_ tidak mempengaruhi _project_ lainnya.
Dengan kata lain, setiap _Django project_ sebaiknya memiliki _virtualenv_ nya sendiri.

> Pastikan saat pembuatan virtualenv, yang digunakan adalah python versi 3 (cek dengan `python --version` )
>
> Sebelum memulai pengembangan web, biasakan untuk selalu mengaktifkan virtualenv terlebih dahulu.

## Struktur _Django Project_

`django-admin` adalah _script_ yang digunakan untuk pembuatan _Django project_. Perintah untuk membuat suatu _project_

`django-admin startproject <NAMA-PROJECT>`

> Ganti `<NAMA-PROJECT>` dengan nama yang kalian inginkan, misalkan Lab-PBP-2021

Struktur project yang dihasilkan,

1. `virtualenv` sebagai sub-dir _project_ <NAMA-PROJECT>

```python
- <NAMA-PROJECT>
    - manage.py
    - <NAMA-PROJECT>
        __init__.py
        settings.py
        urls.py
        wsgi.py
    - <django-apps-1>
        ...
    - <django-apps-2>
        ...
    - virtualenv
        ...
```

2. `virtualenv` satu level dengan _project_ <NAMA-PROJECT>

```python
- virtualenv
    ...
- <NAMA-PROJECT>
    - manage.py
    - <NAMA-PROJECT>
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
    - <django-apps-1>
        ...
    - <django-apps-2>
        ...
```

> Direktori virtualenv bisa berada dalam direktori utama _project_ `<NAMA-PROJECT>` (sebagai sub-direktori)
> atau bisa di luar, satu level dengan direktori utama _project_ `<NAMA-PROJECT>`).
>
> Jangan lupa untuk memasukkan `virtualenv` ke dalam `.gitignore`

Perhatikan bahwa direktori dengan nama `<NAMA-PROJECT>` ada dua buah.  
Direktori yang pertama adalah direktori utama _project_ , sementara direktori yang kedua adalah
direktori konfigurasi atau pengaturan _project_ yang di dalamnya terdapat berkas `settings.py`.

`django-apps-1` dan `django-apps-2` merupakan `apps` milik Django. Contoh yang sudah ada ialah `lab_1`.
Dalam satu _project_ bisa terdapat banyak `apps`. Untuk membuat suatu app, gunakan perintah

`python manage.py startapp <app-name>`

> ganti` <app-name>` menggunakan nama sesuai kebutuhan/keinginan kalian, misalkan `lab_x`.
> sebelum menjalankan perintah ini, pastikan sudah berada satu direktori dengan berkas `manage.py`.
>
> Coba perintah `ls` (linux) atau `dir` (windows)

Struktur umum dari suatu `apps` ialah :

```python
    - <app-name>
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
        - migrations
            ...
        - templates
            ...
```

> Suatu `app` dianggap aktif atau terpakai jika `app` tersebut didaftarkan di pengaturan `INSTALLED_APPS`
> pada berkas `settings.py` (ada pada direktori pengaturan _project_, yang nama direktorinya sama dengan nama _project_ Django)

Secara _default_ , tidak ada berkas `urls.py` karena Django memberikan kebebasan untuk membuat _routing_ sesuai kebutuhan pengembang.
Namun untuk _best practice_ dan kemudahan pengembangan, berkas `urls.py` dibuat manual untuk setiap `app`. Berkas `urls.py` satu level
(satu direktori) dengan berkas `views.py`

Selain itu, untuk menyimpan berkas `HTML` (misalkan `index.html`) biasanya dibuat suatu direktori bernama `templates` di
dalam direktori `<app-name>`, jadi struktur dari suatu `app` nantinya akan menjadi

```python
    - <app-name>
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
        urls.py
        - migrations
            ...
        - templates
            ...
```

> Apa beda `Project` dan `App` ? _Project_ adalah kumpulan konfigurasi dan beberapa app (aplikasi) untuk suatu website tertentu.
> Sedangkan _App_ adalah suatu aplikasi web yang memiliki fungsi/tugas tertentu, misalkan sebagai database atau sebagai aplikasi survei sederhana.
> Satu _project_ dapat memiliki banyak _app_, dan satu _app_ dapat digunakan di banyak _project_.
>
> Tutorial pembuatan Django _project_ : <cite> https://docs.djangoproject.com/en/3.2/intro/tutorial01/ </cite>

Sekilas tentang berkas `settings.py` , pada berkas ini terdapat _section_ `INSTALLED_APPS` yang berfungsi untuk
mendaftarkan aplikasi yang akan dipakai/dijalankan pada suatu _project_.
Contohnya, mendaftarkan `app` bernama "lab_pbp" ke INSTALLED_APPS :

```python
INSTALLED_APPS = [
    ...
    lab_1,
    lab_pbp,
]
```

> jika "sedang" tidak ingin menggunakan suatu `app`, daripada menghapus folder `app` tersebut, kamu bisa
> menon-aktifkan `app` tersebut dengan menghapusnya dari _INSTALLED_APPS_

## Routing pada Django

Routing dapat diumpamakan sebagai suatu pemetaan. URL (Uniform Resource Locator) atau sederhananya adalah suatu alamat web.
`http://localhost:8000` merupakan contoh sederhana dari suatu URL. `http://localhost` adalah alamat utamanya, sedangkan `8000`
adalah _port_ yang digunakan. Django memiliki python _module_ bernama `URLconf` (URL configuration) berisi sekumpulan
pola atau _pattern_ yang Django akan coba cocokkan untuk menemukan `views` (tampilan) yang benar.

> Django menggunakan _regular expression_ atau _regex_ untuk melakukan pencocokan antara URL dengan `views` (tampilan).
> Kalau penasaran bagaiman membuat _regex_ pada Python , coba cek [link](https://docs.python.org/3/howto/regex.html) berikut

Perhatikan struktur _project_ Django, terdapat sub-dir dengan nama sama persis dengan nama project yang dibuat, dengan struktur :

```python
<NAMA-PROJECT>
    __init__.py
    asgi.py
    settings.py
    urls.py
    wsgi.py
```

Secara sederhana, format penulisan utk URL pada Django ialah `url(regex, view, kwargs=None, name=None)`

- regex ialah _pattern_ yang akan dicocokkan
- `view` ialah fungsi yang untuk memproses _request_ dan mengatur tampilan.
- _kwargs_ dan _name_ saat ini bisa diabaikan/dikosongkan

> Untuk mengetahui lebih lanjut format penulisan urls, cek [link] (https://docs.djangoproject.com/en/3.2/_modules/django/conf/urls/#url) berikut

Berkas `urls.py` pada direktori ini adalah contoh URLconf yang disediakan oleh Django, yang dapat digunakan untuk
melakukan `routing` ke `apps` Django lainnya. Contoh untuk membuat `routing` ke `app` lain , berdasarkan `lab_1` yang sudah dikerjakan (cek repo):

```python
...
from django.urls import path
import lab_1.urls as lab_1
urlpattern = [
    ...
    path('lab-1/', include(lab_1)),
    ...
]
```

> Note: Tanda titik tiga `...` pada kode di atas sebagai tanda bahwa isinya bisa apa saja, sesuai kebutuhan.

Perhatikan bahwa berkas `urls.py` pada `app` Django tidak dibuat secara otomatis oleh Django, melainkan dibuat secara manual.
Pada contoh di atas, dalam direkotri `lab_1` diasumsikan ada berkas `urls.py`. Tanda dot (titik) sebagai penanda
untuk mengakses isi direktori tersebut.

Penjelasan ringkas:

- Baris kode `path('lab-1/', include(lab_1))`, yang artinya untuk setiap
  URL dengan awalan `lab-1/` yang menangani URL tersebut adalah berkas `lab_1.urls`.
- alamat `http://localhost/lab-1/` akan ditangani oleh berkas `lab_1.urls`
- `import lab_1.urls as lab_1` --> `lab_1.urls` diganti namanya dengan `lab_1`,
  sehingga baris kode `include(lab_1, ... )` tetap memanggil berkas `lab_1.urls`

> sumber kode : https://gitlab.com/PBP-2021/pbp-lab/blob/master/lab_1/urls.py

Selanjutnya untuk melihat penggunaan `views`, kita harus melihat isi berkas dari `lab_1.urls` :

```python
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
]

```

Penjelasan ringkas :

- Baris kode `path('', index, name='index')`, yang artinya untuk URL dengan awalan / akan dialihkan ke sebuah `views` bernama `index`
- `index` juga dapat diganti dengan `views.index` tapi sama saja, fungsinya untuk memproses tampilan

Pada berkas `views.py` diasumsikan (dan seharusnya) ada fungsi bernama `index` atau `def index(request):`.
Pada berkas `views.py` ini, juga akan diatur bagaimana _request_ akan diproses sebelum ditampilkan.
Perhatikan fungsi `render` yang ada pada berkas `views.py`, terdapat berkas HTML.
Direktori `templates` berfungsi untuk menyimpan berkas HTML yang dipanggil oleh `views`, jadi
pastikan berkas tersebut ada dan namanya sesuai untuk menghindari kesalahan.

> Untuk memastikan hal tersebut, cek penggunaan `views` pada https://gitlab.com/PBP-2021/pbp-lab/blob/master/lab_1/views.py
>
> INGAT: penulisan variabel, parameter, fungs, dsb, pada Django _case-sensitif_. Jadi harus teliti dalam menulisakan kode
>
> Penjelasan ringkas mengenai URL Django : <cite> https://tutorial.djangogirls.org/en/django_urls/ </cite>
>
> Penjelasan lebih detail bagaimana URLconf bekerja : <cite> https://docs.djangoproject.com/en/3.2/topics/http/urls/ </cite>

## Cara Menampilkan _Webpage_

Pada lab ini anda telah disediakan sebuah _template_ `apps` Django. Tugas Anda adalah melengkapi _template_ yang sudah diberikan sesuai dengan yang sudah diajarkan pada sesi kelas berkaitan dengan _MTV Architecture_.

1.  Bukalah folder `lab_1` lalu lengkapi variable `mhs_name`, `birth_date`, dan `npm` dalam `views.py`.

2.  Lengkapi _attributes_ pada model `Friend` yang belum ada, yaitu NPM dan tanggal lahir (DOB).

3.  Daftarkan model `Friend` pada file `admin.py` di dalam folder `lab_1` sehingga nantinya kita bisa menambahkan entri teman menggunakan dashboard admin. Untuk menambahkan entri teman menggunakan dashboard admin dapat mengikuti tutorial berikut [ini](https://docs.djangoproject.com/en/3.2/intro/tutorial02/#introducing-the-django-admin). Jalankan command berikut agar kita dapat memasukkan data ke dashboard admin.

```python
python manage.py makemigrations
python manage.py migrate
```

4.  Jangan lupa untuk memanggil model `Friend` yang sudah dibuat pada file `views.py` di dalam folder `lab_1` serta modifikasi file `friend_list_lab1.html` di dalam folder `lab_1/templates` agar dapat menampilkan daftar teman yang sudah kita masukkan melalui dashboard admin.

5.  Bukalah file `urls.py` di dalam folder `lab_1`. Disini akan ditulis konfigurasi URL yang akan diproses. Dalam hal ini
    kalian harus menambahkan URL untuk menampilkan halaman list teman dengan menggunakan _template_ yang sudah disediakan.
    Modifikasi `urls.py` agar pada saat _request_ diberikan pada `<HOSTNAME>/lab-1/friends` maka halaman yang ada pada
    [friend_list_lab1.html](../../lab_1/templates/friend_list_lab1.html) bisa dimunculkan.

6.  Jalankan Django secara lokal :

    > python manage.py runserver 8000

7.  Selamat, kalian sudah berhasil menampilkan `lab_1`

8.  `commit` dan `push` pekerjaan kalian ke repo masing - masing

## Checklist

1. [ ] Create Your own Gitlab Repo. If you did the previous Tutorial (Initial Setup and Doing the Tutorial), then you're good to go.

2. [ ] Create virtual environment and make sure you can run your Django project (see Tutorial: Running Your Django Project)

3. [ ] Create an admin user (see: https://docs.djangoproject.com/en/1.8/intro/tutorial02/)

4. Display your profile page:

   1. [ ] Implement TODOs on test.py
   2. [ ] Open views.py on lab_1 folder, implement code in lines 4, 6, and 7.
   3. [ ] Refresh http://localhost:8000/
   4. [ ] See your profile on the webpage

5. Create friend list page:
   1. [ ] Implement TODOs on models.py
   2. [ ] Register your model on admin.py so you can access your database from Django Admin later
   3. [ ] Implement TODOs on urls.py
   4. [ ] Fix unit test related to friend list URL on test.py
   5. [ ] Implement TODOs on views.py
   6. [ ] Implement TODOs on templates/friend_list_lab1.html
   7. [ ] Add your friends' information via Django Admin (see: https://docs.djangoproject.com/en/1.8/intro/tutorial02/)
   8. [ ] Access friend list URL and see your friends' information on the page
