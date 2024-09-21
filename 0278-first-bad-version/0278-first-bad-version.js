/**
 * Definition for isBadVersion()
 * 
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function(n) {
        let left = 1;        // Start at the first version
        let right = n;       // End at the last version
        
        while (left < right) { // While there's more than one version to check
            let mid = Math.floor((left + right) / 2); // Find the middle version
            
            if (isBadVersion(mid)) {
                right = mid;  // Move to the left side (include mid)
            } else {
                left = mid + 1; // Move to the right side
            }
        }
        
        return left; // This is the first bad version
    };
        

};