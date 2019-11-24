Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).

```
Test.it("works for some examples")
Test.assert_equals(is_triangle(1, 2, 2), True, "didn't work when sides were 1, 2, 2")
Test.assert_equals(is_triangle(7, 2, 2), False, "didn't work when sides were 7, 2, 2")
Test.assert_equals(is_triangle(1, 2, 3), False, "didn't work when sides were 1, 2, 3")
```