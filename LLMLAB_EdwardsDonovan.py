#!/usr/bin/env python3
"""
Screentone Pattern Generator - CLI Application
Generates screentone patterns from clipboard images and outputs to clipboard.
Based on the algorithm from: https://github.com/sensai7/screentone-generator
"""

import argparse
import math
import random
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageGrab


# ============================================================================
# Core Screentone Algorithm - Direct Port from JavaScript
# ============================================================================

def get_random_int_inclusive(min_val, max_val):
    """Get a random integer between min and max inclusive."""
    min_val = math.ceil(min_val)
    max_val = math.floor(max_val)
    return math.floor(random.random() * (max_val - min_val + 1)) + min_val


def apply_screentone(image_data, width, height, frequency, angle, shape, use_alpha=True, color=(255,255,255)):
    """
    Apply screentone effect to image data.
    
    Args:
        image_data: numpy array of RGBA values
        width: image width
        height: image height
        frequency: pattern frequency
        angle: pattern rotation angle in degrees
        shape: pattern shape type
        use_alpha: if True, convert black to transparent; if False, use black/white
    
    Returns:
        PIL Image with screentone applied
    """
    # Create threshold pattern
    threshold_pattern = create_threshold_pattern(width, height, frequency, angle, shape)
    
    # Create output array
    output_data = np.zeros((height, width, 4), dtype=np.uint8)
    
    # Apply screentone
    for y in range(height):
        for x in range(width):
            # Get RGB values
            index_r = 0
            index_g = 1
            index_b = 2
            
            r = image_data[y, x, index_r]
            g = image_data[y, x, index_g]
            b = image_data[y, x, index_b]
            
            # Convert to grayscale
            gray = (int(r) + int(g) + int(b)) / 3
            
            # Get threshold from pattern
            pattern_y = y % len(threshold_pattern)
            pattern_x = x % len(threshold_pattern[0])
            threshold = threshold_pattern[pattern_y][pattern_x]
            
            # Apply threshold
            alpha = 0 if gray < threshold else 255
            
            if use_alpha:
                # Black becomes transparent, white stays opaque
                # Set RGB to white and modulate alpha
                output_data[y, x, 0] = color[0]
                output_data[y, x, 1] = color[1]
                output_data[y, x, 2] = color[2]
                output_data[y, x, 3] = alpha  # 0 for transparent, 255 for opaque
            else:
                # Original behavior: black and white
                output_data[y, x, 0] = alpha
                output_data[y, x, 1] = alpha
                output_data[y, x, 2] = alpha
                output_data[y, x, 3] = 255  # Always opaque
    
    return Image.fromarray(output_data, 'RGBA')


def create_threshold_pattern(width, height, frequency, angle, shape):
    """
    Create a threshold pattern based on shape and parameters.
    
    Args:
        width: pattern width
        height: pattern height
        frequency: pattern frequency
        angle: pattern angle in degrees
        shape: pattern shape type
    
    Returns:
        2D list of threshold values (0-255)
    """
    coef = None
    angle_degrees = angle
    
    # Apply shape-specific corrections
    if shape == 'sine-cosine':
        angle_degrees = angle - 45
    elif shape == 'circles':
        frequency = frequency / math.sqrt(2)
    elif shape == 'lines':
        pass
    elif shape == 'squares':
        angle_degrees = angle - 45
    elif shape == 'sparkles':
        angle_degrees = angle - 45
    elif shape == 'inception':
        angle_degrees = angle - 45
    elif shape == 'tartan':
        angle_degrees = angle - 45
    elif shape == 'harmonic':
        angle_degrees = angle - 45
        coef = get_harmonic_coef()
    
    # Convert angle to radians for calculations
    angle_rad = angle_degrees * math.pi / 180
    
    if shape != "random":
        if angle_degrees != 0:
            pattern = get_pattern(width, height, shape, angle_rad, frequency, coef)
        else:
            # For 0 degrees, create a tile pattern
            pixel_radius = 32  # Default tile size
            pattern = get_pattern(pixel_radius, pixel_radius, shape, angle_rad, frequency, coef)
            
            # Normalize
            min_val = min_value(pattern)
            max_val = max_value(pattern)
            pattern = normalize_2d(pattern, min_val, max_val)
            
            # Tile the pattern
            pattern = create_tiled_array(pattern, width, height)
    else:
        # Random pattern
        pattern = []
        for y in range(height):
            row = []
            for x in range(width):
                row.append(get_random_int_inclusive(0, 255))
            pattern.append(row)
    
    return pattern


