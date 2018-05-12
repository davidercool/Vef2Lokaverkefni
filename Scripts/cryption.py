def encrypt(text, step=2):
    ans = ""
    for x in text:
        ans += chr(ord(x)+step)
    return ans


def decrypt(text, step=2):
    ans = ""
    for x in text:
        ans += chr(ord(x)-step)
    return ans
