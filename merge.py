from PIL import Image

def merge_images_vertically(image1_path, image2_path, output_path):
    try:
        # Open images using PIL
        image1 = Image.open(image1_path)
        image2 = Image.open(image2_path)

        # Resize image2 to match the width of image1
        width = min(image1.width, image2.width)
        image2 = image2.resize((width, int(image2.height * width / image2.width)))

        # Create a new image with height large enough to fit both images stacked vertically
        merged_height = image1.height + image2.height
        merged_image = Image.new('RGB', (width, merged_height))

        # Paste images into the new image
        merged_image.paste(image1, (0, 0))
        merged_image.paste(image2, (0, image1.height))

        # Save the merged image
        merged_image.save(output_path)
        print(f"Merged images saved as {output_path}")

    except Exception as e:
        print(f"Error merging images: {e}")

# Example usage:
merge_images_vertically('sebastian4.png', 'sebastian6.png', 'merged_image_vertical.jpg')
