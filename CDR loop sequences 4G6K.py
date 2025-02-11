abnum=open('input.txt','r')

def find_kabat(input):
    lines = input.readlines()
    found_amino_acids = []
    for line in lines:
        CDR_loop_H1 = ["H31 ", "H32 ", "H33 ", "H34 ", "H35 ", "H35A ", "H35B "]
        for amino_acid in CDR_loop_H1:
            if line.find(amino_acid) != -1:
                poista_nimi = line.replace(amino_acid, '')
                poista_enter = poista_nimi.replace('\n', '')
                found_amino_acids.append(poista_enter)
    print(''.join(found_amino_acids))

find_kabat(abnum)