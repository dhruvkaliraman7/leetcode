/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    const tmp = init
    return {
        decrement: () => {
            return --init
        },
        increment: () => {
            return ++init
        },
        reset: () => {
            init = tmp
            return tmp
        }
        
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */