import requests
import re
def get_response(html_url):
    headers = {
        'cookie': 
            'buvid3=2AE2B00E-CFD5-0C57-1928-2732A079975307288infoc;b_nut=1722046007; _uuid=8736D9A6-B216-AF35-78AA-'
                  'E1E2D2CB755909221infoc; buvid4=BC66B086-A092-4CB3-9C92-'
                  '54AB511F007416429-024072702-lRKx4HRn1XaRVvOJQEmB8g%3D%3D; '
                 'header_theme_version=CLOSE; enable_web_push=DISABLE; CURRENT_FNVAL=4048; rpdid=|(JuuuJJmRY0J'
                 ''
                 'u~kk|~~YJm; DedeUserID=202277834; DedeUserID__ckMd5=fb1a3d04ff7a02f7; buvid_fp_plain=undefined; hit-dyn-v2=1; '
                 'fingerprint=929f09a3b4eb758b2c259ab255927059; home_feed_column=5; browser_resolution=1528-738; bp_t_offset_202277834=982132104311603200;'
                 ' bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjgyNzA5MDEsImlhdCI6MTcyODAxMTY0MSwicGx0IjotMX0.T9QhXIbr6QeFdH5JNirBGVjtUU9MZfsRi3X9nYvX_Z0;'
                 ' bili_ticket_expires=1728270841; SESSDATA=20b8c878%2C1743563702%2C2780e%2Aa1CjD1xocAOJPkCkaHA8_Uc-lIHSjyLM6kRNilG1fWXBpT-B5mGTtgfoqLVBXvt799rBASVm5jV1pDSGNlS21MWEFpQ2hJTG81V0tOazgx'
                 'RXZxLUtfb0dBZVNpT0p3QVVWODIxUDZ5RENneXB3M1piMVhnOENKMnVBbVpFY1ZENUppOHlDellSaFZRIIEC; bili_jct=917bdce49a3e737b5ebc8a7e1ef5c7d7;'
                 ' sid=7ljpr260; b_lsid=9A4C1F89_1925D556D3E; buvid_fp=2AE2B00E-CFD5-0C57-1928-2732A079975307288infoc'
                  ,
        'origin': 'https://www.bilibili.com',
        'referer': 'https://www.bilibili.com/video/BV1qt411j7fV',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'
                       }
    response = requests.get(url=html_url, headers=headers)
    return response
url = f'https://api.bilibili.com/x/v2/dm/wbi/web/seg.so?type=1&oid=4149764&pid=2657770&segment_index=1&pull_mode=1&ps=120000&pe=360000&web_location=1315873&w_rid=926bb2bfd11bc57d1c716d220dd482be&wts=1728213114'
html_data = get_response(url).text

result = re.findall(".*?([\u4E00-\u9FA5]+).*?", html_data)
print(result)
with open('py.txt', 'w', encoding='utf-8') as f:
    for item in result:
        f.write(f"{item}\n")