# Evangelos Kontopantelis, Ivan Olier, Claire Planner, David Reeves, Darren M Ashcroft, Linda Gask, Tim Doran, Sioban Reilly, 2023.

import sys, csv, re

codes = [{"code":"N05zA00","system":"readv2"},{"code":"N05zB00","system":"readv2"},{"code":"N05zD00","system":"readv2"},{"code":"N05zF00","system":"readv2"},{"code":"N05zK00","system":"readv2"},{"code":"N05zM00","system":"readv2"},{"code":"N05zP00","system":"readv2"},{"code":"N05zQ00","system":"readv2"},{"code":"N05zS00","system":"readv2"},{"code":"N05zT00","system":"readv2"},{"code":"N05zU00","system":"readv2"},{"code":"7130AC","system":"oxmis"},{"code":"7130EA","system":"oxmis"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('osteoarthritis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["osteoarthritis-joint---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["osteoarthritis-joint---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["osteoarthritis-joint---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
