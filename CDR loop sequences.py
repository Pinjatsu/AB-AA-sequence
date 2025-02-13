kabat_sequence=open('kabat_input.txt','r')
martin_sequence=open('martin_input.txt','r')
chothia_sequence=open('chothia_input.txt','r')
CDR_loop_kabat_H1 = ["H31 ", "H32 ", "H33 ", "H34 ", "H35 ", "H35A ", "H35B "]
CDR_loop_martin_H1 = ["H26 ", "H27 ", "H28 ", "H29 ", "H30 ", "H31 ", "H31A ", "H31B ", "H32 ", "H33 ", "H34 ", "H35 "]
CDR_loop_chothia_H1 = ["H26 ", "H27 ", "H28 ", "H29 ", "H30 ", "H31 ", "H31A ", "H31B ", "H32 "]

CDR_loop_kabat_H2 = ["H50 ", "H51 ", "H52 ", "H53 ", "H54 ", "H55 ", "H56 ", "H57 ", "H58 ", "H59 ", "H60 ", "H61 ", "H62 ", "H63 ", "H64 ", "H65 "]
CDR_loop_martin_H2 = ["H50 ", "H51 ", "H52 ", "H53 ", "H54 ", "H55 ", "H56 ", "H57 ", "H58 "]
CDR_loop_chothia_H2 = ["H52 ", "H53 ", "H54 ", "H55 ", "H56 "]

CDR_loop_H3 = ["H95 ", "H96 ", "H97 ", "H98 ", "H99 ", "H100 ", "H100A ", "H100B ", "H101 ", "H102 "]

def find_amino_acid(line, CDR_loop):
    for amino_acid in CDR_loop:
        if line.find(amino_acid) != -1:
            poista_nimi = line.replace(amino_acid, '')
            poista_enter = poista_nimi.replace('\n', '')
            return poista_enter
        
def find_kabat(input):
    kabat_H1 = ""
    kabat_H2 = ""
    H3 = ""
    lines = input.readlines()
    for line in lines:
        if find_amino_acid(line, CDR_loop_kabat_H1) != None:
            kabat_H1 += find_amino_acid(line, CDR_loop_kabat_H1)
        if find_amino_acid(line, CDR_loop_kabat_H2) != None:
            kabat_H2 += find_amino_acid(line, CDR_loop_kabat_H2)
        if find_amino_acid(line, CDR_loop_H3) != None:
            H3 += find_amino_acid(line, CDR_loop_H3)
    print("\nKabat\nH1 loop: \n", kabat_H1, "\nH2 loop: \n", kabat_H2, "\nH3 loop: \n", H3 , "\n")
   
def find_martin(input):
    martin_H1 = ""
    martin_H2 = ""
    H3 = ""
    lines = input.readlines()
    for line in lines:
        if find_amino_acid(line, CDR_loop_martin_H1) != None:
            martin_H1 += find_amino_acid(line, CDR_loop_martin_H1)
        if find_amino_acid(line, CDR_loop_martin_H2) != None:
            martin_H2 += find_amino_acid(line, CDR_loop_martin_H2)
        if find_amino_acid(line, CDR_loop_H3) != None:
            H3 += find_amino_acid(line, CDR_loop_H3)
    print("\nMartin\nH1 loop: \n", martin_H1, "\nH2 loop: \n", martin_H2, "\nH3 loop: \n", H3 , "\n")

def find_chothia(input):
    chothia_H1 = ""
    chothia_H2 = ""
    H3 = ""
    lines = input.readlines()
    for line in lines:
        if find_amino_acid(line, CDR_loop_chothia_H1) != None:
            chothia_H1 += find_amino_acid(line, CDR_loop_chothia_H1)
        if find_amino_acid(line, CDR_loop_chothia_H2) != None:
            chothia_H2 += find_amino_acid(line, CDR_loop_chothia_H2)
        if find_amino_acid(line, CDR_loop_H3) != None:
            H3 += find_amino_acid(line, CDR_loop_H3)
    print("\nChothia\nH1 loop: \n", chothia_H1, "\nH2 loop: \n", chothia_H2, "\nH3 loop: \n", H3 , "\n")

find_kabat(kabat_sequence)
find_martin(martin_sequence)
find_chothia(chothia_sequence)