/**
 * @param {number} n
 * @return {boolean}
 */
var isUgly = function(n) {
    if (n <= 0) return false;
    let cons=[2,3,5]
    for(let i of cons){
        while(n%i===0){
            n /= i

        }
    }
    return n===1
};