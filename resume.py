import requests
# from rest_framework.generics import GenericAPIView
# from rest_framework.response import Response
import logging
# from RoleAuth_app import serializers

_logger = logging.getLogger(__name__)


search_query = "python"
user_name = "mrashed@vrdella.com"
access_token = "5613e19a-682c-5a23-b044-e5628a8aee56"  # Replace with your Dice.com access token
json1={
  "data_1": {
    "city": "Toronto",
    "country": "Canada",
    "currentJobTitle": "QRP",
    "currentCompany": "Good",
    "experience": {
      "current": {
        "org": "Good",
        "periodEnd": {
          "day": 1,
          "month": 1,
          "year": 2015
        },
        "periodStart": {
          "day": 1,
          "month": 1,
          "year": 2008
        },
        "title": "QRP"
      },
      "history": [
        {
          "org": "Good",
          "periodEnd": {
            "day": 1,
            "month": 1,
            "year": 2015
          },
          "periodStart": {
            "day": 1,
            "month": 1,
            "year": 2008
          },
          "title": "QRP"
        },
        {
          "periodEnd": {
            "day": 1,
            "month": 1,
            "year": 2015
          },
          "periodStart": {
            "day": 1,
            "month": 1,
            "year": 2008
          },
          "title": "Associate Team Lead/ Agile Scrum Master"
        },
        {
          "org": "Very Good",
          "periodEnd": {
            "day": 1,
            "month": 1,
            "year": 2016
          },
          "periodStart": {
            "day": 1,
            "month": 1,
            "year": 2007
          },
          "title": "Python"
        },
        {
          "title": "Sr Software Engineer"
        },
        {
          "title": "Software Developer"
        },
        {
          "org": "SBN Technologics Pvt Ltd",
          "title": "Software Engineer"
        }
      ]
    },
    "firstName": "Suhail",
    "fullName": "Suhail Kassim",
    "dateLastActive": "2023-07-10T19:01:04Z",
    "dateResumeLastUpdated": "2023-01-03T22:37:30.456Z",
    "desiredJobTitles": [
      "Technical Architect"
    ],
    "hasEmail": 'true',
    "hasPhone": 'true',
    "id": "c77a231bb61cbf693c4b3db49da797d520796f8a",
    "candidateId": "c65f0ff3-80bc-412f-803a-3c7e90273df3",
    "legacyIds": [
      "c77a231bb61cbf693c4b3db49da797d520796f8a",
      "a1797451f8e033c07de3d42d4f210dd06424eef8",
      "e8898081e67d0d8cfc4a01bc6e1beada69831713",
      "4b353a9e96efaf5e65b4726bb67e3b18ea501951",
      "195c451a56e2583884043ad351c30f3920a32d48",
      "58ffb828369a18c32eabe5aed7e1524346618855",
      "8cfc3f87ce727ce852462b011191d76f35999506",
      "81fb7426226f937ccb9a9530d3dd46f5fadee5b2",
      "d04277a41f224f071984fe34eca710f09843f19e",
      "19148ef9fdfefb4c9bf5d506f2cf94a3"
    ],
    "isThirdParty": 'false',
    "lastName": "Kassim",
    "likelyToMove": 'false',
    "likelyToMoveScore": 0,
    "locations": [
      {
        "city": "Toronto",
        "country": "Canada",
        "countryCode": "CA",
        "latitude": 43.8127403259277,
        "longitude": -79.2005233764648,
        "postalCode": "M1B 5A3",
        "region": "Ontario",
        "source": "dice",
        "text": "Toronto, Ontario, Canada"
      }
    ],
    "region": "Ontario",
    "skills": [
      {
        "lastUsed": 2023,
        "skill": "python",
        "yearsUsed": 18
      },
      {
        "lastUsed": 2023,
        "skill": "good clinical practice",
        "yearsUsed": 4
      },
      {
        "lastUsed": 2023,
        "skill": "data analysis",
        "yearsUsed": 3
      },
      {
        "lastUsed": 2023,
        "skill": "amazon web services",
        "yearsUsed": 2
      },
      {
        "lastUsed": 2016,
        "skill": "software",
        "yearsUsed": 10
      },
      {
        "lastUsed": 2016,
        "skill": "agile",
        "yearsUsed": 9
      },
      {
        "lastUsed": 2016,
        "skill": "microsoft sql server",
        "yearsUsed": 7
      },
      {
        "lastUsed": 2016,
        "skill": "opentext",
        "yearsUsed": 6
      },
      {
        "lastUsed": 2016,
        "skill": "oracle",
        "yearsUsed": 6
      },
      {
        "lastUsed": 2016,
        "skill": "team building",
        "yearsUsed": 6
      },
      {
        "lastUsed": 2016,
        "skill": "integration",
        "yearsUsed": 5
      },
      {
        "lastUsed": 2016,
        "skill": "leadership",
        "yearsUsed": 2
      },
      {
        "lastUsed": 2016,
        "skill": "microsoft windows azure",
        "yearsUsed": 2
      },
      {
        "lastUsed": 2015,
        "skill": "angularjs",
        "yearsUsed": 7
      },
      {
        "lastUsed": 2015,
        "skill": "automation",
        "yearsUsed": 7
      },
      {
        "lastUsed": 2015,
        "skill": "banking",
        "yearsUsed": 7
      },
      {
        "lastUsed": 2015,
        "skill": "commerce",
        "yearsUsed": 7
      },
      {
        "lastUsed": 2015,
        "skill": "computer science",
        "yearsUsed": 7
      },
      {
        "lastUsed": 2015,
        "skill": "data management",
        "yearsUsed": 7
      },
      {
        "lastUsed": 2015,
        "skill": "data processing",
        "yearsUsed": 7
      },
      {
        "lastUsed": 2015,
        "skill": "finance",
        "yearsUsed": 7
      },
      {
        "lastUsed": 2015,
        "skill": "linux",
        "yearsUsed": 7
      },
      {
        "lastUsed": 2015,
        "skill": "plsql",
        "yearsUsed": 7
      },
      {
        "lastUsed": 2015,
        "skill": "scripting",
        "yearsUsed": 7
      },
      {
        "lastUsed": 2015,
        "skill": "scrum master",
        "yearsUsed": 7
      },
      {
        "lastUsed": 2015,
        "skill": "shell",
        "yearsUsed": 7
      },
      {
        "lastUsed": 2015,
        "skill": "solaris",
        "yearsUsed": 7
      },
      {
        "lastUsed": 2015,
        "skill": "spring",
        "yearsUsed": 7
      },
      {
        "lastUsed": 2015,
        "skill": "team leadership",
        "yearsUsed": 7
      },
      {
        "lastUsed": 2015,
        "skill": "telecommunications",
        "yearsUsed": 7
      },
      {
        "lastUsed": 2015,
        "skill": ".net",
        "yearsUsed": 4
      },
      {
        "lastUsed": 2015,
        "skill": "database",
        "yearsUsed": 4
      },
      {
        "lastUsed": 2015,
        "skill": "microsoft windows",
        "yearsUsed": 4
      },
      {
        "lastUsed": 2015,
        "skill": "migration",
        "yearsUsed": 4
      },
      {
        "lastUsed": 2015,
        "skill": "software engineering",
        "yearsUsed": 4
      },
      {
        "lastUsed": 2015,
        "skill": "system requirements",
        "yearsUsed": 4
      },
      {
        "lastUsed": 2015,
        "skill": "technical writing",
        "yearsUsed": 4
      }
    ],
    "socialProfiles": [
      {
        "icon_64": "https://dmf1ol3sc7oaa.cloudfront.net/64/dice.png",
        "source": "Dice"
      }
    ],
    "workPermitDocuments": [
      "TN Permit Holder"
    ],
    "workPermitLocations": [
      "US"
    ],
    "workPreferences": [
      {
        "employmentType": [
          "Full-time",
          "Part-time"
        ],
        "hourlyRate": {
          "currency": "USD",
          "max": 0,
          "min": 75
        },
        "willingToRelocate": 'false',
        "travelPreference": 0
      }
    ],
    "yearsOfExperience": 16,
    "securityAllowance": {
      "status": 'true'
    }
  },
  "data_2": {
    "city": "Rochester",
    "country": "United States",
    "currentJobTitle": "Python Developer",
    "currentCompany": "Liberty Mutual",
    "experience": {
      "current": {
        "org": "Liberty Mutual",
        "periodEnd": {
          "day": 1,
          "month": 5,
          "year": 2023
        },
        "periodStart": {
          "day": 1,
          "month": 10,
          "year": 2022
        },
        "title": "Python Developer"
      },
      "history": [
        {
          "org": "Liberty Mutual",
          "periodEnd": {
            "day": 1,
            "month": 5,
            "year": 2023
          },
          "periodStart": {
            "day": 1,
            "month": 10,
            "year": 2022
          },
          "title": "Python Developer"
        },
        {
          "org": "Wells Fargo Bank",
          "periodEnd": {
            "day": 1,
            "month": 12,
            "year": 2019
          },
          "periodStart": {
            "day": 1,
            "month": 6,
            "year": 2019
          },
          "title": "Python Developer"
        },
        {
          "org": "Cayaba Care",
          "periodEnd": {
            "day": 1,
            "month": 5,
            "year": 2019
          },
          "periodStart": {
            "day": 1,
            "month": 7,
            "year": 2017
          },
          "title": "Python Developer"
        }
      ]
    },
    "firstName": "Rashmitha",
    "fullName": "Rashmitha Garipally",
    "dateLastActive": "2023-06-12T15:42:03Z",
    "dateResumeLastUpdated": "2023-05-15T14:59:20.626Z",
    "desiredJobTitles": [
      "Python Developer"
    ],
    "hasEmail": 'true',
    "hasPhone": 'true',
    "id": "ef87cb7b7643adfc302282de5e1a56a17a1cae54",
    "candidateId": "d8d29846-968f-4fd0-a16b-00e9cb8a12e8",
    "legacyIds": [
      "ef87cb7b7643adfc302282de5e1a56a17a1cae54",
      "07cc2c684356d03a171b6811e93f25aa98bbee90",
      "41d365ab88a9cd395d660eda1fedb0bb"
    ],
    "isThirdParty": 'false',
    "lastName": "Garipally",
    "likelyToMove": 'false',
    "likelyToMoveScore": 0,
    "locations": [
      {
        "city": "Rochester",
        "country": "United States",
        "countryCode": "US",
        "latitude": 43.0915832519531,
        "longitude": -77.6421585083008,
        "postalCode": "14623",
        "region": "New York",
        "source": "dice",
        "text": "Rochester, New York, United States"
      }
    ],
    "region": "New York",
    "skills": [
      {
        "lastUsed": 2023,
        "skill": "ajax",
        "yearsUsed": 5
      },
      {
        "lastUsed": 2023,
        "skill": "api",
        "yearsUsed": 5
      },
      {
        "lastUsed": 2023,
        "skill": "css",
        "yearsUsed": 5
      },
      {
        "lastUsed": 2023,
        "skill": "database",
        "yearsUsed": 5
      },
      {
        "lastUsed": 2023,
        "skill": "django",
        "yearsUsed": 5
      },
      {
        "lastUsed": 2023,
        "skill": "framework",
        "yearsUsed": 5
      },
      {
        "lastUsed": 2023,
        "skill": "html5",
        "yearsUsed": 5
      },
      {
        "lastUsed": 2023,
        "skill": "javascript",
        "yearsUsed": 5
      },
      {
        "lastUsed": 2023,
        "skill": "jquery",
        "yearsUsed": 5
      },
      {
        "lastUsed": 2023,
        "skill": "json",
        "yearsUsed": 5
      },
      {
        "lastUsed": 2023,
        "skill": "mysql",
        "yearsUsed": 5
      },
      {
        "lastUsed": 2023,
        "skill": "python",
        "yearsUsed": 5
      },
      {
        "lastUsed": 2023,
        "skill": "restful",
        "yearsUsed": 5
      },
      {
        "lastUsed": 2023,
        "skill": "scripting",
        "yearsUsed": 5
      },
      {
        "lastUsed": 2023,
        "skill": "soap",
        "yearsUsed": 5
      },
      {
        "lastUsed": 2023,
        "skill": "web services",
        "yearsUsed": 5
      },
      {
        "lastUsed": 2023,
        "skill": "xml",
        "yearsUsed": 5
      },
      {
        "lastUsed": 2023,
        "skill": "software",
        "yearsUsed": 4
      },
      {
        "lastUsed": 2023,
        "skill": "stored procedures",
        "yearsUsed": 4
      },
      {
        "lastUsed": 2023,
        "skill": "bootstrap",
        "yearsUsed": 3
      },
      {
        "lastUsed": 2022,
        "skill": "agile",
        "yearsUsed": 5
      },
      {
        "lastUsed": 2022,
        "skill": "shell scripting",
        "yearsUsed": 5
      },
      {
        "lastUsed": 2022,
        "skill": "ui",
        "yearsUsed": 3
      }
    ],
    "socialProfiles": [
      {
        "icon_64": "https://dmf1ol3sc7oaa.cloudfront.net/64/dice.png",
        "source": "Dice"
      }
    ],
    "workPermitDocuments": [
      "Employment Auth. Document"
    ],
    "workPermitLocations": [
      "US"
    ],
    "workPreferences": [
      {
        "employmentType": [
          "Full-time",
          "Part-time",
          "Contract - Corp-to-Corp",
          "Contract - Independent",
          "Contract - W2",
          "Contract to Hire - Corp-to-Corp",
          "Contract to Hire - Independent",
          "Contract to Hire - W2"
        ],
        "annualSalary": {
          "currency": "USD",
          "max": 0,
          "min": 130000
        },
        "hourlyRate": {
          "currency": "USD",
          "max": 0,
          "min": 65
        },
        "willingToRelocate": 'true',
        "travelPreference": 0
      }
    ],
    "yearsOfExperience": 6,
    "securityAllowance": {
      "status": 'false'
    }
  }
}

