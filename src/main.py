import sys
import time

def solve_hvlcs(alphabet_values, s1, s2):
    n = len(s1)
    m = len(s2)
    
    # Set up dp array
    dp = [[0] * (m+1) for i in range(n+1)]
    
    # Fill dp
    for i in range(1, n+1):
        char1 = s1[i-1]
        val = alphabet_values.get(char1, 0)
        for j in range(1, m+1):
            if char1 == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + val
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    # Reconstruct the sequence, basically very similar to pseudocode from the slides
    res = []
    i = n
    j = m
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            res.append(s1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    # Output
    return dp[n][m], "".join(reversed(res))


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
  
        # Now, solve and output
        max_val, hvlcs = solve_hvlcs(vals, s1, s2)
        print(max_val)
        print(hvlcs)
        
    except (ValueError, IndexError) as e:
        print("Unable to parse input data, please make sure input file follows the given format on Canvas.")
        




if __name__ == "__main__":
    main()
