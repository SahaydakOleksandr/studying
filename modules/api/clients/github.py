import requests


class GitHub:
    BASE_URL = "https://api.github.com"
    
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": name}
        )
        body = r.json()

        return body
    
    def get_user(self, username):
        url = f"{self.BASE_URL}/users/{username}"
        response = requests.get(url)
        return response.json()

    def search_repo(self, name):
        url = f"{self.BASE_URL}/search/repositories"
        params = {'q': name}
        response = requests.get(url, params=params)
        return response.json()
    
    def get_emojis(self):
        url = f"{self.BASE_URL}/emojis"
        response = requests.get(url)
        return response.json()
    
    def list_commits(self, owner, repo):
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/commits"
        response = requests.get(url)
        return response.json()
