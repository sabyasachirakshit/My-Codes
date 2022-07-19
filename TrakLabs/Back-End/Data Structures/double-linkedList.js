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
  addWithIndex(element, index) {
    if (index < 0 || index > this.size)
      return `Invalid Syntax. cannot add Node ${element} at index ${index} because size of Double Linked List is : ${this.size}`;
    else {
      var node = new Node(element);
      if (element == this.head.element) {
        node.next = this.head;
        this.head = node;
        node.prev = null;
      } else {
        var it = 0;
        var prev;
        var current = this.head;
        while (it < index) {
          prev = current;
          current = current.next;
          it++;
        }
        prev.next = node;
        node.next = current;
        node.prev = prev;
      }
    }
    this.size++;
  }

  removeNodeIndex(index) {
    //To be done later..
  }
  removeNodeValue(value) {
    //To be done later..
  }
  searchNode(value) {
    //To be done later..
  }
  modifyNode(oldValue, newValue, index) {
    //To be done later..
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
console.log("Adding 100 at index 2..");
myDoubleLinkedList.addWithIndex(100, 2);
console.log(
  `Now the double linked list becomes: ${myDoubleLinkedList.showDoubleLinkedList()}`
);
