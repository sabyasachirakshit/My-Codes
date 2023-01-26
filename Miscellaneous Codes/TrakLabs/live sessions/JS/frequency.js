// count frequency of all letters in a string:


function calculateFrequency(test_str) {
    var freq = {};
    for (var i = 0; i < test_str.length; i++) {
        var character = test_str.charAt(i);
        if (freq[character]) {
            freq[character]++;
        } else {
            freq[character] = 1;
        }
    }
    return freq;
}
let str = window.prompt("Enter String:");
calculateFrequency(str);