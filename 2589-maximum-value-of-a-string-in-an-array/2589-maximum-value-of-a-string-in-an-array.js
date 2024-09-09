
var maximumValue = function(strs) {
    let maxval = 0;
    let value;

    for (let i of strs) {
        // Check if the string contains only digits
        if (/^\d+$/.test(i)) {
            value = parseInt(i, 10);
        } else {
            value = i.length;
        }

        maxval = Math.max(maxval, value);
    }

    return maxval;
};

//         // Check if the string contains only digits
//         if (/^\d+$/.test(str)) {
//             // Convert to numeric value
//             value = parseInt(str, 10);
//         } else {
//             // If it contains letters, use its length
//             value = str.length;
//         }

//         // Update maxValue if the current value is greater
//         maxValue = Math.max(maxValue, value);
//     }

//     return maxValue;
// }

// // Example usage
// const strs = ["alic3", "bob", "3", "4", "00000"];
// console.log(maximumValue(strs));  // Output: 5
