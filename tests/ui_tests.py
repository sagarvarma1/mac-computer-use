#!/usr/bin/env python3
"""
Tests for Mac Control Tools

This script tests the mouse and keyboard control functions from tools.py.
It includes both automated tests and interactive tests that require user verification.
"""

import time
import unittest
from tools import (
    move_mouse, click_mouse, double_click, drag_mouse, get_mouse_position,
    type_text, press_key, press_hotkey, key_down, key_up
)

class AutomatedTests(unittest.TestCase):
    """Tests that can be verified programmatically"""
    
    def test_get_mouse_position(self):
        """Test that get_mouse_position returns a tuple of two integers"""
        position = get_mouse_position()
        self.assertIsInstance(position, tuple)
        self.assertEqual(len(position), 2)
        self.assertIsInstance(position[0], int)
        self.assertIsInstance(position[1], int)
    
    def test_move_mouse_returns_position(self):
        """Test that move_mouse returns the new position"""
        # Save current position to restore later
        original_position = get_mouse_position()
        
        # Move mouse and check return value
        new_position = move_mouse(100, 100)
        self.assertIsInstance(new_position, tuple)
        self.assertEqual(len(new_position), 2)
        
        # Restore original position
        move_mouse(*original_position)

class InteractiveTests(unittest.TestCase):
    """Tests that require user verification"""
    
    def setUp(self):
        """Prepare for each test"""
        # Save original mouse position
        self.original_position = get_mouse_position()
        print("\n" + "="*50)
        print(f"Original mouse position: {self.original_position}")
        print("="*50)
        
        # Give user time to prepare
        print("Test will begin in 3 seconds...")
        time.sleep(3)
    
    def tearDown(self):
        """Clean up after each test"""
        # Return mouse to original position
        move_mouse(*self.original_position)
        print(f"Mouse returned to original position: {self.original_position}")
        print("="*50)
        
        # Give user time between tests
        time.sleep(1)
    
    def test_move_mouse(self):
        """Test moving the mouse to different positions"""
        print("TESTING: move_mouse()")
        
        # Test moving to absolute coordinates
        print("Moving mouse to position (100, 100)...")
        move_mouse(100, 100, duration=0.5)
        time.sleep(1)
        
        # Test moving to center of screen
        import pyautogui
        screen_width, screen_height = pyautogui.size()
        center_x, center_y = screen_width // 2, screen_height // 2
        print(f"Moving mouse to center of screen ({center_x}, {center_y})...")
        move_mouse(center_x, center_y, duration=0.5)
        time.sleep(1)
        
        # Verify with user
        result = input("Did the mouse move to the specified positions? (y/n): ")
        self.assertEqual(result.lower(), 'y')
    
    def test_click_mouse(self):
        """Test clicking the mouse"""
        print("TESTING: click_mouse()")
        print("Opening a text editor is recommended for this test.")
        
        # Move to a safe position and click
        print("Moving to position (200, 200) and clicking...")
        click_mouse(x=200, y=200)
        time.sleep(1)
        
        # Verify with user
        result = input("Did the mouse click at position (200, 200)? (y/n): ")
        self.assertEqual(result.lower(), 'y')
    
    def test_double_click(self):
        """Test double-clicking the mouse"""
        print("TESTING: double_click()")
        print("Opening a text editor or file browser is recommended for this test.")
        
        # Move to a safe position and double-click
        print("Moving to position (300, 300) and double-clicking...")
        double_click(x=300, y=300)
        time.sleep(1)
        
        # Verify with user
        result = input("Did the mouse double-click at position (300, 300)? (y/n): ")
        self.assertEqual(result.lower(), 'y')
    
    def test_drag_mouse(self):
        """Test dragging the mouse"""
        print("TESTING: drag_mouse()")
        print("Opening a drawing program or text editor is recommended for this test.")
        
        # Drag from one position to another
        print("Dragging from (400, 400) to (500, 500)...")
        drag_mouse(400, 400, 500, 500, duration=1.0)
        time.sleep(1)
        
        # Verify with user
        result = input("Did the mouse drag from (400, 400) to (500, 500)? (y/n): ")
        self.assertEqual(result.lower(), 'y')
    
    def test_type_text(self):
        """Test typing text"""
        print("TESTING: type_text()")
        print("Please open a text editor and place the cursor where text can be typed.")
        input("Press Enter when ready...")
        
        # Type some text
        test_text = "Hello, this is a test of the typing function!"
        print(f"Typing: '{test_text}'")
        type_text(test_text)
        time.sleep(1)
        
        # Verify with user
        result = input("Was the text typed correctly? (y/n): ")
        self.assertEqual(result.lower(), 'y')
    
    def test_press_key(self):
        """Test pressing individual keys"""
        print("TESTING: press_key()")
        print("Please open a text editor and place the cursor where keys can be pressed.")
        input("Press Enter when ready...")
        
        # Press some keys
        print("Pressing the 'a' key...")
        press_key('a')
        time.sleep(0.5)
        
        print("Pressing the 'enter' key...")
        press_key('enter')
        time.sleep(0.5)
        
        # Verify with user
        result = input("Were the keys pressed correctly? (y/n): ")
        self.assertEqual(result.lower(), 'y')
    
    def test_press_hotkey(self):
        """Test pressing hotkeys"""
        print("TESTING: press_hotkey()")
        print("Please open a text editor with some text that can be selected and copied.")
        input("Press Enter when ready...")
        
        # Test copy hotkey (Command+C on Mac)
        print("Selecting all text with Command+A and copying with Command+C...")
        press_hotkey('command', 'a')
        time.sleep(0.5)
        press_hotkey('command', 'c')
        time.sleep(0.5)
        
        # Verify with user
        result = input("Did the hotkeys work correctly? (y/n): ")
        self.assertEqual(result.lower(), 'y')
    
    def test_key_down_and_up(self):
        """Test pressing and releasing keys"""
        print("TESTING: key_down() and key_up()")
        print("Please open a text editor and place the cursor where keys can be pressed.")
        input("Press Enter when ready...")
        
        # Press and hold a key, then release it
        print("Pressing and holding the 'a' key for 2 seconds...")
        key_down('a')
        time.sleep(2)
        key_up('a')
        time.sleep(0.5)
        
        # Verify with user
        result = input("Was the key pressed and held correctly? (y/n): ")
        self.assertEqual(result.lower(), 'y')

def run_automated_tests():
    """Run only the automated tests"""
    suite = unittest.TestLoader().loadTestsFromTestCase(AutomatedTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

def run_interactive_tests():
    """Run only the interactive tests"""
    suite = unittest.TestLoader().loadTestsFromTestCase(InteractiveTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

def run_all_tests():
    """Run all tests"""
    automated_suite = unittest.TestLoader().loadTestsFromTestCase(AutomatedTests)
    interactive_suite = unittest.TestLoader().loadTestsFromTestCase(InteractiveTests)
    all_tests = unittest.TestSuite([automated_suite, interactive_suite])
    unittest.TextTestRunner(verbosity=2).run(all_tests)

if __name__ == "__main__":
    print("Mac Control Tools Test Suite")
    print("===========================")
    print("1. Run automated tests only")
    print("2. Run interactive tests only")
    print("3. Run all tests")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        run_automated_tests()
    elif choice == '2':
        run_interactive_tests()
    elif choice == '3':
        run_all_tests()
    else:
        print("Invalid choice. Exiting.") 