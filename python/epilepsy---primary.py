# Siobhan Reilly, Ivan Olier, Claire Planner, Tim Doran, David Reeves, Darren M Ashcroft, Linda Gask, Evangelos Kontopantelis, 2023.

import sys, csv, re

codes = [{"code":"667B.00","system":"readv2"},{"code":"F25..00","system":"readv2"},{"code":"F254000","system":"readv2"},{"code":"F254200","system":"readv2"},{"code":"F254300","system":"readv2"},{"code":"F255100","system":"readv2"},{"code":"F255200","system":"readv2"},{"code":"F255500","system":"readv2"},{"code":"F257.00","system":"readv2"},{"code":"F25D.00","system":"readv2"},{"code":"F25E.00","system":"readv2"},{"code":"F25F.00","system":"readv2"},{"code":"F25y000","system":"readv2"},{"code":"F25y100","system":"readv2"},{"code":"F25y400","system":"readv2"},{"code":"F25z.00","system":"readv2"},{"code":"SC20000","system":"readv2"},{"code":"2932","system":"oxmis"},{"code":"3032EP","system":"oxmis"},{"code":"342 E","system":"oxmis"},{"code":"3450","system":"oxmis"},{"code":"3451","system":"oxmis"},{"code":"3453AT","system":"oxmis"},{"code":"3453P","system":"oxmis"},{"code":"3453T","system":"oxmis"},{"code":"3459A","system":"oxmis"},{"code":"3459AB","system":"oxmis"},{"code":"3459BA","system":"oxmis"},{"code":"3459D","system":"oxmis"},{"code":"3459N","system":"oxmis"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('epilepsy-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["epilepsy---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["epilepsy---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["epilepsy---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
