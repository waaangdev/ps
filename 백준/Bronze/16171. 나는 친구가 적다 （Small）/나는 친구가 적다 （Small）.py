st = input()
for i in range(10):
    st = st.replace(str(i),'')
if(st.find(input()) != -1):
    print(1)
else:
    print(0)