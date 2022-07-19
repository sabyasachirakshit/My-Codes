class Node {
  constructor(element) {
    this.prev = null;
    this.element = element;
    this.next = null;
  }
}

class doubleLinkedList {
  constructor() {
    this.head = null;
    this.size = 0;
  }
  add(element) {
    var node = new Node(element);
    if (this.head == null) {
      this.head = node;
    } else {
      let current = this.head;
      while (current.next) {
        current = current.next;
      }
      current.next = node;
      node.prev = current;
      node.next = null;
    }
    this.size++;
  }
  showDoubleLinkedList() {
    let current = this.head;
    let str = "";
    while (current) {
      str += `${current.element} <--> `;
      current = current.next;
    }
    return str;
  }
}

let myDoubleLinkedList = new doubleLinkedList();
myDoubleLinkedList.add(1);
myDoubleLinkedList.add(2);
myDoubleLinkedList.add(3);
myDoubleLinkedList.add(4);
myDoubleLinkedList.add(5);
console.log(
  `My Double Linked List is : ${myDoubleLinkedList.showDoubleLinkedList()}`
);
myDoubleLinkedList.add(6);
console.log(
  `Adding Node 6 at the rear of the double Linked List, The List now becomes: ${myDoubleLinkedList.showDoubleLinkedList()}`
);
