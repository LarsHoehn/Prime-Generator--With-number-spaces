whoareu="-"
banner2=""" (   (    (( (   (   (  (   ( (  (           )   (( ((   
 )\  )\   ))\)\: )\  )\ )\  )\)\ )\         ()) (\()))\  
((_)((_)(((_)(_)((_)((_)_()(_)(_)(_)       (())))(_)(_)))"""

Banner1= """| _ \ _ \_ _|  \/  |_  /   \ || | |        / __| __| \| |
|  _/   /| || |\/| |/ /| - | __ | |__     | (_ | _|| .  |
|_| |_|_\___|_|  |_|___|_|_|_||_|____|     \___|___|_|\_|"""


def Main():
     global y
     global x
     global whoareu
     global Argument
     global Print
     for start in range(1):
          
                        try:

                           import colorama  
                           colorama.init()
                           from colorama import Fore, Back, Style
                           import os
                           
                        except:
                            print("imports gone wrong")
                            break
                        if "known" in whoareu:
                              os.system('cls')
                              print(Fore.RED+ "ur start need to be lower than ur end :(")
                              print(Style.RESET_ALL)
                        whoareu="known"
                        Argument="-"
                        print(Fore.RED+ banner2)
                        print(Fore.GREEN+ Banner1)
                       

                        print(Fore.MAGENTA+ "                     <<--fmAcvg-->>")
                        Prime= []
                        NotPrime=[]
                        number= []
                        x=2
                        y=1
                        input1=input("What number do u want to start?? ==> ")
                        input1=int(input1)
                        while int(input1)>x:
                            x=input1+1
                        input2=input("What number do u want to end?? ==> ")
                        y=1
                        input2=int(input2)
                        def Try():
                                global Argument
                                if input1>input2:
                                    global Argument
                                    Argument="Wrong"
                                    Main()
                        Try()
                        def findprime():
                            global x
                            global y
                            global Print
                            while x<input2:
                                    y=y+1
                                    x=x+1
                                    number.append(y)
                                    submit=False
                                    listlengh= len(number)
                                    for i in range(listlengh):
                                                    divisor= int(number[i])
                                                    if x % divisor == 0:
                                                        submit=True
                                                        break
                                                        
                                                    else:
                                                        pass
                                    if submit==False:
                                        Print=str(x)
                                        print(Fore.GREEN+ 'foundnumber'+ Print)
                                        Prime.append(x)

                                    else:
                                        Print=str(x)
                                        NotPrime.append(x)
                                        print(Fore.RED+ 'Wrong'+ Print)

                        if "Wrong" in Argument:
                            pass
                        else: 
                                findprime()
                                print(Fore.CYAN+ '**----------------------------------------Finish----------------------------------------**')
                                print(Fore.RED +'NonPrimes==      '+str(NotPrime))
                                print(Fore.GREEN +'Primes==      '+str(Prime))

            

Main()
