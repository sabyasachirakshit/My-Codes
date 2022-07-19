//Implementing Queue in JavaScript

class Queue {
  constructor() {
    this.items = [];
  }

  //Add Element inside queue
  enqueue(element) {
    return this.items.push(element);
  }

  //Remove Element from the queue
  dequeue() {
    if (this.items.length > 0) {
      return this.items.shift();
    }
  }

  //Viewing last element
  peek() {
    return this.items[this.items.length - 1];
  }

  //Check if Queue is empty
  isEmpty() {
    if (this.items.length == 0) {
      return true;
    } else {
      return false;
    }
  }

  //Check size of Queue
  checkSize() {
    return this.items.length;
  }

  //Clear the Queue
  clearQueue() {
    this.items = [];
  }
}
var x = 12;
let myQueue = new Queue();
myQueue.enqueue(1);
myQueue.enqueue(2);
myQueue.enqueue(3);
myQueue.enqueue(4);
myQueue.enqueue(5);
console.log(`After enqueuing 5 elements, Queue is: ${myQueue.items}`);
myQueue.dequeue();
myQueue.dequeue();
console.log(`After running dequeue function 2 times, Queue is: ${myQueue.items}`);
console.log(`Peeking inside Queue...returned value = ${myQueue.peek()}`);
console.log(`Checking if Queue is empty or not. Returned Result is ${myQueue.isEmpty()}`);
console.log(`Checking size of Queue. Size is ${myQueue.checkSize()}`);
myQueue.clearQueue();
console.log(`Running clearing function... Now the Queue is: ${myQueue.items}`);