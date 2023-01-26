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
    if (index < 0 || index > this.size) {
      return `Cannot find index ${index} in double linked list of size ${this.size}`;
    } else {
      var current, previous;
      current = this.head;
      var it = 0;
      while (it < index) {
        previous = current;
        current = current.next;
        it++;
      }
      previous.next = current.next;
      current.next = null;
    }
    this.size--;
  }
  removeNodeValue(value) {
    if (value == this.head.element) {
      this.head = this.head.next;
      this.head.next = this.head.next.next;
    } else {
      var current = this.head;
      var previous;
      while (current.element != value) {
        previous = current;
        current = current.next;
      }
      previous.next = current.next;
      current.next = null;
    }
    this.size--;
  }
  searchNode(value) {
    var it = 0;
    var current = this.head;
    while (it < this.size) {
      if (current) {
        if (current.element == value)
          if (it + 1 == this.size)
            return `Node with value ${current.element} present at the end of the list`;
          else
            return `Node with value ${current.element} present before ${current.next.element}`;
        else {
          current = current.next;
          it++;
        }
      } else {
        return `Node with value ${value} not found in the Linked List`;
      }
    }
  }
  modifyNode(oldValue, newValue, index) {
    var it = 0;
    var current = this.head;
    while (it < this.size) {
      if (current) {
        if (current.element == oldValue) {
          this.removeNodeValue(oldValue);
          this.addWithIndex(newValue, index);
          return "Modification successfull!";
        } else {
          current = current.next;
          it++;
        }
      } else {
        return `Node with value ${oldValue} not found in the Linked List, so cannot modify!!`;
      }
    }
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
console.log("Removing node from index 3...");
myDoubleLinkedList.removeNodeIndex(3);
console.log(
  `Now my Double linked list becomes: ${myDoubleLinkedList.showDoubleLinkedList()}`
);
console.log("Removing Node 100 by value... ");
myDoubleLinkedList.removeNodeValue(100);
console.log(
  `Now my Double linked list becomes: ${myDoubleLinkedList.showDoubleLinkedList()}`
);
console.log("Searching for Node 3 in Linked List...");
console.log(myDoubleLinkedList.searchNode(3));
console.log("Searching for Node 6 in Linked List...");
console.log(myDoubleLinkedList.searchNode(6));
console.log("Modifying Node with value 4 to 3...");
console.log(myDoubleLinkedList.modifyNode(4, 3, 2));
console.log("Linked List becomes: ");
console.log(myDoubleLinkedList.showDoubleLinkedList())
console.log(`Modifying Node that does not exists with value '29' to '19'.. `);
console.log(myDoubleLinkedList.modifyNode(29, 19, 8));
