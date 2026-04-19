#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <tuple> // Needed for std::tuple used as map key

using namespace std;

/**
 * @brief Computes the next state of the word based on the given rewriting rules.
 * 
 * Applies the rewriting rules simultaneously to all characters of the current word.
 * The new character at position i depends on characters at positions (i-2), i, and (i+1)
 * in the current word. Indices are handled cyclically modulo n.
 * 
 * @param current_word The current word state.
 * @param n The length of the word.
 * @param final_rules A vector of characters representing the rewriting rules. 
 *                    final_rules[k] gives the output character for the rule indexed by k.
 *                    Index k is calculated from the three input characters (c1, c2, c3)
 *                    mapped to binary ('a'->0, 'b'->1) as k = k1*4 + k2*2 + k3.
 * @return The word state after one rewriting step.
 */
string compute_next_word(const string& current_word, int n, const vector<char>& final_rules) {
    // Initialize the next word string. Can be empty string of size n or copy of current word.
    // Using string(n, ' ') is efficient as it avoids copying potentially large string content.
    string next_word = string(n, ' '); 
    
    for (int i = 0; i < n; ++i) {
        // Determine the context characters c1, c2, c3 based on current word state.
        // Use modulo arithmetic with `+ n` to handle negative indices correctly.
        char c1 = current_word[(i - 2 + n) % n]; // Character at position i-2
        char c2 = current_word[i];               // Character at position i
        char c3 = current_word[(i + 1) % n];     // Character at position i+1

        // Map context characters 'a','b' to binary values 0,1 respectively.
        int k1 = (c1 == 'b'); 
        int k2 = (c2 == 'b');
        int k3 = (c3 == 'b');

        // Calculate the rule index based on the binary values.
        // This maps the tuple (c1, c2, c3) to an integer index in [0, 7].
        int rule_index = k1 * 4 + k2 * 2 + k3; 
        
        // Assign the new character to position i in the next word based on the determined rule.
        // Assumes rule_index is valid [0,7] and final_rules has size 8.
        next_word[i] = final_rules[rule_index]; 
    }
    return next_word; // Return the computed next word state.
}

/**
 * @brief Finds the lexicographically smallest cyclic shift of a given word.
 * 
 * Generates all n cyclic shifts of the word and returns the one that comes first
 * lexicographically.
 * 
 * @param word The input word string.
 * @param n The length of the word.
 * @return The lexicographically smallest cyclic shift of the word.
 */
string find_smallest_cyclic_shift(const string& word, int n) {
    string smallest_shift = word; // Initialize smallest shift found so far with the original word
    string current_shift = word; // A mutable copy to generate shifts
    
    // Iterate through all possible non-trivial shifts (1 to n-1)
    for (int i = 1; i < n; ++i) {
        // Generate the next cyclic shift by rotating the string left by 1 position.
        // std::rotate modifies the string in place.
        rotate(current_shift.begin(), current_shift.begin() + 1, current_shift.end()); 
        
        // Compare the newly generated shift with the smallest one found so far.
        if (current_shift < smallest_shift) {
            smallest_shift = current_shift; // Update if the current shift is lexicographically smaller.
        }
    }
    return smallest_shift; // Return the overall smallest shift found.
}


