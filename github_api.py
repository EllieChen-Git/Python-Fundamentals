import requests

def create_query(languages, min_stars=50000):
    query = f"stars:>{min_stars} "

    for language in languages:
        query += f"language:{language} "

    return query

def repos_with_most_stars(languages, sort="stars", order="desc"):
    gh_api_repo_search_url = "https://api.github.com/search/repositories"
    query = create_query(languages)
    parameters = {"q": query, "sort": sort, "order": order}
    response = requests.get(gh_api_repo_search_url, params=parameters)

    status_code = response.status_code
    if status_code != 200:
        raise RuntimeError(f"An error occured. Status code was {status_code}")
    else:
        return response.json()["items"]


if __name__ == "__main__":
    languages = ["Python", "JavaScript", "Ruby"]
    results = repos_with_most_stars(languages)

    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]

        print(f"-> {name} is a {language} repo with {stars} stars.")


