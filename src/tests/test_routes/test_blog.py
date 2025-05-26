from tests.utils.blog import create_random_blog


def test_all_blogs_route(client, db_session):
    blog = create_random_blog(db_session)
    response = client.get("/blogs")
    assert response.status_code == 200  # get method
    print(blog)
    assert response.json()[0]["title"] == blog.title
    assert response.json()[0]["content"] == blog.content


def test_post_route(client, db_session):
    body = {"title": "new creation  test", "content": "new content creation test"}
    response = client.post("/blogs/", json=body)
    assert response.status_code == 201  # post method successful
    assert response.json()["content"] == "new content creation test"
    assert response.json()["title"] == "new creation  test"  # check info


def test_get_specific_blog_route(client, db_session):
    blog = create_random_blog(db_session)
    response = client.get(f"/blogs/{blog.id}")
    assert response.status_code == 200  # get method
    assert response.json()["title"] == blog.title  # check info


def test_put_route(client, db_session):
    blog = create_random_blog(db_session)
    body = {"id": 1, "title": "new update  test", "content": "new content changed"}
    response = client.put(f"/blogs/{blog.id}", json=body)
    assert response.status_code == 200  # put method successful
    assert response.json()["content"] == "new content changed"
    assert response.json()["title"] == "new update  test"  # check info


def test_delete_route(client, db_session):
    blog = create_random_blog(db_session)
    response = client.delete(f"/blogs/{blog.id}")
    assert response.status_code == 200  # delete method successful
    # assert response.json()["message"] == "blog deleted successfully"
