import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 13
    assert 'become-qa-auto' in r['items'][0]['name'] 


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0
    

 
@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0

@pytest.mark.api
def test_user_exists(github_api):
    response = github_api.get_user('defunkt')
    assert 'login' in response
    assert response['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    response = github_api.get_user('butenkosergii')
    assert 'message' in response
    assert response['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    response = github_api.search_repo('become-qa-auto')
    assert 'total_count' in response
    assert response['total_count'] == 25

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    response = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert 'total_count' in response
    assert response['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    response = github_api.search_repo('s')
    assert 'total_count' in response
    assert response['total_count'] != 0

@pytest.mark.api
def test_get_emojis(github_api):
    response = github_api.get_emojis()
    assert response, "The emoji list should not be empty"
    assert 'smile' in response, "The emoji list should contain 'smile' emoji"

@pytest.mark.api
def test_list_commits(github_api):
    response = github_api.list_commits('octocat', 'Hello-World')
    assert isinstance(response, list), "Commits should be returned as a list"
    assert len(response) > 0, "There should be at least one commit in the list"
    assert 'sha' in response[0], "Each commit should have a 'sha' attribute"       