def get_pattern(width, height, shape, angle, frequency, coef):
    """
    Generate pattern based on shape type.
    
    Args:
        width: pattern width
        height: pattern height
        shape: shape type
        angle: angle in radians
        frequency: frequency parameter
        coef: coefficients for harmonic shape
    
    Returns:
        2D list of pattern values
    """
    pattern = []
    
    for y in range(height):
        row = []
        for x in range(width):
            value = 0
            
            if shape == 'sine-cosine':
                transform_x = x * frequency * math.cos(angle) - y * frequency * math.sin(angle)
                transform_y = x * frequency * math.sin(angle) + y * frequency * math.cos(angle)
                value = math.cos(transform_x) * math.cos(transform_y)
                
            elif shape == 'circles':
                transform_x = x * frequency * math.cos(angle) - y * frequency * math.sin(angle)
                transform_y = x * frequency * math.sin(angle) + y * frequency * math.cos(angle)
                value = abs(math.sin(transform_x)) + abs(math.cos(transform_y))
                
            elif shape == 'lines':
                transform_x = x * frequency * math.cos(angle) - y * frequency * math.sin(angle)
                value = math.cos(transform_x)
                
            elif shape == 'squares':
                value = coef2_harmonic_series(x, y, frequency, 
                    [1, 0, 0.11111, 0, 0.04, 0, 0.02041, 0, 0.01234, 0, 0.00826], angle)
                
            elif shape == 'sparkles':
                value = coef2_harmonic_series(x, y, frequency,
                    [1, 0, 0.22222, 0, 0.12, 0, 0.0816, 0, 0.0617], angle)
                
            elif shape == 'inception':
                value = coef2_harmonic_series(x, y, frequency,
                    [1, 0, 0, 0, 1], angle)
                
            elif shape == 'tartan':
                value = coef2_harmonic_series(x, y, frequency,
                    [1, -0.4, 0.4, -0.2, -0.65, 0.4, 0.35, -0.95], angle)
                
            elif shape == 'harmonic':
                value = coef2_harmonic_series(x, y, frequency, coef, angle)
            
            row.append(value)
        pattern.append(row)
    
    # Normalize to 0-255
    min_val = min_value(pattern)
    max_val = max_value(pattern)
    pattern = normalize_2d(pattern, min_val, max_val)
    
    return pattern


def coef2_harmonic_series(x, y, frequency, coef_table, angle):
    """
    Calculate value using harmonic series with coefficients.
    
    Args:
        x: x coordinate
        y: y coordinate
        frequency: frequency parameter
        coef_table: list of coefficients
        angle: angle in radians
    
    Returns:
        Calculated value
    """
    x_freq = (x - 1) * frequency
    y_freq = (y - 1) * frequency
    
    transform_x = x_freq * math.cos(angle) - y_freq * math.sin(angle)
    transform_y = x_freq * math.sin(angle) + y_freq * math.cos(angle)
    
    result = 0
    for i, coef in enumerate(coef_table):
        result += coef * math.cos((i + 1) * transform_x) * math.cos((i + 1) * transform_y)
    
    return result


def get_harmonic_coef():
    """Get harmonic coefficients (default values)."""
    return [1, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125]


def min_value(arr):
    """Find minimum value in 2D array."""
    return min(min(row) for row in arr)


def max_value(arr):
    """Find maximum value in 2D array."""
    return max(max(row) for row in arr)


def normalize_2d(arr, min_val, max_val):
    """
    Normalize 2D array values to 0-255.
    
    Args:
        arr: 2D list
        min_val: minimum value
        max_val: maximum value
    
    Returns:
        Normalized 2D list
    """
    if max_val == min_val:
        return arr
    
    range_val = max_val - min_val
    normalized = []
    for row in arr:
        normalized_row = []
        for val in row:
            normalized_val = (val - min_val) / range_val * 255
            normalized_row.append(normalized_val)
        normalized.append(normalized_row)
    
    return normalized


def create_tiled_array(pattern, width, height):
    """
    Tile a pattern to fill a larger area.
    
    Args:
        pattern: 2D pattern array
        width: target width
        height: target height
    
    Returns:
        Tiled 2D array
    """
    tile_width = len(pattern[0])
    tile_height = len(pattern)
    new_array = []
    
    for y in range(height):
        row = []
        for x in range(width):
            pattern_x = x % tile_width
            pattern_y = y % tile_height
            row.append(pattern[pattern_y][pattern_x])
        new_array.append(row)
    
    return new_array


# ============================================================================
# Clipboard Utilities
# ============================================================================

def get_image_from_clipboard():
    """
    Get image from system clipboard.
    
    Returns:
        PIL Image object or None if no image in clipboard
    """
    try:
        image = ImageGrab.grabclipboard()
        if image is None:
            return None
        return image
    except Exception as e:
        print(f"Error reading from clipboard: {e}", file=sys.stderr)
        return None


