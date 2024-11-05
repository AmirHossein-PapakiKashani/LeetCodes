#include <stdio.h>
#include <stdlib.h>  // For malloc and free

// Function to calculate valid numbers after XOR checks
int xor_func(int n) {
    int *numbers = (int *)malloc(n * sizeof(int));  // Array to store numbers 0 to n-1
    int *valid_numbers = (int *)malloc(n * sizeof(int));  // Array to track valid numbers
    int valid_count = n;  // Initially, all numbers are considered valid

    // Initialize the numbers array from 0 to n-1
    for (int i = 0; i < n; i++) {
        numbers[i] = i;
        valid_numbers[i] = 1;  // Mark all numbers as valid initially
    }

    // Iterate over each number to check XOR condition
    for (int i = 0; i < n; i++) {
        if (valid_numbers[i] == 0) continue;  // Skip if number is already invalid
        for (int j = 0; j < n; j++) {
            int result = numbers[i] ^ numbers[j];  // XOR operation
            if (result < 0 || result >= n) {  // If XOR result is out of range
                valid_numbers[i] = 0;  // Mark current number as invalid
                valid_count--;  // Decrease valid count
                if (result > 0 && valid_numbers[j]) {  // Optionally mark the "other" as invalid
                    valid_numbers[j] = 0;
                    valid_count--;
                }
                break;  // Break out of inner loop as this number is no longer valid
            }
        }
    }

    // Free dynamically allocated memory
    free(numbers);
    free(valid_numbers);

    return valid_count;  // Return the count of valid numbers
}

int main() {
    int mm;
    printf("Enter the number of test cases: ");
    scanf("%d", &mm);  // Read number of test cases

    // Loop over the number of test cases
    for (int i = 0; i < mm; i++) {
        int n;
        printf("Enter n for test case %d: ", i + 1);
        scanf("%d", &n);  // Read input for each test case
        printf("%d\n", xor_func(n));  // Call xor_func and print the result
    }

    return 0;
}
