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
    # "x-csrftoken": "f2nu3U9f4nqxqVEMZudAwF20nXtAbgXJ8GVQzO4RKJXMnOz1FNawlGvtJYoXVda0",
    # "cookie": "csrftoken=f2nu3U9f4nqxqVEMZudAwF20nXtAbgXJ8GVQzO4RKJXMnOz1FNawlGvtJYoXVda0; __auc=32b8654717a4d03593189695cd9; gr_user_id=75daf27c-2663-47ee-89e0-84b6e139b2b4; _ga=GA1.2.86932946.1624789704; a2873925c34ecbd2_gr_last_sent_cs1=vansin; _gid=GA1.2.1086993762.1626831318; __asc=79a9e88717acbcaee5a845153b9; a2873925c34ecbd2_gr_session_id=87fa5ebd-a713-48b8-9ec1-e258e8e41929; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=87fa5ebd-a713-48b8-9ec1-e258e8e41929; a2873925c34ecbd2_gr_session_id_87fa5ebd-a713-48b8-9ec1-e258e8e41929=true; NEW_PROBLEMLIST_PAGE=1; __appToken__=; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1626741079,1626831317,1626916712,1626922350; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1626922561; a2873925c34ecbd2_gr_cs1=vansin"
}

page = '1'
data = "{\"operationName\":\"recentSubmissions\",\"variables\":{\"userSlug\":\"vansin\"},\"query\":\"query " \
       "recentSubmissions($userSlug: String!) {\\n  recentSubmissions(userSlug: $userSlug) {\\n    status\\n    " \
       "lang\\n    source {\\n      sourceType\\n      ... on SubmissionSrcLeetbookNode {\\n        slug\\n        " \
       "title\\n        pageId\\n        __typename\\n      }\\n      __typename\\n    }\\n    question {\\n      " \
       "questionFrontendId\\n      title\\n      translatedTitle\\n      titleSlug\\n      __typename\\n    }\\n    " \
       "submitTime\\n    __typename\\n  }\\n}\\n\"}"

url = "https://leetcode-cn.com/graphql"


r_json = requests.post(url=url, headers=headers, data=data).json()


recentSubmissions = r_json['data']['recentSubmissions']

print(r_json)

