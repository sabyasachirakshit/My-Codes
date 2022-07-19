//Linked List is a dynamic data structure, as we can add or remove elements at ease, and it can even grow as needed.

class Node {
  constructor(element) {
    this.element = element; //element holds the data of node
    this.next = null; //next holds the pointer to the next node
  }
}

class LinkedList {
  constructor() {
    this.head = null; //indicates first node of a Linked List
    this.size = 0; //indicates size of Linked List
  }

  add(element) {
    var node = new Node(element); //creating new node
    var current; //To store current node
    if (this.head == null) {
      this.head = node;
    } else {
      current = this.head;
      while (current.next) {
        current = current.next;
      }
      current.next = node; //Iterating to the last of node and setting the value
    }
    this.size++;
  }
  insertAt(element, index) {
    if (index < 0 || index > this.size) {
      return console.log("Please enter valid index");
    } else {
      //creating a new Node
      var node = new Node(element);
      var curr, prev;
      curr = this.head;
      //add element to first index
      if (index == 0) {
        node.next = this.head;
        this.head = node;
      } else {
        curr = this.head;
        var it = 0;
        //iterate over the list to find position to insert
        while (it < index) {
          it++;
          prev = curr;
          curr = curr.next;
        }
        node.next = curr;
        prev.next = node;
      }
      this.size++;
    }
  }
  removeFrom(index) {
    if (index < 0 || index > this.size) {
      return console.log("Please enter valid index");
    } else {
      var previous, current;
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
  showLinkedList() {
    var current = this.head;
    var str = "";
    while (current) {
      str += `${current.element}-->`;
      current = current.next;
    }
    console.log(str);
  }
}

var myLinkedList = new LinkedList();
myLinkedList.add(1);
myLinkedList.add(2);
myLinkedList.add(3);
myLinkedList.add(4);
myLinkedList.add(5);
myLinkedList.showLinkedList();
console.log("Linked List after removing data from index 2 is:");
myLinkedList.removeFrom(2);
myLinkedList.showLinkedList();
