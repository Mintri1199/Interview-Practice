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

pascalTriangle(row: 15)

//1
//1    1
//1    2    1
//1    3    3    1
//1    4    6    4    1
//1    5    10    10    5    1
//1    6    15    20    15    6    1
//1    7    21    35    35    21    7    1
//1    8    28    56    70    56    28    8    1
//1    9    36    84    126    126    84    36    9    1
//1    10    45    120    210    252    210    120    45    10    1
//1    11    55    165    330    462    462    330    165    55    11    1
//1    12    66    220    495    792    924    792    495    220    66    12    1
//1    13    78    286    715    1287    1716    1716    1287    715    286    78    13    1
//1    14    91    364    1001    2002    3003    3432    3003    2002    1001    364    91    14    1