# search_params = {
#     'locations': '[{"value":"Buffalo, NY, USA","distance":100,"distanceUnit":"miles"}]',
#     'skillsKeyword': '',
#     'skillYearsOfExperience': [],
#     'skills': [],
#     'jobTitleKeyword': search_query,
#     'jobTitle': 'python',
#     'searchType': 'Integrated',
#     'language': 'English',
#     'excludeThirdParty': 'false',
#     'excludeFounders': 'false',
#     'hasPatent': 'false',
#     'onlyWithSecurityClearance': 'false',
#     'willingToRelocate': 'false',
#     'willingToRelocatePreferredLocationsOnly': 'false',
#     'willingToRelocateIncludeLocals': 'false',
#     'sortBy': 'relevancy',
#     'sortByDirection': 'asc',
#     'page': '1',
#     'pageSize': '25'
# }

search_params = {
                'locations': '[{"value":"Toronto,Canada"}]',
                'skillsKeyword' : "Python OR data analysis",
                # 'skillYearsOfExperience' : '["PHP|8", "SQL|5"]',
                # 'jobTitleKeyword': search_query,
                # 'jobTitle' : 'developer^tester',
                # 'companyKeyword' : 'vr della AND tcs',
                # 'companyCurrent' : 'true',
                # 'company': 'vr della',
                # 'lastActive' : 10,
                # 'searchType': 'Integrated',
                # 'excludeThirdParty': 'false',
                # 'willingToRelocate': 'false',
                # 'hasEmail': 'true',
                # 'hasPhoneNumber': 'true',
                # 'likelyToSwitch': 'true',
                # 'likelyToMove': {"min":25000},
                # 'yearsExperience': '{"min": 3, "max": 5}',
                # 'educationDegree': "b.tech^m.tech",
                # 'language':'tamil and english',
                # 'socialProfiles':['github', 'stackoverflow', 'twitter','instagram'],
                # 'excludeFounders':'true',
                # 'hasPatent':'true',
                # 'dateResumeLastUpdated':30,
                # 'employmentType':'full time,part time',
                # 'workPermitLocation':'UK OR US',
                # 'workPermit':'us citizenship or green card or employment auth document',
                # 'compensation':'{"max": 150000, "currency": "GBP", "frequency": "yearly", "includeUnspecified": true}',
                # 'onlyWithSecurityClearance':'true',
                # 'willingToRelocatePreferredLocationsOnly': 'false',
                # 'willingToRelocateIncludeLocals': 'false',
                # 'travelPreference': '0',
                # 'facets':'company, skills, jobTitle',
                # 'sortBy': 'relevancy',
                # 'sortByDirection': 'asc',
                # 'page': '1',
                # 'pageSize': '25'
            }

url = 'https://jsonviewer.stack.hu/'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers,params=search_params)

query = str(response)
job_search_response_details = response.json()

print(query)