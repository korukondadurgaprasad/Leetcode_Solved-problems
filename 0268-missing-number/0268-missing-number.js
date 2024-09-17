/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let a=nums.length
    let totalsum= (a*(a+1))/2
    let sum=0
    for(num of nums){
        sum+=num;
    }

    let missingnum=totalsum-sum;
    return missingnum

    
};