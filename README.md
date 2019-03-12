# github-issues-detail
A django app which will get issues count from github 

## requirements
To run this you need to have django and requests module installed

## Runserver
Clone the repository and then go into the project folder
and runserver by running 
```
python manage.py runserver 0:8000
```
In the browser go to localhost:8000 and you will see the app running

It will show an input box you can enter the github repository url and it will show the total no of issues opened,
Total no of issues opened in 24 hours, total no of issues opened in the last 7 days after 24 hours and total no of issues opened before seven days

## Logic
### total no of issues opened
  - When you go to the repo url using github api it will giv the total no of issues opened 
### total no of issues opened in 24 hours
  - We can make github api request to get issues since some time github api per page gives 30 results and in header gives the next page url and last page url. Getting the last page url from header and getting the no of records in that page 
  - suppose the last page is 9. so per till 8th page we will have 30 records per page so 8*30= 240 issues and in last page we have 22 records so 240 + 22= 262 issues 
### total no of issues opened in the last 7 days and before 24 hours 
  - getting the total no of issues opened in the last 7 days and subbtracting the no of issues opened in the 24 hours with it
### total no of issues before 7 days
  - subtracting the total no of issues opened in 7 days with total no of issues
