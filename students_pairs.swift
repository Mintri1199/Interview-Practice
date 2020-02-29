/*
You are a developer for a university. Yosur current project is to develop a system for students to find courses they share with friends. The university has a system for querying courses students are enrolled in, returned as a list of (ID, course) pairs.
Write a function that takes in a list of (student ID number, course name) pairs and returns, for every pair of students, a list of all courses they share.
Sample Input:
student_course_pairs_1 = [
["58", "Linear Algebra"],
["94", "Art History"],
["94", "Operating Systems"],
["17", "Software Design"],
["58", "Mechanics"],
["58", "Economics"],
["17", "Linear Algebra"],
["17", "Political Science"],
["94", "Economics"],
["25", "Economics"],
["58", "Software Design"],
]
Sample Output (pseudocode, in any order):
find_pairs(student_course_pairs_1) =>
{
[58, 17]: ["Software Design", "Linear Algebra"]
[58, 94]: ["Economics"]
[58, 25]: ["Economics"]
[94, 25]: ["Economics"]
[17, 94]: []
[17, 25]: []
}
Additional test cases:
Sample Input:
student_course_pairs_2 = [
["42", "Software Design"],
["0", "Advanced Mechanics"],
["9", "Art History"],
]
Sample output:
find_pairs(student_course_pairs_2) =>
{
[0, 42]: []
[0, 9]: []
[9, 42]: []
}
*/



// func findStudentsPairs(input: [[String]]) {
//     var studentProfiles = Dictionary<String, Set<String>>()

//     // Building the dictionary
//     for value in input {
//         let name: String = value[0]
//         let studentClass: String = value[1]

//         if studentProfiles[name] == nil {
//             studentProfiles[name] = Set([studentClass])
//         } else {
//             if var set = studentProfiles[name] {
//                 set.insert(studentClass)
//                 studentProfiles[name] = set
//             }
//         }
//     }

//     print(studentProfiles)
// }

// let example = [
// ["58", "Linear Algebra"],
// ["94", "Art History"],
// ["94", "Operating Systems"],
// ["17", "Software Design"],
// ["58", "Mechanics"],
// ["58", "Economics"],
// ["17", "Linear Algebra"],
// ["17", "Political Science"],
// ["94", "Economics"],
// ["25", "Economics"],
// ["58", "Software Design"],
// ]

// findStudentsPairs(input: example)

var a = 1


withUnsafePointer(to: &a) {
    print("number value \(a) has address: \($0)")
}
// print(a)  // 1
var closure: (Int) -> Void = {  
    a = $0 
    withUnsafePointer(to: &a) {
       print("number value \(a) has address: \($0)")
    }
}

// closure(5)
// print(a)
