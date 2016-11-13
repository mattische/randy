import csv

def read_csv_file(path, delim=","):
    """
    extension should be .csv
    delim: delimiter; either comma-separated "," or tab "\t" values.
    """
    with open(path, 'r') as my_file:
            reader = csv.reader(my_file, delimiter=delim)
            my_list = list(reader)

    members = []
    for l in my_list:
        for p in l:
            members.append(p.strip(" ")) #strip whitespace

    return len(members), members


def save_list_to_csv(path, members, delim=","):
    """
    save a list() to csv-file. Each item is saved as comma-separated values.
    path - filename to save, extension should be .csv
    members - a list()
    delim - comma-separated values. Other possible values is \t (tab-separated values)
    """
    # write list to CSV file, it works!
    with open(path, 'w') as outfile:
            writer = csv.writer(outfile, delimiter=delim)
            writer.writerow(members)
