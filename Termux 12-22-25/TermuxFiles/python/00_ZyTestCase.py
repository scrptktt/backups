# Static Sets
import sys
''' intructions 1
    Implement the StaticSet class's union(), intersection(), difference(), filter(), and map() methods. 
    Each must not change the StaticSet itself, but rather build and return a new StaticSet.
'''
# from StaticSetTestCases import BinaryOpsTestCase, UnaryOpsTestCase
class StaticSet:
    # Initializes the StaticSet by creating a set with the elements of the argument
    def __init__(self, elements):           
        self.elements = set()           
        for element in elements:        # passes in elements from a set
            self.elements.add(element)  # adds elements to self. 

    def __str__(self):  # joins each element as a string.
        return "{" + ', '.join([str(elt) for elt in self.elements]) + "}"

    def contains(self, element):    
        return element in self.elements

    def get_size(self, ):
        return len(self.elements)

    def print(self, output, separator):
        print(self.elements, file=output, sep=separator)

    # Returns a StaticSet containing every element from self.elements and every
    # element from other_set.
    def union(self, other_set):
        # Replace the next line with your code.
        result = set()
        for element in self.elements:
            result.add(element)
        for element in other_set.elements:
            result.add(element)
        return StaticSet(set(result))

    # Returns a StaticSet containing each element from self.elements that is also
    # in other_set.
    def intersection(self, other_set):
        # Replace the next line with your code.
        result = set()
        for element in self.elements:
            if element in (self.elements and other_set.elements):
                result.add(element)
        return StaticSet(set(result))

    # Returns a StaticSet containing each element from self.elements that is not
    # in other_set.
    def difference(self, other_set):
        # Replace the next line with your code.
        result = set()
        for element in self.elements:
            if (element in self.elements) and (element not in other_set.elements):
                result.add(element)
        return StaticSet(set(result))

    # Returns a StaticSet containing each element from self.elements that
    # satisfies the predicate.
    # - If predicate(element) returns True, element satisfies the predicate.
    # - If predicate(element) returns False, element does not satisfy the predicate.
    def filter(self, predicate):
        # Replace the next line with your code.
        result = set()
        for element in self.elements:
            if predicate(element) == True:
                result.add(element)
            elif predicate(element) == False:
                pass
        return StaticSet(set(result))

    # Calls map_function(element) for each element in self.elements and adds the returned
    # value to a StaticSet. After map_function has been called for each element
    # in self.elements, the StaticSet is returned.
    def map(self, map_function):
        # Replace the next line with your code.
        result = set()
        for element in self.elements:
            result.add(map_function(element))
        return StaticSet(set(result))
# from StaticSet import StaticSet
class StaticSetTestCase:
    def compare_sets(self,
                     test_feedback,
                     actual,
                     expected,
                     title,
                     points):
        passed = True

        # Compare actual vs. expected set's size
        if actual.get_size() != expected.get_size():
            passed = False
        else:
            # Expected and actual have equal sizes, so compare contents
            for element in expected.elements:
                if not actual.contains(element):
                    passed = False

        # Print the pass or fail message with expected and actual sets
        print(f"""{'PASS' if passed else 'FAIL'}: {title}
  Expected: {expected}
  Actual:   {actual}""",
              file=test_feedback)

        return points if passed else 0.0

    def execute(self, test_feedback):
        pass

