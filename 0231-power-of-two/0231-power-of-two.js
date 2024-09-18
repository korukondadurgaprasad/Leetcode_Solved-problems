/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
    if (n <= 0) {
        return false;  // Correct return for non-positive numbers
    } else {
        // Corrected bitwise check and return boolean values
        if ((n & (n - 1)) === 0) {
            return true;   // Return boolean true
        } else {
            return false;  // Return boolean false
        }
    }
};
