def search_google_books(query: str) -> list[dict]:
    return [] if not query else [{"title": query, "author": "Unknown"}]
