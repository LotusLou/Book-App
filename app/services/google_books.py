import httpx

async def search_google_books(query: str):
    clean_query = query.strip()

    # 1. Falls "isbn:" schon im Suchbegriff steht (z.B. aus Swagger), schneiden wir es erst ab:
    if clean_query.lower().startswith("isbn:"):
        raw_number = clean_query[5:].strip()
    else:
        raw_number = clean_query

    # 2. Bereinigen aller Sonderzeichen für den ISBN-Check
    digits_only = (
        raw_number.replace("-", "")
        .replace(" ", "")
        .replace("X", "")
        .replace("x", "")
    )

    # 3. Wenn es eine 10- oder 13-stellige Zahl ist -> exakt einmal "isbn:" davor setzen
    if digits_only.isdigit() and len(digits_only) in [10, 13]:
        search_term = f"isbn:{digits_only}"
    else:
        search_term = clean_query
    
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}"
    API_Key= "AIzaSyAj9UxHhjszpv7e7Q8dtMfhXan61fonBao"
    params = {"q": clean_query, "maxResults": 10, "key" : API_Key}
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params= params)
        data = response.json()

    print("--- ANZAHL ITEMS VON GOOGLE ---")
    print(len(data.get("items", [])))  # Zeigt im Terminal an, wie viele Treffer Google findet
    books = []
    # Prüfen, ob Google überhaupt Treffer liefert
    if "items" in data:
        for item in data["items"]:
            volume_info = item.get("volumeInfo", {})

            # Cover-URL sicher auslesen (falls imageLinks vorhanden ist)
            image_links = volume_info.get("imageLinks")
            cover_url = image_links.get("thumbnail") if image_links else None

            # ISBN sicher suchen
            isbn = None
            for identifier in volume_info.get("industryIdentifiers", []):
                if identifier.get("type") in ["ISBN_13", "ISBN_10"]:
                    isbn = identifier.get("identifier")
                    break

            book_data = {
                "title": volume_info.get("title", "Unbekannter Titel"),
                "authors": ", ".join(
                    volume_info.get("authors", ["Unbekannter Autor"])
                ),
                "total_pages": volume_info.get("pageCount", 0),
                "cover_url": cover_url,
                "categories": volume_info.get("categories", []),
                "isbn": isbn,
            }

            books.append(book_data)

    return books