def copy_to_clipboard(image):
    """
    Copy image to system clipboard with alpha channel preserved.
    
    Args:
        image: PIL Image object
    """
    try:
        import subprocess
        import tempfile
        import io
        
        if sys.platform == 'win32':
            # Convert image to PNG bytes to preserve alpha
            png_bytes = io.BytesIO()
            image.save(png_bytes, format='PNG')
            png_data = png_bytes.getvalue()
            
            # Use PowerShell to copy PNG data to clipboard as image
            # This method preserves alpha channel better
            with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
                temp_path = tmp.name
                tmp.write(png_data)
            
            try:
                # PowerShell command using LoadImage which better preserves alpha
                ps_cmd = (
                    "[System.Reflection.Assembly]::LoadWithPartialName('System.Windows.Forms') | Out-Null; "
                    "[System.Reflection.Assembly]::LoadWithPartialName('System.Drawing') | Out-Null; "
                    f"$img = [System.Drawing.Image]::FromFile('{temp_path}'); "
                    "[System.Windows.Forms.Clipboard]::SetImage($img); "
                    "$img.Dispose()"
                )
                result = subprocess.run(
                    ['powershell', '-NoProfile', '-Command', ps_cmd],
                    check=True,
                    capture_output=True,
                    timeout=5
                )
                print("Successfully copied to clipboard with alpha channel")
            finally:
                try:
                    Path(temp_path).unlink()
                except:
                    pass
        else:
            print("Clipboard support for this platform requires xclip or similar.", file=sys.stderr)
            print("You can use --output to save the image to a file.", file=sys.stderr)
    except Exception as e:
        print(f"Error copying to clipboard: {e}", file=sys.stderr)
        print("You can use --output to save the image to a file.", file=sys.stderr)


# ============================================================================
# CLI Interface
# ============================================================================

def main():
    """Main CLI interface."""
    parser = argparse.ArgumentParser(
        description='Generate screentone patterns from clipboard images',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --pattern lines --size 10 --angle 45
  %(prog)s --pattern circles --size 8
  %(prog)s --pattern squares --size 12 --angle 30
  %(prog)s --pattern lines --noalpha
  
Supported shapes: sine-cosine, circles, lines, squares, sparkles, inception, tartan, harmonic, random

Size parameter: Controls pattern tile size (2-50, smaller = denser pattern)
Angle: 0-360 degrees
        """
    )
    
    parser.add_argument(
        '-p',
        '--pattern',
        type=str,
        default='lines',
        choices=['sine-cosine', 'circles', 'lines', 'squares', 'sparkles', 'inception', 'tartan', 'harmonic', 'random'],
        help='Screentone pattern shape (default: lines)'
    )
    
    parser.add_argument(
        '-s',
        '--size',
        type=float,
        default=32,
        help='Pattern tile size (2-50, smaller = denser, default: 32)'
    )
    
    parser.add_argument(
        '-a',
        '--angle',
        type=float,
        default=45,
        help='Pattern angle in degrees 0-360 (default: 45)'
    )

    parser.add_argument(
        '-c',
        '--color',
        default='#ffffff',
        help='Primary color of the outputted screentone'
    )
    
    parser.add_argument(
        '-i',
        '--input',
        type=str,
        default=None,
        help='Input image file (default: read from clipboard)'
    )
    
    parser.add_argument(
        '-o',
        '--output',
        type=str,
        default=None,
        help='Output image file (default: copy to clipboard)'
    )
    
    parser.add_argument(
        '-n',
        '--noalpha',
        action='store_true',
        help='Disable alpha transparency (use black/white instead of transparent)'
    )
    
    args = parser.parse_args()
    
    # Validate size
    if args.size < 2 or args.size > 50:
        print("Error: size must be between 2 and 50", file=sys.stderr)
        sys.exit(1)
    
    # Get input image
    if args.input:
        try:
            image = Image.open(args.input).convert('RGBA')
            print(f"Loaded image from: {args.input}")
        except Exception as e:
            print(f"Error loading input image: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        image = get_image_from_clipboard()
        if image is None:
            print("Error: No image found in clipboard. Use --input to specify a file.", file=sys.stderr)
            sys.exit(1)
        print("Loaded image from clipboard")
    
    # Convert to RGBA if needed
    if image.mode != 'RGBA':
        image = image.convert('RGBA')
    
    width, height = image.size
    print(f"Image size: {width}x{height}")
    
    # Determine alpha mode
    use_alpha = not args.noalpha
    alpha_mode = "off" if args.noalpha else "on (transparent black)"
    print(f"Applying screentone: shape={args.pattern}, size={args.size}, angle={args.angle}, alpha={alpha_mode}")
    
    # Convert image to numpy array
    image_array = np.array(image)
    
    # Calculate frequency from size: frequency = (2π) / size
    frequency = (math.pi * 2) / args.size

    hex = args.color.lstrip('#')
    color = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
    
    # Apply screentone
    try:
        result = apply_screentone(image_array, width, height, frequency, args.angle, args.pattern, use_alpha, color)
        print("Screentone applied successfully")
    except Exception as e:
        print(f"Error applying screentone: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    # Save output
    if args.output:
        try:
            result.save(args.output)
            print(f"Saved output to: {args.output}")
        except Exception as e:
            print(f"Error saving output: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        copy_to_clipboard(result)
        print("Copied result to clipboard")


if __name__ == '__main__':
    main()
