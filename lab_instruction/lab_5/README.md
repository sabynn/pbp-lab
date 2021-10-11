# Lab 5: JavaScript and AJAX

CSGE602022 - Platform-Based Programming (Pemrograman Berbasis Platform) @
Faculty of Computer Science Universitas Indonesia, Odd Semester 2021/2022

---

## Tujuan Pembelajaran

Setelah menyelesaikan tutorial ini, mahasiswa diharapkan untuk mengerti :

- Pengenalan fungsi JavaScript pada front-end development
- Penggunaan dasar JavaScript
- Penggunaan AJAX

## Pengenalan Javascript

#### Apa itu Javascript

JavaScript merupakan bahasa pemrograman multi-paradigma tingkat tinggi lintas
platform (cross platform high-level multi-paradigm programming language). Sifat
multi-paradigma membuat JavaScript mendukung konsep object-oriented programming, imperative programming, dan functional programming. JavaScript sendiri merupakan
implementasi dari ECMAScript, yang merupakan core dari bahasa JavaScript. Beberapa
implementasi lain dari ECMAScript yang mirip dengan JavaScript antara lain JScript (Microsoft)
dan ActionScript (Adobe).

JavaScript, bersama dengan HTML dan CSS, menjadi 3 teknologi utama yang dipakai
pada pengembangan web. Keuntungan menggunakan JavaScript dalam pengembangan
web, pada dasarnya, antara lain JavaScript dapat memanipulasi halaman web secara
dinamis dan memberikan interaksi lebih kepada pengguna. Oleh karena itu, hampir semua
website modern saat ini menggunakan JavaScript dalam halaman web mereka untuk memberikan
pengalaman terbaik kepada pengguna. Beberapa contoh hal yang dapat kita lakukan dengan
menggunakan JavaScript antara lain menampilkan informasi berdasarkan waktu, mengenali jenis
browser pengguna, melakukan validasi form atau data, membuat cookies (bukan kue, tapi
[cookies](https://en.wikipedia.org/wiki/HTTP_cookie)), mengganti styling dan CSS suatu element secara dinamis, dan lain­lain.
Pada pengembangan web umumnya kode JavaScript digunakan pada client-side suatu
web (Client­side JavaScript) namun beberapa jenis kode JavaScript saat ini digunakan pada
server­side suatu web (Server­side JavaScript) seperti node.js. Istilah Client-side menunjukkan
bahwa kode JavaScript akan dieksekusi atau dijalankan pada browser pengguna, bukan pada
server website. Hal ini berarti kompleksitas kode JavaScript tidak akan mempengaruhi performa
server website tersebut namun mempengaruhi performa browser dan komputer, semakin
kompleks kode JavaScript semakin banyak memori komputer yang dikonsumsi oleh browser.

Pada mata kuliah PBP ini kita hanya akan fokus pada kode client-side JavaScript.

#### Bagaimana tahapan JavaScript dieksekusi oleh browser?

Perhatikan diagram berikut.

![javascript-works](https://preview.ibb.co/e258TG/Screenshot_from_2017_10_31_14_29_13.png)

Setelah browser mengunduh halaman HTML web maka tepat dimana tag <script></script>
berada, browser akan melihat tag script tersebut, apakah tag tersebut berisi kode embedded
JavaScript atau merujuk file external JavaScript. Jika merujuk pada file external JavaScript maka
browser akan mengunduh file tersebut terlebih dahulu.

**Cara penulisan Javascript**

Cara penulisan JavaScript bisa dilakukan dengan **embedded javascript** atau **external javascript**.
Kode JavaScript dapat didefinisikan atau dituliskan secara embedded pada file HTML maupun
secara terpisah pada file tersendiri. Jika ditulis dalam file terpisah dari HTML, ekstensi file yang
digunakan untuk file JavaScript adalah .js. Berikut contoh beberapa pendefinisian dan JavaScript.

JavaScript dapat di letakkan pada head atau body dari HTML page. Selain itu, kode JavaScript
**HARUS** dimasukkan di antara tag `<script>` dan `</script>`. Anda dapat meletakkan lebih dari satu
tag script yang berisi JavaScript pada suatu file HTML.

**Embedded JavaScript pada HTML**

index.html

```html
<script type="text/JavaScript">
  alert("Hello World!");
</script>
```

**External JavaScript pada HTML**

index.html

```html
<script type="text/JavaScript" src="js/script.js"></script>
```

js/script.js

```javascript
alert("Hello World!");
```

Pada file external JavaScript tidak perlu lagi menambahkan tag `<script>`.
Memisahkan JavaScript pada file tersendiri memberikan beberapa keuntungan seperti kode dapat
digunakan di file HTML lain, kode JavaScript dan HTML tidak bercampur sehingga lebih fokus,
mempercepat loading halaman. File .js biasanya akan di cache oleh browser sehingga jika kita load page yang sama dan tidak ada perubahan pada file .js maka browser tidak akan request file .js tersebut ke server lagi, akan menggunakan file dari cache yang sudah disimpan sebelumnya.

#### Eksekusi JavaScript

Kemudian setelah JavaScript sudah terunduh dengan sempurna maka browser akan langsung
mulai mengeksekusi kode JavaScript. Jika kode tersebut BUKAN merupakan event triggered
maka kode langsung dieksekusi. Jika kode tersebut merupakan event triggered maka kode
tersebut hanya akan dieksekusi jika event yang didefinisikan triggered.

```javascript
// langsung dieksekusi
alert("Hello World");

// langsung dieksekusi
var obj = document.getElementById("object");
// langsung dieksekusi, menambahkan event handler onclick untuk element object
obj.onclick = function () {
  // hanya dieksekusi jika element 'object' di klik
  alert("You just click the object!");
};
```

#### Syntax JavaScript

**Variable**

Mendefinisikan variabel pada JavaScript cukup mudah. Contohnya seperti

```javascript
var contoh = 0; // var contoh merupakan sebuah bilangan
var contoh = "contoh"; // var contoh merupakan sebuah string
var contoh = true; // var contoh merupakan sebuah boolean
```

Javascript dapat menampung banyak jenis data, mulai string, integer hingga object sekalipun.
Berbeda dengan Java, yang penandaan jenis data dibedakan dengan head variable (contoh ingin
membuat variable int, int x = 9), JavaScript mempunyai ciri khas loosely typed or a dynamic
language, yakni kalian tidak perlu menuliskan jenis data pada head variable, dan JavaScript
nantinya akan secara otomatis membaca jenis data kalian berdasarkan standar yang ada. Seperti
pada contoh diatas. Untuk lebih jelasnya kalian bisa baca pada link ​ini​.

Ada beberapa aturan dalam pemilihan indentifiers atau nama variable dalam JavaScript. Karakter
pertama HARUS ​merupakan alphabet, underscore ( \_ ), atau karakter dollar ($). ​Selain itu
JavaScript identifiers bersifat case sensitive.

**Aritmatika**

Javascript juga dapat melakukan operasi aritmatika, contoh dibawah ini adalah kalkulator
sederhana dengan menggunakan HTML DOM (DOM akan dijelaskan di bawah).

Kode index.html

```javascript
...
<form>
    <h3>Kalkulator Penambahan </h3>
    Angka Pertama: <input type="text" id="number1" />
    Angka Kedua: <input type="text" id="number2" />
    <input type="button" name="submit" value="Submit" onclick="tambahkan();" />
    <p id ="hasil"></p>
</form>
...
```

Kode javascript.js

```javascript
function tambahkan() {
  var x = parseInt(document.getElementById("number1").value);
  var y = parseInt(document.getElementById("number2").value);
  var z = x + y;
  document.getElementById("hasil").innerHTML = z;
}
```

**String Concatenation**

Dalam JavaScript, kita juga dapat menyambungkan string dengan string lainnya seperti pada
Java.

```javascript
var str1 = "PBP" + " " + "Asik";
var str2 = "PBP";
var str3 = "Asik";
var str4 = str2 + " " + str3;
```

#### Javascript Scope

**Local Variable**

Variable yang didefinisikan dalam function hanya dapat diakses oleh kode didalam fungsi
tersebut, bersifat lokal

```javascript
// kode diluar fungsi iniFungsi() tidak dapat mengakses variable namaMatkul
function iniFungsi() {
  var namaMatkul = "PBP";
  // kode di dalam fungsi ini dapat mengakses variable namaMatkul
}
```

**Global Variable**

Variable yang didefinisikan DI LUAR ​function bersifat global dan dapat diakses oleh kode lain
dalam file JavaScript tersebut

```javascript
var namaMatkul = "PBP";
function iniFungsi() {
  // kode di dalam fungsi ini dapat mengakses variable namaMatkul
}
```

**Auto Global Variable**

Value yang di­assign pada variable yang belum dideklarasikan otomatis menjadi global variable
walaupun variable tersebut berada di dalam suatu function.

```javascript
iniFungsi(); // function iniFungsi() perlu dipanggil terlebih dahulu
console.log(namaMatkul); // print "PBP" pada JavaScript console
function iniFungsi() {
  namaMatkul = "PBP";
}
```

**Mengakses Global Variable dari HTML**

Anda dapat mengakses global variable ​yang berada dalam file JavaScript pada file HTML yang
mengunduh file JavaScript tersebut

```html
...
<input type="text" onclick="this.value=namaMatkul" />
...
```

```javascript
...
var namaMatkul = "PBP";
...
```

#### Function dan Event

Function adalah grup­grup dari kode­kode yang bisa dipanggil dimanapun pada bagian
kode program (mirip dengan method java). Hal ini mengurangi redundansi untuk mengurangi
kode­kode yang dapat sama berulang­ulang. Selain itu, function pada JavaScript sangat berguna
untuk memudahkan elemen pemanggilan secara dinamis. Function dapat dipanggil sesama
function dan dapat juga dipanggil karena event (akan dijelaskan di bawah). Sebagai contoh,
berikut kode yang terdapat pada index.html

```html
...
<input type="button" value="magicButton" id="magicButton" onclick="hore();" />
...
```

kemudian berikut adalah kode pada javascript.js

```javascript
...
function hore(){
    alert("Hati­hati tugas 1 PBP berbahaya!");
}
...
```

Sehingga apabila magicButton ditekan maka dengan fungsi onclick akan menjalankan function hore() pada javascript.js,
lalu muncul alert sesuai yang sudah diassign disitu.

Kode onclick sebenarnya adalah salah satu contoh kemampuan JavaScript yang disebut
event. Event adalah kemampuan JavaScript untuk membuat sebuah website dinamis. Maksud
dari onclick adalah penanda apa yang akan dilakukan JavaScript jika elemen tersebut ditekan.
Lebih jauh, event biasanya diberikan sebuah function yang berguna sebagai command­command
untuk JavaScript. Selain itu, banyak contoh­contoh event lainnya seperti : onchange,
onmouseover, onmouseout dan lain sebagainya yang bisa kalian baca pada link
[ini](https://www.tutorialspoint.com/javascript/javascript_events.html)

#### Javasciprt HTML & CSS DOM

**HTML DOM**

HTML DOM (Document Object Model) adalah standar bagaimana mengubah,
mengambil, menghapus HTML elements. HTML DOM dapat diakses melalui JavaScript atau
dengan bahasa pemrograman lainnya. Dengan lengkapnya dapat dilihat
[disini](https://www.w3schools.com/js/js_htmldom.asp)

Berikut contoh implementasinya :

```html
...     
<div>
  <p onclick="myFunction()" id="demo">Ini Percobaan HTML DOM</p>
      
</div>
...
```

```javascript
...
    function myFunction() {
document.getElementById("demo").innerHTML = "YOU CLICKED ME!";
    }
...
```

**CSS DOM**

Sama dengan HTML DOM, DOM CSS dapat mengubah CSS secara dinamis melalui
JavaScript. Lebih lengkapnya terdapat [disini](https://www.w3schools.com/js/js_htmldom_css.asp)
Berikut ini adalah contohnya :

index.html

```html
...
<p id="textBiru" onclick="gantiWarna()">Click me v2</p>
...
```

javascript.js

```javascript
...
function gantiWarna(){
    document.getElementById("textBiru").style.color="blue";
}
...
```

## Web Storage

Dengan penyimpanan lokal, aplikasi web dapat menyimpan data secara lokal dalam browser pengguna.
Sebelum HTML5, data aplikasi harus disimpan dalam cookies , termasuk dalam setiap permintaan server. penyimpanan lokal lebih aman, dan sejumlah besar data dapat disimpan secara lokal, tanpa mempengaruhi kinerja website.
Tidak seperti cookies , batas penyimpanan jauh lebih besar (at least 5MB) dan informasi yang tidak pernah ditransfer ke server.
Penyimpanan lokal adalah per asal (per domain and protocol) . Semua halaman, dari satu asal, dapat menyimpan dan mengakses data yang sama.

Terdapat 2 cara menyimpan data menggunakan web storage. Yaitu : - window.localStorage - menyimpan data tanpa tanggal kadaluarsa - window.sessionStorage - menyimpan data untuk satu session (data hilang ketika tab browser ditutup)

**localStorage Object**

Objek localStorage menyimpan data tanpa tanggal kedaluwarsa. Data tidak akan dihapus ketika browser ditutup, dan akan tersedia pada hari berikutnya, minggu, atau tahun.

Berikut contoh implementasinya :

index.html

```html
...
<p><button onclick="clickCounter()" type="button">Click me!</button></p>
<div id="result"></div>
<p>Click the button to see the counter increase.</p>
<p>
  Close the browser tab (or window), and try again, and the counter will
  continue to count (is not reset).
</p>
...
```

```javascript
...
function clickCounter() {
    if(typeof(Storage) !== "undefined") {
        if (localStorage.clickcount) {
            localStorage.clickcount = Number(localStorage.clickcount)+1;
        } else {
            localStorage.clickcount = 1;
        }
        document.getElementById("result").innerHTML = "You have clicked the button " + localStorage.clickcount + " time(s).";
    } else {
        document.getElementById("result").innerHTML = "Sorry, your browser does not support web storage...";
    }
}
...
```

Apabila dijalankan program tersebut, ketika tombol di click maka terhitung jumlah click akan bertambah.
Ketika browser di close, dan kita membuka kembali, dapat dilihat bahwa perhitungan jumlah click
akan dilanjutkan dari yang sebelumnya.

**sessionStorage Object**

Sama dengan yang atas cuma diganti menggunakan sessionStorage. Yang terjadi adalah apabila browser di close
dan membuka lagi page tersebut, click count akan kembali menjadi 0.

Berikut lebih lengkapanya untuk
[HTML5 WebStorage](http://www.w3im.com/id/html/html5_webstorage.html)

## Pengenalan jQuery

Selain itu ada library JavaScript yang cukup terkenal, yakni jQuery. Seperti slogannya yakni, The Write Less, Do More, jQuery membuat kode dari JavaScript menjadi sangat singkat dari pada sebelumnya. jQuery dibuat oleh John Resign pada tahun 2006. Beberapa kode JavaScript seperti document traversing, event handling, animating, dan AJAX dapat didukung oleh jQuery dengan akses sangat mudah. Instalasi jQuery dapat menggunakan 2 cara, yakni mendownload jQuery dari [jquery.com](https://jquery.com) atau diakses melalui CDN. Pada tutorial kali ini, kita akan mencoba menggunakan jQuery (menggunakan CDN) dalam mengerjakan soal yang ada. Untuk lebih lanjut dalam menggunakan jQuery dapat dibaca di link berikut [ini](https://www.w3schools.com/jquery/default.asp).

## Pengenalan AJAX

AJAX merupakan singkatan dari **A**synchronous **J**avaScript **A**nd **X**ML.

AJAX bukanlah sebuah programming language. AJAX menggunakan browser untuk merequest data dari web server dan JavaScript serta HTML DOM untuk menampilkan data. AJAX dapat menggunakan XML untuk mengirim data tetapi dapat juga menggunakan text ataupun JSON format. AJAX membuat web page mengupdate data secara asinkronus dengan mengirimkan data ke server dibalik layar, artinya kita dapat mengupdate sebagian elemen data pada page tanpa harus mereload keseluruhan page.

Berikut ini adalah cara kerja AJAX:

![ajax-works](https://www.w3schools.com/js/pic_ajax.gif)

1. Sebuah event terjadi pada page (contoh: button submit data ditekan)
2. Sebuah XMLHttpRequest object dibuat oleh JavaScript
3. XMLHttpRequest object mengirimkan request ke server
4. Server memproses request tersebut
5. Server mengembalikan response kembali ke page
6. Response dibaca oleh JavaScript
7. Aksi berikutnya akan ditrigger oleh JavaScript sesuai dengan step yang dibuat (contoh: update data di page tersebut)

Anda bisa menggunakan jQuery untuk melakukan AJAX, penjelasan lebih lanjut dapat dibaca melalui link berikut [ini](https://www.w3schools.com/jquery/jquery_ajax_intro.asp).

## Tugas

Anda diminta untuk membuat sebuah app baru di dalam project ini bernama `lab_5` yang berbasis dari `lab_4` dengan beberapa modifikasi. Tambahkan sebuah kolom baru bernama `Actions` di page yang berisi table dengan tiga buah tombol navigasi:

1. Tombol `View`
   - Akan memunculkan sebuah modal / pop-up yang berisi data pada row tersebut
2. Tombol `Edit`
   - Akan memunculkan sebuah modal / pop-up yang berisi form untuk mengubah data pada row tersebut
   - Setelah data diubah, data pada tabel harus terload dengan data terbaru **tanpa meredirect atau mereload page**
3. Tombol `Delete`
   - Akan memunculkan sebuah confirmation / pop-up untuk konfimasi penghapusan.
   - Setelah data dihapus, data pada tabel harus terload dengan data terbaru **tanpa meredirect atau mereload page**

Tips: Anda dapat menggunakan endpoint yang sudah dibuat pada `lab-2` untuk memudahkan dalam pemanggilan AJAX.

## Checklist

1. [ ] Create new app by running `django-admin startapp lab_5` in root directory (`pbp-lab`).

2. [ ] Register `lab-5/` path in `praktikum/urls.py` file, so that you can access the app by accessing [http://localhost:8000/lab-5](http://localhost:8000/lab-5)

3. [ ] Add `lab_5` into `INSTALLED_APPS` in `praktikum/settings.py` file.

4. Show page to list created `Note` with table format:

   1. [ ] Create `index` method in `lab_5/views.py` that render HTML for our response. Implement it just like we implement `index` method in [lab_2/views.py](../../lab_2/views.py).
   2. [ ] Create a template named `lab5_index.html` in `lab_5/templates` folder that contains a table as a template for our `Note` model. You can use [lab2.html](../../lab_2/templates/lab2.html) as an example and modify it into `lab5_index.html` file.
   3. [ ] Add new column with title `Actions` in the table. It will consist 3 buttons with action `View`, `Edit`, and `Delete`. It will appear in each row of the value.
   4. [ ] Customize HTML and CSS in `lab5_index.html` template with your own imagination.
   5. [ ] Create file `lab_5/urls.py` with route `''` for `index` path so that you can access the result by accessing [http://localhost:8000/lab-5](http://localhost:8000/lab-5).

5. [ ] Import jQuery library into HTML body in `lab_5/templates/lab5_index.html`

6. [ ] Implement AJAX for loading list of `Note` data into the table. You can call the enpoint that you have build in `lab_2` before.

7. Create modal for viewing selected `Note`:

   1. [ ] Implement modal in `lab5_index.html` with HTML code so when we press the view button, it will show a single `Note`.
   2. [ ] Create `get_note` method in `lab_5/views.py` that render HTML for our form.
   3. [ ] Implement `get_note` method so that you can get the selected `Note` with JSON format. For the example you can read the tutorial [here](https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/).
   4. [ ] Add `/notes/<id>` route into `lab_5/urls.py`, so you can call the endpoint by calling [http://localhost:8000/lab-5/notes/notes_id](http://localhost:8000/lab-5/notes/<id>).
   5. [ ] Implement AJAX for loading a single `Note` data into the modal.

8. Create form and modal for editing `Note`:

   1. [ ] Create `forms.py` inside `lab_5` folder.
   2. [ ] Create class `NoteForm` inside `lab_5/forms.py` file.
   3. [ ] Implement class `NoteForm`. Assign `model` in class `Meta` with `Note` model from `lab_2/models.py`.
   4. [ ] Implement form with modal in `lab5_index.html` with HTML code so that it will render our form. Use `POST` as `method` in `<form>` tag.
   5. [ ] Create `update_note` method in `lab_5/views.py` that render HTML for our form.
   6. [ ] Implement `update_note` method so that you can update the selected `Note` with data from the form. For the example you can read the tutorial [here](https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/).
   7. [ ] Check request method in `update_note`. If the request method is `POST` then we need to return `status 200` and `Note instance` after validating form data and save the data if valid with JSON format. Use this tutorial for the [reference](https://www.pluralsight.com/guides/work-with-ajax-django).
   8. [ ] Add `/notes/<id>/update` route into `lab_5/urls.py`, so you can call the endpoint by calling [http://localhost:8000/lab-5/notes/notes_id/update](http://localhost:8000/lab-5/notes/<id>/update).
   9. [ ] Implement AJAX for updating selected `Note` and reload data on the table.

9. Create form and modal for delete `Note`:

   1. [ ] Implement form with modal in `lab5_index.html` with HTML code so that it will render our form. Use `POST` as `method` in `<form>` tag.
   2. [ ] Create `delete_note` method in `lab_5/views.py` that render HTML for our form.
   3. [ ] Implement `delete_note` method so that you can delete the selected `Note`. For the example you can read the tutorial [here](https://www.geeksforgeeks.org/delete-view-function-based-views-django/).
   4. [ ] Check request method in `delete_note`. If the request method is `POST` then we need to return `status 200` with JSON format after succesfully delete selected `Note`. Use this tutorial for the [reference](https://www.pluralsight.com/guides/work-with-ajax-django).
   5. [ ] Add `/notes/<id>/delete` route into `lab_5/urls.py`, so you can call the endpoint by calling [http://localhost:8000/lab-5/notes/notes_id/delete](http://localhost:8000/lab-5/notes/<id>/delete).
   6. [ ] Implement AJAX for deleting selected `Note` and reload data on the table.

10. [ ] Try the application that you have built in this lab using Web Browser.

## Referensi

1. [JavaScript](https://www.w3schools.com/js/default.asp)
2. [jQuery](https://www.w3schools.com/jquery/default.asp)
3. [PBP-2017 Lab 6](https://gitlab.com/PPW-2017/ppw-lab/-/blob/master/lab_instruction/lab_6/README.md)
