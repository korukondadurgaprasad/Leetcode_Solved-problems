/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {

    // Handle base cases
    if (n === 0) return 0;
    if (n === 1) return 1;

    // Initialize the first two Fibonacci numbers
    let prev2 = 0; // F(0)
    let prev1 = 1; // F(1)
    let current;

    // Calculate Fibonacci numbers iteratively
    for (let i = 2; i <= n; i++) {
        current = prev1 + prev2; // F(i) = F(i-1) + F(i-2)
        prev2 = prev1; // Move to next
        prev1 = current; // Move to next
    }

    return current; // This holds F(n)

};