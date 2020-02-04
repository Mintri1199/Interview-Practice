// A Coding challenge from Exercism
//https://exercism.io/my/solutions/ec9adf9e266f40de99fc041e258b831c
//Compute Pascal's triangle up to a given number of rows.
//
//In Pascal's Triangle each number is computed by adding the numbers to the
//right and left of the current position in the previous row.
// column 1 |1   ROW 1
//          |1 1
//          |1 2 1
//          |1 3 3 1
//          |1 4 6 4 1

// A wrapper to allow a tuple to be hashable
struct Two<T:Hashable,U:Hashable> : Hashable {
    let values: (T, U)

    func hash(into hasher: inout Hasher) {
        hasher.combine(values.0)
        hasher.combine(values.1)
    }

    static func == (lhs: Two<T, U>, rhs: Two<T, U>) -> Bool {
        return lhs.values == rhs.values
    }
}

// Allow the program to look one row up instead of start from adding ones
var memoryDict = Dictionary<Two<Int,Int>,Int>()

// This function will return the number value of the current spot within the triangle
func pascalSpot(row: Int, col: Int) -> Int{
    let index = Two(values: (row, col))

    // This cover the recursive calls and prevent the function from starting at 1
    if memoryDict[index] != nil {
        return memoryDict[index]!
    }

    if col == 1 {
        return 1
    } else if row == col {
        return 1
    }
    // Call resursively to get the value of the row above
    let upLeft = pascalSpot(row: row - 1, col: col - 1)
    let upRight = pascalSpot(row: row - 1, col: col)

    // store the sum of the two values from the row above
    memoryDict[index] = upLeft + upRight
    return upLeft + upRight
}

func pascalTriangle(row: Int) {
    for r in 1 ... row {
        var rowString = ""
        for column in 1 ... r {
            rowString += String(pascalSpot(row: r, col: column)) + "\t"
        }
        print(rowString)
    }
}

pascalTriangle(row: 5)
