import requests
import pandas as pd

from Document import Document


def fetch_documents_from_api():
    documents = []
    try:
        # RIS
        url = 'https://www.filingsexpert.com/api/v1/fe/documents?highlighting=true&limit=200&query=((classification:25+OR+classification:23)+AND+documentType:5)&sort=Date&start=0'
        # SEDAR
        # url = 'https://www.filingsexpert.com/api/v1/fe/documents?highlighting=true&limit=100&query=((classification:25+OR+classification:23)+AND+documentType:163)+AND+issueDate:%5B2023-04-03+TO+2023-04-08%5D+AND+language:1+AND+year:2023&sort=Date&start=0'
        payload={}
        headers ={ 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlprS1JOdlhFeWNGQmkxN1QzYlZhX2VtLVJMZyIsImtpZCI6IlprS1JOdlhFeWNGQmkxN1QzYlZhX2VtLVJMZyJ9.eyJpc3MiOiJodHRwOi8vYXV0aDIucGVyZmVjdGluZm8uY29tIiwiYXVkIjoiaHR0cDovL2F1dGgyLnBlcmZlY3RpbmZvLmNvbS9yZXNvdXJjZXMiLCJleHAiOjE3NDA3ODA1OTksIm5iZiI6MTY3NzY2NTM5OSwiY2xpZW50X2lkIjoiaW9uQXBpIiwic2NvcGUiOlsicGlBcGkiLCJwaVByb2R1Y3RzIl0sInN1YiI6IjI3MzI0MyIsImF1dGhfdGltZSI6MTY3NzY2NTM5OSwiaWRwIjoiaWRzcnYiLCJwcm9kdWN0IjpbIkZFIiwiREUiLCJNQUkiLCJTRUMiXSwiYW1yIjpbInBhc3N3b3JkIl19.hOYICoytdrP0ag2zHuPXDzlICLAVu2wIgfkPKU5xKhQ_gSDPv-0kt4nC8Nbfbe0JtK1PB57DSJYJt6hllJeSOmpXH-Gvd_QvSoHjuYONfisS8LP91vMa2PXEHfWs3dS5gOSZofhialem8C7aFvoiMcdHhpcJQ73x7m3nkvhjE_PJT6mZA6wezSOPNCgIcKbeeZcQFWofc4dvpKuPfB0aTjkQ5H85uCqGZ5QoWWC07kAYCaT77QUb7p30imO0UdwY5Qrg0vMn2whKL5AgetatnKQoO_tmJW6rF8tpvuXTGQmDwJOjN7bL1nTUsG1S9BL62X7ZODBtipDCSEJ6PnDU_4sYKnRdp4b-1J7MyjvTrtcrkxXMctWiCx3bm79FfL3kBxFvJeOytpisZlGF_A-mWa-GPhdHImKN7seK4coXKjkbUoR7tR3A0qNx_bPRy_K_ksXE5nfVxkrb5eGOslA_ALxbUUQlFyZzssRc00396CS1w8BYLacJf1S52foPJO3vEG5BUSbrbghopM0-gF2uu0RoAhIM1d41GXfa4pBNWp0NMBt70w7qTOILFglhyKFmSF4k4UjieVYHS8cdYJD1g1MVWkcj04XefnyzsSViUxqZGmW19r2H632bE1XrZxBufLCen1xj_c4yYtqL2FzyS3OC7jdytydVf4uw-CdQTAM',
                    'Cookie': 'AWSALB=07UmjlyMzIsH7Dey6JRAsLjCUK+lzmIpNdTTiSr65yj8AxHYIJL2esGdS2/hKzHDro3OuvAdbCQ+/iN9/occr8NT0qIRMEIkOzIt8x7b3Ra18XPoJnazrgCXPdNi; AWSALBCORS=07UmjlyMzIsH7Dey6JRAsLjCUK+lzmIpNdTTiSr65yj8AxHYIJL2esGdS2/hKzHDro3OuvAdbCQ+/iN9/occr8NT0qIRMEIkOzIt8x7b3Ra18XPoJnazrgCXPdNi' }
        response = requests.request("GET", url, headers=headers, data=payload)
        json_response = response.json()
        documents = json_response['documents']
        # print(json_response)
        return documents
    except:
        print("Some Issue with the Filing Expert API")
        return None


data = fetch_documents_from_api()
