"""
Script to capture screenshots from the Django application
This script opens each page and guides you to take screenshots
"""

import webbrowser
import time

# Define the pages to capture
PAGES = {
    'home.png': 'http://127.0.0.1:8000/',
    'doctor-list.png': 'http://127.0.0.1:8000/doctors/',
    'book-appointment.png': 'http://127.0.0.1:8000/book/1/',
    'patient-login.png': 'http://127.0.0.1:8000/patient-login/',
    'admin-login.png': 'http://127.0.0.1:8000/admin-panel/login/',
}

def main():
    print("=" * 60)
    print("HealthHub Screenshot Capture Guide")
    print("=" * 60)
    print("\nBefore running this script:")
    print("1. Make sure Django server is running: python manage.py runserver 127.0.0.1:8000")
    print("2. Have your screenshot tool ready (Windows Snipping Tool or similar)")
    print("3. Save each screenshot in the 'screenshots' folder with the exact filename\n")
    
    for filename, url in PAGES.items():
        print(f"\n{'=' * 60}")
        print(f"Screenshot: {filename}")
        print(f"URL: {url}")
        print(f"{'=' * 60}")
        
        response = input(f"\nReady to capture {filename}? (yes/no/skip): ").lower().strip()
        
        if response == 'yes' or response == 'y':
            print(f"\nOpening {url} in browser...")
            webbrowser.open(url)
            time.sleep(2)
            
            print(f"\n1. Take a screenshot of the page")
            print(f"2. Save it as: screenshots/{filename}")
            print(f"3. Press Enter when done...")
            input()
            
            print(f"✓ {filename} - Ready to commit")
        elif response == 'skip' or response == 's':
            print(f"⊘ Skipping {filename}")
        else:
            print("⊘ Cancelled")
            break
    
    print(f"\n{'=' * 60}")
    print("Screenshot capture complete!")
    print(f"{'=' * 60}")
    print("\nNext steps:")
    print("1. Verify all screenshots are saved in the screenshots/ folder")
    print("2. Run: git add screenshots/*.png")
    print("3. Run: git commit -m 'Add UI screenshots'")
    print("4. Run: git push origin main")

if __name__ == '__main__':
    main()
