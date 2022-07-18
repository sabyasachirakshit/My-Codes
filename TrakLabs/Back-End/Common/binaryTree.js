console.log("JS LINKED!");

//Node Class
class Node {
  constructor(data) {
    this.data = data;
    this.left = null;
    this.right = null;
  }
}

// Binary Search tree class
class BinarySearchTree {
  constructor() {
    // root of a binary search tree
    this.root = null;
  }
  insertNode(node, newNode) {
    if (newNode.data < node.data) {
      if (node.left == null) {
        node.left = newNode;
        console.log(node.data + "-->");
      } else {
        this.insertNode(node.left, newNode);
      }
    } else {
      if (node.right == null) {
        node.right = newNode;
        console.log(node.data + "-->");
      } else {
        this.insertNode(node.right, newNode);
      }
    }
  }

  insert(data) {
    var newNode = new Node(data); //Created a node with left and right as null
    if (this.root == null) {
      this.root = newNode; //Setting the node as root
    } else {
      this.insertNode(this.root, newNode); //Positioning the node in the tree
    }
  }

  findMinNode(node) {
    if (node.left === null) return node;
    else return this.findMinNode(node.left);
  }

  removeNode(node, key) {
    if (!node) {
      return null;
    } else if (key < node.data) {
      node.left = this.removeNode(node.left, key);
      return node;
    } else if (key > node.data) {
      node.right = this.removeNode(node.right, key);
      return node;
    } else {
      if (node.left === null && node.right === null) {
        node = null;
        return node;
      }
      if (node.left === null) {
        node = node.right;
        return node;
      } else if (node.right === null) {
        node = node.left;
        return node;
      }
      var aux = this.findMinNode(node.right);
      node.data = aux.data;

      node.right = this.removeNode(node.right, aux.data);
      return node;
    }
  }
  remove(data) {
    this.root = this.removeNode(this.root, data);
  }

  inorder(node) {
    if (node !== null) {
      this.inorder(node.left);
      console.log(node.data);
      this.inorder(node.right);
    }
  }

  preorder(node) {
    if (node !== null) {
      console.log(node.data);
      this.preorder(node.left);
      this.preorder(node.right);
    }
  }
  postorder(node) {
    if (node !== null) {
      this.postorder(node.left);
      this.postorder(node.right);
      console.log(node.data);
    }
  }
  getRootNode() {
    return this.root;
  }
  search(node, data) {
    if (node === null) return null;
    else if (data < node.data) return this.search(node.left, data);
    else if (data > node.data) return this.search(node.right, data);
    else return node;
  }
}
var allNodes = [];
var BST = new BinarySearchTree();
document.getElementById("nodeBtn").addEventListener("click", () => {
  var getNode = Number(document.getElementById("node").value);
  allNodes.push(getNode);
  document.getElementById("node").value = "";
});

// BST.insert(1);
// BST.insert(2);
// BST.insert(3);
// BST.insert(4);
// BST.insert(5);
// BST.insert(6);
