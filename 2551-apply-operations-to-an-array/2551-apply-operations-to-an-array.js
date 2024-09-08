/**
 * @param {number[]} nums
 * @return {number[]}
 */
var applyOperations = function(nums) {
    for (var i=0;i<nums.length;i++)
    {
        if (nums[i]===nums[i+1])
        {
            nums[i]=nums[i]*2;
            nums[i+1]=0
        }
    }

    var result=nums.filter(nums=>{
        return nums!==0;
    })

    while (result.length<nums.length)
    {
        result.push(0);
    }

    return result

};