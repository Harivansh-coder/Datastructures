// Node for BST

function node(val, left, right){

    this.val = val
    this.left = left
    this.right = right
}

const root = new node(1,2,3);


// Inorder

const inorder = (root)=>{
    const nodes = []
    if (root){
        inorder(root.left)
        nodes.push(root.val)
        inorder(root.right)
    }
    return nodes
}

// Preorder

const preorder = (root)=>{
    const nodes = []
    if (root){
        nodes.push(root.val)
        preorder(root.left)
        preorder(root.right)
    }
    return nodes
}

// Postorder

const postorder = (root)=>{
    const nodes = []
    if (root){

        postorder(root.left)
        postorder(root.right)
        nodes.push(root.val)
    }
    return nodes
}

// Depth of BST

const maxDepth = function(root){
    const calc = (node) => {
        if (!node) return 0
        return Math.max(1 + calc(node.left), 1 + calc(node.right))
    }

    return calc(root)
}

console.log(inorder(root));
console.log(postorder(root));
console.log(preorder(root));
console.log(maxDepth(root));


/*
# Output

  [ 1 ]
  [ 1 ]
  [ 1 ]
  2

*/
