/**
 * @param {string} s
 * @return {boolean}
 */
var validPalindrome = function(s) {
    let left=0;
    let right=s.length-1
    while(left<right){
        if (s[left]===s[right]){
            left++;
            right--;
        }
        else{
            return isPalin(s,left+1,right) || isPalin(s,left,right-1)
        }
    }
    return true
};

function isPalin(s,left,right){
        while(left<right){
            if (s[left]===s[right]){
            left++;
            right--;
            }
            else{
                return false;
                }
        }
        return true

}