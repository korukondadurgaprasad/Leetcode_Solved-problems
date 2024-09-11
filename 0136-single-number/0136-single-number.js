/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let result=0;
    nums.sort((a,b)=> a-b)
    for (num of nums){
        result^=num;

    }
    return result;
};