def roman_to_int(roman):
    romains={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    integer=0
    i=0
    while i<len(roman):
        if i+1<len(roman) and romains[roman[i]]<romains[roman[i+1]]:
            integer+=romains[roman[i+1]]-romains[roman[i]]
            i+=2
        else:
            integer+=romains[roman[i]]
            i+=1
    return integer

if __name__=="__main__":
    roman=input("Enter  the roman number:   ")
    print(roman_to_int(roman))