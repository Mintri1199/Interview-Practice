class DecimalTreeNode {

    var data: Any?
    var next: [DecimalTreeNode?] = []

    init(data: Any?) {
        self.data = data
        self.next = Array(repeating: nil, count: 10)
    }

    func isLeaf() -> Bool {
        // Check if the current node is a leaf or not
        // Count the number of nil values in self.next
        for item in self.next {
            if item != nil {  // There is a child of the node
                return false
            }
        }
        // The node has no children
        return true
    }

    func isBranch() -> Bool{
        // Check if the current node is a branch or not
        return !self.isLeaf()
    }

    func height() -> Int{
        /*
         Return the height of the node (the number of edges on the longest
         downward path from this node to a descendant leaf node).
         */
        // Early break
        if self.isLeaf(){
            return 0
        }
        // Create a array of int to keep track of the height of each branch
        var tenPath = Array<Int>(repeating: 0, count: 10)

        // Traverse each child node
        for path in 0 ... 10 {
            // Check if there is a node to begin with
            if let newPath = self.next[path]{
                tenPath[path] += newPath.height()
            }
        }
        // The program have travese all of it children
        return tenPath.max()! + 1
    }
}

class DecimalSearchTree{

    let root: DecimalTreeNode = DecimalTreeNode(data: "+")
    var size: Int = 11  // number of nodes in the tree and the unuse node
    var usedSize: Int = 0 // Number of nodes that are used

    func isEmpty() -> Bool{
        // Return true if this decimal search tree is empty (has no nodes)
        return self.root.isLeaf()
    }

    func height() -> Int{
        // Return the height of this tree (the number of edges on the longest
        // downward path from this tree's root node to a descendant leaf node).
        return self.root.height()
    }

    func contains(numbers: String) -> Bool{
        // Return true if this Decimal search tree contains a path at contains
        // all the numbers iteratively.

        var currentNode: DecimalTreeNode? = self.root

        for character in numbers {
            let index = Int(String(character))

            if let newNode = currentNode?.next[index!] {
                currentNode = newNode
            } else {
                currentNode = nil
                break
            }
        }
        return currentNode != nil
    }

    func search(number: String) -> Any?{
        // Return an item in this decimal search tree matching the given number,
        // or nil if the given item is not found.
        if let node = findNodeRecursive(number: number, node: self.root) {
            return node.data
        } else {
            return nil
        }
    }

    func insert(number: String, data: Any) {
        // Insert the data in order of the number to the Decimal Search Tree
        // recursively.
        insertNodeRecursive(number: number, data: data, node: self.root)
    }



    func insertNodeRecursive(number: String, data: Any, node: DecimalTreeNode) {
        // Helper function for insert

        // Check if the program has done traversing
        if number.count == 0 {
            // Insert the data is there aren't any
            if node.data == nil {
                node.data = data
                self.usedSize += 1
            }
            return
        }

        let nextIndex = Int(String(number.prefix(1)))
        let remainder = String(number.dropFirst())

        if node.next[nextIndex!] == nil {
            node.next[nextIndex!] = DecimalTreeNode(data: nil)
            self.size += 10
        }

        insertNodeRecursive(number: remainder, data: data, node: node.next[nextIndex!]!)
    }

    func findNodeRecursive(number: String, node: DecimalTreeNode) -> DecimalTreeNode? {
        /*
         Return the node containing the given item in this decimal search tree,
         or None if the given item is not found. Search is performed recursively
         starting from the given node (give the root node to start recursion).
         */

        if number.count == 0 {
            // Signalling that the tree has a path that contains all the numbers
            return node
        }

        // Use the first number of the string as index to the child node
        let nextIndex = Int(number.prefix(1))

        // Drop the first number of the string
        let remainder = String(number.dropFirst())

        // Check if there is a child node
        if let nextNode = node.next[nextIndex!] {
            // If so then call the function again with the remainder string
            // and the child node in the parameters
            return findNodeRecursive(number: remainder, node: nextNode)
        } else {
            // Did not find a node and the remainder still contains characters.
            // Meaning the tree doesn't have a path that contains all the numbers.
            return nil
        }
    }
}
