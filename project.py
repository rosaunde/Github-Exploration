import urllib.parse
import requests
import matplotlib.pyplot as plt
from collections import Counter


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





new_url = url + '/repos'

json_data2 = requests.get(new_url).json()

languages = []

i=0;
while (i < len(json_data2)):
    language = json_data2[i]['language']
    languages.append(language)
    i = i + 1


cnt = Counter(languages)

common_languages = cnt.most_common(5)

language_names = []
i = 0
while(i < len(common_languages)):
    language_names.append(common_languages[i][0])
    i = i+1

language_counts = []
i=0
while(i < len(common_languages)):
    language_counts.append(common_languages[i][1])
    i = i+ 1


plt.bar(language_names, language_counts)
plt.xlabel('Language')
plt.ylabel('Repository Count')
plt.title('Most used languages by Repository')
plt.show()





#This actually doesn't work because the events page on the api doesn't extend past 2017, but I couldn't figure out how to rectify this
#If the API page displayed all events it would work

new_url2 = url + '/events'
json_data3 = requests.get(new_url2).json()

years = [[2013,0],[2014,0],[2015,0],[2016,0],[2017,0]]
i=0
while(i < len(json_data3)):
    if (json_data3[i]['type'] == 'CreateEvent' or 'PushEvent'):
        date = json_data3[i]['created_at']
        year = date[:4]
        if (year == '2013'):
            years[0][1] = (years[0][1] + 1)
        if (year == '2014'):
            years[1][1] = (years[1][1] + 1)
        if (year == '2015'):
            years[2][1] = (years[2][1] + 1)
        if (year == '2016'):
            years[3][1] = (years[3][1] + 1)
        if (year == '2017'):
            years[4][1] = (years[4][1] + 1)
    i = i + 1

year_names = []
i = 0
while(i < len(years)):
    year_names.append(years[i][0])
    i = i+1

year_counts = []
i=0
while(i < len(years)):
    year_counts.append(years[i][1])
    i = i+ 1

plt.plot(year_names, year_counts)
plt.xlabel('Year')
plt.ylabel('Commit Count')
plt.title('Commits per Year')
plt.show()




#This only creates a piechart if the user follows people and has followers

new_url3 = url + '/following'
json_data4 = requests.get(new_url3).json()

following_list = []

i = 0;
while (i < len(json_data4)):
    following_list.append(json_data4[i]['id'])
    i = i + 1

new_url4 = url + '/followers'
json_data5 = requests.get(new_url4).json()

followers_list = []

i = 0;
while (i < len(json_data5)):
    followers_list.append(json_data5[i]['id'])
    i = i + 1

follow_back = list(set(followers_list).intersection(following_list))

following_number = len(following_list)
follow_back_number = len(follow_back)

if (following_number != 0):
    follow_back_percent = (follow_back_number / following_number) * 100
else:
    follow_back_percent = 0

other_percent = 100 - follow_back_percent

slices = [follow_back_number, (following_number-follow_back_number)]
names = ['Following back (' + str(round(follow_back_percent, 1) ) + '%)', 'Not Following Back (' + str(round(other_percent, 1)) + '%)']
cols = ['green', 'red']

plt.pie(slices, labels = names, colors = cols)
plt.title('Total Followers')
plt.show()
