#!/usr/bin/env python3
"""
Automated release script for reflex-katex library.

This script:
1. Runs poetry version (patch/minor/major) to increment the version
2. Commits the version bump to main branch
3. Gets the new version number
4. Creates a git tag with the version
5. Pushes the tag and commit to origin

Usage:
    python release.py --patch    # Increment patch version (0.0.1 -> 0.0.2)
    python release.py --minor    # Increment minor version (0.0.1 -> 0.1.0)
    python release.py --major    # Increment major version (0.0.1 -> 1.0.0)
    python release.py           # Interactive selection (IDE mode)
"""

import argparse
import re
import subprocess
import sys


def run_command(cmd, description):
    """Run a command and return the output, or exit on failure."""
    print(f"Running: {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        if result.stdout.strip():
            print(f"Output: {result.stdout.strip()}")
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error {description}: {e}")
        if e.stderr:
            print(f"Error output: {e.stderr}")
        sys.exit(1)

def get_version_type():
    """Get version type interactively from user."""
    print("\nSelect version increment type:")
    print("1. patch (0.0.1 -> 0.0.2) - Bug fixes")
    print("2. minor (0.0.1 -> 0.1.0) - New features")
    print("3. major (0.0.1 -> 1.0.0) - Breaking changes")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-3): ").strip()
            if choice == "1":
                return "patch"
            elif choice == "2":
                return "minor"
            elif choice == "3":
                return "major"
            else:
                print("❌ Invalid choice. Please enter 1, 2, or 3.")
        except KeyboardInterrupt:
            print("\n❌ Release cancelled by user.")
            sys.exit(1)


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Automated release script for reflex-katex library")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--patch", action="store_true", help="Increment patch version (bug fixes)")
    group.add_argument("--minor", action="store_true", help="Increment minor version (new features)")
    group.add_argument("--major", action="store_true", help="Increment major version (breaking changes)")
    
    args = parser.parse_args()
    
    # Determine version type
    if args.patch:
        version_type = "patch"
    elif args.minor:
        version_type = "minor"
    elif args.major:
        version_type = "major"
    else:
        # Interactive mode
        version_type = get_version_type()
    
    print("🚀 Starting automated release process...")
    print(f"   Version type: {version_type}")
    
    # Step 1: Increment version
    print(f"\n📝 Step 1: Incrementing {version_type} version...")
    version_output = run_command(f"poetry version {version_type}", "incrementing version")
    
    # Step 2: Extract the new version number
    print("\n🔍 Step 2: Getting new version number...")
    # Poetry version outputs something like "Bumping version from 0.0.5 to 0.0.6"
    version_match = re.search(r'to (\d+\.\d+\.\d+)', version_output)
    if not version_match:
        print("❌ Could not extract version number from poetry output")
        sys.exit(1)
    
    new_version = version_match.group(1)
    tag_name = new_version  # No 'v' prefix - matches GitHub workflow tag pattern
    print(f"New version: {new_version}")
    print(f"Tag name: {tag_name}")
    
    # Step 3: Commit version bump to main
    print("\n💾 Step 3: Committing version bump to main...")
    commit_message = f"Bump version to {new_version} in pyproject.toml"
    run_command("git add .", "staging all changes")
    run_command(f'git commit -m "{commit_message}"', "committing version bump")
    
    # Step 4: Create git tag
    print(f"\n🏷️  Step 4: Creating git tag {tag_name}...")
    run_command(f"git tag {tag_name}", "creating git tag")
    
    # Step 5: Push commit and tag to origin
    print("\n⬆️  Step 5: Pushing commit and tag to origin...")
    run_command("git push origin main", "pushing commit to origin")
    run_command(f"git push origin {tag_name}", "pushing tag to origin")
    
    print("\n✅ Release process completed successfully!")
    print(f"   Version: {new_version}")
    print(f"   Tag: {tag_name}")
    print("   Commit and tag pushed to origin")

if __name__ == "__main__":
    main()