''' instructions 2
    BinaryOpsTestCase represents an executable test case for the StaticSet's
    union(), intersection(), and difference() methods
'''
class BinaryOpsTestCase(StaticSetTestCase):
    def __init__(self,
                 A_elements,
                 B_elements,
                 expected_union_elements,
                 expected_intersection_elements,
                 expected_A_minus_B_elements,
                 expected_B_minus_A_elements):
        self.set_A = StaticSet(A_elements)
        self.set_B = StaticSet(B_elements)
        self.expected_union = StaticSet(expected_union_elements)
        self.expected_intersection = StaticSet(expected_intersection_elements)
        self.expected_A_minus_B = StaticSet(expected_A_minus_B_elements)
        self.expected_B_minus_A = StaticSet(expected_B_minus_A_elements)

    def execute(self, test_feedback):
        # Print sets A and B first
        print(f"""A = {self.set_A}""", file=test_feedback)
        print(f"""B = {self.set_B}""", file=test_feedback)

        # Create the two StaticSet objects from the StaticSet objects
        static_set_A = StaticSet(self.set_A.elements)
        static_set_B = StaticSet(self.set_B.elements)

        # Create the union, intersection, and differences
        actual_union = static_set_A.union(static_set_B)
        actual_intersection = static_set_A.intersection(static_set_B)
        actual_A_minus_B = static_set_A.difference(static_set_B)
        actual_B_minus_A = static_set_B.difference(static_set_A)

        # Verify that performing operations didn't change either StaticSet's size
        size_checks = ((static_set_A, self.set_A, "A"),
                       (static_set_B, self.set_B, "B")
                       )

        for size_check in size_checks:
            set1, set2, set_name = size_check
            if set1.get_size() != set2.get_size():
                print(f"""FAIL: creating the union/intersection/difference of static_sets A and B
changed set {set_name}'s size from {set1.get_size()} to {set2.get_size()}""",
                      file=test_feedback)
                return 0.0

        # Compare actual vs. expected sets
        total_points = 0.0
        total_points += self.compare_sets(
            test_feedback,
            actual_union,
            self.expected_union,
            "Union operation",
            1.0
        )
        total_points += self.compare_sets(
            test_feedback,
            actual_intersection,
            self.expected_intersection,
            "Intersection operation",
            1.0
        )
        total_points += self.compare_sets(
            test_feedback,
            actual_A_minus_B,
            self.expected_A_minus_B,
            "A \ B operation",
            0.5
        )
        total_points += self.compare_sets(
            test_feedback,
            actual_B_minus_A,
            self.expected_B_minus_A,
            "B \ A operation",
            0.5)

        return  total_points

''' instructions 3
    UnaryOpsTestCase represents an executable test case for the StaticSet's
    filter() and map() methods
'''
class UnaryOpsTestCase(StaticSetTestCase):
    def __init__(self,
                 source_set,
                 filter_predicate,
                 map_function,
                 expected_filtered,
                 expected_mapped
                 ):
        self.source_set = StaticSet(source_set)
        self.filter_predicate = filter_predicate
        self.map_function = map_function
        self.expected_filtered = StaticSet(expected_filtered)
        self.expected_mapped = StaticSet(expected_mapped)

    def execute(self, test_feedback):
        # Print the source set first
        print(f"""Set = {self.source_set}""", file=test_feedback)

        # Create the StaticSet object from the set source
        static_set = StaticSet(self.source_set.elements)

        # Create the filtered and mapped sets
        actual_filtered = static_set.filter(self.filter_predicate)
        actual_mapped = static_set.map(self.map_function)

        # Verify that performing operations didn't change static_set's size
        if static_set.get_size() != self.source_set.get_size():
            print(f"""FAIL: filtering and/or mapping static_set S changed S's size \
from {self.source_set.get_size()} to {static_set.get_size()}""",
                  file=test_feedback)
            return 0.0

        # Compare actual vs. expected sets
        total_points = 0.0
        total_points += self.compare_sets(
            test_feedback,
            actual_filtered,
            self.expected_filtered,
            "Filter operation",
            1.0
        )
        total_points += self.compare_sets(
            test_feedback,
            actual_mapped,
            self.expected_mapped,
            "Map operation",
            1.0
        )

        return total_points

def main():
    # First test case tests binary operations: union, intersection, and
    # difference
    binary_ops_test_case = BinaryOpsTestCase(
        (42, 63, 99, 32, 18, 77, 64, 50, 12),
        (64, 16, 32, 8, 4, 1, 2),
        (1, 2, 4, 8, 12, 16, 18, 32, 42, 50, 63, 64, 77, 99),  # expected union
        (32, 64),                                              # expected intersection
        (42, 63, 99, 18, 77, 50, 12),                          # expected A minus B
        (1, 2, 4, 8, 16)                                       # expected B minus A
   )
    binary_test_case_points = binary_ops_test_case.execute(sys.stdout)

    # Next test case tests unary operations: filter and map
    print()
    unary_ops_test_case = UnaryOpsTestCase(
        ("zero", "one", "two", "three", "four", "five",
          "six", "seven", "eight", "nine", "ten"),
        # Filter each string with a length <= 4
        lambda str: len(str) <= 4,
        # Map from the string to the string's length
        lambda str: len(str),
        ("zero", "one", "two", "four", "five", "six", "nine", "ten"), # expected filtered
        (3, 4, 5)                                              # expected mapped
   )
    unary_test_case_points = unary_ops_test_case.execute(sys.stdout)

    print()
    print("Binary operations score:", binary_test_case_points, "out of 3")
    print("Unary operations score:", unary_test_case_points, "out of 2")

if __name__ == '__main__':
    main()