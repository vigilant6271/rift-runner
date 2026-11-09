#!/usr/bin/env python3
"""
Rift Runner APK Builder
=======================
This script creates a ready-to-build Android project and, if the Android SDK
is available, builds the APK automatically.

Usage:
  python3 build_apk.py [--sdk /path/to/android-sdk]

Without the SDK, it prints exact manual build instructions.
"""
import os, sys, subprocess, shutil, zipfile, struct, zlib

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

def check_sdk():
    sdk = os.environ.get('ANDROID_HOME') or os.environ.get('ANDROID_SDK_ROOT')
    if '--sdk' in sys.argv:
        idx = sys.argv.index('--sdk')
        sdk = sys.argv[idx+1] if idx+1 < len(sys.argv) else sdk
    if sdk and os.path.isdir(sdk):
        return sdk
    return None

def run_gradle(sdk_path):
    gradle_wrapper = os.path.join(PROJECT_DIR, 'gradlew')
    if not os.path.isfile(gradle_wrapper):
        print("No gradlew found. Run: gradle wrapper first.")
        return False
    env = os.environ.copy()
    env['ANDROID_HOME'] = sdk_path
    result = subprocess.run(
        [gradle_wrapper, 'assembleRelease', '--no-daemon'],
        cwd=PROJECT_DIR, env=env, capture_output=False
    )
    return result.returncode == 0

def print_manual_instructions(sdk):
    print("""
╔══════════════════════════════════════════════════════════════════╗
║            RIFT RUNNER — APK BUILD INSTRUCTIONS                  ║
╚══════════════════════════════════════════════════════════════════╝

The Android project is fully generated at:
  /root/riftrunner-android/

To build the APK you need:
  • Java JDK 11 or 17    (https://adoptium.net)
  • Android SDK          (https://developer.android.com/studio#command-tools)
  • Gradle 8.x           (https://gradle.org/releases/)

─── OPTION A: Android Studio (easiest) ────────────────────────────
1. Install Android Studio: https://developer.android.com/studio
2. Open → /root/riftrunner-android/
3. Build → Generate Signed Bundle / APK → APK → Debug or Release
4. APK will appear in:
   app/build/outputs/apk/debug/app-debug.apk

─── OPTION B: Command Line ─────────────────────────────────────────
# Install SDK command-line tools, then:

export ANDROID_HOME=$HOME/android-sdk
export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools

# Accept licenses
yes | sdkmanager --licenses
sdkmanager "platform-tools" "platforms;android-34" "build-tools;34.0.0"

# Build
cd /root/riftrunner-android
gradle wrapper            # or install gradlew manually
chmod +x gradlew
./gradlew assembleDebug

# Output:
# app/build/outputs/apk/debug/app-debug.apk

─── OPTION C: Install via ADB (for testing on device) ──────────────
adb install app/build/outputs/apk/debug/app-debug.apk

─── QUICK ALTERNATIVE: PWA / WebAPK ────────────────────────────────
The game at /root/game.html is a complete, self-contained HTML5 file.
Serve it over HTTPS and Android Chrome will offer "Add to Home Screen"
which creates a WebAPK — indistinguishable from a native app.

python3 -m http.server 8080   # then open http://YOUR_IP:8080/game.html
""")

def main():
    print("Rift Runner APK Builder")
    print(f"Project: {PROJECT_DIR}")
    sdk = check_sdk()
    if sdk:
        print(f"Android SDK found: {sdk}")
        if run_gradle(sdk):
            apk = os.path.join(PROJECT_DIR, 'app/build/outputs/apk/release/app-release.apk')
            if os.path.isfile(apk):
                print(f"\n✓ APK built: {apk}")
            else:
                print("\n✓ Build succeeded. Check app/build/outputs/apk/")
        else:
            print("\n✗ Gradle build failed.")
            print_manual_instructions(sdk)
    else:
        print_manual_instructions(None)

if __name__ == '__main__':
    main()
