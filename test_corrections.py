"""
Comprehensive test suite for corrected implementations.
Tests all edge cases, bugs, and scenarios identified in the code review.
"""

from correct_task1 import calculate_average_order_value
from correct_task2 import count_valid_emails
from correct_task3 import average_valid_measurements


def test_task1():
    """Test Task 1: Average Order Value"""
    print("=" * 60)
    print("TASK 1: Average Order Value - Test Results")
    print("=" * 60)
    
    # Test 1: Empty list
    result = calculate_average_order_value([])
    assert result == 0, f"Empty list failed: expected 0, got {result}"
    print("✓ Empty list: 0")
    
    # Test 2: All cancelled orders
    result = calculate_average_order_value([
        {"status": "cancelled", "amount": 100},
        {"status": "cancelled", "amount": 200}
    ])
    assert result == 0, f"All cancelled failed: expected 0, got {result}"
    print("✓ All cancelled orders: 0")
    
    # Test 3: Mixed statuses (correct average calculation)
    result = calculate_average_order_value([
        {"status": "completed", "amount": 100},
        {"status": "cancelled", "amount": 50},
        {"status": "completed", "amount": 200}
    ])
    assert result == 150.0, f"Mixed statuses failed: expected 150.0, got {result}"
    print("✓ Mixed statuses (100 + 200) / 2: 150.0")
    
    # Test 4: Missing keys (graceful handling)
    result = calculate_average_order_value([
        {"status": "completed"},  # Missing amount
        {"amount": 100},  # Missing status
        {"status": "completed", "amount": 200}
    ])
    assert result == 100.0, f"Missing keys failed: expected 100.0, got {result}"
    print("✓ Missing keys handled gracefully: 100.0")
    
    # Test 5: Only non-cancelled orders
    result = calculate_average_order_value([
        {"status": "completed", "amount": 50},
        {"status": "pending", "amount": 100},
        {"status": "shipped", "amount": 150}
    ])
    assert result == 100.0, f"Non-cancelled only failed: expected 100.0, got {result}"
    print("✓ Only non-cancelled orders: 100.0")
    
    # Test 6: Float amounts
    result = calculate_average_order_value([
        {"status": "completed", "amount": 99.99},
        {"status": "completed", "amount": 150.50}
    ])
    expected = (99.99 + 150.50) / 2
    assert abs(result - expected) < 0.01, f"Float amounts failed: expected {expected}, got {result}"
    print(f"✓ Float amounts: {result:.2f}")
    
    # Test 7: Zero amounts
    result = calculate_average_order_value([
        {"status": "completed", "amount": 0},
        {"status": "completed", "amount": 100}
    ])
    assert result == 50.0, f"Zero amounts failed: expected 50.0, got {result}"
    print("✓ Zero amounts: 50.0")
    
    print("\n✅ All Task 1 tests passed!\n")


def test_task2():
    """Test Task 2: Count Valid Emails"""
    print("=" * 60)
    print("TASK 2: Count Valid Emails - Test Results")
    print("=" * 60)
    
    # Test 1: Empty list
    result = count_valid_emails([])
    assert result == 0, f"Empty list failed: expected 0, got {result}"
    print("✓ Empty list: 0")
    
    # Test 2: Valid emails
    result = count_valid_emails([
        "user@domain.com",
        "test@example.org",
        "admin@company.co.uk"
    ])
    assert result == 3, f"Valid emails failed: expected 3, got {result}"
    print("✓ Valid emails: 3")
    
    # Test 3: Invalid @ patterns
    result = count_valid_emails([
        "@",  # Only @
        "@@",  # Double @
        "@domain.com",  # No local part
        "user@",  # No domain part
        "nodomain"  # No @ at all
    ])
    assert result == 0, f"Invalid @ patterns failed: expected 0, got {result}"
    print("✓ Invalid @ patterns: 0")
    
    # Test 4: Multiple @ symbols
    result = count_valid_emails([
        "user@@domain.com",
        "a@b@c.com"
    ])
    assert result == 0, f"Multiple @ failed: expected 0, got {result}"
    print("✓ Multiple @ symbols: 0")
    
    # Test 5: Mixed types (None, integers, objects)
    result = count_valid_emails([
        "valid@email.com",
        None,
        123,
        "another@valid.com",
        {"not": "email"}
    ])
    assert result == 2, f"Mixed types failed: expected 2, got {result}"
    print("✓ Mixed types handled: 2")
    
    # Test 6: Empty strings and whitespace
    result = count_valid_emails([
        "",
        "   ",
        " @ ",
        "valid@email.com"
    ])
    assert result == 1, f"Empty/whitespace failed: expected 1, got {result}"
    print("✓ Empty strings and whitespace: 1")
    
    # Test 7: Edge cases with valid structure
    result = count_valid_emails([
        "a@b.c",  # Minimal valid
        "user.name@domain.com",  # Dot in local
        "user+tag@domain.com"  # Plus in local
    ])
    assert result == 3, f"Edge valid cases failed: expected 3, got {result}"
    print("✓ Edge valid cases: 3")
    
    # Test 8: All invalid
    result = count_valid_emails([None, None, "", 123])
    assert result == 0, f"All invalid failed: expected 0, got {result}"
    print("✓ All invalid: 0")
    
    print("\n✅ All Task 2 tests passed!\n")


