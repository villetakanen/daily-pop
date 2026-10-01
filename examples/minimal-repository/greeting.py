def greet(name):
    return f"Hello, {name.strip() if name else 'friend'}!"


if __name__ == "__main__":
    print(greet("   "))
