from flask import url_for

def test_get_hello(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    res = client.get(
        url_for('hello_world'), headers=headers)
    assert res.status_code == 200
    assert res.json == {"id": "1", "message": "Hello world"}
