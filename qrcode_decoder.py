import cv2

print("To exit, type:", end="")
exit_cmds = ("exit","quit","q","-1")
for cmd in exit_cmds:
    print(" '" + cmd + "' |",end="")
print("\n")

input_info_to_user = "Filename of the QR-code you want to decode: "

decoder = cv2.QRCodeDetector()
file = input(input_info_to_user)
while (file not in exit_cmds):
    text, _, _ = decoder.detectAndDecode(cv2.imread(file))
    print("Decoded text is: ", text)
    file = input(input_info_to_user)
