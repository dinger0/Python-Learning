import requests
base_url='https://api.github.com'

def construct_url(endpoint):
    return '/'.join([base_url,endpoint])

def basic_auth():
    #基本认证
    response=requests.get(construct_url('user'),auth=('imoocdemo','imoocdemo123'))
    print(response.text)
    print(response.request.headers)

def basic_oauth():
    headers={'Authorization':'token dd6322fa6c57a548268453dc245cbcdc352a7811'}
    # user/emails
    response=requests.get(construct_url('user/emails'),headers=headers)
    print(response.headers)
    print(response.text)
    print(response.status_code)

from requests.auth import AuthBase

class GithubAuth(AuthBase):
    def __init__(self,token):
        self.token=token

    def __call__(self, r):
        # requests 加 headers
        r.headers['Authorization']=' '.join(['token',self.token])
        return r

def oauth_advanced():
    auth=GithubAuth('dd6322fa6c57a548268453dc245cbcdc352a7811')
    response=requests.get(construct_url('user/emails'),auth=auth)
    print(response.text)



if __name__=='__main__':
    #basic_oauth()
    oauth_advanced()

