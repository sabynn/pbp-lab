# Lab 2: Data Delivery Using HTML, XML, and JSON

CSGE602022 - Platform-Based Programming (Pemrograman Berbasis Platform) @
Faculty of Computer Science Universitas Indonesia, Odd Semester 2021/2022

---

## Tujuan Pembelajaran

Setelah menyelesaikan tutorial ini, mahasiswa diharapkan untuk mengerti:

- Mengerti HTML, XML, dan JSON sebagai salah satu metode _Data Delivery_.
- Mengerti perbedaan JSON dan XML.
- Mengerti perbedaan HTML dengan XML.

---

## HTML (Hyper Text Markup Language)

### Apa Itu HTML?

HTML adalah singkatan dari _Hyper Text Markup Language_.

HTML mendeskripsikan struktur dari sebuah halaman web. HTML berisi beberapa macam elemen yang akan menyampaikan informasi kepada browser bagaimana untuk menampilkan konten.

### Stuktur HTML

Elemen HTML didefiniskan dengan tag pembuka (`start tag`), beberapa konten, dan tag penutup (`end tag`).

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Note</title>
  </head>
  <body>
    <h1>Cukup</h1>
    <p>Cukup Rhoma!!! Cukup!!!</p>
  </body>
</html>
```

Penjelasan singkat:

- `<!DOCTYPE html>` mendefinisikan bahwa dokumen ini adalah dokumen HTML5.
- Elemen `<html>` merupakan `root` elemen dari halaman HTML.
- Elemen `<head>` berisi informasi tentang halaman HTML, seperti `<title>` yang merupakan judul dari halaman HTML tersebut yang akan muncul pada title di browser.
- Elemen `<body>` berisi isi dari dokumen HTML tersebut yang akan tampil di browser, seperti _headings_, paragraf, tabel, gambar, link, dan lainnya.
- Elemen `<h1>` mendefinisikan _heading_ yang besar, semakin kecil angka yang mengikuti `h` tersebut maka semakin besar pula ukurannya.
- Elemen `<p>` mendefinisikan paragraf.

Untuk elemen lainnya dapat dipelajari sendiri di link berikut [ini](https://www.w3schools.com/html/html_elements.asp).

## XML (Extensible Markup Language)

### Apa Itu XML?

XML adalah singkatan dari _eXtensible Markup Language_.

XML didesain menjadi _self-descriptive_, jadi dengan membaca XML tersebut kita bisa mengerti informasi apa yang ingin disampaikan dari data yang tertulis.

XML digunakan dibanyak aplikasi web maupun _mobile_, yaitu untuk menyimpan dan mengirimkan data.

XML hanyalah informasi yang dibungkus di dalam tag. Kita perlu menulis program untuk mengirim, menerima, menyimpan, atau menampilkan informasi tersebut.

### Stuktur Dokumen XML

Berikut ini adalah struktur dokumen XML dari pesan Ani untuk Roma.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<note>
  <to>Rhoma</to>
  <from>Ani</from>
  <title>Cukup</title>
  <message>Cukup Rhoma!!! Cukup!!!</message>
</note>
```

XML di atas sangatlah _self-descriptive_:

- Ada informasi pengirim (`from`)
- Ada informasi penerima (`to`)
- Ada judul pesan (`title`)
- Ada isi pesan (`message`)

Dokumen XML membentuk struktur seperti `tree` yang dimulai dari `root`, lalu `branch`, hingga berakhir pada `leaves`.

Dokumen XML **harus mengandung sebuah _root element_** yang merupakan _parent_ dari element lainnya. Pada contoh di atas `<note>` adalah _root element_.

Untuk baris `<?xml version="1.0" encoding="UTF-8"?>` biasa disebut sebagai **XML Prolog**. XML prolog sifatnya opsional, akan tetapi jika ada maka posisinya harus berada di awal dokumen XML.

Pada dokumen XML **semua elemen wajib memiliki _closing tag_**.

**Tag pada XML sifatnya _case sensitive_**, sehingga tag `<from>` berbeda dengan tag `<From>`.

## JSON (JavaScript Object Notation)

### Apa Itu JSON?

JSON adalah singkatan dari _JavaScript Object Notation_.

JSON didesain menjadi _self-describing_, sehingga JSON sangat mudah untuk dimengerti.

JSON digunakan dibanyak aplikasi web maupun _mobile_, yaitu untuk menyimpan dan mengirimkan data.

