import qrcode
import validators

print("To exit, type:", end="")
exit_cmds = ("exit","quit","q","-1")
for cmd in exit_cmds:
    print(" '" + cmd + "' |",end="")
print("\n")

input_info_to_user = "Url of the website you want a QR-code for: "

url = input(input_info_to_user)
while (url not in exit_cmds):
    if validators.url(url):
        qr_img = qrcode.make(url)

        name = url.split("://")[1]
        name = name.split(".")
        if name[0] == "www":
            name = name[1]
        else:
            name = name[0]

        qr_img.save(name+"QR.png")
        print("QR-code saved")
    else:
        print("invalid url")
    url = input(input_info_to_user)
