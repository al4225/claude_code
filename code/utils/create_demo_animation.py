#!/usr/bin/env python3
"""
Create Demo Animation Script
Generates an animated GIF showing Claude Code usage from installation to basic operations
"""

import os
import time
from PIL import Image, ImageDraw, ImageFont
import numpy as np

class TerminalAnimator:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.bg_color = (30, 30, 30)  # Dark terminal background
        self.text_color = (200, 200, 200)  # Light gray text
        self.prompt_color = (100, 200, 100)  # Green prompt
        self.output_color = (150, 150, 250)  # Light blue output
        self.frames = []
        
        # Try to use a monospace font
        try:
            self.font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 14)
        except:
            self.font = ImageFont.load_default()
    
    def create_frame(self, lines):
        """Create a single frame with terminal content"""
        img = Image.new('RGB', (self.width, self.height), self.bg_color)
        draw = ImageDraw.Draw(img)
        
        # Draw terminal header
        draw.rectangle([(0, 0), (self.width, 30)], fill=(50, 50, 50))
        draw.text((10, 8), "Terminal - Claude Code Demo", fill=(200, 200, 200), font=self.font)
        
        # Draw terminal content
        y_offset = 40
        for line in lines:
            if line.startswith('$'):
                # Command prompt
                draw.text((10, y_offset), line, fill=self.prompt_color, font=self.font)
            elif line.startswith('>'):
                # User input
                draw.text((10, y_offset), line, fill=(100, 250, 100), font=self.font)
            elif line.startswith('#'):
                # Comments
                draw.text((10, y_offset), line, fill=(100, 100, 100), font=self.font)
            else:
                # Output
                draw.text((10, y_offset), line, fill=self.text_color, font=self.font)
            y_offset += 20
        
        return img
    
    def add_typing_effect(self, full_line, prefix="", frames_per_char=2):
        """Add frames showing typing effect"""
        for i in range(len(full_line) + 1):
            partial_line = prefix + full_line[:i] + "_"
            for _ in range(frames_per_char):
                yield partial_line
    
    def generate_demo(self):
        """Generate the full demo animation"""
        scenarios = [
            # Installation
            {
                'title': "# Installing Claude Code",
                'lines': [
                    "# Installing Claude Code",
                    "",
                    "$ npm install -g @anthropic-ai/claude-code",
                    "added 142 packages in 15s",
                    "",
                    "$ export ANTHROPIC_API_KEY='sk-ant-...'",
                    "",
                    "$ claude-code --version",
                    "claude-code version 1.0.0"
                ]
            },
            # Starting Claude Code
            {
                'title': "# Starting Claude Code",
                'lines': [
                    "# Starting Claude Code",
                    "",
                    "$ claude-code",
                    "Welcome to Claude Code!",
                    "Type your request or /help for commands",
                    "",
                    "> Hello! Create a simple Python hello world program",
                    "",
                    "Creating hello.py...",
                    "✓ File created successfully"
                ]
            },
            # Code explanation
            {
                'title': "# Code Explanation",
                'lines': [
                    "# Code Explanation",
                    "",
                    "> Explain the code in calculator.py",
                    "",
                    "Reading calculator.py...",
                    "",
                    "This file contains a simple calculator with:",
                    "- add(a, b): Returns sum of two numbers",
                    "- subtract(a, b): Returns difference",
                    "- calculate(): Main function that routes operations"
                ]
            },
            # Debugging
            {
                'title': "# Debugging Code",
                'lines': [
                    "# Debugging Code",
                    "",
                    "> My code has an error, please help debug",
                    "",
                    "Analyzing buggy_code.py...",
                    "",
                    "Found issues:",
                    "- Line 8: Division by zero not handled",
                    "- Line 15: Using == instead of = for assignment",
                    "- Line 22: Missing vowels 'o' and 'u'",
                    "",
                    "Would you like me to fix these issues?"
                ]
            },
            # Git operations
            {
                'title': "# Git Integration",
                'lines': [
                    "# Git Integration",
                    "",
                    "> Show git status",
                    "",
                    "$ git status",
                    "On branch main",
                    "Changes to be committed:",
                    "  new file:   calculator.py",
                    "  new file:   todo_app.py",
                    "",
                    "> Commit with message 'Add initial features'",
                    "",
                    "✓ Changes committed successfully"
                ]
            }
        ]
        
        # Generate frames for each scenario
        for scenario in scenarios:
            lines = []
            # Show title
            lines.append(scenario['title'])
            self.frames.extend([self.create_frame(lines)] * 30)
            
            # Show content with typing effect for commands
            for line in scenario['lines'][1:]:
                if line.startswith('>') or line.startswith('$'):
                    # Typing effect for commands
                    base_lines = lines.copy()
                    for partial in self.add_typing_effect(line[2:], line[:2]):
                        current_lines = base_lines + [partial]
                        self.frames.append(self.create_frame(current_lines))
                    lines.append(line)
                else:
                    # Instant display for output
                    lines.append(line)
                    self.frames.append(self.create_frame(lines))
                
                # Small pause between lines
                self.frames.extend([self.create_frame(lines)] * 10)
            
            # Pause at end of scenario
            self.frames.extend([self.create_frame(lines)] * 60)
    
    def save_gif(self, filename):
        """Save frames as animated GIF"""
        if self.frames:
            self.frames[0].save(
                filename,
                save_all=True,
                append_images=self.frames[1:],
                duration=50,  # 50ms per frame
                loop=0
            )
            print(f"Animation saved to {filename}")

def main():
    print("Creating Claude Code demo animation...")
    
    animator = TerminalAnimator()
    animator.generate_demo()
    
    output_path = "test/outputs/demo_animation.gif"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    animator.save_gif(output_path)
    
    # Also create a simple text version
    with open("test/outputs/demo_script.txt", "w") as f:
        f.write("""Claude Code Demo Script
======================

1. Installation
   $ npm install -g @anthropic-ai/claude-code
   $ export ANTHROPIC_API_KEY='your-key'
   $ claude-code --version

2. Basic Usage
   $ claude-code
   > Create a Python hello world program
   [Claude creates hello.py]

3. Code Explanation
   > Explain the code in calculator.py
   [Claude explains the code structure]

4. Debugging
   > Help me debug my code
   [Claude identifies and fixes errors]

5. Git Integration
   > Commit my changes
   [Claude handles git operations]

For the full animated demo, see demo_animation.gif
""")
    
    print("Demo animation script created!")
    print("Note: For a real animation, you'll need PIL/Pillow installed:")
    print("pip install Pillow")

if __name__ == "__main__":
    main()