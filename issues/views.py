import json
import re
from datetime import datetime, timedelta

from urllib import parse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, render_to_response

import requests

def home(request):
    return render(request, 'index.html')

def make_req(url):
    req = requests.get(url=url)
    return req.json(), req.headers

def get_issue_for_date(day, repo_url):
    #subtracting day from todays datetime to get previous date
    previous_date = datetime.today() - timedelta(days=day)
    previous_date = previous_date.isoformat()
    #making request to get issues
    request_url = repo_url + '/issues?page=1&state=open&since=' + str(previous_date)
    resp, headers = make_req(request_url)
    #github api returns a key in header called link which will contain info if there are more pages
    if headers.get('link', ''):
            link = re.split('<|>', head.get('link', ''))[-2]
            total_pages = int(parse.parse_qs(parse.urlsplit(link)))
            temp_issues = (total_pages - 1)*30
            resp, headers = make_req(request_url)
            total_issues = len(resp) + temp_issues
    else: total_issues = len(resp)
    return total_issues

@csrf_exempt
def get_all_issues(request):
    url = request.POST['url']
    #get the repository path
    url_path = parse.urlsplit(url).path
    api_host = 'https://api.github.com/repos'

    #making the github api link
    #github api returns the total no of issue when you look for repository data
    repo_url = api_host + url_path
    resp, headers = make_req(repo_url)
    total_open_issue = resp.get('open_issues_count', '')
    
    #getting issue which were opened 24hours ago
    issue_before_day = get_issue_for_date(1, repo_url)

    #getting issue which were opened 7days ago
    seven_day_issue = get_issue_for_date(7, repo_url)
    #removing no of issues opend before 24 hours from total issue between 7 days 
    #to get issues between 24 hours and 7 days 
    issue_between_seven_day = seven_day_issue - issue_before_day

    #subtrating the total no issue with total issue opened within 7 days to get issues before 7 days
    issue_before_seven_day = int(total_open_issue) - seven_day_issue

    return JsonResponse({
            'total_issue' : total_open_issue,
            'issue_in_day' : issue_before_day,
            'issue_in_seven_day' : issue_between_seven_day,
            'issue_before_seven_day' : issue_before_seven_day
            })
