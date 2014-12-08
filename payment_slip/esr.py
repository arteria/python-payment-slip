"""
Function for generating ESR-numbers for orange swiss payment slips (so called "Oranger Einzahlungsschein").
Ported to Python, based on https://github.com/NicolasZanotti/Swiss-PaymentSlip-Tools/blob/master/esr.js
Thanks

 @author Jason Rubichi, Nicolas Zanotti, Philippe O. Wagner
 @param
    bc "Belegartcodes": fix, "01" or "04"
    chf: dynamic, amount in chf without rappen, must have eight chars minimum (if less than eight chars, insert zeros before)
    rappen: dynamic, amount in rappen
    help1, help2, help3: fix, "+" or ">", no editing required
    referenceNumber: dynamic, contains matag number, zeros, client number and job number
    participantNumber: dynamic, bankaccount number

 @usage generateCodeline("01", "4378", "85", ">", "94476300000000128001105152", "+", "01200027", ">")
 
"""

def moduloTenRecursive(number):
    lut = [0, 9, 4, 6, 8, 2, 7, 1, 3, 5];
    carryover = 0;
    for i in str(number):
        t = carryover + int(i)
        carryover = lut[t % 10];
    return str((10 - carryover) % 10)
    
     
def generateCodeline(bc, chf, rappen, help1, referenceNumber, help2, participantNumber, help3):
    chf = ''
    rappen = ''
    if str(bc) == "01":
        chf = str(chf)
        rappen = str(rappen) 
        if len(chf) < 8:  # check if amount has less than eight chars
            chf = (8-len(chf))*"0" + chf
    elif str(bc) == "04":
        p1 = moduloTenRecursive(bc)
    else:
        raise Exception("Belegart nicht unterstuetzt!")
    # dynamic, check digit for bc and value (calculated with modulo 10 recursive)
    p1 = moduloTenRecursive(bc + chf + rappen)     
    # dynamic, check digit for referenceNumber (calculated with modulo 10 recursive)
    p2 = moduloTenRecursive(referenceNumber)
    # dynamic, check digit for participantNumber (calculated with modulo 10 recursive)
    p3 = moduloTenRecursive(participantNumber)
    return bc + chf + rappen + p1 + help1 + referenceNumber + p2 + help2 + " " + participantNumber + p3 + help3
