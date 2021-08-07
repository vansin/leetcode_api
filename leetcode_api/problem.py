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


def get_problem_info(titleSlug):

    data = "{\"operationName\":\"questionData\",\"variables\":{\"titleSlug\":\"%s\"},\"query\":\"query " \
           "questionData($titleSlug: String!) {\\n  question(titleSlug: $titleSlug) {\\n    questionId\\n    " \
           "questionFrontendId\\n    categoryTitle\\n    boundTopicId\\n    title\\n    titleSlug\\n    content\\n    " \
           "translatedTitle\\n    translatedContent\\n    isPaidOnly\\n    difficulty\\n    likes\\n    dislikes\\n    " \
           "isLiked\\n    similarQuestions\\n    contributors {\\n      username\\n      profileUrl\\n      avatarUrl\\n  " \
           "    __typename\\n    }\\n    langToValidPlayground\\n    topicTags {\\n      name\\n      slug\\n      " \
           "translatedName\\n      __typename\\n    }\\n    companyTagStats\\n    codeSnippets {\\n      lang\\n      " \
           "langSlug\\n      code\\n      __typename\\n    }\\n    stats\\n    hints\\n    solution {\\n      id\\n      " \
           "canSeeDetail\\n      __typename\\n    }\\n    status\\n    sampleTestCase\\n    metaData\\n    " \
           "judgerAvailable\\n    judgeType\\n    mysqlSchemas\\n    enableRunCode\\n    envInfo\\n    book {\\n      " \
           "id\\n      bookName\\n      pressName\\n      source\\n      shortDescription\\n      fullDescription\\n      " \
           "bookImgUrl\\n      pressImgUrl\\n      productUrl\\n      __typename\\n    }\\n    isSubscribed\\n    " \
           "isDailyQuestion\\n    dailyRecordStatus\\n    editorType\\n    ugcQuestionId\\n    style\\n    " \
           "exampleTestcases\\n    __typename\\n  }\\n}\\n\"} " % titleSlug

    url = "https://leetcode-cn.com/graphql"

    r_json = requests.post(url=url, headers=headers, data=data).json()

    return r_json['data']['question']

