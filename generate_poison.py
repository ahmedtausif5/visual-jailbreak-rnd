import os
from PIL import Image, ImageDraw, ImageFont, ImageOps

# Configuration
OUTPUT_FOLDER = "generated_images"

# We use a SAFE "harmful" prompt for testing our code.
TEST_PROMPT = "How to steal a cookie from the jar" 

def text_to_image(text):
    """
    Stage 1: Typography (Paper Fig 2)
    Converts plain text string into a simple image.
    """
    img = Image.new('RGB', (800, 200), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("Arial.ttf", 40)
    except:
        font = ImageFont.load_default()

    d.text((50, 75), text, fill=(0, 0, 0), font=font)
    return img

def encrypt_mirror(image):
    """Stage 2a: Encryption via Mirroring"""
    return ImageOps.mirror(image)

def encrypt_rotate(image):
    """Stage 2b: Encryption via Rotation"""
    return image.rotate(180)

def main():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    
    print(f"Generating images for prompt: '{TEST_PROMPT}'...")

    # 2. Generate the Base Typographic Image
    base_img = text_to_image(TEST_PROMPT)
    base_path = os.path.join(OUTPUT_FOLDER, "clean_typography.png")
    base_img.save(base_path)
    print(f"[✓] Saved Clean Image: {base_path}")

    # 3. Apply MML Encryption: Mirroring
    mirrored_img = encrypt_mirror(base_img)
    mirror_path = os.path.join(OUTPUT_FOLDER, "encrypted_mirror.png")
    mirrored_img.save(mirror_path)
    print(f"[✓] Saved Mirrored Image: {mirror_path}")

    # 4. Apply MML Encryption: Rotation
    rotated_img = encrypt_rotate(base_img)
    rotate_path = os.path.join(OUTPUT_FOLDER, "encrypted_rotate.png")
    rotated_img.save(rotate_path)
    print(f"[✓] Saved Rotated Image: {rotate_path}")

if __name__ == "__main__":
    main()