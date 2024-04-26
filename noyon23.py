#---------------logo---------------#
logo=(f'''{B}
`7MM"""Mq. `7MMF' `7MN.   `7MF'  .g8"""bgd
{warna}  MM   `MM.  MM     MMN.    M  .dP'     `M
{B}  MM   ,M9   MM     M YMb   M  dM'       `
{warna}  MMmmdM9    MM     M  `MN. M  MM
 {B} MM         MM     M   `MM.M  MM.    `7MMF'
{warna}  MM         MM     M     YMM  `Mb.     MM
{B}.JMML.     .JMML. .JML.    YM    `"bmmmdPY
{warna}--------------------------------------------{B}
 Owner    : {C}MD NOYON {B}
 Guthub   : NOYON18639
 Facebook : HADI FAOUR
 Tools    : F{C}/{B}R{C}/{B}G{M} •{warna}[{H}TRAIL{warna}]{warna}
--------------------------------------------{B}''')
#--------------facebook-------------#
def facebook_information():
	facebook=input("{Wh}/n Enter Facebook id:{Gr}") #INPUT FACEBOOK INFORMATION
    print()
    print(f' {Wh}=========={Gr}SHOW THE FACEBOOK INFORMATION{Wh}==========')
    req_api = requests.get(f"http://facebookwho.is/{id}")  # API FACEBOOK INFORMATION WHOIS.IS
    facebook_information= json.loads(req_api.text)
    time.sleep(2)
    print(f"{Wh}\n Facebook id target         :{Gr}", channel link)
    print(f"{Wh} Gmail      :{Gr}", facebook_information["gmail"])
    print(f"{Wh} Password    :{Gr}",facebook_information ["password"])
#---------------end---------------# 