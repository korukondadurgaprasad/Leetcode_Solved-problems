/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let b=s.trim()
    let arr=b.split(' ')
    let word=arr[arr.length-1]
     return word.length

    
};