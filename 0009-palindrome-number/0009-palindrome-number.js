/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    var y=String(x)
    var z=y.split('').reverse().join('')
    if (z===y){
        return true
    }
    else{
        return false
    }
};