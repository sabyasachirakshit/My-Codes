class TreeNode {
  constructor(data) {
    this.data = data;
    this.left = null;
    this.right = null;
  }
}
class BinarySearchTree {
  constructor() {
    this.root = null;
  }
  insert(data) {
    //  it creates a new node to be inserted and calls insertNode()
    var newNode = new TreeNode(data);
    if (this.root === null) this.root = newNode;
    else this.insertNode(this.root, newNode);
  }

  insertNode(node, newNode) {
    // if the data is less than the node data move left of the tree
    if (newNode.data < node.data) {
      if (node.left === null) node.left = newNode;
      else this.insertNode(node.left, newNode);
    } else {
      // if the data is greater than the node data move right of the tree
      if (node.right === null) node.right = newNode;
      else this.insertNode(node.right, newNode);
    }
  }

  remove(data) {
    // it calls the removeNode with a given data
    this.root = this.removeNode(this.root, data);
  }

  removeNode(node, key) {
    // it remove node with a given data and recur over the tree to find the data and removes it
    if (node === null) return null;
    else if (key < node.data) {
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
      var store = this.findMinNode(node.right);
      node.data = store.data;
      node.right = this.removeNode(node.right, store.data);
      return node;
    }
  }
  inorder(node) {
    if (node !== null) {
      this.inorder(node.left);
      let html = `Inorder nodes of tree are in order of:<br> ${
        node.data + "-->"
      }`;
      document.getElementById("showTree").innerHTML = html;
      console.log(node.data + "-->");
      this.inorder(node.right);
      // return node.data + "-->";
    }
  }
  preorder(node) {
    if (node !== null) {
      console.log(node.data + "-->");
      this.preorder(node.left);
      this.preorder(node.right);
    }
  }
  postorder(node) {
    if (node !== null) {
      this.postorder(node.left);
      this.postorder(node.right);
      console.log(node.data + "-->");
    }
  }

  findMinNode(node) {
    //  finds the minimum node in tree and  starts search from given node
    if (node.left === null) return node;
    else return this.findMinNode(node.left);
  }

  getRootNode() {
    // returns root of the tree
    return this.root;
  }

  search(node, data) {
    // search for a node with given data
    if (node == null) return null;
    else if (data < node.data) return this.search(node.left, data);
    else if (data > node.data) return this.search(node.right, data);
    else return node;
  }
}

var BST = new BinarySearchTree();
var arr = [];
document.getElementById("nodeBtn").addEventListener("click", () => {
  BST.insert(Number(document.getElementById("node").value));
  // arr.push(Number(document.getElementById("node").value));
  console.log(`${document.getElementById("node").value} added`);
  document.getElementById("node").value = "";
  // arr.forEach((element) => {
  //   BST.insert(element);
  // });
});
// BST.insert(15);
// BST.insert(25);
// BST.insert(10);
// BST.insert(7);
// BST.insert(22);
// BST.insert(17);
// BST.insert(13);
// BST.insert(5);
// BST.insert(9);
// BST.insert(27);

function showTree() {
  var root = BST.getRootNode();
  BST.inorder(root);
}
document.getElementById("showMyTree").addEventListener("click", showTree);
// var root = BST.getRootNode();
// console.log("Inorder nodes of tree are in order of:" + "<br>");
// BST.inorder(root);

BST.remove(5);

var root = BST.getRootNode();
console.log("Inorder nodes of tree after removing 5 are in order of:" + "<br>");
BST.inorder(root);

BST.remove(7);
var root = BST.getRootNode();
console.log("Inorder nodes of tree after removing 7 are in order of:" + "<br>");
BST.inorder(root);

BST.remove(15);
var root = BST.getRootNode();
console.log(
  "Inorder nodes of tree after removing 15 are in order of:" + "<br>"
);
BST.inorder(root);

console.log("Inorder traversal:" + "<br>");
BST.inorder(root);

console.log("Postorder traversal" + "<br>");
BST.postorder(root);

console.log("Preorder traversal" + "<br>");
BST.preorder(root);
