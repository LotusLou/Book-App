import pytest
from app.services.google_books import search_books_by_title

async def test_search_books_returns_results():

    results = await search_books_by_title("Atomic Habits")

    assert isinstance(results, list)
    assert len(results) > 0 
    assert "Atomic Habits" in results[0]["title"]