Sintaks JSON merupakan turunan dari Object JavaScript. Akan tetapi tetapi format JSON berbentuk text, sehingga kode untuk membaca dan membuat JSON banyak terdapat dibanyak bahasa pemrograman.

### Stuktur JSON

Berikut ini adalah contoh dari JSON untuk objek `note`:

```json
{
  "to": "Rhoma",
  "from": "Ani",
  "title": "Cukup",
  "message": "Cukup Rhoma!!! Cukup!!!"
}
```

Data pada JSON disimpan dalam bentuk `key` dan `value`. Pada contoh di atas yang menjadi `key` adalah `to`, `from`, `title`, dan `message`. `Value` dapat berupa tipe data primitif (`string`, `number`, `boolean`) ataupun berupa objek.

## Tugas

Anda diminta untuk membuat sebuah app baru di dalam project ini bernama `lab_2` yang akan menampilkan `Note` dengan atribut `to`, `from`, `title`, dan `message`. Kemudian data tersebut akan ditampilan dalam tiga buah format:

1. HTML page yang menyajikan sebuah tabel
2. XML document
3. JSON

Kemudian juga ada beberapa pertanyaan singkat yang perlu dijawab dalam file `lab_answer/lab_2.md`, yaitu:

1. Apakah perbedaan antara JSON dan XML?
2. Apakah perbedaan antara HTML dan XML?

## Lab Checklist

1. [ ] Create new app by running `django-admin startapp lab_2` in root directory (`pbp-lab`).

2. [ ] Register `lab-2/` path in `praktikum/urls.py` file, so that you can access the app by accessing [http://localhost:8000/lab-2](http://localhost:8000/lab-2)

3. [ ] Add `lab_2` into `INSTALLED_APPS` in `praktikum/settings.py` file.

4. Create `Note` model:

   1. [ ] Create `Note` model that contains `to`, `from`, `title`, and `message`.
   2. [ ] Register your model on `lab_2/admin.py` so you can access your database from Django Admin. Don't forget to run migration.
   3. [ ] Add `Note` information via Django Admin (see: https://docs.djangoproject.com/en/3.2/intro/tutorial02/).

5. Return `Note` in HTML format:

   1. [ ] Create `index` method in `lab_2/views.py` that render HTML for our response.
   2. [ ] Load `Note` model in `index` method, so that you can show it later.
   3. [ ] Create a template named `lab2.html` in `lab_2/templates` folder that contains a table as a template for out `Note` model. You can use [friend_list_lab1.html](../../lab_1/templates/friend_list_lab1.html) as an example and modify it into `lab2.html` file.
   4. [ ] Create file `lab_2/urls.py` with route `''` for `index` path so that you can access the result by accessing [http://localhost:8000/lab-2](http://localhost:8000/lab-2)

6. Return `Note` in XML format:

   1. [ ] Import `HttpResponse` from `django.http.response` at the beginning of `lab_2/views.py`.
   2. [ ] Import `serializers` from `django.core` below import in step 6.1.
   3. [ ] Create `xml` method in `lab_2/views.py` that render XML for our response.
   4. [ ] Load `Note` model in `xml` method, so you can show it later.
   5. [ ] Serialize data from `Note` model into XML by using this code: `data = serializers.serialize('xml', Note.objects.all())`.
   6. [ ] Return the `xml` method with the following code: `return HttpResponse(data, content_type="application/xml")`.
   7. [ ] Add `/xml` route into `lab_2/urls.py`, so you can access the result by accessing [http://localhost:8000/lab-2/xml](http://localhost:8000/lab-2/xml).

7. Return `Note` in JSON format:

   1. [ ] Create `json` method in `lab_2/views.py` that render JSON for our response.
   2. [ ] Load `Note` model in `json` method, so you can show it later.
   3. [ ] Serialize data from `Note` model into JSON by using this code: `data = serializers.serialize('json', Note.objects.all())`.
   4. [ ] Return the `json` method with the following code: `return HttpResponse(data, content_type="application/json")`.
   5. [ ] Add `/json` route into `lab_2/urls.py`, so you can access the result by accessing [http://localhost:8000/lab-2/json](http://localhost:8000/lab-2/json).

8. [ ] Access all the endpoint that you have built in this lab using Web Browser, cURL, or Postman.

9. [ ] Write the answer from the question above in `lab_answer/lab_2.md` file.

## Referensi

1. [HTML](https://www.w3schools.com/html/default.asp)
2. [XML Tutorial](https://www.w3schools.com/xml/default.asp)
3. [JSON](https://www.w3schools.com/js/js_json_intro.asp)
