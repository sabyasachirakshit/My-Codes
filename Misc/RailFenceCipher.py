def encoding(p_text,key):
    cipher_text=""
    if key==2:
        l1=len(p_text)
        l2=l1
        row1=[]
        row2=[]
        while(l1!=0):
            row1.append('r1')
            l1-=1
        while(l2!=0):
            row2.append('r2')
            l2-=1
        p_text_str=list(p_text)
        for pos,value in enumerate(p_text_str):
            if pos==0 or pos%2==0:
                row1[pos]=value
            if pos%2!=0:
                row2[pos]=value
        cipher1=""
        cipher2=""
        for i in row1:
            if i!="r1":
                cipher1+=i
        for i in row2:
            if i!="r2":
                cipher2+=i
        cipher_text=cipher1+cipher2
    elif key==3:
        l1=len(p_text)
        l2=l1
        l3=l2
        lt=0
        lt2=1
        lt3=2
        row1=[]
        row2=[]
        row3=[]
        lst=[]
        lst2=[]
        lst3=[]
        while(l1!=0):
            row1.append('r1')
            l1-=1
        while(l2!=0):
            row2.append('r2')
            l2-=1
        while(l3!=0):
            row3.append('r3')
            l3-=1
        p_text_str=list(p_text)
        cipher1=""
        cipher2=""
        cipher3=""
        while lt<len(p_text):
            lst.append(lt)
            lt+=4
        while lt2<len(p_text):
            lst2.append(lt2)
            lt2+=2
        while lt3<len(p_text):
            lst3.append(lt3)
            lt3+=4
        for pos,value in enumerate(p_text_str):
            if pos in lst:
                row1[pos]=value
            if pos in lst2:
                row2[pos]=value
            if pos in lst3:
                row3[pos]=value
        for i in row1:
            if i!="r1":
                cipher1+=i
        for i in row2:
            if i!="r2":
                cipher2+=i
        for i in row3:
            if i!="r3":
                cipher3+=i
        cipher_text=cipher1+cipher2+cipher3
        return cipher_text
    return cipher_text

plain_text=input("Enter PlainText: ")
key=int(input("Enter Key [2-3]:"))
print(f"The CipherText of {plain_text} is {encoding(plain_text,key)}")