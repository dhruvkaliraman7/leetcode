/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const tmp = [];
    for (let i = 0; i < arr.length ; i++){
        if (fn(arr[i],i)){
            tmp.push(arr[i]);
        }
    }
    return tmp;
    
};