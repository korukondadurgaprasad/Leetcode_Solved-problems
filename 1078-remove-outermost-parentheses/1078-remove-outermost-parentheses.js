/**
 * @param {string} s
 * @return {string}
 */
var removeOuterParentheses = function(s) {
    let res="";
    let count=0
    for (let char of s){
        if(char=='('){
            if(count>0){
                res+=char
            }
            count++;
        }
 
        else if(char===')'){
            count--;
            if(count>0){
                res+=char
            }
        }
    }
    return res
};