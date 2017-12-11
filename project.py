import urllib.parse
import requests

main_api = 'https://api.github.com/users/'

user = input('Github Login: ')


url = main_api + user

json_data = requests.get(url).json()

id_number = json_data['id']
name = json_data['name']
company = json_data['company']
blog = json_data['blog']
location = json_data['location']
email = json_data['email']
followers = json_data['followers']
following = json_data['following']
number_of_repos = json_data['public_repos']


print('User = ' + str(user) + '\n' + 'ID = ' + str(id_number) + '\n' + 'Name = ' + str(name) + '\n' + 'Company ='
    + str(company) + '\n' + 'Blog =' + str(blog) + '\n' + 'Location = ' + str(location) + '\n' + 'Email = ' + str(email)
        + '\n' + 'Follower count =' + str(followers) + '\n' + 'Following count = ' + str(following) + '\n' + 'Repo count =' 
            + str(number_of_repos))
