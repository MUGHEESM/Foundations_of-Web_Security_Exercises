def render(template: str, context: dict[str, str]) -> str:
    output = template
    for key, value in context.items():
        output = output.replace("{{" + key + "}}", value)
    return output


if __name__ == "__main__":
    user_template = "Hello {{name}}"
    print(render(user_template, {"name": "student"}))
