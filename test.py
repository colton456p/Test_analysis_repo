
def main():
    text = """
    # Weekly Team Log

    ## Date Range:

    - June 14th 2024 - June 24th 2024

    ## Features in the Project Plan Cycle:

    - Great addings
    - Front end 
    - Backend
    - Tailwind
    - docker

    ## Associated Tasks from Project Board:

    | Task ID | Description        | Feature   | Assigned To | Status   |
    | ------- | ------------------ | --------- | ----------- | -------- |
    | 1   | Make something so great that you'll love it | 1| colton  | done |
    | 2   | fantastic description | 1| colton  | in progress |


    ## Tasks for Next Cycle:

    | Task ID | Description        | Estimated Time (hrs) | Assigned To |
    | ------- | ------------------ | -------------------- | ----------- |
    | 1   | fantastic description | 5     | colton  |
    | 2  | fantastic description | 5    | colton  |


    ## Burn-up Chart (Velocity):

    - ![docs/weekly logs/Burn Up Charts/[Burn Up Chart Image]](path/to/burnupchart.png)


    ## Completed Tasks:

    | Task ID | Description        | Completed By |
    | ------- | ------------------ | ------------ |
    | 1  | fantastic description  | Colton   |
    | 2   | fantastic description  | Colton   |

    ## In Progress Tasks/ To do:

    | Task ID | Description        | Assigned To |
    | ------- | ------------------ | ----------- |
    | 1   | fantastic description  | Colton |
    | 2   | fantastic description  | Colton  |

    ## Test Report / Testing Status:

    N/A

    ## Overview:

    The team focused on [Summary of work done]. The Kanban Board has been populated with user stories and tasks, milestones have been added, and the dashboard visuals creation has been completed. The next cycle will focus on [Tasks for the next cycle].

    """
    
    list_of_parsable_text = ["## Date Range:", 
                             "## Features in the Project Plan Cycle:", 
                             "## Associated Tasks from Project Board:", 
                             "## Tasks for Next Cycle:",
                             "## Burn-up Chart (Velocity):",
                             "## Completed Tasks:",
                             "## In Progress Tasks/ To do:",
                             "## Test Report / Testing Status:",
                             "## Overview:",
                             ]
    count_inclusions = len(list_of_parsable_text)
    
    for item in list_of_parsable_text:
        if item in text:
            count_inclusions -= 1
    if count_inclusions == 0:
        print("All items are present")
        
        # Parse date range
        sections = text.split(list_of_parsable_text[0])
        date_range = sections[1].strip().split("\n")[0]
        date_range = date_range[1:].strip(" - ")
        print("Date Ranges: ", date_range)
        
        # parse feautures
        
        sections = text.split(list_of_parsable_text[1])
        features = sections[1].strip().split("\n")
        feature_list = []
        template_features = ["[Feature 1]", "[Feature 2]", "[Feature 3]", "[Feature 4]", "[Feature 5]"]
        for feature in features:
            feature = feature.strip()
            if feature != list_of_parsable_text[2]:
                feature = feature.strip(" - ")
                if feature not in template_features and feature != "":
                    feature_list.append(feature)
            else:
                break
            
        print("Implemented features: ", feature_list)
        
        # Parse testing
        sections = text.split(list_of_parsable_text[7])
        
        testing = sections[1].strip().split("\n")
        
        for test in testing:
            test = test.strip()
            lines_referencing_testing = 0
            if test != list_of_parsable_text[8]:
                test = test.strip(" - ")
                if test != "" and test != "N/A":
                    lines_referencing_testing +=1     
            else:
                break
        if lines_referencing_testing == 0:
            print("No mention of testing")
        else:
            print("Testing added to report")
            
        template_overview_str ="The team focused on [Summary of work done]. The Kanban Board has been populated with user stories and tasks, milestones have been added, and the dashboard visuals creation has been completed. The next cycle will focus on [Tasks for the next cycle]."
            
        # Parse overview
        sections = text.split(list_of_parsable_text[8])
        overview = sections[1].strip().split("\n")[0]
        if overview == template_overview_str:
            print("Overview not added")
        elif overview.length() > 0:
            print("Overview added to report")
        
    else:
        print(f"There are {count_inclusions} items missing from the log report.")
        
    
            
        
    
    
    
    


if __name__ == "__main__":
    main()