int main() {
    // Optimize C++ standard input/output streams for speed.
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n; // Word length
    // Process multiple test blocks from input until EOF.
    while (cin >> n) {
        string initial_word; // The starting word for the L-system
        cin >> initial_word; 

        // Use a map to temporarily store rules read from input.
        // The key is a tuple of the three context characters (c1, c2, c3).
        // The value is the resulting character c4.
        map<tuple<char, char, char>, char> rules_map;
        for (int i = 0; i < 8; ++i) {
            string rule_str; // Rule is given as a 4-character string "c1c2c3c4"
            cin >> rule_str; 
            // Basic validation: ensure rule string has the expected length.
            if (rule_str.length() == 4) {
                 // Store the rule mapping (c1, c2, c3) -> c4
                 rules_map[{rule_str[0], rule_str[1], rule_str[2]}] = rule_str[3];
            } 
            // No explicit error handling for malformed input needed for typical competitive programming.
        }
        
        // Create a vector `final_rules` of size 8. This vector will store the rule outcomes (c4)
        // indexed directly by the integer representation of the context (c1, c2, c3).
        vector<char> final_rules(8);
        bool rules_ok = true; // Flag to check if all rules were provided (completeness check)
        for(int k1=0; k1<=1; ++k1) { // Iterate through possibilities for first context char ('a' or 'b')
             for(int k2=0; k2<=1; ++k2) { // Iterate for second context char
                 for(int k3=0; k3<=1; ++k3) { // Iterate for third context char
                     char c1 = (k1 == 0) ? 'a' : 'b';
                     char c2 = (k2 == 0) ? 'a' : 'b';
                     char c3 = (k3 == 0) ? 'a' : 'b';
                     int rule_index = k1 * 4 + k2 * 2 + k3; // Calculate the index 0-7
                     
                     // Find the rule for this context (c1, c2, c3) in the map.
                     auto it = rules_map.find({c1, c2, c3});
                     if (it != rules_map.end()) {
                         // If found, store the result character c4 in the `final_rules` vector at the calculated index.
                         final_rules[rule_index] = it->second;
                     } else {
                         // If a rule is not found, set flag and break. Problem statement guarantees completeness.
                         rules_ok = false; 
                         break; 
                     }
                 }
                 if (!rules_ok) break; // Exit middle loop if a rule was missing
             }
             if (!rules_ok) break; // Exit outer loop if a rule was missing
        }
        // Assuming the problem statement holds true, rules_ok will remain true.

        long long s; // Number of rewriting steps, can be very large.
        cin >> s;

        // Handle the base case: if s=0 steps, the word is unchanged.
        if (s == 0) {
            cout << find_smallest_cyclic_shift(initial_word, n) << endl;
            continue; // Proceed to the next input block.
        }

        // Use a map to detect cycles: store the first time step each word state is encountered.
        map<string, long long> first_occurrence; 
        // Use a vector to store the history of word states generated.
        vector<string> history; 
        string current_word = initial_word; // Start the simulation with the initial word.
        
        long long t = 0; // Current time step counter.
        string final_word; // Variable to store the final word state W_s.

        // Simulate the rewriting process step by step, up to s steps.
        while (t < s) { 
            // Check if the current word state has been seen before (cycle detection).
            auto it = first_occurrence.find(current_word);
            if (it != first_occurrence.end()) {
                // Cycle detected!
                long long t0 = it->second; // The step number when this state first occurred.
                long long p = t - t0; // The period length of the cycle (p >= 1).
                
                // Calculate how many steps remain from the current step 't' to the target step 's'.
                long long remaining_steps = s - t; 
                // Find the position within the cycle corresponding to step 's'.
                long long cycle_offset = remaining_steps % p; 
                
                // The final word W_s is the word at index (t0 + cycle_offset) in the history.
                // Cast index to size_t for vector access. The index calculation is safe.
                final_word = history[(size_t)(t0 + cycle_offset)]; 
                
                goto found_final_word_cycle; // Jump directly to output phase.
            }

            // If the state is new, record its first occurrence step and add it to history.
            first_occurrence[current_word] = t;
            history.push_back(current_word);

            // Compute the word state for the next step.
            current_word = compute_next_word(current_word, n, final_rules);
            t++; // Increment the time step counter.
        }
        
        // If the loop completes without detecting a cycle reaching state 's' 
        // (i.e., s is smaller than the step number where cycle is detected, or s is within pre-period),
        // then the `current_word` holds the state W_s.
        final_word = current_word;

    found_final_word_cycle: // Label for goto statement after finding W_s using cycle property.
        // Compute the lexicographically smallest cyclic shift of the final word W_s.
        cout << find_smallest_cyclic_shift(final_word, n) << endl;

    } // End of while loop processing input blocks.

    return 0; // Indicate successful execution.
}