#include <stdio.h>

// O(1) - Constant time complexity
void constantTime(int n) {
    printf("This is an example of O(1) time complexity.\n");
}

// O(n) - Linear time complexity
void linearTime(int n) {
    printf("This is an example of O(n) time complexity.\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", i);
    }
    printf("\n");
}

// O(n^2) - Quadratic time complexity
void quadraticTime(int n) {
    printf("This is an example of O(n^2) time complexity.\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("(%d, %d) ", i, j);
        }
        printf("\n");
    }
}

int main() {
    int n;

    printf("Enter a value for n: ");
    scanf("%d", &n);

    // Demonstrate constant time complexity
    constantTime(n);

    // Demonstrate linear time complexity
    linearTime(n);

    // Demonstrate quadratic time complexity
    quadraticTime(n);

    return 0;
}
