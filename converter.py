from PIL import Image

def converter(output_type, input_name="", output_name=""):
    if input_name == "":
        return False, "Empty file path"
    
    try:
        img = Image.open(input_name)

        if output_type.lower() in ["jpg", "jpeg"]:
            img = img.convert("RGB")

        if output_name == "":
            output = f"converted.{output_type}"
        else:
            output = output_name + "." + output_type

        img.save(output, output_type.upper())

        return True, output

    except Exception as e:
        return False, str(e)




#converter("png","resources/input.svg")

