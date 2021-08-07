import requests

import json

headers = {
    "accept": "*/*",
    "accept-language": "en",
    "content-type": "application/json",
    "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin"
}

def get_user_info(userSlug):


    data = "{\"operationName\":\"recentSubmissions\",\"variables\":{\"userSlug\":\"%s\"},\"query\":\"query " \
           "recentSubmissions($userSlug: String!) {\\n  recentSubmissions(userSlug: $userSlug) {\\n    status\\n    " \
           "lang\\n    source {\\n      sourceType\\n      ... on SubmissionSrcLeetbookNode {\\n        slug\\n        " \
           "title\\n        pageId\\n        __typename\\n      }\\n      __typename\\n    }\\n    question {\\n      " \
           "questionFrontendId\\n      title\\n      translatedTitle\\n      titleSlug\\n      __typename\\n    }\\n    " \
           "submitTime\\n    __typename\\n  }\\n}\\n\"}" % userSlug

    url = "https://leetcode-cn.com/graphql"

    r_json = requests.post(url=url, headers=headers, data=data).json()
    recentSubmissions = r_json['data']['recentSubmissions']
    return recentSubmissions
