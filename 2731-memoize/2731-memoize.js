function memoize(fn) {
    const cache = {}; // This object will store the cached results
    let callCount = 0; // This variable will track how many times the original function is actually called

    return function(...args) { // Return a new function that can take any number of arguments
        const key = args.toString(); // Convert the arguments to a string to use as a key in the cache

        if (key in cache) { // If the key (arguments) is already in the cache
            return cache[key]; // Return the cached result immediately
        }

        const result = fn(...args); // If not in cache, call the original function with the arguments
        cache[key] = result; // Store the result in the cache
        callCount++; // Increment the call count since the function was called
        return result; // Return the calculated result
    };
}

// Adding a way to check the number of times the original function was called
memoize.getCallCount = function() {
    return callCount;
};


