#!/usr/bin/env python3

import os
import subprocess
import argparse
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def check_repomix_installed():
    """Check if repomix is installed and available in PATH"""
    try:
        result = subprocess.run(["repomix", "--version"], capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def run_repomix():
    """Run repomix to generate codebase snapshot"""
    print("🔄 Running repomix to create codebase snapshot...")
    
    try:
        result = subprocess.run(["repomix"], capture_output=True, text=True, cwd=".")
        if result.returncode != 0:
            print(f"❌ Error running repomix: {result.stderr}")
            return None
        
        print("✅ Repomix snapshot created successfully")
        return "repomix-output.xml"
    
    except Exception as e:
        print(f"❌ Failed to run repomix: {e}")
        return None

def read_codebase_content(file_path):
    """Read the repomix output file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"❌ Error reading {file_path}: {e}")
        return None

def analyze_with_gemini(instruction, codebase_content, api_key):
    """Send codebase and instruction to Gemini for analysis"""
    
    system_prompt = """You are an expert software engineer and code analyst specializing in comprehensive codebase analysis. Your role is to help AI coding agents understand entire codebases for debugging, planning, and development tasks.

CORE RESPONSIBILITIES:
1. **Holistic Analysis**: Analyze the complete codebase structure, not just isolated snippets
2. **Interdependency Mapping**: Understand how modules, classes, and functions interact across the entire project
3. **Architectural Understanding**: Identify design patterns, data flow, and system architecture
4. **Debugging Context**: Provide insights that help trace issues across multiple files and layers
5. **Planning Support**: Offer guidance for modifications that considers ripple effects

ANALYSIS APPROACH:
- Read through the entire codebase to understand the project's purpose and structure
- Map out key dependencies and relationships between components
- Identify critical paths and potential bottlenecks
- Consider how changes in one area might affect other parts
- Focus on providing actionable, specific insights with file references

RESPONSE FORMAT:
- Be detailed and comprehensive
- Include specific file paths and references when relevant
- Quote the code snippets in fence blocks when relevant
- Highlight important relationships and dependencies
- Provide clear, actionable recommendations
- Structure your response logically (overview → specific analysis → recommendations)

The user will provide an instruction followed by the complete codebase content. Analyze thoroughly before responding."""

    try:
        print("🔄 Analyzing codebase with Gemini...")
        
        client = genai.Client(api_key=api_key)
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.2
            ),
            contents=f"INSTRUCTION: {instruction}\n\n=== COMPLETE CODEBASE ===\n{codebase_content}"
        )
        
        print("✅ Analysis completed")
        return response.text
    
    except Exception as e:
        print(f"❌ Error calling Gemini API: {e}")
        return None

def cleanup_file(file_path):
    """Clean up the repomix output file"""
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"🧹 Cleaned up {file_path}")
    except Exception as e:
        print(f"⚠️  Warning: Could not clean up {file_path}: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Codebase Analysis Tool - Analyze entire codebases using Repomix and Gemini",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example:
  python3 codeingest.py --instruction "I'm getting a bug in user authentication. Help me understand the auth flow across the codebase"
        """
    )
    
    parser.add_argument(
        "--instruction", 
        required=True, 
        help="The instruction/question for analyzing the codebase"
    )
    
    parser.add_argument(
        "--verbose", 
        action="store_true", 
        help="Enable verbose output"
    )
    
    args = parser.parse_args()
    
    # Load environment variables
    load_dotenv()
    
    # Check for API key
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    if not GEMINI_API_KEY:
        print("❌ Error: GEMINI_API_KEY environment variable not set")
        print("Please set your Gemini API key in a .env file or environment variable")
        sys.exit(1)
    
    # Check if repomix is installed
    if not check_repomix_installed():
        print("❌ Error: repomix is not installed or not found in PATH")
        print("Please install repomix first: npm install -g repomix")
        sys.exit(1)
    
    if args.verbose:
        print(f"📝 Instruction: {args.instruction}")
        print(f"📁 Working directory: {os.getcwd()}")
    
    repomix_output_file = None
    
    try:
        # Step 1: Run repomix
        repomix_output_file = run_repomix()
        if not repomix_output_file:
            sys.exit(1)
        
        # Step 2: Read the codebase content
        codebase_content = read_codebase_content(repomix_output_file)
        if not codebase_content:
            sys.exit(1)
        
        if args.verbose:
            print(f"📊 Codebase content size: {len(codebase_content)} characters")
        
        # Step 3: Analyze with Gemini
        analysis_result = analyze_with_gemini(args.instruction, codebase_content, GEMINI_API_KEY)
        if not analysis_result:
            sys.exit(1)
        
        # Step 4: Output the result
        print("\n" + "="*60)
        print("🔍 CODEBASE ANALYSIS RESULT")
        print("="*60)
        print(analysis_result)
        print("="*60)
        
    except KeyboardInterrupt:
        print("\n⚠️  Operation cancelled by user")
        sys.exit(1)
    
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)
    
    finally:
        # Step 5: Clean up
        if repomix_output_file:
            cleanup_file(repomix_output_file)

if __name__ == "__main__":
    main()