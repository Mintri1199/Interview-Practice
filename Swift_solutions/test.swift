var a = 1
// print(a)  // 1
var closure: () -> Void = { a += 1 }


func something(c: () -> Void) {
    print(a)
    c()
    print(a)
}

something(c: closure)