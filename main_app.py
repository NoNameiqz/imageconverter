from wand.image import Image

def converter(output_type,input_name="",output_name=""):
    if input_name == "":
        return False, "Empty file path"
    try:
        with Image(filename=input_name) as img:
            img.format = output_type
            if output_name == "":
                output = f"output.{output_type}"
            else:
                output = output_name + "." + output_type
            img.save(filename=output)
        return True, output
    except Exception as e:
        return False, e




#converter("png","resources/input.svg")

