a = " abcdefghijklmnopqrstuvwxyz"
b = " abcdefghijklmnopqrstuvwxyz"
ciphers = [0xAEDE0273C4C0DA3477F919018A05DA71A2530F5A0020E4E0ACA80FF2DE,0xA8C80426C2DEC16D31F90D1497129475A45447561D74EEF1B8BF0FFCDC ,0xA9D30426D3C7CB202EB8050E9717C734A5484A13126CE0FDABA212FBDF
     ,0xB49B166FDAC58E2A25F90A159914D134B84E0F551677A7FFB6A512FBC1 , 0xB49B126ED7C5C26D20EA07149D40C771B2555D565373E8F4ADBC07E1D7, 0xB3DE1763C489DC2822EB0B40970ED134A54942565370E6F6F9A003EAC1]


def xorHEX(h1,h2):
    xored = (h1 ^ h2)
    return "{0:0{1}x}".format(xored, 58)

def sxor(s1, s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))
for targetCipher in ciphers:
    for iteratingCipher in ciphers:
        cipherXored = xorHEX(targetCipher,iteratingCipher)
        cipherXored = [cipherXored[i:i+2] for i in range(0, len(cipherXored), 2)]
        #print(cipherXored)
        brokenCipher = [None]*25
        index =0
        for xor in cipherXored:
            for firstAlpha in a:
                for secondAlpha in b:
                        if ((hex (ord(sxor(firstAlpha,secondAlpha))) == ('0x'+xor)) and ((" "in firstAlpha)or " " in secondAlpha)):
                            brokenCipher[index] = (firstAlpha + secondAlpha).strip()
                            #print( firstAlpha + secondAlpha)
                            if firstAlpha == " " and secondAlpha == " ":
                                brokenCipher[index] = " "

                            #print( firstAlpha + secondAlpha + " " + str(index) + " "  + xor)
            index+=1
        print(brokenCipher)
    print("end of cipher breaking")