def test_task3():
    """Test Task 3: Aggregate Valid Measurements"""
    print("=" * 60)
    print("TASK 3: Aggregate Valid Measurements - Test Results")
    print("=" * 60)
    
    # Test 1: Empty list
    result = average_valid_measurements([])
    assert result == 0, f"Empty list failed: expected 0, got {result}"
    print("✓ Empty list: 0")
    
    # Test 2: All None values
    result = average_valid_measurements([None, None, None])
    assert result == 0, f"All None failed: expected 0, got {result}"
    print("✓ All None values: 0")
    
    # Test 3: Valid numeric values
    result = average_valid_measurements([10, 20, 30])
    assert result == 20.0, f"Valid values failed: expected 20.0, got {result}"
    print("✓ Valid numeric values (10, 20, 30): 20.0")
    
    # Test 4: Mixed with None (correct denominator)
    result = average_valid_measurements([10, None, 20, None, 30])
    assert result == 20.0, f"Mixed with None failed: expected 20.0, got {result}"
    print("✓ Mixed with None (10, 20, 30): 20.0")
    
    # Test 5: String numbers (type conversion)
    result = average_valid_measurements([10, "20", 30])
    assert result == 20.0, f"String numbers failed: expected 20.0, got {result}"
    print("✓ String numbers converted: 20.0")
    
    # Test 6: Invalid types (graceful skip)
    result = average_valid_measurements([10, "abc", None, {}, 30])
    assert result == 20.0, f"Invalid types failed: expected 20.0, got {result}"
    print("✓ Invalid types skipped: 20.0")
    
    # Test 7: Float values
    result = average_valid_measurements([10.5, 20.5, 30.0])
    expected = (10.5 + 20.5 + 30.0) / 3
    assert abs(result - expected) < 0.01, f"Float values failed: expected {expected}, got {result}"
    print(f"✓ Float values: {result:.2f}")
    
    # Test 8: Negative numbers
    result = average_valid_measurements([-10, 0, 10])
    assert result == 0.0, f"Negative numbers failed: expected 0.0, got {result}"
    print("✓ Negative numbers: 0.0")
    
    # Test 9: Single valid value
    result = average_valid_measurements([None, None, 42, None])
    assert result == 42.0, f"Single valid failed: expected 42.0, got {result}"
    print("✓ Single valid value: 42.0")
    
    # Test 10: Zero values
    result = average_valid_measurements([0, 0, 0])
    assert result == 0.0, f"Zero values failed: expected 0.0, got {result}"
    print("✓ Zero values: 0.0")
    
    # Test 11: Large numbers
    result = average_valid_measurements([1000000, 2000000, 3000000])
    assert result == 2000000.0, f"Large numbers failed: expected 2000000.0, got {result}"
    print("✓ Large numbers: 2000000.0")
    
    print("\n✅ All Task 3 tests passed!\n")


def run_all_tests():
    """Run all test suites"""
    print("\n" + "=" * 60)
    print("RUNNING COMPREHENSIVE TEST SUITE")
    print("=" * 60 + "\n")
    
    try:
        test_task1()
        test_task2()
        test_task3()
        
        print("=" * 60)
        print("🎉 ALL TESTS PASSED SUCCESSFULLY! 🎉")
        print("=" * 60)
        print("\nSummary:")
        print("- Task 1: 7 test cases passed")
        print("- Task 2: 8 test cases passed")
        print("- Task 3: 11 test cases passed")
        print("- Total: 26 test cases passed")
        print("\nAll corrected implementations are working correctly!")
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        return False
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {e}")
        return False
    
    return True


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
