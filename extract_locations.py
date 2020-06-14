# 


# extract all the text from the disarrayed file
# split each time the key text (see below) appears
# ('jsan="7.title">')


with open("locations.txt", "r") as f_in:

    # tag that prefixes every instance of a location's html section
    # is used to seperate (and isolate) each name into seperate indexes
    split_contents = f_in.read().split("jsan=\"7.title\">")

    # the header element doesnt contain any locations
    split_contents.pop(0)

    # is used to store each scanned name
    location_name_list = []

    # isolating the location names from any other text
    for i in split_contents:
        extraction_list = i.split(">")
        
        # removes the trailing characters of each extraction_list[index]
        # to leave just the name
        location_name_list.append(extraction_list[0][:-5])

    # used to convert the location_name_list into a pseudo-set
    final_list_ordered = []

    # remove duplicates while retaining order (unlike the set() method)
    # the set method removes duplicates however it removes
    # them chronologically, so the 'time spent' measure may not
    # be conserved in the final file
    for i in range(0, len(location_name_list)):
        if location_name_list[i] not in final_list_ordered:
            final_list_ordered.append(location_name_list[i])
            
    with open("visited_locations.txt", "w") as f_out:
        for i in final_list_ordered:
            f_out.write(i + "\n")
    

