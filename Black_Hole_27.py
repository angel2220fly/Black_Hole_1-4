import os  
from time import time
import binascii
import math
import os.path
long_1=0
name=""
add_bits=""
Make_togher=""


name_input = input("c,  compress or e, extract? ")
#@Author Jurijus Pacalovas
class compression:
        def cryptograpy_compression4(self):
              
               


               

                def Count_adds(M1,En,En1,En3,En4, En6, En7, En8, En9, En10, En11, En12, En13, En14, En15, En16, En17, En18, En19, En20, En21, En22, En23, En24, En25, En26, En27, En28, En29, En30, En31, En32, En33, En34, En35, En36, En37, En38, En39, En40, En41):
                        if M1==0:
                                En-=1
                                                                             

                        if En == 10 or M1 == 1:
                            En += 1
                            M1 = 1
                        
                        if En == 8191:
                            En1 += 1
                            # print(En1)
                            M1 = 0
                            En = 255
                        

                        if En1 == 15:
                            En = 255
                            En1 = 0
                            M1 = 0
                            En3 += 1
                        
                        counters = [En3, En4, En6, En7, En8, En9, En10, En11, En12, En13, En14, En15, En16, En17, En18, En19, En20, En21, En22, En23, En24, En25, En26, En27, En28, En29, En30, En31, En32, En33, En34, En35, En36, En37, En38, En39, En40, En41]
                        
                        for i in range(len(counters)):
                            if counters[i] == 15:
                                counters[i] = 1
                                if i + 1 < len(counters):
                                    counters[i + 1] += 1
                        
                        En3, En4, En6, En7, En8, En9, En10, En11, En12, En13, En14, En15, En16, En17, En18, En19, En20, En21, En22, En23, En24, En25, En26, En27, En28, En29, En30, En31, En32, En33, En34, En35, En36, En37, En38, En39, En40, En41 = counters

                  
                        
                        
                        return M1,En,En1,En3,En4, En6, En7, En8, En9, En10, En11, En12, En13, En14, En15, En16, En17, En18, En19, En20, En21, En22, En23, En24, En25, En26, En27, En28, En29, En30, En31, En32, En33, En34, En35, En36, En37, En38, En39, En40, En41
                



        




  







                  
                
  
                

                                     
                  
                                                                      
                                   
                        

                self.name = "Written: Jurijus pacalovas"
                if name_input!="c" and name_input!="e":
                        print("The wrong letter")
                        raise SystemExit
                if name_input=="c" or name_input=="e":        
                    if name_input=="c":
                        i=1
                    if name_input=="e":
                      
                        i=2
                    Clear=""
                    name = input("What is name of file input? ")
                    name_output= input("What is name of file output? ")

                        
    
                 
               
                       
                    Key = 1
                    level = 2
                    L=40
                    
                    
        
                    
                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                    x=0
                    C1=1
                    x1=0
                    x2=0
                    x3=0
                    X2=0
                    C1=0
                    C2=0
                    C3=0
                    C4=0
                    C5=0
                    n=0
                    x = time()
                    File_information6_Times2_1=0
                    name_2=name
                    Long_Change=len(name_2)
                    compress_or_not_compress=1
                    File_information6_Times3=0
                    if i==2:
                        C=1
                    Long_Change=len(name_2)
                    s=""
                    File_information5=""
                    File_information5_2=""
                    Clear=""
                    Translate_info_Decimal=""
                    D=0
                    long_name=len(name)
           
                    with open(name, "rb") as binary_file:
                        data = binary_file.read()

                        s=str(data)
                        long_11=len(data)
                        long_17=len(data)
                        if long_17==0:
                        	 raise SystemExit
                        END_working=0
                        File_information6_Times2=0
                        File_information5_23=""
                        INFO18=""
                        File_information5_29=""
                        SpinS=0
                        while END_working<10:
                            File_information6_Times3=File_information6_Times3+1
                            D=1
                            if D==1:
                                if File_information6_Times3==1:
                                    INFO=bin(int(binascii.hexlify(data),16))[2:]#data to binary
                                    long_1=len(INFO)
                                    long_11=len(data)
                                    count_bits=(long_11*8)-long_1
                                    z=0
                                    if count_bits!=0:
                                        while z<count_bits:
                                            INFO="0"+INFO
                                            z=z+1
                                    if File_information6_Times3==1:
                                        File_information5_2=INFO
                                    n = int(File_information5_2, 2)
                                    width_bits=len(File_information5_2)
                                    width_bits=(width_bits/8)*2
                                    width_bits=str(width_bits)
                                    width_bits="%0"+width_bits+"x"
                                    width_bits3=binascii.unhexlify(width_bits % n)                                    
                                    width_bits2=len(width_bits3)
                                    data=width_bits3
                                    long_15=len(data)
                                    INFO=bin(int(binascii.hexlify(data),16))[2:]
                                    long_1=len(INFO)
                                    long_11=len(data)
                                    count_bits=(long_11*8)-long_1
                                    z=0
                                    if count_bits!=0:
                                        while z<count_bits:
                                            INFO="0"+INFO
                                            z=z+1
                                    File_information5_2=INFO
                                    Extact=File_information5_2
                                    A=int(Extact,2)                                    
                                
                                        
                                    long_13=len(File_information5_2)
                                long_12=len(File_information5_2)
                                if i==1:
                                    if long_17>=(2**26)-1 and i==1:
                                        print("print file is too big!")
                                        raise SystemExit

                                if i==1:
                                   

                                             
                                                Ex=1
                                                if Ex==1:
                                                

                                                    Extract1=0
                                                    Find=0
                                                    En=255
                                                    Ci=1
                                                    M1=0
                                                    En1=0
                                                    input_string=""
                                                    C1=""
                                                    En3=2
                                                    En4=2
                                                    I4=INFO# reverse
                                                    En6=En7=En8=En9=En10=En11=En12=En13=En14=En15=En16=En17=En18=En19=En20=En21=En22=En23=En24=En25=En26=En27=En28=En29=En30=En31=En32=En33=En34=En35=En36=En37=En38=En39=En40=En41=2



                                                    while Find!=1:


