from PIL import Image, ImageDraw
import os

def create_rounded_image(input_path, output_path, corner_radius=0.2):
    """
    Create a rounded version of an image
    corner_radius: fraction of the image size (0.0 = no rounding, 0.5 = fully rounded)
    """
    # Open the original image
    img = Image.open(input_path)
    
    # Convert to RGBA if not already
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # Create a new image with the same size
    rounded_img = Image.new('RGBA', img.size, (0, 0, 0, 0))
    
    # Create a mask for rounded corners
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    
    # Calculate corner radius
    radius = int(min(img.size) * corner_radius)
    
    # Draw rounded rectangle mask
    draw.rounded_rectangle([0, 0, img.size[0]-1, img.size[1]-1], radius=radius, fill=255)
    
    # Apply the mask
    rounded_img.paste(img, (0, 0))
    rounded_img.putalpha(mask)
    
    # Save the rounded image
    rounded_img.save(output_path, 'PNG')
    print(f"Created rounded version: {output_path}")

def main():
    # Create output directory
    output_dir = "favicon_io_rounded"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # List of favicon files to process
    favicon_files = [
        "favicon-16x16.png",
        "favicon-32x32.png", 
        "apple-touch-icon.png",
        "android-chrome-192x192.png",
        "android-chrome-512x512.png"
    ]
    
    # Process each favicon file
    for filename in favicon_files:
        input_path = os.path.join("favicon_io", filename)
        output_path = os.path.join(output_dir, filename)
        
        if os.path.exists(input_path):
            # Use different corner radius for different sizes
            if "16x16" in filename or "32x32" in filename:
                corner_radius = 0.3  # More rounded for small icons
            elif "apple-touch" in filename:
                corner_radius = 0.25  # Medium rounding for Apple touch icon
            else:
                corner_radius = 0.2  # Standard rounding for larger icons
            
            create_rounded_image(input_path, output_path, corner_radius)
        else:
            print(f"File not found: {input_path}")
    
    # Copy the webmanifest file
    webmanifest_src = os.path.join("favicon_io", "site.webmanifest")
    webmanifest_dst = os.path.join(output_dir, "site.webmanifest")
    if os.path.exists(webmanifest_src):
        with open(webmanifest_src, 'r') as f:
            content = f.read()
        with open(webmanifest_dst, 'w') as f:
            f.write(content)
        print(f"Copied: {webmanifest_dst}")
    
    print(f"\nAll rounded favicons created in '{output_dir}' directory!")
    print("You can now replace the original favicon_io folder with this new one.")

if __name__ == "__main__":
    main() 