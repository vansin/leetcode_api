from leetcode_api import *
import json
import time

def is_today(item):

    timestamp = time.time()
    timestamp_24hours = timestamp - 60*60*24

    if item['submitTime']>timestamp_24hours:
        return True
    else:
        return False

recentSubmissions = get_user_info('vansin')
recentSubmissions = filter(is_today, recentSubmissions)
daily_info = {}
daily_info['total_submit'] = 0
daily_info['problem_submit'] = 0

problems_stat_dict = {}
problems_stat_list = []


for submission in recentSubmissions:

    titleSlug = submission['question']['titleSlug']

    if titleSlug not in problems_stat_dict:

        item = dict()
        problems_stat_list.append(item)
        problems_stat_dict[titleSlug] = len(problems_stat_list)-1

        problem_info = get_problem_info(submission['question']['titleSlug'])
        stats = json.loads(problem_info['stats'])
        difficulty = problem_info['difficulty']
        acRate = stats['acRate']
        item['titleSlug'] = titleSlug
        item['title'] = problem_info['title']
        item['translatedTitle'] = problem_info['translatedTitle']
        item['difficulty'] = difficulty
        item['acRate'] = acRate
        item['submit_nums'] = 0

    item = problems_stat_list[problems_stat_dict[titleSlug]]
    item['submit_nums'] += 1


print(problems_stat_list)

import pandas as pd
dataframe = pd.DataFrame.from_records(problems_stat_list)
dataframe.to_csv('stat.csv')

print(recentSubmissions)

