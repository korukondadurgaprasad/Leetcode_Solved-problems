/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let min= -Math.pow(2,31);
    let max=Math.pow(2,31)-1;

    let sign =x>0?1:-1

    let ans =parseInt(Math.abs(x).toString().split('').reverse().join(''))*sign

    if(ans<min || ans>max){
        return 0
    }
    else{
        return ans
    }
};