//Implementing queue using stacks

class Queue {
  constructor() {
    this.s1 = [];
    this.s2 = [];
  }

  enQueue(x) {
    //Move all elements from stack 1 to stack 2
    while (this.s1.length != 0) {
      this.s2.push(this.s1.pop());
    }

    //Push items into s1
    this.s1.push(x);

    //Push everything back to s1
    while (this.s2.length != 0) {
      this.s1.push(this.s2.pop());
    }
  }

  //Dequeue an item from queue
  deQueue() {
    if (this.s1.length == 0) {
      return "Queue is empty";
    }
    let x = this.s1[this.s1.length - 1];
    this.s1.pop();
    return x;
  }
}

let myQueue = new Queue();
myQueue.enQueue(1);
myQueue.enQueue(2);
myQueue.enQueue(3);
console.log(myQueue.deQueue());
console.log(myQueue.deQueue());
console.log(myQueue.deQueue());
