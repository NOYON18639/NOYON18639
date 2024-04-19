#---------------logo----------------#
logo='''
________               __      ______                __  
/ ____/ /_  ____  _____/ /_    /_  __/________ ______/ /__
 / / __/ __ \/ __ \/ ___/ __/_____/ / / ___/ __ `/ ___/ //_/
 / /_/ / / / / /_/ (__  ) /_/_____/ / / /  / /_/ / /__/ ,<   
\____/_/ /_/\____/____/\__/     /_/ /_/   \__,_/\___/_/|_|
'''
#--------------------youtube-------------------#
is_option
def YOUTUBE CHANNEL_Hack():
     = input(f"{Wh}\n Enter Youtube channel link target : {Gr}")  # INPUT YOUTUBE CHANNEL
    print()
    print(f' {Wh}============= {Gr}SHOW INFORMATION FOR YOUTUBE CHANNEL LINK{Wh}=============')
    req_api = requests.get(f"http://youtube channel.is/{channel}")  # API YOUTUBE CHANNELWHOIS.IS
    link_information= json.loads(req_api.text)
    time.sleep(2)
    print(f"{Wh}\n Youtube Channel target         :{Gr}", channel link)
    print(f"{Wh} Gmail      :{Gr}", link_information["gmail"])
    print(f"{Wh} Password    :{Gr}",link_information ["password"])
#-------------end--------------#
