import sys

def solve_hvlcs(alphabet_values, s1, s2):
    pass

def main():
    # Parse input
    if len(sys.argv) < 2:
        # If no file provided, read from stdin (for testing)
        input_data = sys.stdin.read().split()
    else:
        with open(sys.argv[1], 'r') as f:
            input_data = f.read().split()
            
    if not input_data:
        return

    # Parse input data
    try:
        # K
        K = int(input_data[0])
        
        # x1 v1 \n ... \n xK vK
        line = 1
        vals = {}
        for i in range(K):
            vals[input_data[line]] = int(input_data[line+1])
            line += 2
            
        # A \n B    
        s1 = input_data[line]
        s2 = input_data[line+1]
        
    except (ValueError, IndexError) as e:
        print("Unable to parse input data, please make sure input file follows the given format on Canvas.")
        
        
    # Now, solve and output
    max_val, hvlcs = solve_hvlcs(vals, s1, s2)
    print(max_val)
    print(hvlcs)
        




if __name__ == "__main__":
    main()
