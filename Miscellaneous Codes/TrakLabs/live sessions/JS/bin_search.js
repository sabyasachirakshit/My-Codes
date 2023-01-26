var array = [12,1,5,7,45,23,98,43,65,88,19,43,67,69,76,34,44];
array.sort();
function binSearch(arr, search_element) {
    first = 0;
    last = arr.length - 1;
    while (first <= last) {
        var mid = Math.floor((first + last) / 2);
        if (arr[mid] === search_element) {
            return 'Number Found';
        } else if (arr[mid] < search_element) {
            first = mid + 1;
        } else {
            last = mid - 1;
        }
    }
    return 'Number not found!';
}

console.log(binSearch(array, 6));