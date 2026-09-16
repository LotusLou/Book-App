# Book-App

App to get an overview over books you have read.
## Start
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
## Projektstruktur

```text
app/
  __init__.py
  main.py
  core/
    config.py
    security.py
  db/
    database.py
    models.py
  routers/
    pages.py
    books.py
    gamification.py
  services/
    google_books.py
    gamification_calc.py
  templates/
    base.html
    components/
      navbar.html
      book_card.html
      searchbar.html
    pages/
      index.html
      books.html
      profile.html
static/
  js/barcode_scanner.js
  js/radar_chart.js
  img/
requirements.txt
```
