/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let j=0;
    for (let i=0;i<nums.length;i++){
        if (nums[i]!==val)
        {
            nums[j]=nums[i];
            j++;
        }
    }
    return j;
};
// var removeElement = function(nums, val) {
//     for (let i = 0; i < nums.length; i++) {
//         if (nums[i] === val) {
//             nums.splice(i, 1); // Remove the element at index `i`
//             i--; // Decrement `i` to recheck the current index
//         }
//     }
//     return nums.length;
// };

