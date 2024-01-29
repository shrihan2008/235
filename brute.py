import requests

for i in range(1,1001):
    url="http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/api/get-customer?id="+i
    r=requests.get(url=url)
    if r.status_code==200:
        print(url)