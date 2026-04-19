d = {
    "fdsajkl;":"in-out",
    "jkl;fdsa":"in-out",
    "asdf;lkj":"out-in",
    ";lkjasdf":"out-in",
    "asdfjkl;":"stairs",
    ";lkjfdsa":"reverse",
}
i = input()
if(i in d):
    print(d[i])
else:
    print("molu")