# Continue until En41
                                                                    M1, En, En1, En3, En4, En6, En7, En8, En9, En10, En11, En12, En13, En14, En15, En16, En17, En18, En19, En20, En21, En22, En23, En24, En25, En26, En27, En28, En29, En30, En31, En32, En33, En34, En35, En36, En37, En38, En39, En40, En41 = Count_adds(M1, En, En1, En3, En4, En6, En7, En8, En9, En10, En11, En12, En13, En14, En15, En16, En17, En18, En19, En20, En21, En22, En23, En24, En25, En26, En27, En28, En29, En30, En31, En32, En33, En34, En35, En36, En37, En38, En39, En40, En41)



                                                                    I2 = I4
                                                                    I3 = len(INFO)
                                                                    I5 = ""
                                                                    # print(I3)
                                                                    En5 = -1
                                                                    bi = 0
                                                                    
                                                                    reverse_indices = {
                                                                        37: En3, 36: En4, 35: En6, 34: En7, 33: En8, 32: En9, 31: En10,
                                                                        30: En11, 29: En12, 28: En13, 27: En14, 26: En15, 25: En16, 24: En17,
                                                                        23: En18, 22: En19, 21: En20, 20: En21, 19: En22, 18: En23, 17: En24,
                                                                        16: En25, 15: En26, 14: En27, 13: En28, 12: En29, 11: En30, 10: En31,
                                                                        9: En32, 8: En33, 7: En34, 6: En35, 5: En36, 4: En37, 3: En38, 2: En39,
                                                                        1: En40, 0: En41
                                                                    }
                                                                    
                                                                    while bi < I3:
                                                                        En5 += 1
                                                                        if En5 == 38:
                                                                            En5 = 0
                                                                    
                                                                        if En5 in reverse_indices:
                                                                            slice_length = reverse_indices[En5]
                                                                            if bi + slice_length <= I3:
                                                                                I = I2[bi:bi + slice_length]
                                                                                I6 = I[::-1]
                                                                                bi += slice_length
                                                                                I5 += I6
                                                                    
                                                                    INFO = I5

                                                                    #print(INFO)
                                                                 
                    
                                                                    Z4=""
                                                                    N3=0                                                                    
                                                                    long_F=len(INFO)
                                                                    block=0
                                                                    
                                                                    
                                                                    while block<long_F:
                                                                        INFO_A=INFO[block:block+En]
                                                                        if En1!=0:
                                                                                INFO_A1=INFO[block+En:block+En+En1]
                                                                        longl=len(INFO_A)
                                                                        
                                                                        Counts=int(INFO_A,2)
                                                                        C=format(Counts,'01b')
                                                                        C3=En-len(C)
                                                                        #print(C1)
                                                                        if C3>=4+3 and En<=15 or C3>=5+3 and En<=31 or C3>=6 +3 and En<=63 or C3>=7+3 and En<=127 or C3>=8+3 and En<=255 or C3>=9+3 and En<=511 or C3>=10+3 and En<=1023 or C3>=11+3 and En<=2047 or C3>=12+3 and En<=4095 or C3>=13+3 and En<=8191 or INFO_A[:3]=="011" or INFO_A[:3]=="010":
                                                                            
    
                                                                                #print(C3)
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                     
    
                                                                                      
                                                                            
                                                                          
                                                                             
    
                                                                              
                                                                             
                                                                                
                                                                            Counts=int(INFO_A,2)
                                                                            C=format(Counts,'01b')
                                                                            C4=En-len(C)
                                                                            if En<=15:
                                                                                C1=format(C4,'04b')
                                                                                
                                                                                
                                                                            elif En<=31:
                                                                                C1=format(C4,'05b')
                                                                                
                                                                            elif En<=63:
                                                                                C1=format(C4,'06b')                                                                           
                                                                            elif En<=127:
                                                                                C1=format(C4,'07b')                                                                                                                                                                     

                                                                            elif En<=255:
                                                                                C1=format(C4,'08b') 
                                                                                
                                                                            elif En<=511:
                                                                                C1=format(C4,'09b')                                                                                                         
                                                                                
                                                                            elif En<=1023:
                                                                                C1=format(C4,'010b')   
                                                                                
                                                                            elif En<=2047:
                                                                                C1=format(C4,'011b')  
                                                                                
                                                                            elif En<=4095:
                                                                                C1=format(C4,'012b')                                                                                                                                                                                                                                                                        
                                                                            elif En<=8191:
                                                                                C1=format(C4,'013b')                  
                                                                            C2=format(longl,'06b') 
                                                                                                                                                        
    
                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                                                                                   
                                                                                   
                                                                            if C3!=1:
                                                                                   Z5="011"+C1+C
                                                                                   if En1!=0 and block+En1+En<=long_F:
                                                                                           Z5="011"+C1+C+INFO_A1
                                                                                           block+=En1
                                                                                   #print(Z5) 
                                                                                       
                                                                                   
                                                                            if C3==1:
                                                                                   Z5="010"+INFO_A[2:]
                                                                                   #print(Z5)
                                                                                   
                                                                                   
                                                                                   
                                                                                                                                                                                                                                   #print(INFO_A)
                                                                               #print(C1)
                                                                               #print(INFO_A)
                                                                        else:
                                                                        
                                                                               Z5=INFO_A
                                                                               
                                                                               #not six zeros else 7 zeros or more left or 2-5 zeros
                                                                        
                    
                                                                        
                                                                             #change back
                                                                            
                                                                     
                                                                            #same size
                                                                            
                    
                                                                       
                                                                        Z4+=Z5
                                                                        #print(Find)
                                                                        block+=En
                                                                        
                                                               

                                                         
                                                                                               
                                                                    



                                                                              
                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                
                                                                    if len(Z4)+8+(4*40)+8+13+len(C1) < long_11*8 or En41==15:
                                                                                Find=1
                                                                                Extract1=1    
                                                                        #print(len(input_string))
                                                                   
                                                                        
                                                                    
                                                                        
                                                                        
                                                                        

                                                                             #print(input_string)
                                                                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                                                                       

                                                                        
                                                                           
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                    if Ci==1:               
                                                            
                                                           
                                                                N3=1
                                                                                                                 
                                                                

                                                                W="0"+str(len(C1))+"b"
                                                                CL1 = format(longl, W)
                                                                CL2 = format(En, '013b')
                                                                Counts_V=1
                                                                if Counts_V==1:
            
                                                                    counters = [En1, En3, En4, En6, En7, En8, En9, En10, En11, En12, En13, En14, En15, En16, En17, En18, En19, En20, En21, En22, En23, En24, En25, En26, En27, En28, En29, En30, En31, En32, En33, En34, En35, En36, En37, En38, En39, En40, En41]
                                                                    CL_list = [format(counter, '04b') for counter in counters]
                                                                    
                                                                    CL2, CL3, CL4, CL5, CL6, CL7, CL8, CL9, CL10, CL11, CL12, CL13, CL14, CL15, CL16, CL17, CL18, CL19, CL20, CL21, CL22, CL23, CL24, CL25, CL26, CL27, CL28, CL29, CL30, CL31, CL32, CL33, CL34, CL35, CL36, CL37, CL38, CL39, CL40, CL41 = [CL2] + CL_list
                                                                    
                                                                    
                                                                                                                                    
                                                                    
                                                                if N3==1:
                                                                           N3=1                                                                       
                                                                if N3==1:
                                                                               File_information5_17="1"+CL41+CL40+CL39+CL38+CL37+CL36+CL35+CL34+CL33+CL32+CL31+CL30+CL29+CL28+CL27+CL26+CL25+CL24+CL23+CL22+CL21+CL20+CL19+CL18+CL17+CL16+CL15+CL14+CL13+CL12+CL11+CL10+CL9+CL8+CL7+CL6+CL5+CL4+CL3+CL2+CL1+Z4
                                                                               long_1=len(File_information5_17)
                                                                               add_bits=""
                                                                               count_bits=8-long_1%8
                                                                               z=0
                                                                               if count_bits!=0:
                                                                                       while z<count_bits:
                                                                                               add_bits="0"+add_bits
                                                                                               z=z+1
                                                                               File_information5_17=add_bits+File_information5_17                                                                            

                                                                               z=0
                                                                               Extract1=1
                                                                               if Extract1==1:                
                                                                                                                    L=len(File_information5_17)
                                                                                                                    #print(L)
                                                                                                                    n = int(File_information5_17, 2)
                                                                                                                    width_bits=len(File_information5_17)
                                                                                                                    width_bits=(width_bits//8)*2
                                                                                                                    width_bits=str(width_bits)
                                                                                                                    width_bits="%0"+width_bits+"x"
                                                                                                                    width_bits3=binascii.unhexlify(width_bits % n)
                                                                                                                    width_bits2=len(width_bits3)
                                                                                                                    File_information5_2=Clear
                                                                                                                    name=name+".bin"
                                                                                                                    jl=width_bits3
                                                        
                                                                                                           
                                                                                                            
                                                                                                                    with open(name_output, "wb") as f2:
                                                                                                                        f2.write(jl)
                                                                                                                    
                                                                                                                    x2 = time()
                                                                                                                    x3=x2-x
                                                                                                                    xs=float(x3)
                                                                                                                    xs=str(xs)
                                                                                                                    return xs;
                         


                                if i==2:
                                    if C==1:
                                        if   File_information6_Times2==0:
                                            File_information5=INFO
                                        if   File_information6_Times2==0:
                                                long_16=len(File_information5)

                                                if File_information5[:1]=="0":
                                                    while File_information5[:1]!="1":
                                                        if File_information5[:1]=="0":
                                                            File_information5=File_information5[1:]
                                                            
                                                            
                                                if File_information5[:1]=="1":
                                                    File_information5=File_information5[1:]
                                                    


                                                
                                                Extract=File_information5

                                                            
                                    INFO=Extract

                                    En41 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En40 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En39 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En38 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En37 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En36 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En35 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En34 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En33 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En32 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En31 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En30 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En29 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En28 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En27 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En26 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En25 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En24 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En23 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En22 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En21 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En20 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En19 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En18 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En17 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En16 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En15 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En14 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En13 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En12 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En11 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En10 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En9 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En8 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En7 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En6 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En4 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En3 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En2 = int(INFO[:4], 2)
                                    INFO = INFO[4:]
                                    
                                    En = int(INFO[:13], 2)
                                    INFO = INFO[13:]

                                        
                                    #print(En)

                   
                                 

                                    
                                    if En<=15:
                                        longl=int(INFO[:4],2)
                                        #print(longl)
                                        INFO=INFO[4:]
                                        SEN=4     
                                    
                                    elif En<=31:
                                        longl=int(INFO[:5],2)
                                        #print(longl)
                                        INFO=INFO[5:]
                                        SEN=5                                  
                                    elif En<=63:
                                        longl=int(INFO[:6],2)
                                        INFO=INFO[6:]
                                        SEN=6 
                                        
                                    elif En<=127:
                                        longl=int(INFO[:7],2)
                                        INFO=INFO[7:]
                                        SEN=7                                       
                                                                                                                  
                                    elif En<=255:
                                        longl=int(INFO[:8],2) 
                                        INFO=INFO[8:]  
                                        SEN=8                                      
                                                                                
                                                                                                                                                                
                                    elif En<=511:
                                        longl=int(INFO[:9],2) 
                                        INFO=INFO[9:]
                                        SEN=9                                       
                                    elif En<=1023:
                                        longl=int(INFO[:10],2) 
                                        INFO=INFO[10:]
                                        SEN=10                                                                                                                            
                                    elif En<=2047:
                                        longl=int(INFO[:11],2) 
                                        INFO=INFO[11:]
                                        SEN=11                     
     
                                    elif En<=4095:
                                        longl=int(INFO[:12],2) 
                                        INFO=INFO[12:]
                                        SEN=12
                                        
                                        
                                    elif En<=8191:
                                        longl=int(INFO[:13],2) 
                                        INFO=INFO[13:]
                                        SEN=13                                                                                   
                                                                                                                                                                   
                                    
                                    #print(longl)                                    
                                    
                                    Extract1=0

                                    Z4=""
                                    N3=0
                                    
                                    while Extract1!=1:
                                                long_F=len(INFO)
                                                block=0
                                                Save=0
                                                while Save!=1:
                                                      if Save==0:
                                                            C9=0
                                                          
                                                        
                                                            O=INFO[block:block+3]
                                                            
                                                            
                                                            
                                                            if O=="010":
                                                       
                                                                   block+=3
                                                                   OC=INFO[block:block+En-2]
                                                                   E=int(OC,2)
                                                                   En1="0"+str(En-2)+"b"
                                                                   
                                                                   ZE=format(E,En1)
                                                                   C="0"+str(longl-2)+"b"
                                                                   ZE=format(E,En1)
                                                                   Z2Z=format(E,C)
                                                                   ZE="01"+ZE
                                                                   Z2Z="01"+Z2Z
                                                                   block+=En-2                                                                                   

                                                                     
                                                                
                                                                
                                                                
                                                                                                    
                                                            
                                                            elif O=="011":
                                                       
                                                       
                                                                block+=3
                                                                
                                                                if En<=8191:                                                         
                                                                
                                                                    OCl=INFO[block:block+SEN]
                                                                    Size=int(OCl,2)
                                                                    block+=SEN                                                               


                                                                   
                                                                EB=INFO[block:block+(En-Size)]
                                                               
                                                                block+=(En-Size)
                                                                En1="0"+str(En)+"b"
                                                                
                                                             
                                                                E=int(EB,2)
                                                                ZE=format(E,En1)
                                                                C="0"+str(longl)+"b"
                                                                ZE=format(E,En1)
                                                                Z2Z=format(E,C)
                                                                if En2!=0:
                                                                        CAll=0
                                                                        CAll=int(block)+int(En2)
                                                                        if CAll<=long_F:
                                                                            EB1=INFO[block:block+En2]
                                                                            ZE=ZE+EB1
                                                                            block+=En2
                                                                            C9=1
                                                                            
                                                            else:
                                                                   EB=INFO[block:block+En]
                                                                   block+=En
                                                                   En1="0"+str(En)+"b"
                                                                  

                                                                   E=int(EB,2)
                                                                   ZE=format(E,En1)
                                                                   C="0"+str(longl)+"b"
                                                                   ZE=format(E,En1)
                                                                   Z2Z=format(E,C)                                                                                                   
    
                                                            
                                                                                                            
                                                         
                                                    
                                                            Z2=ZE
                                                            #print(Z2)

                                                            Z4+=Z2                                                            
                                                            #print(block)
                                                            #print(long_F)
                                                            if block>=long_F:
                                                                Save=1
                                                                #print(Save)
                                                          

                                                       
                                                                                                                                                                                                            

                                            
                                                #print(Z4)
                                             
                                                
                                                long_L=len(Z4)
                                                #print(long_L)
                                                if C9==0:
                                                    Z4=Z4[:long_L-En]
                                                    Z4+=Z2Z
                                                
                                                    
                                                N3=1
                                                
                                               
                                                #print(N3)
                                                                                                         
                                                if N3==1:
                                                       
                                                       
                                                       
                                                     #print(len(Z4))
                                                       
                                                        INFO = Z4
                                                        bi = 0
                                                        
                                                        I2 = INFO
                                                        I3 = len(INFO)
                                                        I5 = ""
                                                        En5 = -1
                                                        
                                                        reverse_indices = {
                                                            37: En3, 36: En4, 35: En6, 34: En7, 33: En8, 32: En9, 31: En10,
                                                            30: En11, 29: En12, 28: En13, 27: En14, 26: En15, 25: En16, 24: En17,
                                                            23: En18, 22: En19, 21: En20, 20: En21, 19: En22, 18: En23, 17: En24,
                                                            16: En25, 15: En26, 14: En27, 13: En28, 12: En29, 11: En30, 10: En31,
                                                            9: En32, 8: En33, 7: En34, 6: En35, 5: En36, 4: En37, 3: En38, 2: En39,
                                                            1: En40, 0: En41
                                                        }
                                                        
                                                        while bi < I3:
                                                            En5 += 1
                                                            if En5 == 38:
                                                                En5 = 0
                                                        
                                                            if En5 in reverse_indices:
                                                                slice_length = reverse_indices[En5]
                                                                if bi + slice_length <= I3:
                                                                    I = I2[bi:bi + slice_length]
                                                                    I6 = I[::-1]
                                                                    bi += slice_length
                                                                    I5 += I6

                                                     
                                                        Z4 = I5
                                                        N3=1
                                                        N3=1
                                                        if N3==1:
                                                       
                                                     
                                                     #print(len(Z4))
                                                        

                                                               File_information5_17=Z4
                                                               long_1=len(File_information5_17)
                                                               add_bits=""
                                                               count_bits=8-long_1%8
                                                               z=0
                                                               if count_bits!=0:
                                                                       while z<count_bits:
                                                                               add_bits="0"+add_bits
                                                                               z=z+1
                                                               File_information5_17=File_information5_17
                                                               Extract1=1
                                    if Extract1==1:                
                                            L=len(File_information5_17)
                                            n = int(File_information5_17, 2)
                                            width_bits=len(File_information5_17)
                                            width_bits=(width_bits//8)*2
                                            width_bits=str(width_bits)
                                            width_bits="%0"+width_bits+"x"
                                            width_bits3=binascii.unhexlify(width_bits % n)
                                            width_bits2=len(width_bits3)
                                            File_information5_2=Clear
                                         
                                            jl=width_bits3
                                            
                                   
                                           
                                   
                                            
                                            long_extract=len(name)
                                            name=name[:long_extract-4]
                                            
                                            with open(name_output, "wb") as f2:
                                                f2.write(width_bits3)
                                            x2 = time()
                                            x3=x2-x
                                            xs=float(x3)
                                            xs=str(xs)
                                            return xs;                                                           
                                                            
                                                            
d=compression()
xw1=d.cryptograpy_compression4()
print(xw1)