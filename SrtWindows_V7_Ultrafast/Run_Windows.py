import os
import sys
import platform
import webbrowser

# Fix for Windows DLL loading issues (Python 3.8+)
if platform.system() == "Windows":
    runtime_dir = os.path.abspath("pyarmor_runtime_000000")
    if os.path.exists(runtime_dir):
        # Force add the directory to DLL search path
        os.add_dll_directory(runtime_dir)
    
    # Check Python version
    major, minor = sys.version_info[:2]
    if (major, minor) != (3, 13):
        print("!" * 70)
        print(f"CRITICAL ERROR: Python {major}.{minor} detected.")
        print("This program REQUIRES Python 3.13 (64-bit) to function correctly.")
        print("-" * 70)
        print("Step 1: Install Python 3.13 from the link below:")
        print("URL: https://www.python.org/ftp/python/3.13.2/python-3.13.2-amd64.exe")
        print("\nStep 2: Restart your terminal/PowerShell and try again.")
        print("!" * 70)
        
        choice = input("\nWould you like to open the download page now? (y/n): ")
        if choice.lower() == 'y':
            webbrowser.open("https://www.python.org/ftp/python/3.13.2/python-3.13.2-amd64.exe")
        
        sys.exit(1)

try:
    print("🚀 Launching SRT Suite...")
    import main
except ImportError as e:
    print(f"❌ Error loading protection: {e}")
    print("\nPRO TIP: You might need to install Microsoft Visual C++ Runtime.")
    url = "https://aka.ms/vs/17/release/vc_redist.x64.exe"
    print(f"Download Link: {url}")
    
    choice = input("\nWould you like to open the C++ runtime download link? (y/n): ")
    if choice.lower() == 'y':
        webbrowser.open(url)
    
    input("\nPress Enter to exit...")
