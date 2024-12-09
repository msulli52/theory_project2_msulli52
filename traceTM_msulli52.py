import csv
from tabulate import tabulate

# NTM class 
class NTM:

    # initialize NTM 
    def __init__(self, machine_file):
        self.transitions = {}
        self.machine_name = None
        self.start_state = None
        self.accept_state = None
        self.reject_state = None
        self.parse_machine_file(machine_file)

    # parse the input csv file to load the NTM description into memory
    def parse_machine_file(self, machine_file):
        with open(machine_file, 'r') as file:
            reader = csv.reader(file)
            lines = list(reader)
            
            # extract info 
            self.machine_name = lines[0][0]
            self.start_state = lines[4][0]
            self.accept_state = lines[5][0]
            self.reject_state = lines[6][0]

            # process each transition rule and store in the transitions dictionary
            for row in lines[7:]:
                state, char, next_state, write_char, move_dir = row
                if (state, char) not in self.transitions:
                    self.transitions[(state, char)] = [] # create entry 
                self.transitions[(state, char)].append((next_state, write_char, move_dir)) # add transition


    def run(self, input_string, depth_limit):
        # list of lists representing each level of the NTM tree structure
        tree = [[("", self.start_state, input_string)]]
        total_transitions = 0
        accept_found = False
        explored_configurations = 0
        visited = set()
        stop_processing = False
        stopped_due_to_depth_limit = False

        # want to continue simulation while there are configurations in curr level and stop_processing is False
        while tree[-1] and not stop_processing:
            current_level = tree[-1]
            next_level = []
            all_reject = True  # assume all paths lead to reject unless proven otherwise

            # process each configuration in the curr level 
            for left, state, right in current_level:
                config_key = (left, state, right)
                if config_key in visited: # skip configurations already visited
                    continue
                visited.add(config_key)

                explored_configurations += 1

                # check for accept state
                if state == self.accept_state:
                    accept_found = True
                    continue  # don't add further configurations for this path

                # check for reject state
                if state == self.reject_state:
                    continue

                all_reject = False  # if valid transitions found, not all paths reject
                # get char under head of tape 
                head_char = right[0] if right else "_"
                # get possible transitions
                transitions = self.transitions.get((state, head_char), [])

                # if theres no valid transitions, reject
                if not transitions:
                    next_level.append((left, self.reject_state, right))
                    total_transitions += 1
                    continue

                # process all valid transitions for the curr configuration
                for next_state, write_char, move_dir in transitions:
                    total_transitions += 1
                    new_left, new_right = left, right 

                    # update tape with the char to write
                    if right:
                        new_right = write_char + right[1:]
                    else:
                        new_right = write_char

                    # move head left or right
                    # left 
                    if move_dir == "L":
                        if new_left:
                            new_right = new_left[-1] + new_right
                            new_left = new_left[:-1]
                        else:
                            new_right = "_" + new_right
                    # right
                    elif move_dir == "R":
                        if new_right:
                            new_left = new_left + new_right[0]
                            new_right = new_right[1:] if len(new_right) > 1 else "_"
                        else:
                            new_left = new_left + "_"

                    # add new configuration to the next level
                    new_config = (new_left, next_state, new_right)
                    if new_config not in visited:  # Only add unique configurations
                        next_level.append(new_config)

            # stop if depth limit is reached
            if len(tree) >= depth_limit:
                stopped_due_to_depth_limit = True
                break

            # add the next level to the tree
            tree.append(next_level)

            # stop if all paths reject or if no new configurations added
            if all_reject or not next_level:
                stop_processing = True

        # calculate nondeterminism
        nondeterminism = self.calculate_nondeterminism(tree)

        # generate output
        result = self.generate_output(tree, total_transitions, explored_configurations, nondeterminism, accept_found, stopped_due_to_depth_limit, depth_limit)
        return result, accept_found, total_transitions + 1, nondeterminism, tree


    # calculate the nondeterminism (average number of transitions per configuration)
    def calculate_nondeterminism(self, tree):
        nonleaves = 0 # this is the count of configurations with transitions
        total_transitions = 0 # total transitions generated
        for level in tree:
            for left, state, right in level:
                head_char = right[0] if right else "_"
                if (state, head_char) in self.transitions:
                    total_transitions += len(self.transitions[(state, head_char)])
                    nonleaves += 1
        return total_transitions / nonleaves if nonleaves > 0 else 0

    # generate output summary for a particular test machine and string
    def generate_output(self, tree, total_transitions, explored_configurations, nondeterminism, accept_found, stopped_due_to_depth_limit, depth_limit):
        result = []
        result.append(f"Machine Name: {self.machine_name}")
        result.append(f"Initial String: {tree[0][0][2]}")
        result.append(f"Tree Depth: {len(tree) - 1}")
        result.append(f"Total Transitions Simulated: {total_transitions + 1}")
        result.append(f"Measured nondeterminism: {nondeterminism:.2f}")

        if stopped_due_to_depth_limit:
            result.append(f"Execution stopped after {depth_limit} steps")
        elif accept_found:
            result.append(f"String accepted in {len(tree) - 1} steps")
        else:
            result.append(f"String rejected in {len(tree) - 1}")

        # add each level of the tree to the result
        for level in tree:
            level_line = " ".join([f"{left}{state}{right}" for left, state, right in level])
            result.append(level_line)

        return "\n".join(result)

if __name__ == "__main__":
    test_cases = {
        "data_a_plus_msulli52.csv": ["aaa", "aab", "aaaaaaaaaaaaaa", ""],
        "data_a_plus_DTM_msulli52.csv": ["aaa", "aab", "aaaaaaaaaaaaaa", ""],
        "data_equal_01s_msulli52.csv": ["011100111001110", "01", "1110", "1"],
        "data_equal_01s_DTM_msulli52.csv": ["011100111001110", "01", "1110", "1"],
        "data_abc_star_msulli52.csv": ["aabdeccc", "aabbcc", "abcd", "a"], 
        "data_abc_star_DTM_msulli52.csv": ["aabdeccc", "aabbcc", "abcd", "a"], 
        "data_even_1s_msulli52.csv": ["11", "00010", "0101", "11111111111"], 
        "data_even_1s_DTM_msulli52.csv": ["11", "00010", "0101", "11111111111"]
    }
    
    depth_limit = 50
    output_file = "output_msulli52.txt"
    table_file = "output_table_msulli52.txt"

    open(output_file, "w").close() # clear the output file
    open(table_file, "w").close()

    table_rows = []

    # write to the output file for each test file and string 
    with open(output_file, "a") as file:
        for input_file, input_strings in test_cases.items():
            for string in input_strings:
                ntm = NTM(input_file)
                output, accept_found, total_transitions, nondeterminism, tree = ntm.run(string, depth_limit)
                file.write(output + "\n\n")
                
                # add row for table
                path = "\n".join([" ".join([f"{left}{state}{right}" for left, state, right in level]) for level in tree])
                table_rows.append([
                    ntm.machine_name,
                    string,
                    len(tree) - 1,
                    total_transitions,
                    f"{nondeterminism:.2f}",
                    "Accepted" if accept_found else "Rejected",
                    path
                ])

                # print(output) 
                # print() 

    # generate output table
    with open(table_file, "w") as table_file:
        table_file.write(tabulate(table_rows, headers=["Machine Name", "Initial String", "Tree Depth", "Total Transitions", "Nondeterminism", "Result", "Path"], tablefmt="grid"))