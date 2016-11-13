from random import randint
import sys
import csvlib.filehandler as csv


def menu():

    nbr_of_names = 0
    members = []
    c = ""

    while (c != "c") and (c != "f"):
        try:
            c = input("Input names from (c)ommand line or read from csv (f)ile?")
        except ValueError:
            print("Wrong input type.")
            print("Please enter correct datatype.")
            menu()
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
    try:
        #read from cmd
        if c == "c":
            nbr_of_names, members = read_members_from_console()
            #read from csv file
        else:
            p = input("Path to csv file (include .csv): ")
            nbr_of_names, members = csv.read_csv_file(p)


        print(nbr_of_names, "items/members read;")
        print(members)
        
        #randomized members (of original)
        randomized = randomize_list(members)

    
        #nbr of groups/teams
        nbr_of_groups = int(input("How many groups? "))

        print("People in each group:", (round(nbr_of_names//nbr_of_groups, 0)))
        odd_count = nbr_of_names%nbr_of_groups
        print(odd_count, "members will be put in other group(s).")

        create_groups_of_list(randomized, nbr_of_groups)
    except ValueError:
        print("Wrong input type.")
        print("Please enter correct datatype.")
        menu()
    except OSError as err:
        print("OS error: {0}".format(err))
        print("Please enter correct filename.")
        menu()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise



def read_members_from_console():
    """
    input members into list from stdin, via input
    """
    
    #nbr of total members/people
    nbr_of_names = int(input("How many people? "))

    #read all members
    members = []
    i = 0
    while i < nbr_of_names:
        members.append(input("Enter name (" + str((i+1)) + " of " + str(nbr_of_names) + "): "))
        i += 1
    return nbr_of_names, members


def randomize_list(members):
    #randomize members
    randomized = []
    while len(members) > 0:
        randomized.append(members.pop(randint(0, ((len(members)-1)))))

    print("Randomized members:", randomized)
    return randomized


    
def create_groups_of_list(member_list, nbr_of_groups):
    """
    divides a list into groups of lists.
    member_list - a list containing items
    nbr_of_groups - divide the above list into several lists with original list items in it
    returns - list with sublists
    """
    #teams/groups
    groups = []
    #calculate how many members in each team
    m_each_group = round(len(member_list) // nbr_of_groups, 0)
    #if uneaven, how many of those needs to be spread out over the teams
    odd_count = len(member_list) % nbr_of_groups
    
    start = 0 #start-index for each team
    end = m_each_group #end-index for each team
    odd_start_index = end #first index of uneven members
    for i in range(nbr_of_groups):
        print("Making slice from", start, "to", end)
        groups.insert(i, member_list[start:end])
        print("Finished round", i)
        start += m_each_group
        end += m_each_group
        odd_start_index = end - m_each_group

    print("Persons left index:", odd_start_index)
    
    # odd ones - must be distributed over existing groups
    odd_members = member_list[odd_start_index:len(member_list)]
    print("Odds:", odd_members)                     

    if len(odd_members) > 0:
        for i in range(odd_count):
            groups[i].append(member_list.pop())


    #Output constructed groups;
    print("\n")
    
    gi = 1
    for g in groups:
        print("GROUP", gi, "\n----------")
        gm = 1
        for s in g:
            print(gm, s)
            gm += 1
        print("-----------\n")
        gi += 1
            
    #print(groups)

#if run directly in terminal.
#ok to import this script.
if __name__=="__main__":
    menu()
