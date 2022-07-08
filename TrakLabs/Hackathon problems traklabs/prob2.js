var length_of_array = 5;
var arr = [6,4,3,4,1];



function countOfNumbers(A,n){
    var count = 0;
    var new_arr = [];
    for (let i = 0; i < n; i++) {
        count = 0;
        for(let j = 1; j<n;j++){
            if(A[i]%A[j]==0){ 
                count++;
            }
        }
        new_arr.push(count);
    }
    return new_arr;
}
console.log(countOfNumbers(arr,length_of_array));