let A1=[1,2,3,4,5];
let A2=[6,7,8,9,10];

console.log(A1);
console.log(A2);

let mergedArray=[]
// let mergedArrayLength = A1.length + A2.length;
for (let index = 0; index < A2.length; ++index) {
    mergedArray.push(A1[index]);
    mergedArray.push(A2[index]);
}
console.log(mergedArray);