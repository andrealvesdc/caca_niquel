import sys
import time
def exibir_resultado(resultado,s1,s2,s3):
    if "win" in sys.platform:
        import winsound
        winsound.PlaySound("SBT.wav", winsound.SND_ASYNC+0)
    if resultado=="trinca":
        print("sorteando...")
        time.sleep(7)
        print(s1)
        time.sleep(7)
        print(st2)
        time.sleep(7)
        print(st3)
        time.sleep(2)
        print("")
        print("-----RESULTADO-----")
        print("   ",s1, s2, s3,"  ")
        print("-------------------")
        print("")        

    elif resultado=="trincabonuscifrão":
        print("sorteando...")
        time.sleep(7)
        print(s1)
        time.sleep(7)
        print(s2)
        time.sleep(7)
        print(s3)
        time.sleep(2)
        print("")
        print("-----RESULTADO-----")
        print("   ",s1, s2, s3,"  ")
        print("-------------------")
        print("")

    elif resultado=="par":
        print("sorteando...")
        time.sleep(7)
        print(s1)
        time.sleep(7)
        print(s2)
        time.sleep(7)
        print(s3)
        time.sleep(2)
        print("")
        print("-----RESULTADO-----")
        print("   ",s1, s2, s3,"  ")
        print("-------------------")
        print("")

    elif resultado=="parbonuscifrão":
        print("sorteando...")
        time.sleep(7)
        print(s1)
        time.sleep(7)
        print(s2)
        time.sleep(7)
        print(s3)
        time.sleep(2)
        print("")
        print("-----RESULTADO-----")
        print("   ",s1, s2, s3,"  ")
        print("-------------------")
        print("")                

    elif resultado=="cifrão":
        print("sorteando...")
        time.sleep(7)
        print(s1)
        time.sleep(7)
        print(s2)
        time.sleep(7)
        print(s3)
        time.sleep(2)
        print("")
        print("-----RESULTADO-----")
        print("   ",s1, s2, s3,"  ")
        print("-------------------")
        print("")

    elif resultado=="perdeu":
        print("sorteando...")
        time.sleep(7)
        print(s1)
        time.sleep(7)
        print(s2)
        time.sleep(7)
        print(s3)
        time.sleep(2)
        print("")
        print("-----RESULTADO-----")
        print("   ",s1, s2, s3,"  ")
        print("-------------------")
        print("")

    
