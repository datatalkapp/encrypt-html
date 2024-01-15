import base64
import os
import re

def base64_encode_file(file_path):
    with open(file_path, "rb") as f:
        file_data = f.read()
        return base64.b64encode(file_data).decode()

def replace_external_references_with_data_uris(html_content, base_dir):
    # Replace image references
    html_content = re.sub(
        r'src="([^"\s]+)"',
        lambda match: f'src="data:image/{os.path.splitext(match.group(1))[1][1:]};base64,{base64_encode_file(os.path.join(base_dir, match.group(1)))}"',
        html_content,
        flags=re.MULTILINE
    )

    # find video tags
    video_tags = re.findall(r'<video[^>]*>', html_content, flags=re.MULTILINE)
    for video_tag in video_tags:
        # find source tags
        source_tags = re.findall(r'<source[^>]*>', video_tag, flags=re.MULTILINE)
        for source_tag in source_tags:
            # replace src attribute with data uri
            html_content = html_content.replace(
                source_tag,
                re.sub(
                    r'src="([^"\s]+)"',
                    lambda match: f'src="data:video/{os.path.splitext(match.group(1))[1][1:]};base64,{base64_encode_file(os.path.join(base_dir, match.group(1)))}"',
                    source_tag,
                    flags=re.MULTILINE
                )
            )
    
    # fonts in css
    # find font references in css eg src: url('roboto.ttf')
    font_references = re.findall(r'src: url\(([^)]+)\)', html_content, flags=re.MULTILINE)
    for font_reference in font_references:
        # replace font reference with data uri
        html_content = html_content.replace(
            font_reference,
            re.sub(
                r'\'([^"\s]+)\'',
                lambda match: f'\'data:font/{os.path.splitext(match.group(1))[1][1:]};base64,{base64_encode_file(os.path.join(base_dir, match.group(1)))}\'',
                font_reference,
                flags=re.MULTILINE
            )
        )
    return html_content


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python embed.py <html_file> <output_file>")
        sys.exit(1)
    with open(sys.argv[1], "r") as f:
        html_content = f.read()
        html_content = replace_external_references_with_data_uris(html_content, os.getcwd())
        with open(sys.argv[2], "w") as f:
            f.write(html_content)