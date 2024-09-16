/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    s=s.toLowerCase().replace(/[^a-z0-9]/gi,'')
    var x=s.split('').reverse().join('')
    if (s===x){
        return true
    }
    else{
        return false
    }
};