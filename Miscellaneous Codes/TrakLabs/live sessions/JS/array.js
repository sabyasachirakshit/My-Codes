let array = [1,2,5,10,3,45,34,2,7,96,5,11];
let big_elements = []
for (let index = 0; index < array.length; index++) {
    if(array[index]!=0 || array[index]!=array.length-1){
        if((array[index]>array[index-1])&&(array[index]>array[index+1])){
            big_elements.push(array[index]);
        }
    }  
}
console.log(big_elements);