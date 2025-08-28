from http import HTTPStatus


def test_get_chart(client, chart):
    response = client.get('/charts/A0')

    entries_lenght = 15

    assert response.status_code == HTTPStatus.OK
    assert len(response.json()['entries']) == entries_lenght
