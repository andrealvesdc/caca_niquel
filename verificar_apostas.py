def verificar(s1,s2,s3,tipo,ap):
    if(s1==s2) and (s2==s3) and (tipo=='trinca'):
        if(s1==ap[6])and(s2==ap[6])and(s3==ap[6]):
            return "trincabonuscifrão"
        elif(s1==ap[7])and(s2==ap[7])and(s3==ap[7]):
            return "trincabonusestrela"
        else:
            return "trinca"
                
    elif(s1==s2) and (tipo=='par'):
        if(s1==s2) and (s3==ap[6]):
            return "parbonuscifrão"
        elif(s1==s2) and (s3==ap[7]):
            return "parbonusestrela"
        else:
            return "par"
              
    elif(s1==s3) and (tipo=='par'):
        if(s1==s3) and (s2==ap[6]):
            return "parbonuscifrão"
        elif(s1==s3) and (s2==ap[7]):
            return "parbonusestrela"
        else:
            return "par"
                
    elif(s2==s3) and (tipo=='par'):
        if(s2==s3) and (s1==ap[6]):
            return "parbonuscifrão"
        elif(s2==s3) and (s1==ap[7]):
            return "parbonusestrela"
        else:
            return "par"
                
    elif(s1==ap[6]) or (s2==ap[6]) or (s3==ap[6]):
        return "cifrão"
                          
    elif(s1==ap[7]) or (s2==ap[7]) or (s3==ap[7]):                              
        return "estrela"
                          
    
    elif(s1!=s2)and(s2!=s3)and(s1!=s3):
        return "perdeu"
