/**
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var countSymmetricIntegers = function(low, high) {
    let finalcount=0;
    for (i=low;i<high+1;i++){
        let numStr=i.toString();
        if (numStr.length%2===0){
            let n=numStr.length/2;
            let firsthalf=0;
            for(let i=0;i<n;i++){
                firsthalf+=parseInt(numStr[i],10)
            }

            let secondhalf=0;
            for(let j=n;j<numStr.length;j++){
                secondhalf+=parseInt(numStr[j],10)
            }

            if(firsthalf===secondhalf){
                finalcount++;
            }
        }
    }
    return finalcount

    };
