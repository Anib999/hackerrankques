if __name__ == '__main__':
    s = input()
    isAlphaNum = isAlpha = isNumeric = isLower = isUpper = False
    for i in range(len(s)):
        if s[i].isalnum():
            isAlphaNum = True
        if s[i].isalpha():
            isAlpha = True
        if s[i].isnumeric():
            isNumeric = True
        if s[i].islower():
            isLower = True
        if s[i].isupper():
            isUpper = True
    print(isAlphaNum)
    print(isAlpha)
    print(isNumeric)
    print(isLower)
    print(isUpper)
    # print(True if s.isalnum() else False)
    # print(True if s.isalpha() else False)
    # print(True if s.isnumeric() else False)
    # print(True if s.islower() else False)
    # print(True if s.isupper() else False)