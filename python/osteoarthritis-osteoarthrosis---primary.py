# Evangelos Kontopantelis, Ivan Olier, Claire Planner, David Reeves, Darren M Ashcroft, Linda Gask, Tim Doran, Sioban Reilly, 2023.

import sys, csv, re

codes = [{"code":"N050400","system":"readv2"},{"code":"N050600","system":"readv2"},{"code":"7130AA","system":"oxmis"},{"code":"7130AB","system":"oxmis"},{"code":"7130AG","system":"oxmis"},{"code":"7130AW","system":"oxmis"},{"code":"7130B","system":"oxmis"},{"code":"7130C","system":"oxmis"},{"code":"7130CT","system":"oxmis"},{"code":"7130D","system":"oxmis"},{"code":"7130E","system":"oxmis"},{"code":"7130EL","system":"oxmis"},{"code":"7130FT","system":"oxmis"},{"code":"7130H","system":"oxmis"},{"code":"7130MD","system":"oxmis"},{"code":"7130N","system":"oxmis"},{"code":"7131A","system":"oxmis"},{"code":"7131C","system":"oxmis"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('osteoarthritis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["osteoarthritis-osteoarthrosis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["osteoarthritis-osteoarthrosis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["osteoarthritis-osteoarthrosis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
