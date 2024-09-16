def pn_formatter(phonenumber):
    if len(phonenumber) == 11:
        if phonenumber[0] == "0":
            pn = phonenumber.replace("0", "+98", 1)
            return pn
        else:
            return "Invalid phone number"
    else:
        return "Invalid phone number"


print(pn_formatter("09126256040"))
