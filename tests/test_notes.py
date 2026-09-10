"""Increment 1: create a note and see it in the list (newest first)."""


def test_home_renders(client):
    r = client.get("/")
    assert r.status_code == 200
    assert "Quick Notes" in r.text
    assert "No notes yet" in r.text


def test_create_note_shows_in_list_newest_first(client):
    client.post("/notes", data={"title": "First", "body": "one"})
    client.post("/notes", data={"title": "Second", "body": "two"})
    r = client.get("/")
    assert r.status_code == 200
    assert r.text.index("Second") < r.text.index("First")


def test_empty_title_is_rejected(client):
    r = client.post("/notes", data={"title": "", "body": "x"}, follow_redirects=False)
    assert r.status_code == 422
    assert "x" not in client.get("/").text.split("<ul")[1]
