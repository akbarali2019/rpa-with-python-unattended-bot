def search_inqFacility(self, facilityNumber):
        try:
            pyautogui.press('tab', 4, 0.2)
            pyautogui.press('right', 2, 0.2)

            myDesiredVal = facilityNumber  # Set your desired value

            # Initial copy and paste to get the screenCopiedVal
            pyautogui.hotkey('ctrl', 'c')  # Copy from screen
            time.sleep(0.3)  # Short delay to ensure copy completes
            screenCopiedVal = pyperclip.paste()  # Paste copied value

            # Use a for loop with a maximum of 300 iterations
            for _ in range(300):  # Try up to 300 times
                if screenCopiedVal == myDesiredVal:
                    #pyautogui.press('enter')  # Perform the desired action on match
                    print("Match found:", screenCopiedVal)
                    time.sleep(0.5)  # Optional delay after match
                    return True  # Return True when match is found

                pyautogui.press('down')  # Perform the action (e.g., move down)
                time.sleep(0.1)  # Delay to avoid overwhelming the CPU

                pyautogui.hotkey('ctrl', 'c')  # Copy new value from screen
                time.sleep(0.3)  # Short delay
                screenCopiedVal = pyperclip.paste()  # Update screenCopiedVal

            # If no match is found within 300 iterations, return False
            print("Match not found within 300 iterations")
            return False

        except Exception as e:
            # Log the error for debugging
            self.logger.error(f"Error in search_inqFacility with facilityNumber '{facilityNumber}': {e}")
            return False  # Return False in case of an error

