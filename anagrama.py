def is_anagrama(word1, word2):
    if len(word1) != len(word2):
        return False
    lst = list(word2)
    for i in word1:
        if i in lst:
            lst.remove(i)
        else:
            return False
    return True

print(is_anagrama(input("Ente a text: "), input("Ente a text: ")))
# չկարողացա list-ի մեջ հավաքեմ փորձեցի երկու բառ ստուգեմ իրարով