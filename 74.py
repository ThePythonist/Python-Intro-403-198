people = {
    "09121475852": "10 rooze 10 gig",
    "09364605681": "30 rooze 15 gig",
    "09217659152": "01 rooze 01 gig"
}


def send_warning(phonenumber):
    for k, v in phonenumber.items():
        print("""
Moshtarake gerami {} hajm ya zamane basteye
{} shoma roo be etmam ast. lotfan nesbat be tamdid ya kharid
baste eghdam namayid.
""".format(k, v))


send_warning(people)
