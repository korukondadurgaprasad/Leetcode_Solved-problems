/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const stack = [];
    
    for (let char of s) {
        // If it's an opening bracket, push the corresponding closing bracket onto the stack
        if (char === '(') stack.push(')');
        else if (char === '{') stack.push('}');
        else if (char === '[') stack.push(']');
        // If it's a closing bracket, check if it matches the top of the stack
        else if (stack.length === 0 || stack.pop() !== char) return false;
    }
    
    // If the stack is empty, the string is valid
    return stack.length === 0;

    
};