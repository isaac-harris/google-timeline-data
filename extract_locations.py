# extract all the text from the disarrayed file
# split each time the key text (see below) appears
# ('jsan="7.title">')


with open("locations.txt", "r") as fin:
    
    contents = fin.read()

    # tag that predates every instance of a location's name
    split_contents = contents.split("jsan=\"7.title\">")

    # the header element doesnt contain any locations
    split_contents.pop(0)

    final_list = []

    # isolating the location names from any other text
    for i in split_contents:
        extraction_list = i.split(">")
        
        final_list.append(extraction_list[0][:-5])

    final_list_ordered = []

    # remove duplicates while retaining order (unlike the set() method)
    for i in range(0, len(final_list)):
        if final_list[i] not in final_list_ordered:
            final_list_ordered.append(final_list[i])
            
    with open("visited_locations.txt", "w") as fout:
        for i in final_list_ordered:
            fout.write(i + "\n")
    

