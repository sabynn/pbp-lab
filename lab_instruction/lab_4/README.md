# Lab 4: Web Design Using HTML and CSS3

CSGE602022 - Platform-Based Programming (Pemrograman Berbasis Platform) @
Faculty of Computer Science Universitas Indonesia, Odd Semester 2021/2022

---

## Tujuan Pembelajaran

Setelah menyelesaikan tutorial ini, mahasiswa diharapkan untuk mengerti :

- Mengerti susunan tag pada _HTML5_
- Mengetahui berbagai jenis tag _HTML5_
- Mengerti cara penulisan CSS
- Mengetahui static files dalam django
- Mengerti penggunaan selector pada CSS

## Pengenalan HTML

Silahkan pelajari dan mencoba sendiri HTML pada referensi [ini](https://www.w3schools.com/html/default.asp).

## Pengenalan CSS

#### Apa itu CSS

Cascading Style Sheets (CSS) adalah bahasa yang digunakan untuk mendeskripsikan tampilan dan format dari sebuah website yang ditulis pada markup language ( seperti HTML ). Kegunaannya menjadikan tampilan website lebih menarik.

#### Cara penulisan CSS

Secara umum, CSS dapat dituliskan dalam bentuk sebagai berikut.

```css
selector {
  properties: value;
}
```

Terdapat 3 jenis cara penulisan CSS

**1. Inline Styles**

Inline styles adalah styles yang didefinisikan langsung pada elemen dan hanya berlaku pada elemen tersebut. Biasa digunakan untuk mengatur tampilan yang bersifat unik pada single element. Definisi dilakukan dengan menambahkan attribute style yang memiliki CSS property dan value yang diinginkan.

```html
	...
	<div id=”main”
		style=”background­-color: #f0f0f0;
		color: red;
		font­-family: georgia;
		font-­size: 0.8em;”>
		...
	</div>
	...
```

Attribute style pada `div` di atas merupakan contoh penulisan inline style. Hal ini akan menyebabkan `div` tersebut akan memiliki properties seperti value yang diberikan.

**2. Internal Style Sheet**

Internal style sheet didefinisikan dalam elemen `style` di dalam elemen `head`. Biasa digunakan jika suatu halaman memiliki style yang unik. Kalian akan mencoba tampilan yang sama seperti pada inline style sebelumnya dengan menggunakan Internal style sheet. Hapus atribut style yang dibuat sebelumnya, kemudian buat element `style` pada elemen head seperti berikut.

```html
...
<head>
  ...
  <style>
    #main {
      background­-color: #f0f0f0;
      color: red;
      font­-family: georgia;
      font­-size: 0.8em;
    }
  </style>
  ...
</head>
<body>
  <div id="main">...</div>
</body>
...
```

**3. External Style Sheet**

External style sheet didefinisikan secara terpisah dari dokumen HTML. External style sheet memungkinkan untuk mengubah tampilan lebih dari satu halaman dengan cara memberikan referensi ke satu file css. Untuk mengenal External Style Sheet dapat diikuti tutorial dibawah.

Pertama-tama, Kalian akan membuat `tutorial.html` yang merujuk pada `tutorial.css` dengan struktur folder seperti berikut.

    	lab_4
    	├──migrations
    	├──templates
    		├──lab_4
    			├── tutorial.html
    	├──static
    		├── css
    		│   ├── tutorial.css

Kemudian, kalian dapat membuat `tutorial.css` sebagai berikut.

```css
#main {
  background­-color: #f0f0f0;
  color: red;
  font­-family: georgia;
  font­-size: 0.8em;
}
```

Terakhir, kalian dapat membuat file template HTML kalian merujuk pada file css `tutorial.css`

```html
{% load staticfiles %}
<html>
  <head>
    <title>Tutorial CSS Yay</title>
    <link rel="stylesheet" href="{% static 'css/tutorial.css' %}" />
  </head>
  <body>
    <div>
      <h1>Tutorial CSS Yay</h1>
    </div>
    <div id="main">
      <div>
        <p>published: 04 Oktober 2021</p>
        <h1><a href="">Tutorial CSS ku</a></h1>
        <p>Yay ini tutorial yang gampang!</p>
      </div>
    </div>
  </body>
</html>
```

Hal ini dapat terjadi karena CSS merupakan `static files` di Django. Tentang `static files` dijelaskan pada bagian selanjutnya.

> Jika terdapat lebih dari satu style yang didefinisikan untuk suatu elemen, maka style yang akan diterapkan adalah yang memiliki prioritas yang lebih tinggi. Berikut ini urutan prioritasnya, nomor 1 yang memiliki prioritas paling tinggi.
>
> 1.  Inline style
> 2.  External dan internal style sheets
> 3.  Browser default

#### Static files di Django

Pada framework Django, terdapat file - file yang disebut dengan static files. `static files`merupakan file - file pendukung HTML pada suatu website. Contoh `static files` antara lain seperti CSS, Javascript dan gambar. Pengaturan untuk `static files` terdapat dalam `settings.py`

```python
    ...

    # Static files (CSS, JavaScript, Images)
    # httpsdocs.djangoproject.comen1.9howtostatic-files
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
    STATIC_URL = 'static'

    ...
```

Pada `settings.py` terdapat `STATIC_ROOT` yang menentukan _absolute path_ ke direktori `static files` ketika menjalankan perintah `collectstatic` pada project dan terdapat `STATIC_URL` yang merupakan url yang dapat diakses publik untuk memperoleh `static files` tersebut.

Perintah `collectstatic` adalah perintah untuk mengumpulkan `static files` dari semua `app` sehingga mempermudah akses untuk semua `app`

Lebih lengkap mengenai static files
[static files](httpsdocs.djangoproject.comen1.11howtostatic-files)

## Selector pada CSS

Untuk mempermudah tutorial, kalian dapat tetap menggunakan 'tutorial.html' dan 'tutorial.css'. kalian akan mempelajari 3 buah selector pada CSS, yaitu element selector, class selector, dan id selector

**1. Element Selector**

Element selector menggunakan tag html sebagai selector untuk mengubah properties yang terdapat dalam tag tersebut. Pada bagian ini, kalian akan menggunakan element selector sebagai berikut pada `tutorial.css`.

```css
h1 {
  color: #fca205;
  font-family: "Monospace";
  font-style: italic;
}
```

Dapat dilihat perubahan tampilan yang terjadi. Properties element `h1` mengalami perubahan.

**2. Id Selector**

Id selector menggunakan id pada tag sebagai selectornya.

kalian dapat menambahkan id pada template HTML sebagai berikut (id harus bersifat unik).

```html
...
<body>
  <div id="header">
    <h1>Tutorial CSS Yay</h1>
  </div>
  ...
</body>
```

Kemudian id tersebut sebagai selector pada 'tutorial.css'.

```css
#header {
  background-color: #f0f0f0;
  margin-top: 0;
  padding: 20px 20px 20px 40px;
}
```

Dapat dilihat perubahan tampilan yang terjadi. Silahkan menambahkan id selector lain untuk mengubah properties.

**3. Class Selector**

Selanjutnya, class selector yang dapat digunakan untuk memperindah tampilan template HTML.

Tambahkan beberapa class pada tag HTML

```HTML
	...
		<div id="main">
			<div class="content_section">
			    <p class="date">published: 5 Oktober 2021</p>
			    <h2><a href="">Tutorial CSS ku</a></h2>
			    <p id="content_1">Yay ini tutorial yang gampang!</p>
			</div>
			<div class="content_section">
			    <p class="date ">published: 6 Oktober 2021</p>
			    <h2><a href="">Tutorial CSS mu</a></h2>
			    <p id="content_2">Yay ini tutorial yang mudah!</p>
			</div>
			<div class="content_section">
			    <p>published: 7 Oktober 2021</p>
			    <h2><a href="">Tutorial CSS semua</a></h2>
			    <p id="content_3">Yay ini tutorial yang tidak sulit!</p>
			</div>
		</div>
	...
```

Kemudian menambahkan class selector pada css

```css
.content_section {
  background-color: #3696e1;
  margin-bottom: 30px;
  color: #000000;
  font-family: cursive;
  padding: 20px 20px 20px 40px;
}
```

Dapat dilihat perubahan tampilan yang terjadi. Silahkan menambahkan class selector lain untuk mengubah properties.

> Perbedaan penulisan id selector dan class selector
> Id Selector menggunakan format #[id_name] selalu diawali #
> sedangkan class selector menggunakan format .[class_name] diawali .

Untuk memperdalam pengetahuan mengenai CSS Selector Reference anda dapat membaca info berikut:
https://www.w3schools.com/cssref/css_selectors.asp

## Tips & Tricks CSS

#### Mengenal Combinators

Setelah mengetahui selector pada CSS, kalian dapat mengenal `Combinators` pada CSS. `Combinators` adalah suatu menanda hubungan antar element, class atau id dalam CSS. Terdapat 4 `Combinators` pada CSS :

**1. Descendant selector (space)**

Dengan `Combinators` ini, kalian dapat memilih semua element keturunannya (_descendant_) yang sesuai pola. Contoh sebagai berikut.

```html
...
<div>
  <p>Something here</p>
  <span><p>something special</p></span>
</div>
<p>Another thing</p>
<p>Another thing, again</p>
...
```

```css
div p {
  background-color: red;
}
```

Dari kode diatas, maka semua tag `p` keturunan tag `div` akan terpilih.

**2. Child selector (>)**

Mirip dengan _descendant selector_, tetapi _child selector_ hanya memilih keturunan pertama _(child)_ dari element yang sesuai pola.

```css
div > p {
  background-color: red;
}
```

Silahkan dicoba, dan lihat perbedaannya.

**3. Adjacent sibling selector (+)**

_Adjacent sibling selector_ hanya memilih satu element dengan level yang setara _(sibling)_ sesuai dengan pola.

```css
div + p {
  background-color: red;
}
```

**4. General sibling selector (~)**

Sedangkan _general sibling selector_ akan memilih seluruh _sibling_ yang sesuai dengan pola.

```css
div ~ p {
  background-color: red;
}
```

#### Mengenal CSS Pseudo-class

Pseudo-class digunakan untuk mendefinisikan state khusus dari sebuah element. Contoh beberapa pseudo-class

- :active memilih elemen yang sedang aktif
- :cheked memilih elemen yang telah dicentang
- :disabled memilih elemen yang telah di-nonaktifkan
- :enabled memilih elemen yang telah di-aktifkan
- :link memilih link yang belum pernah di kunjungi
- :hover memilih elemen pada saat mouse berada di atasnya
- :visited memilih link yang sudah pernah di kunjungi

Umum pseudo-class dituliskan dalam bentuk sebagai berikut.

```css
selector:pseudo-class {
  properties: value;
}
```

#### Perbedaan Margin, Border dan Padding

<img src="http://1.bp.blogspot.com/-RUtAOT_XsS4/UywVWVG8ohI/AAAAAAAAAL4/HDf0cL0GbGs/s1600/css+margin+padding.gif" alt="margin_padding" width="500" height="300"/>

Dapat dilihat untuk perbedaan margin, border dan padding untuk properties suatu element

#### Pengenalan Bootstrap

Terdapat banyak framework CSS yang sering digunakan sekarang ini, salah satunya adalah Bootstrap CSS. Bootstrap CSS menyediakan class - class yang sering digunakan dalam pengembangan suatu website. Class - class yang disediakan seperti navbar, card, footer, carousel dan lain - lain. Lebih lagi, Bootstrap CSS juga menyediakan banyak fitur yang berguna salah satunya, grid system untuk membagi halaman website menjadi lebih mudah dan menarik.

Lebih lengkap mengenai Bootstrap CSS:
[Bootstrap](httpsgetbootstrap.comdocs3.3csshttpsgetbootstrap.comdocs3.3css)

#### Responsive Web Design

Responsive web design merupakan pendekatan untuk tampilan website tetap terlihat baik pada semua perangkat (baik _desktop_, _tablets_, atau _phones_). Responsive web design tidak mengubah content yang ada, hanya mengubah cara penyajian pada setiap perangkat agar sesuai. Responsive web design menggunakan CSS untuk _resize_, menyusutkan, atau membesarkan suatu element.

> Content is like water
>
> -- Responsive Web Design

Untuk membuka fitur Toggle Device Mode pada browser chrome

Windows/Linux : `CTRL + SHIFT + M`
Mac : `Command + Shift + M`

Lebih lengkap mengenai Reponsive Web Design
[Responsive Web Design](https://web.dev/responsive-web-design-basics/)

## Tugas

Anda diminta untuk membuat sebuah app baru di dalam project ini bernama `lab_4` yang akan menampilkan `Note` seperti pada `lab_2`. Kemudian data tersebut akan ditampilan dalam tiga buah page:

1. Page berisi daftar note yang sudah dimasukkan dalam bentuk **tabel**
2. Page berisi daftar note yang sudah dimasukkan dalam bentuk **card**
3. Page berisi **form** untuk memasukkan data note

Anda perlu untuk membuat navigasi agar page-page tersebut mudah untuk diakses. Anda bebas berkreasi untuk mencoba HTML dan CSS.

## Checklist

1. [ ] Create new app by running `django-admin startapp lab_4` in root directory (`pbp-lab`).

2. [ ] Register `lab-4/` path in `praktikum/urls.py` file, so that you can access the app by accessing [http://localhost:8000/lab-4](http://localhost:8000/lab-4)

3. [ ] Add `lab_4` into `INSTALLED_APPS` in `praktikum/settings.py` file.

4. Show page to list created `Note` with table format:

   1. [ ] Create `index` method in `lab_4/views.py` that render HTML for our response. Implement it just like we implement `index` method in [lab_2/views.py](../../lab_2/views.py).
   2. [ ] Create a template named `lab4_index.html` in `lab_4/templates` folder that contains a table as a template for our `Note` model. You can use [lab2.html](../../lab_2/templates/lab2.html) as an example and modify it into `lab4_index.html` file.
   3. [ ] Customize HTML and CSS in `lab4_index.html` template with your own imagination.
   4. [ ] Create file `lab_4/urls.py` with route `''` for `index` path so that you can access the result by accessing [http://localhost:8000/lab-4](http://localhost:8000/lab-4).

5. Create form for creating new `Note`:

   1. [ ] Create `forms.py` inside `lab_4` folder.
   2. [ ] Create class `NoteForm` inside `lab_4/forms.py` file.
   3. [ ] Implement class `NoteForm`. Assign `model` in class `Meta` with `Note` model from `lab_2/models.py`.
   4. [ ] Create a template named `lab4_form.html` in `lab_4/templates` folder that contains a form for inserting our new `Note` object.
   5. [ ] Implement `lab4_form.html` with HTML code so that it will render our form. Use `POST` as `method` and `""` as `action` in `<form>` tag.
   6. [ ] Customize HTML and CSS in `lab4_form.html` template with your own imagination.
   7. [ ] Create `add_note` method in `lab_4/views.py` that render HTML for our form.
   8. [ ] Implement `add_note` method so that you can create `Note` with data from the form. For the example you can read the tutorial [here](https://www.geeksforgeeks.org/django-modelform-create-form-from-models/).
   9. [ ] Check request method in `add_note`. If the request method is `POST` then we need to redirect to [`/lab-4`](http://localhost:8000/lab-4) after validating form data and save the data if valid.
   10. [ ] Add `add-note` route into `lab_4/urls.py`, so you can access the result by accessing [http://localhost:8000/lab-4/add-note](http://localhost:8000/lab-4/add-note).

6. Show page to list created `Note` with card format:

   1. [ ] Create `note_list` method in `lab_4/views.py` that render HTML for our response. Implement it just like we implement `index` method in [lab_4/views.py](../../lab_4/views.py).
   2. [ ] Create a template named `lab4_note_list.html` in `lab_4/templates` folder as the template to show our `Note` model in card format.
   3. [ ] Customize HTML and CSS in `lab4_note_list.html` template with your own imagination.
   4. [ ] Add `note-list` route into `lab_4/urls.py`, so you can access the result by accessing [http://localhost:8000/lab-4/note-list](http://localhost:8000/lab-4/note-list).

7. [ ] Implement navigation bar on every page, so we can access the page easily with only a click.

8. [ ] Access all the endpoint that you have built in this lab using Web Browser.

## Referensi

1. [HTML](https://www.w3schools.com/html/default.asp)
2. [CSS](https://www.w3schools.com/css/default.asp)
3. [PPW-2017 Lab 4](https://gitlab.com/PPW-2017/ppw-lab/-/blob/master/lab_instruction/lab_4/README.md)
4. [PPW-2017 Lab 5](https://gitlab.com/PPW-2017/ppw-lab/-/blob/master/lab_instruction/lab_5/README.md)
