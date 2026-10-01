def greet(name):
    return f"Hello, {name.strip() or 'friend'}!"


if __name__ == "__main__":
    print(greet("   "))
